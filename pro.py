while True:
 total=0
 customer_name= input("Enter your name: ")
 while True:
  items=int(input("Enter the number of items: "))
  quantity= int(input("Enter the quantity of items: "))
  total= quantity*items
  repeat=input("Do you wish to add more items to the cart?(y,Y,n,N)")
  if repeat=="n" or repeat=="N":
   print("Name of the customer: ", customer_name)
   print("Your Bill costs: ", total)
   print()
   print("****Thank you for shopping with us!****")
   print("       ***Have a good day!***")
  else:
   print("Okay then* Enjoy your shopping and come back for billing")
   break
  break
 new_customer=input("Any customer in the queue?(Y,y,n,N)")
 if new_customer=="n" or new_customer=="N":
  break
