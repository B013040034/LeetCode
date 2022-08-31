class MyCalendar:

    def __init__(self):
        self.arr = []

    def book(self, start, end):
        if self.arr == []:
            self.arr = [[start, end]]
            return True
        else:
            nums = [start, end]
            if nums[1] <= self.arr[0][0]:
                self.arr.insert(0, nums)
                return True
            elif nums[0] >= self.arr[-1][1]:
                self.arr.append(nums)
                return True
            else:
                a = self.binary_search(nums)
                if a == -1:
                    return False
                if nums[1] <= self.arr[a][0]:
                    self.arr.insert(a, nums)
                    return True
        return False
            
    def binary_search(self, nums):
        left = 0
        right = len(self.arr) -1
        while left < right:
            mid = (left + right)/2
            if nums[0] < self.arr[mid][0]:
                right = mid
            elif nums[0] >= self.arr[mid][1]:
                left = mid + 1
            else:
                return -1
        return left


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
