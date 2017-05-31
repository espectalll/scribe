import os, configparser

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi_composites import GtkTemplate

PATH = os.path.dirname(os.path.abspath(__file__)) # + '/' + __name__

class Template():
    name = None
    description = None
    path = None

    def __init__(self, path):
        config = configparser.ConfigParser()
        config.read(path + '/scribe.ini')
        self.name = config['Template']['Name']
        self.description = config['Template']['Description']
        self.path = path

@GtkTemplate(ui=PATH + '/templates.ui')
class TemplateListItem(Gtk.Box):
    __gtype_name__ = 'TemplateListItem'

    template = None
    widgets = GtkTemplate.Child().widgets(2)
    title = widgets[0]
    description = widgets[1]

    def __init__(self, template):
        super(Gtk.Box, self).__init__()
        self.init_template()

        self.template = template
        self.title.set_text(template.name)
        self.description.set_text(template.description)

class Project():
    name = "Empty name"
    description = "Empty description"
    author = "Nobody"
    template = None
