import sublime
import sublime_plugin
import datetime
from .subz_tools_aclr8 import *
from .subz_tools_subl import *
from .subz_sections import *
from distutils.dir_util import copy_tree
from shutil import rmtree

class SubzAclr8Version(sublime_plugin.WindowCommand):
  def run(self):
    run_aclr8_command("--version", append_output_panel)

class SubzAclr8Base(sublime_plugin.WindowCommand):
  def on_fail(self, path, is_temporary):
    self.remove_temp(path, is_temporary)

  def remove_temp(self, path, is_temporary):
    if is_temporary:
      if os.path.isdir(path):
        rmtree(path)
      else:
        os.remove(path)

class SubzAclr8Tests(SubzAclr8Base):
  def run(self):
    path, is_temporary = save_ion()
    run_aclr8_command("test " + path, lambda output: self.on_success(output, path, is_temporary), lambda: self.on_fail(path, is_temporary))

  def on_success(self, output, path, is_temporary):
    append_output_panel(output + "All tests passed.")
    self.remove_temp(path, is_temporary)

class SubzAclr8TestsCoupled(SubzAclr8Tests):
  def run(self):
    view = sublime.active_window().active_view()
    is_temporary = False

    if not ion_is_saved(view):
      sublime.message_dialog("Please save all changes before running tests")
    else:
      file_path = view.file_name()
      working_path = os.path.normpath(os.path.join(file_path, os.path.pardir))

      if "coupled" not in working_path:
        is_temporary = True
        tmp_dir = os.path.join(tempfile.mkdtemp(), "coupled")

        copy_tree(working_path, tmp_dir)

        working_path = tmp_dir

      if not working_path.endswith("/"):
        working_path = "{}/".format(working_path)

      run_aclr8_command("test " + working_path, lambda output: self.on_success(output, working_path, is_temporary), lambda: self.on_fail(working_path, is_temporary))

class SubzAclr8Query(SubzAclr8Base):
  last_query = None

  def run(self):
    today = datetime.date.today()
    checkin = datetime.datetime(year=today.year + 1, month=1, day=1)

    today_formatted = today.strftime("%Y%m%d")
    checkin_formatted = checkin.strftime("%Y%m%d")

    view = self.window.active_view()
    hotel_code = get_contract_section_string_type_value(view, "hotel_code", "TEST")
    source = get_contract_section_string_type_value(view, "source", "TEST")

    ask_user(
      "Enter the query: ",
      SubzAclr8Query.last_query or "HB{0}${1}:{2}/{3}+1/A1".format(today_formatted, source, hotel_code, checkin_formatted),
      self.run_aclr8_command
    )

  def run_aclr8_command(self, query):
    path, is_temporary = save_ion()
    SubzAclr8Query.last_query = query
    run_aclr8_command("repl " + path, lambda output: self.on_success(output, path, is_temporary), lambda: self.on_fail(path, is_temporary), query)

  def on_success(self, output, path, is_temporary):
    append_output_panel(output)
    self.remove_temp(path, is_temporary)

class SubzAclr8QueryCoupled(SubzAclr8Query):
  last_query = None

  def run_aclr8_command(self, query):
    view = sublime.active_window().active_view()
    is_temporary = False

    if not ion_is_saved(view):
      sublime.message_dialog("Please save all changes before running tests")
    else:
      file_path = view.file_name()
      working_path = os.path.normpath(os.path.join(file_path, os.path.pardir))

      if "coupled" not in working_path:
        is_temporary = True
        tmp_dir = os.path.join(tempfile.mkdtemp(), "coupled")

        copy_tree(working_path, tmp_dir)

        working_path = tmp_dir

      if not working_path.endswith("/"):
        working_path = "{}/".format(working_path)

    SubzAclr8Query.last_query = query
    run_aclr8_command("repl " + working_path, lambda output: self.on_success(output, working_path, is_temporary), lambda: self.on_fail(working_path, is_temporary), query)
