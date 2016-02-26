import sublime, sublime_plugin

class ToggleLogCommandsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        toggle_on = (self.settings().get("log_commands") == False)
        sublime.message_dialog(str(toggle_on))

class ToggleLogCommandsOnCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sublime.log_commands(True)

class ToggleLogCommandsOffCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sublime.log_commands(False)