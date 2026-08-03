import time

my_time=int(input("Enter the time in seconds:"))

for i in range(my_time,0,-1):
    sec=i%60
    min=int((i/60)%60)
    hou=int((i/3600)%24)
    print(f"{hou:02}:{min:02}:{sec:02}")
    
    time.sleep(1)

print("Time's up!")