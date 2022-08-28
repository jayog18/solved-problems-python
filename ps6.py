cu=2022 
while (True):
  age=int(input("enter your age : "))
  if age>0 and age<100:
    r=100-age
    e=cu+r
    print("you will turn 100 in year",e)
  if age>100:
    print("you are already 100")
