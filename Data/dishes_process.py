import multiprocessing as mp
import os
import time
from datetime import datetime

def washer(dishes, output, now_):
    for dish in dishes:
        now = datetime.now()
        print('Washing', dish, ', time:', now - now_, ', pid', os.getpid())
        time.sleep(1)
        #把東西丟給行程(處理程序)後繼續執行下一個
        output.put(dish)

def dryer(input, now_):
    while True:
        dish = input.get()
        now = datetime.now()
        print('Drying ', dish, ', time:', now - now_, ', pid', os.getpid())
        time.sleep(2)
        input.task_done()

if __name__ == "__main__":
    now_ = datetime.now()
    #建立佇列
    dish_queue = mp.JoinableQueue()
    #創建行程(烘乾人員)
    dryer_proc = mp.Process(target=dryer, args=(dish_queue, now_,))
    dryer_proc.daemon = True
    #啟動行程(上班囉)
    dryer_proc.start()
    #time.sleep(1)

    dishes = ['dish-1', 'dish-2', 'dish-3', 'dish-4']
    washer(dishes, dish_queue, now_)
    dish_queue.join()