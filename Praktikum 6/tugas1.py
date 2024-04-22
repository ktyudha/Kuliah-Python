import time

def print_time(process, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (process, time.ctime(time.time())))

print_time("Proses-1", 2)
print_time("Proses-2", 4)