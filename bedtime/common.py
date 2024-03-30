from typing import Callable, Optional
import threading

class _Listener():
    on_sleep: Callable[[], None]
    on_shutdown: Callable[[], None]
    on_wake: Callable[[], None]

    def _event_thread(self): raise NotImplementedError()

    def __init__(self, *,
                 on_sleep: Optional[Callable[[], None]]=None, 
                 on_shutdown: Optional[Callable[[], None]]=None,
                 on_wake: Optional[Callable[[], None]]=None):
        self.on_sleep = on_sleep or (lambda: 0)
        self.on_shutdown = on_shutdown or (lambda: 0)
        self.on_wake = on_wake or (lambda: 0)
        self._thread = threading.Thread(target=self._event_thread, daemon=True)
        self._thread.start()