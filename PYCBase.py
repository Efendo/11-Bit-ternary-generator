if __name__ != '__main__':
    import random

    class gen():
        def __init__(self, bit, base):
            self.bit = bit
            self.base = base
            self.num = ''
            self.nums = set()
            if self.base > 10 or self.base < 2:
                raise SyntaxError('invalid Base')
    
        def gint(self):
            self.num = ''
            for i in range(0, self.bit):
               self.num +=  str(random.randint(0, self.base-1))
            return self.num
    
        def glis(self):
            self.num = set()
            while len(self.nums) < self.base**self.bit:
                self.nums.add(self.GenNum())
            return sorted(self.nums)

else:
    raise ImportError('to use this module import it into another script')
