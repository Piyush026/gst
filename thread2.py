import threading
import time
from concurrent.futures import ThreadPoolExecutor
from gst import readfile, maain

lst = readfile()
# data = [lst[i:i + 2000] for i in range(0, len(lst), 2000)]
# data1 = data[0][1:10]
# data2 = data[1]
# data3 = data[2]
# data4 = data[3]
# data5 = data[4]

if __name__ == "__main__":
    # t1 = threading.Thread(target=main, args=(data1, lock))
    # # t2 = threading.Thread(target=main, args=(data2, lock))
    # # t3 = threading.Thread(target=main, args=(data3, lock))
    # # t4 = threading.Thread(target=main, args=(data4, lock))
    # # t5 = threading.Thread(target=main, args=(data5, lock))
    #
    # t1.start()
    # # t2.start()
    # # t3.start()
    # # t4.start()
    # # t5.start()
    # # t1.join()
    # # t2.join()
    # # t3.join()
    # # t4.join()
    # # t5.join()
    #
    # print("Done!")
    start_time = time.time()
    print(start_time)
    with ThreadPoolExecutor(max_workers=8) as executor:
        future = executor.map(maain, lst)
        # future1 = executor.map(maain, data2)
        # # future2 = executor.map(maain, data3)
    duration = time.time() - start_time
    print(f"data  in {duration} seconds")


