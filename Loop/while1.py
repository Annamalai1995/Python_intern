# LOOPING
# i=1 
# while(i<=5):
#     i+=1
#     print(i)

seats=1
while seats<=10:

    amt=int(input("Tell us amount "))

    if amt>=190:

     print("Ticket Booked @",seats)
     seats+=1
    else:
       print("Insuffcicent balance")