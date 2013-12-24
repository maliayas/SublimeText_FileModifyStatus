import sublime_plugin
import sublime


class FileModifyStatus(sublime_plugin.EventListener):
    def on_modified(self, view):
        self.settings = sublime.load_settings("File Modify Status.sublime-settings")
        self.check_status(view)

    def on_activated(self, view):
        self.settings = sublime.load_settings("File Modify Status.sublime-settings")
        self.check_status(view)

    def check_status(self, view):
        if view.command_history(0, True) in [(None, None, 0), ('', None, 1), ('', None, 0)]:
            self.mark(view, self.settings.get("unmodified_marker"))

        else:
            self.mark(view, self.settings.get("modified_marker"))

    def mark(self, view, marker):
        # Item key below is based on the standard defined here:
        # https://github.com/maliayas/SublimeText_PluginStandards#status-bar-items
        view.set_status("(.0.file_modify_status", marker + '  ')
