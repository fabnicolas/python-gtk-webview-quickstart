import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

gi.require_version('WebKit', '3.0')
from gi.repository import WebKit

from screeninfo import get_monitors

class PythonWebView:
    def __init__(self):
        window = Gtk.Window()

        self.wview = WebKit.WebView()
        self.wview.load_uri('http://finalgalaxy.github.io/vistriker-FE/')

        screen_info=get_monitors()[0]
        self.size_width=1000
        self.size_height=700
        window.resize(self.size_width,self.size_height)
        window.move(screen_info.width/2 - self.size_width/2, screen_info.height - self.size_height/2) # Center window according to screen size and window size
        window.add(self.wview)
        window.show_all()
        # window.fullscreen() # Toggle fullscreen on
        window.connect('delete-event',Gtk.main_quit)

if __name__ == "__main__":
    PythonWebView()
    Gtk.main()
