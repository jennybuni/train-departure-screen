# Mock GPIO module
BCM = BOARD = OUT = IN = HIGH = LOW = PUD_DOWN = PUD_UP = RISING = FALLING = BOTH = 0

def setmode(*args, **kwargs): pass
def setup(*args, **kwargs): pass
def output(*args, **kwargs): pass
def input(*args, **kwargs): return 0
def cleanup(*args, **kwargs): pass
def add_event_detect(*args, **kwargs): pass
def remove_event_detect(*args, **kwargs): pass