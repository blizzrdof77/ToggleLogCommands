import sublime, sublime_plugin

class ToggleLogCommandsCommand(sublime_plugin.TextCommand):
    def run(self, edit, toggle_state=None):
        if toggle_state is None:
            toggle_state = (self.view.settings().get("log_commands") == False)
        sublime.log_commands(toggle_state)
        self.view.settings().set("log_commands", toggle_state)
        sublime.active_window().run_command("show_panel", {"panel": "console", "toggle": (not toggle_state)})

class ToggleLogCommandsOnCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        ToggleLogCommandsCommand.run(self, edit, True)

class ToggleLogCommandsOffCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        ToggleLogCommandsCommand.run(self, edit, False)