lst = []
import random
import time
start_time = time.time()
for i in range(1000):
    r = random.randint(1, 10)
    lst.append(r)
end_time = time.time()
print(lst)

print("Executed in ", start_time-end_time)
