import sys, os

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import GLib, Gio, Gtk, WebKit2
from scribe.components import Template, TemplateListItem, Project

PATH = os.path.dirname(os.path.abspath(__file__)) # + '/' + __name__

class AppWindow(Gtk.ApplicationWindow):
    __builder__ = None
    project = None

    def __init__(self, app):
        self.Application = app
        self.__builder__ = app.__builder__
        self.MainWindow = self.__builder__.get_object('mainWindow')
        back_button = self.__builder__.get_object('backButton')
        next_button = self.__builder__.get_object('nextButton')
        name_input = self.__builder__.get_object('webNameInput')
        desc_input = self.__builder__.get_object('webDescriptionInput')
        author_input = self.__builder__.get_object('webAuthorInput')
        template_list = self.__builder__.get_object('templateList')

        back_button.connect('clicked', self.on_back_clicked)
        next_button.connect('clicked', self.on_next_clicked)
        name_input.connect('changed', self.on_basic_data_changed)
        desc_input.connect('changed', self.on_basic_data_changed)
        author_input.connect('changed', self.on_basic_data_changed)

        for template_dir in os.walk(PATH + '/templates'):
            if template_dir[0] != PATH + '/templates':
                template = Template(template_dir[0])
                list_item = TemplateListItem(template)
                template_list.add(list_item)
        template_list.connect('row-activated', self.on_template_select)

        self.MainWindow.set_application(app)
        self.MainWindow.show()

    def on_template_select(self, parent, list_item):
        title_stack = self.__builder__.get_object('titleStack')
        root_stack = self.__builder__.get_object('rootStack')
        title_page = title_stack.get_child_by_name('basicDetailsTitlePage')
        root_page = root_stack.get_child_by_name('basicDetailsPage')
        back_button = self.__builder__.get_object('backButton')
        next_button = self.__builder__.get_object('nextButton')

        self.project = Project()
        self.project.template = list_item.get_children()[0].template

        title_stack.set_visible_child(title_page)
        root_stack.set_visible_child(root_page)
        back_button.get_parent().set_reveal_child(True)
        next_button.get_parent().set_reveal_child(True)

    def on_back_clicked(self, button):
        title_stack = self.__builder__.get_object('titleStack')
        root_stack = self.__builder__.get_object('rootStack')
        title_page = title_stack.get_child_by_name('newProjectSelectorPage')
        root_page = root_stack.get_child_by_name('templatesPage')
        back_button = self.__builder__.get_object('backButton')
        next_button = self.__builder__.get_object('nextButton')

        title_stack.set_visible_child(title_page)
        root_stack.set_visible_child(root_page)
        back_button.get_parent().set_reveal_child(False)
        next_button.get_parent().set_reveal_child(False)

    def on_basic_data_changed(self, entry):
        name_input = self.__builder__.get_object('webNameInput')
        desc_input = self.__builder__.get_object('webDescriptionInput')
        author_input = self.__builder__.get_object('webAuthorInput')
        next_button = self.__builder__.get_object('nextButton')

        if name_input.get_text_length() > 0 and \
           desc_input.get_text_length() > 0 and \
           author_input.get_text_length() > 0:
               next_button.set_sensitive(True)
        else:
            next_button.set_sensitive(False)

    def on_next_clicked(self, button):
        name_input = self.__builder__.get_object('webNameInput')
        desc_input = self.__builder__.get_object('webDescriptionInput')
        author_input = self.__builder__.get_object('webAuthorInput')
        title_stack = self.__builder__.get_object('titleStack')
        root_stack = self.__builder__.get_object('rootStack')
        title_page = title_stack.get_child_by_name('editorSwitcherPage')
        root_page = root_stack.get_child_by_name('editorPage')
        back_button = self.__builder__.get_object('backButton')
        next_button = self.__builder__.get_object('nextButton')
        new_button = self.__builder__.get_object('newButton')

        self.project.name = name_input.get_text()
        self.project.description = desc_input.get_text()
        self.project.author = author_input.get_text()

        title_stack.set_visible_child(title_page)
        root_stack.set_visible_child(root_page)
        back_button.get_parent().set_reveal_child(False)
        next_button.get_parent().set_reveal_child(False)
        new_button.get_parent().set_visible(True)
        new_button.get_parent().set_reveal_child(True)

    def close(self, *args):
        self.MainWindow.destroy()

class Application(Gtk.Application):
    __builder__ = Gtk.Builder.new_from_file(PATH + '/ui.glade')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id='bit.espectalll.Scribe',
                         flags=Gio.ApplicationFlags.FLAGS_NONE,
                         **kwargs)
        self.window = None

    def do_startup(self):
        Gtk.Application.do_startup(self)
        self.set_app_menu(self.__builder__.get_object('appMenu'))

    def do_activate(self):
        if not self.window:
            self.window = AppWindow(self)
        self.window.present()
