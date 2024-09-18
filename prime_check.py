def prime_check(n):
    count=0
    i=1
    while(i<=n):
        if(n%i==0):
            count+=1
        i+=1

    if(count==2):
        print("prime")
    elif(count>2):
        print("composite")
    else:
        print("neither prime nor composite")
n=int(input("Enter a number:")) 
prime_check(n)       
        