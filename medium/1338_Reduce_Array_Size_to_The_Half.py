class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        arr2 = []
        tmp = 0
        for i in range(1, len(arr)):
            if arr[tmp] != arr[i]:
                arr2.append(i-tmp)
                tmp = i
        arr2.append(len(arr)-tmp)
        arr2.sort(reverse=True)
        val = 0
        count = 0
        for i in range(len(arr2)):
            val += arr2[i]
            count += 1
            if val >= (len(arr)/2):
                return count
