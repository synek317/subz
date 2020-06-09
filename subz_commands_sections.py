import sublime
import sublime_plugin
import datetime

try:
  from .subz_tools_subl import *
  from .subz_sections import *
except ValueError:
  from subz_tools_subl import *
  from subz_sections import *

class SubzInsertSectionAvlBucketStateCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, AVL_BUCKET_STATE)

class SubzInsertSectionAvlInv(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, AVL_INV)

class SubzInsertSectionAvlState(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, AVL_STATE)

class SubzInsertSectionContractFull(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, CONTRACT_FULL)

class SubzInsertSectionContractMinimal(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, CONTRACT_MINIMAL)

class SubzInsertSectionContractSpo(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, CONTRACT_SPO)

class SubzInsertSectionDefHotel(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, DEF_HOTEL)

class SubzInsertSectionDefMeal(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, DEF_MEAL)

class SubzInsertSectionDefRoom(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, DEF_ROOM)

class SubzInsertSectionQueryTransform(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, QUERY_TRANSFORM)

class SubzInsertSectionRateBase(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, RATE_BASE)

class SubzInsertSectionRateCnx(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, RATE_CNX)

class SubzInsertSectionRateDiscount(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, RATE_DISCOUNT)

class SubzInsertSectionRateDiscountGroup(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, RATE_DISCOUNT_GROUP)

class SubzInsertSectionRatePlan(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, RATE_PLAN)

class SubzInsertSectionRateRule(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, RATE_RULE)

class SubzInsertSectionRateSupplement(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, RATE_SUPPLEMENT)

class SubzInsertSectionTax(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, TAX)

class SubzInsertSectionTaxGroup(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, TAX_GROUP)

class SubzInsertSectionRestriction(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, RESTRICTION)

class SubzInsertSectionTest(sublime_plugin.TextCommand):
  def run(self, edit):
    today = datetime.date.today()
    checkin = datetime.datetime(year=today.year + 1, month=1, day=1)

    today_formatted = today.strftime("%Y%m%d")
    checkin_formatted = checkin.strftime("%Y%m%d")

    hotel_code = get_contract_section_string_type_value(self.view, "hotel_code", "TEST")
    source = get_contract_section_string_type_value(self.view, "source", "TEST")

    sample_query = "HB{0}${1}:{2}/{3}+1/A1".format(today_formatted, source, hotel_code, checkin_formatted)
    test = TEST.replace("SAMPLE_QUERY", sample_query)

    insert_ariz_section(self, edit, test)

class SubzInsertSectionRateSupplementCat(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, RATE_SUPPLEMENT_CAT)

class SubzInsertSectionRateDiscountCat(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, RATE_DISCOUNT_CAT)

class SubzInsertSectionConfig(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, CONFIG)

class SubzInsertSectionCustomInfo(sublime_plugin.TextCommand):
  def run(self, edit):
    insert_ariz_section(self, edit, CUSTOM_INFO)

class SubzReformatAriz(sublime_plugin.TextCommand):
  def run(self, edit):
    SubzAddAllSectionsHeaders.run(self, edit)
    SubzFormatAllSections.run(self, edit)

class SubzAddAllSectionsHeaders(sublime_plugin.TextCommand):
  def run(self, edit):
    for section in SECTIONS_WITH_COLUMN_HEADERS:
      section_lines = split_section_to_lines(section)
      header_regex = section_header_regex(section_lines)
      basic_header = section_basic_header(section_lines)

      find_and_replace(self, edit, header_regex, basic_header)

class SubzFormatAllSections(sublime_plugin.TextCommand):
  def run(self, edit):
    result = is_package_installed("Table Editor")

    if result == False:
      sublime.message_dialog("To format sections you need to install Package 'Table Editor'\nhttps://packagecontrol.io/packages/Table%20Editor")
    else:
      self.view.sel().clear()

      header_regions = self.view.find_all(r"^\|(?!.*\n\|)", 0)
      number_of_regions = len(header_regions)

      if number_of_regions == 0:
        sublime.message_dialog("No sections have been found")
      else:
        for region in header_regions:
          self.view.sel().add(region)
        sublime.active_window().run_command('table_editor_next_field')
        self.view.sel().clear()

        # table editor next_field adds new row in single-column tables, we need to remove them
        empty_rows_regions = self.view.find_all(r"^[\s\n|]*$")

        for region in reversed(empty_rows_regions):
          self.view.replace(edit, region, "")
