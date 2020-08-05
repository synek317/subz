import sublime
import sublime_plugin
import datetime
import re
import tempfile
try:
  from .subz_tools_io import *
  from .subz_tools_subl import *
  from .subz_tools import *
except ValueError:
  from subz_tools_io import *
  from subz_tools_subl import *
  from subz_tools import *

def run_ariz_filter_command(params, on_success=None, on_fail=None, stdin=None):
  ariz_filter_path_from_settings = get_ariz_filter_path()
  path = find_ariz_filter(ariz_filter_path_from_settings) or find_ariz_filter(ariz_filter_path_from_settings + ".exe")

  if path == None:
    ask_user(
      "ARIZ Filter not found in " + ariz_filter_path_from_settings + ". Please enter either executable or source path",
      ariz_filter_path_from_settings,
      lambda value: receive_new_ariz_filter_path(value, params, on_success, on_fail, stdin)
    )
  else:
    stdout, stderr, errcode, command = run_ariz_filter(ariz_filter_path_from_settings, params, stdin)
    header = "### Running " + command + "\n"
    if not is_ariz_filter_success(stdout, stderr, errcode):
      append_output_view("{0}*** An error occured while running command. Error code: {1}.\n*** Standard error output:\n\n{2}\n\n----------\n\n*** Standard output:\n{3}".format(header, str(errcode), stderr, stdout))
      if on_fail != None:
        on_fail()
    else:
      if on_success != None:
        on_success("{0}\n{1}".format(header, stdout))

def is_ariz_filter_success(stdout, stderr, errcode):
  return errcode == 0 and not re.search("... .*fail", stdout)

def receive_new_ariz_filter_path(value, params, on_success, on_fail, stdin):
  set_ariz_filter_path(value)
  sublime.save_settings("subz.sublime-settings")
  run_ariz_filter_command(params, on_success, on_fail, stdin)

def run_ariz_filter(path, params, stdin=None):
  exe = path

  if is_ariz_filter_source_dir(path):
    exe = "cargo"
    params = "run --manifest-path " + get_ariz_filter_cargo_path(path) + " -- " + params

  return run(exe, params, stdin)

def find_ariz_filter(path):
  if path == None or is_ariz_filter(path) or is_ariz_filter_source_dir(path):
    return path

  from_path = which(path)

  if from_path != None and is_ariz_filter(from_path):
    return from_path

  return None

def is_ariz_filter(path):
  if not is_exe(path):
    return False

  stdout, _stderr, errcode, _cmd = run(path, "--help")
  return errcode == 0 and stdout.startswith("ariz_filter")

def is_ariz_filter_source_dir(path):
  ariz_filter_src_path = get_ariz_filter_src_path(path)
  ariz_filter_cargo_path = get_ariz_filter_cargo_path(path)

  return is_dir(ariz_filter_src_path) and is_file(ariz_filter_cargo_path) and 'name = "ariz_filter"' in open(ariz_filter_cargo_path).read()

def get_ariz_filter_src_path(path):
  return os.path.join(path)

def get_ariz_filter_cargo_path(path):
  return os.path.join(get_ariz_filter_src_path(path), "Cargo.toml")

def save_ion():
  view = sublime.active_window().active_view()
  if view.is_dirty() or not view.file_name() or not view.file_name().endswith(".ion"):
    content = view.substr(sublime.Region(0, view.size()))
    fd, path = tempfile.mkstemp(".ion")
    os.write(fd, content.encode("utf-8"))
    os.close(fd)
    return (path, True)
  else:
    return (view.file_name(), False)