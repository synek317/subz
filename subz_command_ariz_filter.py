import sublime
import sublime_plugin
import datetime
try:
  from .subz_tools_ariz_filter import *
  from .subz_tools_subl import *
  from .subz_sections import *
except ValueError:
  from subz_tools_ariz_filter import *
  from subz_tools_subl import *
  from .subz_sections import *

class SubzArizFilterQuery(sublime_plugin.WindowCommand):
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
      SubzArizFilterQuery.last_query or "HB{0}${1}:{2}/{3}+1/A1".format(today_formatted, source, hotel_code, checkin_formatted),
      self.run_ariz_filter_command
    )

  def on_success(self, output, path, is_temporary):
    lines = output.splitlines(True)
    result = []

    for line in lines:
      if " INFO " not in line:
        result.append(line)

    text = "".join(result)

    results_view = sublime.active_window().new_file()
    results_view.set_name(SubzArizFilterQuery.last_query)
    results_view.set_scratch(True)
    results_view.run_command('append', {'characters': text, 'force': True, 'scroll_to_end': False})
    results_view.run_command('subz_reformat_ariz')

    self.remove_temp(path, is_temporary)

  def run_ariz_filter_command(self, query):
    path, is_temporary = save_ion()

    SubzArizFilterQuery.last_query = query

    params = "--input-file '{}' --query '{}'".format(path, query)

    run_ariz_filter_command(params, lambda output: self.on_success(output, path, is_temporary), lambda: self.on_fail(path, is_temporary), query)

  def on_fail(self, path, is_temporary):
    self.remove_temp(path, is_temporary)

  def remove_temp(self, path, is_temporary):
    if is_temporary:
      os.remove(path)
