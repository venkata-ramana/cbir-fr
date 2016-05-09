#!/usr/bin/env python
import gtk
import webkit
import gobject

gobject.threads_init()
win = gtk.Window()
bro = webkit.WebView()
bro.open("http://localhost:5000/")
win.add(bro)
win.show_all()
gtk.main()
