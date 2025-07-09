class add2nums:
    def __init__(self, num):
        self.num = num
    def __add__(self, other):
        self.num += other.num

    def __str__(self):
        return str(self.num)

    def __call__(self, other_nums):
        self.num+=other_nums
        return self
add2nums = add2nums(10)
print(add2nums(3)(10))