#!/usr/bin/env python

import pygtk
import sys
pygtk.require('2.0')

import mateapplet
import gtk

import subprocess

def factory(applet, iid):
	button = gtk.Button()
	button.set_relief(gtk.RELIEF_NONE)
	button.set_label("ExampleButton")
	button.connect("button_press_event", showMenu, applet)
	applet.add(button)
	applet.show_all()
	return True

def showMenu(widget, event, applet):
	if event.type == gtk.gdk.BUTTON_PRESS and event.button == 1:
		showMainDialog()
	if event.type == gtk.gdk.BUTTON_PRESS and event.button == 3:
		widget.emit_stop_by_name("button_press_event")
		create_menu(applet)

def create_menu(applet):
	propxml="""
			<popup name="button3">
			<menuitem name="Item 3" verb="About" label="_About" pixtype="stock" pixname="gtk-about"/>
			</popup>"""
	verbs = [("About", showAboutDialog)]
	applet.setup_menu(propxml, verbs, None)

def showMainDialog():
	window = gtk.Window()
	window.connect("delete-event", gtk.main_quit)
	window.set_border_width(10)

	button = gtk.Button("Hello World")
	button.connect("clicked", on_button_clicked)
	window.add(button)

	window.show_all()
	gtk.main()

def on_button_clicked(button):
	subprocess.call("mate-calculator")

def showAboutDialog(*arguments, **keywords):
	subprocess.call("mate-about")

if len(sys.argv) == 2:
	if sys.argv[1] == "run-in-window":
		mainWindow = gtk.Window(gtk.WINDOW_TOPLEVEL)
		mainWindow.set_title("Ubuntu System Panel")
		mainWindow.connect("destroy", gtk.main_quit)
		applet = mateapplet.Applet()
		factory(applet, None)
		applet.reparent(mainWindow)
		mainWindow.show_all()
		gtk.main()
		sys.exit()

if __name__ == '__main__':
	print "Starting factory"
	mateapplet.matecomponent_factory("OAFIID:Mate_Panel_Example_Factory", mateapplet.Applet.__gtype__, "Simple mate applet example", "1.0", factory)
