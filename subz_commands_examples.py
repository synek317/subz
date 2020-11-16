import sublime
import sublime_plugin
import datetime
try:
  from .subz_tools_subl import *
  from .subz_ariz_ion_examples import *
except ValueError:
  from subz_tools_subl import *
  from subz_ariz_ion_examples import *

class SubzInsertBasicArizIonExample(sublime_plugin.TextCommand):
  def run(self, edit):
    year = datetime.datetime.now().year + 1
    example = BASIC_ARIZ_ION_EXAMPLE.replace("YEAR", str(year))
    insert_ariz_example(self, edit, example)