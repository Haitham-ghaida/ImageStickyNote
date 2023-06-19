#!/usr/bin/env python3
import gi
gi.require_version('GdkPixbuf', '2.0')
from gi.repository import GdkPixbuf
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
import sys

if len(sys.argv) < 2:
    print("Usage: python3 ImageStickyNote.py <image_file> [xpos] [ypos] [width] [height]")
    sys.exit(1)

img = sys.argv[1]
xpos = int(sys.argv[2]) if len(sys.argv) >= 3 else 0
ypos = int(sys.argv[3]) if len(sys.argv) >= 4 else 0
w = int(sys.argv[4]) if len(sys.argv) >= 5 else 400
h = int(sys.argv[5]) if len(sys.argv) >= 6 else 400

class ShowPortrait(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="ImageStickyNote")
        self.connect("destroy", Gtk.main_quit)
        self.set_skip_taskbar_hint(True)
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            img, w, h, preserve_aspect_ratio=True
        )
        image = Gtk.Image.new_from_pixbuf(pixbuf)
        self.add(image)
        self.move(xpos, ypos)
        self.show_all()

ShowPortrait()
Gtk.main()
