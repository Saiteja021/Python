year = int(input("Which year do you want to check? "))  

if year % 400 == 0:
     print("Leap Year")
elif year % 100 == 0:
     print("Not leap year") 
elif year % 4 == 0:
     print("Leap Year") 
else:
     print("Not leap year") 