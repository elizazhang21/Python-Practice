class Solution:
	def __init__(self, lamp, size):
		self.x = lamp[0]
		self.y = lamp[1]
		self.size_x = size[0]
		self.size_y = size[1]

	def solve(self):
		n = 0
		if self.y >= self.x:
			n = (self.x + 1)*self.x/2 + (self.size_y-self.y-1)*(self.x+1) + (self.size_x-self.x-1)*(self.y+1) + (self.size_x - self.x-1)*(self.size_y - self.y-1)
		else:
			n  = (self.y + 1)*self.y/2 + (self.size_y-self.y-1)*(self.x+1) + (self.size_x-self.x-1)*(self.y+1) + (self.size_x - self.x-1)*(self.size_y - self.y-1)
		return n

solution = Solution([2,4],[3,5])
print(solution.solve())
			
