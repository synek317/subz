BASIC_ARIZ_ION_EXAMPLE = """[TEST]
|               query               |   total   | comment |
|-----------------------------------|-----------|---------|
| HBYEAR0101$SRC:TEST/YEAR0110+1/A1 | EUR100.00 |         |

[CONTRACT]
id = "TEST_CONTRACT"
currency = "EUR"
hotel_code = "TEST"
city = "TST"
destinations = ["TST"]
source = "SRC"

[DEF.ROOM]
| code | description |      occ       | grp | properties | base_meal |
|------|-------------|----------------|-----|------------|-----------|
| DBL  | Double room | P1:2 A1:2 C0:1 |     |            |           |

[DEF.MEAL]
| code |    description    | grp | properties |
|------|-------------------|-----|------------|
| BB   | Bed and breakfast | BB  |            |

[RATE.PLAN]
| dates | code |    description     | rooms | rules | properties |
|-------|------|--------------------|-------|-------|------------|
|       | STD  | Standard rate plan | DBL   |       |            |

[RATE.BASE]
|       dates       | charge | room |  occ  | meal | amount | rules | rp  | id |
|-------------------|--------|------|-------|------|--------|-------|-----|----|
| YEAR0101:YEAR0131 | PN     | DBL  | A1:2  | BB   | 100.00 |       | STD |  0 |
"""
