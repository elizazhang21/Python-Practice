# Multiple Process

from multiprocessing import Process


def print_func(continent='Asia'):
	print('The name of continent is :' , continent)

if __name__ == '__main__':
	names = ['America', 'Europe', 'Africa']
	procs = []
	proc = Process(target=print_func)
	procs.append(proc)
	proc.start()

	# instantiating process with arguments
	for name in names:
		# print(name)
		proc = Process(target=print_func, args=(name,))
		procs.append(proc)
		proc.start()

	# complete the process
	for proc in procs:
		proc.join


# Multiple Threads

import threading

def print_cube(num):
	print("Cube: {}".format(num*num*num))

def print_square(num):
	print("Square: {}".format(num*num))

if __name__ == "__main__":
	t1 = threading.Thread(target=print_square, args = (10, ))
	t2 = threading.Thread(target=print_cube, args= (10, ))

	t1.start()
	t2.start()

	t1.join()
	t2.join()

	print('Done!')


# Corooutines using yield

def print_name(prefix):
	print("Searching prefix:{}".format(prefix))
	try:
		while True:
			# yield used to create coroutine
			name = (yield)
			if prefix in name:
				print(name)
	except GeneratorExit:
		print("Closing coroutine!")


corou = print_name("Dear")
corou.__next__()
corou.send("James")
corou.send("Dear James")
corou.close()


# Asynchronous Programming
import asyncio

@asyncio.coroutine
async def hello():
	print('Hello world! (%s)' % threading.currentThread())
	await asyncio.sleep(1)
	print('Hello again (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

