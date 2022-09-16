while True :
  a=int(input("enter number of working days :"))
  e=int(input("enter number of absent days : "))
  x=a-e
  p=x*100/a
  print("ypur attendencde is ",p)
  if p>=75 :
    print("you can sit in exam")
  else :
    print("you can't sit ")
