Sublime-Z
=========

Sublime-Z is a plugin for Sublime Text 3 to edit and test ARIZ files.

# Features:

- Add any section using command or menu item
- Add all section headers using command or menu item (`Add all section headers`)
- Format all sections using command or menu item (`Format all sections`) - when [Table Editor](https://github.com/vkocubinsky/SublimeTableEditor) plugin is installed
- Add missing sections and format all sections using command or menu item (`Reformat ARIZ`) - TableEditor plugin is required
- Use aclr8 either from a binary or source code
- Run aclr8 tests
- Run single query
- Check aclr8 version
- Add ARIZ ION examples
- Filter Ion
- Make use of ANSI escape codes when [ANSIescape](https://github.com/aziz/SublimeANSI) plugin in installed

![demo](https://github.com/anixe/subz/tree/master/img/demo.gif "Demo")

# Installation:

The simplest way is to install this plugin using [Package Control](https://packagecontrol.io):

1. Install [Package Control](https://packagecontrol.io)
2. Add this repository to Package Control repositories:
  - open command input (`[shift] + [ctrl] + [p]`)
  - type "add repository" and press `Enter`
  - paste this repository url: `https://github.com/synek317/subz.git` and press `Enter`
3. Install Sublime-Z package:
  - open command input (`[shift] + [ctrl] + [p]`)
  - type "install package" and press `Enter`
  - type "subz" and press `Enter`

![installation guide](https://github.com/anixe/subz/tree/master/img/install.gif "Installation guide")

Alternatively you can clone this repository, rename it to `subz` and move it to your packages directory. Depending on your system it is:

- Windows: `%APPDATA%\Sublime Text 3`
- OS X: `~/Library/Application Support/Sublime Text 3`
- Linux: `~/.config/sublime-text-3`

# Setup

ARIZ file editting is definitely easier with following packages installed:

- [MarkdownTableFormatter](https://github.com/bitwiser73/MarkdownTableFormatter) for formatting sections
- [ANSIescape](https://github.com/aziz/SublimeANSI) for coloring tests output

In order to run aclr8-related commands, Sublime-Z must be able to find aclr8. Its path is stored in Sublime-Z settings in `aclr8_path` key.
You may provide there

- just the executable name if it is included in your `PATH` env variable
- absolute path to the executable (with or without `.exe` extension)
- absolute path to the root of aclr8 source

It may be good idea to first run `check aclr8 version` command and see if it works. If aclr8 is not found, Sublime-Z will ask you to enter the path. Check recipes for more details.

# Tips and tricks

- There are two versions of `[CONTRACT]` section. The `minimal` one inserts only minimum number of required properties while `full` inserts all possible properties.
- You don't have to type whole command. Typically, section name is enough to narrow down search results to single item.
- Output panel (at the bottom of the window) can be quickly closed by pressing `[Esc]`
- When some of the tests are failing, new tab will be opened. It ignores any changes and can be quickly closed by pressing `[ctrl] + w`
- You *don't* have to save the `.ion` file in order to run tests or query
- Use `Reformat ARIZ` command to add all sections headers and apply formatting

# List of available sections:
- CONTRACT
- CONFIG
- CUSTOM_INFO
- QUERY_TRANSFORM
- DEF_HOTEL
- DEF_MEAL
- DEF_ROOM 
- RATE_PLAN
- RATE_BASE
- RATE_SUPPLEMENT
- RATE_SUPPLEMENT_CAT
- RATE_DISCOUNT
- RATE_DISCOUNT_GROUP
- RATE_DISCOUNT_CAT
- TAX
- TAX_GROUP
- RATE_RULE
- RESTRICTION
- RATE_CNX
- AVL.INV
- AVL.STATE
- AVL.BUCKET_STATE
- TEST

# Recipes:

## Check aclr8 version:

1. Run the command
  a. with mouse: choose `Tools -> Sublime-Z -> Aclr8 -> Check aclr8 version`
  b. with keyboard: press `[shift] + [ctrl] + p` to open command input and then type `Check aclr8 version`
2. If aclr8 is not found, you have to provide it in the input box that pops up at the bottom of the window and confirm with `[Enter]`
3. When everything is configured correctly, the command and aclr8 version should be shown in the output panel at the bottom of the window

![check aclr8 version](https://github.com/anixe/subz/tree/master/img/check_version.gif "Check aclr8 version")

## Create ARIZ:

1. Create new file (`File -> New File` or `[ctrl] + n`)
2. Insert sections using either menu or command
  a. with mouse: choose `Tools -> Sublime-Z -> Insert Section` and then choose selected section
  b. with keyboard: press `[shift] + [ctrl] + p` to open command input and then type `Insert [TEST] section`. Replace `TEST` with any section name.

![create ariz](https://github.com/anixe/subz/tree/master/img/create_ariz.gif "Create ARIZ")

## Run single query

1. Create ARIZ as described previously
2. Open query input
  a. with mouse: choose `Tools -> Sublime-Z -> Aclr8 -> Run aclr8 query`
  b. with keyboard: press `[shift] + [ctrl] + p` to open command input and then type `Run aclr8 query`
3. Fill the query in the input box (by default it shows up at the bottom of the window) and press `[Enter]` when ready
4. The results should appear in the output panel.

![run query](https://github.com/anixe/subz/tree/master/img/run_query.gif "Run query")

## Run tests

1. Create ARIZ as described previously
2. Open query input
  a. with mouse: choose `Tools -> Sublime-Z -> Aclr8 -> Run aclr8 tests`
  b. with keyboard: press `[shift] + [ctrl] + p` to open command input and then type `Run aclr8 tests`
3. If all tests pass, short message will appear in the output panel
4. Otherwise, the output will appear in the `Sublime-Z Results` tab

![run tests](https://github.com/anixe/subz/tree/master/img/run_tests.gif "Run tests")

## Change aclr8i path

1. Open Sublime-Z settings: `Preferences -> Package Settings -> Sublime-Z -> Settings - User`
2. Set new aclr8i path in `aclr8_path` key, e.g.

```
{
  "aclr8_path": "/opt/aclr8i"
}
```

## Filter Ion

1. Create ARIZ as described previously
2. Open Filter input
  a. with mouse: choose `Tools -> Sublime-Z -> Filter Ion`
  b. with keyboard: press `[shift] + [ctrl] + p` to open command input and then type `Filter Ion`
  c. with keyboard shortcut: press `[ctrl] + i, o` to open command input
    Required three groups of arguments separated by ":" -  search_arguments:section_arguments:text_to_search
    Options:
      Search arguments (can be separated by comma delimiter):
        r - regex search,
        s - string search (DEFAULT),
        d - date search,
        i - lines including search text (DEFAULT),
        e - lines excluding search text
      Sections arguments (can be separated by comma delimiter):
        ba - sections: RATE.BASE, RATE.SUPPLEMENT, RATE.DISCOUNT, RATE.RULE, RESTRICTION, DEF.ROOM,
        te - TEST,
        co - CONTRACT,
        dh - DEF.HOTEL,
        dm - DEF.MEAL,
        dr - DEF.ROOM,
        rp - RATE.PLAN,
        rb - RATE.BASE,
        ru - RATE.RULE,
        rs - RATE.SUPPLEMENT,
        sc - RATE.SUPPLEMENT_CAT,
        rd - RATE.DISCOUNT,
        dc - RATE.DISCOUNT_CAT,
        dg - RATE.DISCOUNT_GROUP,
        rr - RESTRICTION,
        qt - QUERY.TRANSFORM,
        rc - RATE.CNX,
        ta - TAX,
        tg - TAX_GROUP,
        rm - RATE.MARKUP,
        ab - AVL.BUCKET_STATE,
        as - AVL.STATE,
        ai - AVL.INV,
        cf - CONFIG,
        ci - CUSTOM_INFO
    Example commands:
      `:dr:P1:2` - search for lines including string `P1:2` in `DEF.ROOM` section
      `de:rb:20180101:20180110` - search for lines in `RATE.BASE` section which dose not contain passed date in section `DATES` column
      `ri:rs,rd:P[1-2]` - search lines matching regex in `RATE.SUPPLEMENT` and `RATE.DISCOUNT` sections
3. To display help write `h` and press Enter
