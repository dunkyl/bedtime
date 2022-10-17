from typing import Callable, TypeAlias
import threading

Action: TypeAlias = Callable[[], None]

class _Listener():
    on_sleep: Action
    on_shutdown: Action

    def _event_thread(self): raise NotImplementedError()

    def __init__(self, *, on_sleep: Action|None=None, on_shutdown: Action|None=None):
        self.on_sleep = on_sleep or (lambda: None)
        self.on_shutdown = on_shutdown or (lambda: None)
        self._thread = threading.Thread(target=self._event_thread, daemon=True)
        self._thread.start()