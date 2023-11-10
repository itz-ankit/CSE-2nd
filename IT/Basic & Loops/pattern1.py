b=0
a=9
for i in range(5):
    for j in range(b):
        print(" ",end="")
    for k in range(a):
        print("* ",end="")
    print("\r")    
    a=a-2
    b+=1

'''

* * * * * * * * * 
 * * * * * * *
  * * * * *
   * * *
    *

'''