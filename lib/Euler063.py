
# import time module
import time

# time at the start of program execution
start =  time.time()

# counter to count the number of instances
counter = 0

# for loop to loop from 1 to 9
for i in range(1, 10):
    power = 1
    while True:
        if power <= len(str(i ** power)):
            counter += 1
        else:
            break
        power += 1

# print the number of instances found
print(counter)

# time at the end of program execution
end = time.time()

# total time taken for the program execution
print(end - start)
