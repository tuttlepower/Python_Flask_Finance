class Stock:
    def __init__(self,date ,open,close, high, low, volume):
        self.date = date
        self.open = open
        self.close = close 
        self.high = high
        self.low = low
        self.volume = volume
        pass

    def open(self):
        return self.open
        
    def close(self):
        return self.close
    
    def high(self):
        return self.high
    
    def low(self):
        return self.low

    def date(self):
        return self.date

    def volume(self):
        return self.volume
    

