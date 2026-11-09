num = int(input("enter a number :"))
if num > 1 :
    for i in range(2,int(num ** 0.5)+ 1):
        if num% i == 0 :
          
          print("it is not a prime number")
          break4
    else : 
        print("it is a prime number")
else : 
    print("it is not a prime number")                