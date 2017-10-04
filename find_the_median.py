class Solution:

    def __init__(self,list,k):
        self.n = len(list)
        self.k = k
        self.list = list

    def solve(self):
        subarray = []
        for i in range(self.n):
            if self.list[i] >= self.k:
                subarray.append(self.list[i])
            else:
                break

        if len(subarray)%2 == 0:
            return (subarray[int(len(subarray)/2-1)]+subarray[int(len(subarray)/2)])/2
        else:
            return (subarray[int(len(subarray)/2)])

solution = Solution([5,4,3,2,1],2)
print(solution.solve())