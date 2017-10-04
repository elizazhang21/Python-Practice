class Solution:
	
	class Drone:
		def set(self, postion, time):
			self.postion = postion
			self.time_elapsed = time

		def __init__(self):
			self.postion = 1
			self.time_elapsed = 0
	
	def __init__(self):
		self.grids = {}
		self.total_time = 0

	def drone_delivery(self,grid,house):
		if grid not in self.grids:
			self.grids[grid] = self.Drone()

		drone = self.grids[grid]
		current_position = drone.postion
		current_time = drone.time_elapsed

		length_left = man(0,house - current_position - (self.total_time - current_time))
		self.total_time += 1 + length_left
		drone.set(house,self.total_time)

		
order_list = {'1234-1','1235-2','1235-3','1234-2'}
solution = Solution()
for order in order_list:
    solution.drone_delivery(order.split('-')[0], int(order.split('-')[1])

print(solution.total_time)	