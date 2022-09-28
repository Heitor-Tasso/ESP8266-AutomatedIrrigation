from kivy.clock import Clock
from kivy.uix.widget import Widget

class BTrigger(Widget):
    
    _count_events = 0
    _started = False

    function = lambda *a: None
    n_events = 0
    interval = 0
    args = ()
    kwargs = {}
    
    size_hint = [None, None]
    size = [0, 0]
    pos = [0, 0]

    def __init__(self, function, n_events, interval, *args, **kwargs):
        super().__init__()
        self.function = function
        self.n_events = n_events
        self.interval = interval
        self.args = args
        self.kwargs = kwargs
    
    def start(self, *args):
        if self._started:
            return None

        self._count_events = 0
        Clock.schedule_interval(self.call_function, self.interval)
        self._started = True

    def stop(self, *args):
        if not self._started:
            return None
        
        self._count_events = 0
        Clock.unschedule(self.call_function)
        self._started = False

    def call_function(self, *args):
        if self._count_events >= self.n_events:
            return self.stop()
        
        self.function(*self.args, **self.kwargs)
        self._count_events += 1
