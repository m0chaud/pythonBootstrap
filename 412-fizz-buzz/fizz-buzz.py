class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        arrayList = []

        for i in range(1,n+1):
            if (i % 15) == 0:
                arrayList.append("FizzBuzz")
            elif (i % 5) == 0:
                arrayList.append("Buzz")
            elif (i % 3) == 0:
                arrayList.append("Fizz")
            else:
                arrayList.append(str(i))
        
        return arrayList
        