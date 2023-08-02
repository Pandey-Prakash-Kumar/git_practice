try:
 numerator=50
 denom=int(input("Enter the denominator: "))
 print (numerator/denom)
 print ("Division performed successfully")
except ZeroDivisionError:
 print ("Denominator as ZERO is not allowed")
except ValueError:
 print ("Only INTEGERS should be entered")
else:
     print("Inside else")
finally:
    print("Inside Finally")
     
