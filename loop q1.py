n=int(input("Enter the number of terms for fibonacci series:"))
n1=0
n2=1
i=0
if n==1:
    print(n1)
else:
    while i<n:
        print(n1,end=',')
        n3=n1+n2
        n1=n2
        n2=n3
        i=i+1
