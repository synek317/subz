AVL_BUCKET_STATE = """[AVL.BUCKET_STATE]
| dates | bucket_name | room | rules | count |
|-------|-------------|------|-------|-------|
* Caution: this is under development *
|       |             |      |       |       |

"""

AVL_INV = """[AVL.INV]
| dates | rules | room | allotments | from_room | from_rules |
|-------|-------|------|------------|-----------|------------|
* Caution: this is under development *
|       |       |      |            |           |            |

"""

AVL_STATE = """[AVL.STATE]
| dates | room | rules | status | cnt | remark |
|-------|------|-------|--------|-----|--------|
|       |      |       |        |     |        |

"""

CONTRACT_FULL = """[CONTRACT]
id = "TEST"
name = "TEST"
currency = "EUR"
active = true
hotel_code = "TEST"
city = "TEST"
booking = "20000101:29991210"
markets = ["TEST"]
markets_excluded = ["pl"]
clients = ["TEST"]
clients_excluded = ["TEST"]
brands = ["TEST"]
destinations = ["TEST"]
source = "TEST"
channel = "TEST"
sales_channel = "TEST"
channel_hotel_code = "TEST"
scrape = false
revision = 0
type = "D"
tz = "CET"
missing_avl_eq_to_no_avl = false
purchase_id = "TEST"
tenant = "test"
source_contract_id = "TEST_123"
parent_id = "TEST_1"
default_meal = "per_room"
product = "hotel"

"""

CONTRACT_MINIMAL = """[CONTRACT]
id = "TEST"
currency = "EUR"
hotel_code = "TEST"
city = "TEST"
destinations = ["TEST"]
source = "TEST"

"""

CONTRACT_SPO = """[CONTRACT]
parent_id = "TEST_1"
spo_prio = "1"
spo_codes = ["TEST"]

"""

DEF_HOTEL = """[DEF.HOTEL]
| hotel_code | name | category | country | city | resort | destination_name | city_name | postal | street | lat | lon | json |
|------------|------|----------|---------|------|--------|------------------|-----------|--------|--------|-----|-----|------|
|            |      |          |         |      |        |                  |           |        |        |     |     |      |

"""

DEF_MEAL = """[DEF.MEAL]
| code | description | grp | properties |
|------|-------------|-----|------------|
|      |             |     |            |

"""

DEF_ROOM = """[DEF.ROOM]
| code | description | occ | grp | properties | base_meal |
|------|-------------|-----|-----|------------|-----------|
|      |             |     |     |            |           |

"""

QUERY_TRANSFORM = """[QUERY.TRANSFORM]
|      occ     | func | args | rate |
|--------------|------|------|------|
| A*C*         | ASC  |      |      |
| C1[0:1]      | DEL  |      |      |
| A1C1[14:255] | SUB  | A2   |      |

"""

RATE_BASE = """[RATE.BASE]
| dates | charge | room | occ | meal | amount | rules | rp | id |
|-------|--------|------|-----|------|--------|-------|----|----|
|       |        |      |     |      |        |       |    |    |

"""

RATE_CNX = """[RATE.CNX]
| dates | time | room | rules | rp | applic | calc | remark | id |
|-------|------|------|-------|----|--------|------|--------|----|
|       |      |      |       |    |        |      |        |    |

"""

RATE_DISCOUNT = """[RATE.DISCOUNT]
| dates | rules | rate | comp | occ | applic | reduct | remark | rp | id |
|-------|-------|------|------|-----|--------|--------|--------|----|----|
|       |       |      |      |     |        |        |        |    |  0 |

"""

RATE_DISCOUNT_GROUP = """[RATE.DISCOUNT_GROUP]
| disc_id/group_id | group_id | strategy | name |
|------------------|----------|----------|------|
|                  |          |          |      |

"""

RATE_PLAN = """[RATE.PLAN]
| dates | code | description | rooms | rules | properties |
|-------|------|-------------|-------|-------|------------|
|       |      |             |       |       |            |

"""

RATE_RULE = """[RATE.RULE]
| dates | room | when | meal | rules | rp |
|-------|------|------|------|-------|----|
|       |      |      |      |       |    |

"""

RATE_SUPPLEMENT = """[RATE.SUPPLEMENT]
| dates | rules | rate | comp | occ | kind | chg | calc | remark | rp | id |
|-------|-------|------|------|-----|------|-----|------|--------|----|----|
|       |       |      |      |     |      |     |      |        |    | 0  |

"""

TAX = """[TAX]
| dates | rules | rate | comp | occ | applic | calc | remark | id |
|-------|-------|------|------|-----|--------|------|--------|----|
|       |       |      |      |     |        |      |        |  0 |

"""

TAX_GROUP = """[TAX_GROUP]
| id |
|----|
|    |

"""

RESTRICTION = """[RESTRICTION]
| room |    occ    | meal | rp | forbid | remark | id |
|------|-----------|------|----|--------|--------|----|
|      |           |      |    |        |        |  0 |

"""

TEST = """[TEST]
|   query      |   total   | comment |
|--------------|-----------|---------|
| SAMPLE_QUERY | EUR100.00 |         |

"""

RATE_SUPPLEMENT_CAT = """[RATE.SUPPLEMENT_CAT]
| cat | id | name |
|-----|----|------|
|     |    |      |

"""

RATE_DISCOUNT_CAT = """[RATE.DISCOUNT_CAT]
| cat | id | name |
|-----|----|------|
|     |    |      |

"""

CONFIG = """[CONFIG]
| name | value | remark |
|------|-------|--------|
|      |       |        |

"""

CUSTOM_INFO = """[CUSTOM_INFO]
| name | value | remark |
|------|-------|--------|
|      |       |        |

"""

SECTIONS_WITH_COLUMN_HEADERS = [AVL_BUCKET_STATE, AVL_INV, AVL_STATE, DEF_HOTEL, DEF_MEAL, DEF_ROOM, QUERY_TRANSFORM, RATE_BASE, RATE_CNX, RATE_DISCOUNT,
  RATE_DISCOUNT_GROUP, RATE_PLAN, RATE_RULE, RATE_SUPPLEMENT, TAX, TAX_GROUP, RESTRICTION, RATE_SUPPLEMENT_CAT, RATE_DISCOUNT_CAT, CONFIG, CUSTOM_INFO, TEST]

HEADER_REGEX = r"(\s*\\|.*\|\s*\n\|-+\|[-|]*\n)?"

def split_section_to_lines(section):
  return section.splitlines(True)

def section_header_regex(section_lines):
  section_name_regex = section_lines[0]
  section_name_regex = section_name_regex.replace("[", "\[")
  section_name_regex = section_name_regex.replace("]", "\]")
  section_name_regex = section_name_regex.replace(".", "\.")

  return section_name_regex + HEADER_REGEX

def section_basic_header(section_lines):
  if section_lines[0].startswith("[CONTRACT]"):
    return section_lines[0]
  else:
    return section_lines[0] + section_lines[1] + section_lines[2]

def get_contract_section_string_type_value(view, field, default_value):
  regex = field + r"\s*=\s*\".*\"\n"
  region = view.find(regex, 0)
  line = view.substr(region)

  splitted_line = line.split('"')
  if len(splitted_line) != 3:
    return default_value

  return splitted_line[1]
