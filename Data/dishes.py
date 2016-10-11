import os
import time
from datetime import datetime

def washer(dishes, now_):
	for dish in dishes:
		now = datetime.now()
		print('Washing', dish, ', time:', now - now_, ', pid', os.getpid())
		time.sleep(1)
		dryer(dish, now_)

def dryer(dish, now_):
	now = datetime.now()
	print('Drying ', dish, ', time:', now - now_, ', pid', os.getpid())
	time.sleep(2)


if __name__ == "__main__":
	now_ = datetime.now()
	dishes = ['dish-1', 'dish-2', 'dish-3', 'dish-4']
	washer(dishes, now_)