class Vector:
    pass
    
    def __init__(self, nums):
        self.nums = nums

        self.dims = len(nums)

        self.norm = self._length()

    def __repr__(self):
        return "vector {}".format(self.nums)

    def __str__(self):
        return self.__repr__()

    def _length(self):
        return sum([c**2 for c in self.nums]) ** 0.5

    def unit_vector(self):
        return Vector([v/self.norm for v in self.nums])
        #print(self.nums)

    def scale_vector(self,scalar):
        return Vector ([scalar*v for v in self.nums])

    def __eq__(self, other):
        return self.nums == other.nums    

'''
    def dot(self, v1):
        if v1.dims != self.dims:
            return "Vectors are not of the same length."
        else:
            return sum([v1c * v2c for v1c,v2c in zip(self.nums, v1.nums)])
'''    