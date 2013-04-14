import sublime, sublime_plugin

class SemicolonCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, self.view.line(self.view.sel()[0].begin()).end(), ";")
