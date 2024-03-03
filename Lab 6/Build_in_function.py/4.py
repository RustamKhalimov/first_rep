import time
x = int(input("Input integer :"))
y = int(input("Input time :"))
start1 = time.time()
start2 = time.sleep(y/1000)
if time.time() - start1 >= (y/1000) :
    print("Square root of" , x , "after" , y , "miliseconds is :" , x**(0.5))
