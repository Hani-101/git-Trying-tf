# countdown timer

import time

my_timer = int(input("Enter the time in seconds: "))

for H in range(my_timer, 0, -1):
    seconds = H % 60
    minutes = int(H / 60) % 60
    hours = int(H / 3600) 
    print(f"{hours:2d}:{minutes:2d}:{seconds:2d}")
    time.sleep(0.5)

    
print("time's up broooooooooooooooo")