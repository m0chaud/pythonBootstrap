class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prevSum = 0
        array = []
        for num in nums:
            prevSum = prevSum + num
            #print(prevSum)
            array.append(prevSum)
        
        return array
        