import time
from AppKit import NSObject, NSWorkspace

from .common import _Listener

class MacOsSleepListener(NSObject):

    def __init__(self):
        # self.callback = callback
        NSWorkspace.sharedWorkspace().notificationCenter().addObserver_selector_name_object_(
            self, self.sleepNotification_, "NSWorkspaceWillSleepNotification", None)

    def callback(self):
        print("sleeping")

    def sleepNotification_(self, notification):
        print(notification)
        self.callback()

class Listener(_Listener):

    def _event_thread(self):
        cb = self.on_sleep
        l = MacOsSleepListener.new()
        self._nsobj = l
        while True:
            time.sleep(1)