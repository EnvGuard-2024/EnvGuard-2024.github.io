from MetaType import BaseType

class State(BaseType):
    high = 0
    middle = 1
    low = 0

    def __init__(self, room):
        super().__init__()
        self.room = room
                                                                                               
    def _only_one(*nums):
        count = 0
        for num in nums:
            count += num & 1
            if count > 1:
                return False
        return count == 1

    def enable_decrease(self):
        assert self._only_one(self.high,self.middle,self.low)
        if self.low == 1:
            return 0
        else:
            return 1

    def enable_increase(self):
        assert self._only_one(self.high,self.middle,self.low)
        if self.high == 1:
            return 0
        else:
            return 1

    def ext_action_decrease(self,env):
        assert self._only_one(self.high,self.middle,self.low)
        if self.high == 1:
            self.high = 0
            self.middle = 1
            self.low = 0
        elif self.middle == 1:
            self.high = 0
            self.middle = 0
            self.low = 1
        elif self.low == 1:
            return

    def ext_action_increase(self,env):
        assert self._only_one(self.high,self.middle,self.low)
        if self.high == 1:
            return
        elif self.middle == 1:
            self.high = 1
            self.middle = 0
            self.low = 0
        elif self.low == 1:
            self.high = 0
            self.middle = 1
            self.low = 0

    def ap_high(self):
        return self.high
        
    def ap_middle(self):
        return self.middle

    def ap_low(self):
        return self.low

    def set_high(self):
        self.high = 1
        self.middle = 0
        self.low = 0
    def set_middle(self):
        self.high = 0
        self.middle = 1
        self.low = 0
    def set_low(self):
        self.high = 0
        self.middle = 0
        self.low = 1