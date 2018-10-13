import time
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

def bubble(data):
        for i in range(len(data)):
                for j in range(len(data)-1-i):
                        if data[j] > data[j+1]:
                                data[j], data[j+1] = data[j+1], data[j]

def quick_sort(items):
        if len(items) > 1:
                pivot_index = len(items) / 2
                smaller_items = []
                larger_items = []

                for i, val in enumerate(items):
                        if i != pivot_index:
                                if val < items[pivot_index]:
                                        smaller_items.append(val)
                                else:
                                        larger_items.append(val)

                quick_sort(smaller_items)
                quick_sort(larger_items)
                items[:] = smaller_items + [items[pivot_index]] + larger_items

# file sorting

print 'bubble sort-----------------------------------------------------------------'
f = open("input.txt", 'r')
i=0
data =[]
while True:
    line = f.readline()
    if not line: break
    line = line.strip()
    data.append(line)

#processing start
bubble_start_time = time.time()

bubble(data)
print data
#processing end
bubble_end_time = time.time()

#print processing time
bubble_time = bubble_end_time - bubble_start_time
print 'bubble sort time: ',bubble_time

print 'quick sort-----------------------------------------------------------------'
f = open("input.txt", 'r')
arr0 =[]
while True:
    line = f.readline()
    if not line: break
    line = line.strip()
    arr0.append(line)

print "Sorting......\n"

#processing start
quick_start_time = time.time()
quick_sort(arr0)
print arr0
quick_end_time = time.time() 


#print processing time
quick_time = quick_end_time - quick_start_time

print 'bubble sort time: ',bubble_time
print 'quick sort time: ',quick_time
