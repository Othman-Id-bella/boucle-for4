N=int(input("enter nomber:"))
S=1
j=1
for i in range(N):
    S=S+j**2
    j=j+2
print("the sum of the numbers is;",S)