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

def run_aclr8_command(params, on_success=None, on_fail=None, stdin=None):
  aclr8_path_from_settings = get_aclr8_path()
  path = find_aclr8(aclr8_path_from_settings) or find_aclr8(aclr8_path_from_settings + ".exe")

  if path == None:
    ask_user(
      "Aclr8 not found in " + aclr8_path_from_settings + ". Please enter either executable or source path",
      aclr8_path_from_settings,
      lambda value: receive_new_aclr8_path(value, params, on_success, on_fail, stdin)
    )
  else:
    stdout, stderr, errcode, command = run_aclr8(aclr8_path_from_settings, params, stdin)
    header = "*** Running " + command + "\n"
    if not is_aclr8_success(stdout, stderr, errcode):
      append_output_view("{0}*** An error occured while running command. Error code: {1}.\n*** Standard error output:\n\n{2}\n\n----------\n\n*** Standard output:\n{3}".format(header, str(errcode), stderr, stdout))
      if on_fail != None:
        on_fail()
    else:
      if on_success != None:
        on_success("{0}\n{1}".format(header, stdout))


def is_aclr8_success(stdout, stderr, errcode):
  return errcode == 0 and not re.search("... .*fail", stdout)

def receive_new_aclr8_path(value, params, on_success, on_fail, stdin):
  set_aclr8_path(value)
  sublime.save_settings("subz.sublime-settings")
  run_aclr8_command(params, on_success, on_fail, stdin)


def run_aclr8(path, params, stdin=None):
  exe = path

  if is_aclr8_source_dir(path):
    exe = "cargo"
    params = "run --manifest-path " + get_repl_cargo_path(path) + " -- " + params

  return run(exe, params, stdin)


def find_aclr8(path):
  if path == None or is_aclr8(path) or is_aclr8_source_dir(path):
    return path

  from_path = which(path)

  if from_path != None and is_aclr8(from_path):
    return from_path

  return None

def is_aclr8(path):
  if not is_exe(path):
    return False

  stdout, _stderr, errcode, _cmd = run(path, "--version")
  return errcode == 0 and stdout.startswith("aclr8i ")

def is_aclr8_source_dir(path):
  repl_src_path = get_repl_src_path(path)
  repl_cargo_path = get_repl_cargo_path(path)

  return is_dir(repl_src_path) and is_file(repl_cargo_path) and 'name = "aclr8i"' in open(repl_cargo_path).read()

def get_repl_src_path(path):
  return os.path.join(path, "repl")

def get_repl_cargo_path(path):
  return os.path.join(get_repl_src_path(path), "Cargo.toml")

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

def ion_is_saved(view):
  return not view.is_dirty() and view.file_name().endswith(".ion")
