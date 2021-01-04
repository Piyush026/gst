import threading
from gst import readfile,main
import time

lst = readfile()

data = [lst[i:i + 2000] for i in range(0, len(lst), 2000)]
print(len(data))
data1 = data[0][513:]
data2 = data[1]
data3 = data[2]
data4 = data[3]
data5 = data[4]

lock = threading.Lock()
if __name__ == "__main__":
   t1 = threading.Thread(target=main, args=(data1,lock))
    #t2 = threading.Thread(target=main, args=(data2,lock))
    #t3 = threading.Thread(target=main, args=(data3,lock))
    #t4 = threading.Thread(target=main, args=(data4,lock))
    #t5 = threading.Thread(target=main, args=(data5,lock))

   t1.start()
    #
   print("Done!")


