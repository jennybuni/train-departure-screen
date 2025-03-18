class SpiDev:
    def __init__(self): pass
    def open(self, *args): pass
    def close(self): pass
    def xfer2(self, *args): return [0] * len(args[0])
