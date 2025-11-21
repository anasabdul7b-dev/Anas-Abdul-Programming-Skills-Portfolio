# EXERCISE 7 - Some Counting

# Count up from 0 to 50 in increments of 1
print("\nCounting up from 0 to 50:")
for i in range(0, 51, 1): # range(start, stop+1, step)
    print (i)

# Count down from 50 to 0 in decrements of 1
print("\nCounting down from 50 to 0:")
for i in range(50, -1, -1): # range(start, stop-1, step)
    print(i)

# Count up from 30 to 50 in increments of 1
print("\nCounting up from 30 to 50:")
for i in range(30, 51, 1):
    print(i)

# Count down from 50 to 10 in decrements of 2
print("\nCounting down from 50 to 10 by 2s:") 
for i in range(50, 9, -2): # Step of -2 for every second number
    print(i)

# Count up from 100 to 200 in increments of 5
print("\nCounting up from 100 to 200 by 5s:")
for i in range(100, 201, 5): # Step of 5 to increment by 5 each time
    print(i)