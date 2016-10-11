import threading, queue
import os
import time
from datetime import datetime

def washer(dishes, dish_queue, now_):
	for dish in dishes:
		now = datetime.now()
		print ("Washing", dish, now - now_, ', pid', os.getpid(), threading.current_thread())
		time.sleep(1)
		dish_queue.put(dish)

def dryer(dish_queue, now_):
	while True:
		dish = dish_queue.get()
		now = datetime.now()
		print ("Drying ", dish, now - now_, ', pid', os.getpid(), threading.current_thread())
		time.sleep(2)
		dish_queue.task_done()

if __name__ == "__main__":
	dish_queue = queue.Queue()
	now_ = datetime.now()
	#控制要開幾條執行緒
	for n in range(2):
		dryer_thread = threading.Thread(target=dryer, args=(dish_queue, now_))
		dryer_thread.daemon = True
		dryer_thread.start()
		
	dishes = ['dishe-1', 'dishe-2', 'dishe-3', 'dishe-4']
	washer(dishes, dish_queue, now_)
	dish_queue.join()