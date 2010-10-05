#! /usr/bin/env python

import gtk
import gtk.glade

class posinstaller:
	def __init__(self, runaslib=True):
		self.screens = [{'body': 'Welcome to the IS4C installations Wizard.  This wizard will walk you through the installation of the IS4C POS system.', 'next': True, 'back': False}, {'body': 'The next screen', 'next': True, 'back':  True}]
		self.current_screen = 0
		# Load Glade XML
		self.xml = gtk.glade.XML("is4c_installation.glade")

		# Get Window
		self.main_window = self.xml.get_widget('page_one_window')
		self.main_window.connect("delete_event", gtk.main_quit)

		# Get Windows child
		self.w_child = self.main_window.get_child()

		# Get our labels
		self.header_label = self.xml.get_widget('header_label')
		self.body_label = self.xml.get_widget('body_label')

		# Connect functions to Buttons
		self.back_button = self.xml.get_widget('back_button')
		self.next_button = self.xml.get_widget('next_button')
		self.cancel_button = self.xml.get_widget('cancel_button')
		self.next_button.connect('clicked', self.move_screens, 'next')
		self.back_button.connect('clicked', self.move_screens, 'back')
		self.cancel_button.connect('clicked', gtk.main_quit)

		# self.widget will be attached to the Activity
		# This can be any GTK widget except a window
		self.widget = self.w_child

		# Initialize the screen
		self.setup_screen(self.screens[self.current_screen])

		if not runaslib:
			self.main_window.show_all()
			gtk.main()

	def setup_screen(self, screen):
		self.body_label.set_markup(screen['body'])
		self.back_button.set_sensitive(screen['back'])
		self.next_button.set_sensitive(screen['next'])

	def move_screens(self, calling_object, direction):
		if direction == 'next':
			self.current_screen += 1
		elif direction == 'back':
			self.current_screen -= 1
		self.setup_screen(self.screens[self.current_screen])
		#self.body_label.set_markup("We are on the next screen.")

if __name__ == '__main__':
	posinstaller(False)
