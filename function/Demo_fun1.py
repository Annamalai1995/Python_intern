# def city():
#     ans=input("Enter the favourite city")
#     if ans=='salem':
#         print("Mango city or Steel city")
#     elif ans=='Manali':
#         print("Manali to coolest place")
#     elif ans=='Kashmir':
#         print("Apple ")
#     else:
#         print("what ever you go")
# city()                   




#List start =0, n-1 
bal=[12000,5000,25000,65000]
def debit(money=0,pos=0):
    if money<=bal[pos]:
        bal[pos]-=money
        print(money,'debited')
        return bal[pos]
    else:
        print("can't debit")
res=debit(1000,1)
print(res)        