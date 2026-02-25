# Use for loop to print numbers 1 to 10 but stop the number use break



for i in range(1 ,11):
    #   print(i)
      if i==7:
       break
      print(i)
      
# Print numbers 1 to 10 skipping the numbeers 5 (use continue)
# 
for i in range(1,10):
    # print(i)
    if i==5:
     continue      
    print(i)


# Write a loop that goes through numbers 1 to 5 but does nothing for number 3 (use pass)


for i in range(1,6):
   match i:
       case 1:
         print(1)
       case 2:
         print(2) 
       case 3:
         pass
       case 4:
         print(4)
       case 5:
         print(5)     
   
    