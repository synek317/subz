import sublime

def settings():
  return sublime.load_settings("subz.sublime-settings")

def get_aclr8_path():
  return settings().get("aclr8_path")

def set_aclr8_path(value):
  settings().set("aclr8_path", value)

def get_show_ansi_escape_hint():
  return settings().get("show_ansi_escape_hint")

def set_show_ansi_escape_hint(value):
  settings().set("show_ansi_escape_hint", value)

def get_latest_search():
  return settings().get("latest_search", "::")

def set_latest_search(value):
  settings().set("latest_search", value)

def get_ariz_filter_path():
  return settings().get("ariz_filter_path")

def set_ariz_filter_path(value):
  settings().set("ariz_filter_path", value)