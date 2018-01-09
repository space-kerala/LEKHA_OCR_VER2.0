import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches
from matplotlib.widgets  import RectangleSelector

class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def on_about(self, widget):
        about_dialog = builder.get_object("about_window")
        about_dialog.show()
    

    def closewindow(self, arg1, arg2):
        about_dialog = builder.get_object("about_window")
        about_dialog.hide()
        return True



    def addimagebuttonclicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a file", None,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
            imgloc = dialog.get_filename()
            sw = Gtk.ScrolledWindow()
            window = builder.get_object("main_window")
            window.add(sw)
            img = builder.get_object("previmage")
            img.set_from_file(imgloc)
            sw.add_with_viewport(img)


        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_img = Gtk.FileFilter()
        filter_img.set_name("Image files")
        filter_img.add_mime_type("image/jpeg")
        filter_img.add_mime_type("image/jpg")
        filter_img.add_mime_type("image/png")
        filter_img.add_mime_type("image/bmp")
        dialog.add_filter(filter_img)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)
    
  

    def scan_button_clicked_cb(self, widget):
        os.system("simple-scan")




builder = Gtk.Builder()
builder.add_from_file("ocrgeneratorui.glade")
builder.connect_signals(Handler())





window = builder.get_object("main_window")
window.show_all()

Gtk.main()
