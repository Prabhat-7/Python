t1=int(input("Enter the first term of the fibonacci sequence:"))
t2=int(input("Enter the second term of the fibonacci sequence:"))
n=int(input("Enter upto which term u want to print the fibonacci sequence:"))
def fib_generator():
    global t1
    global t2
    while True:
        yield t1
        (t1,t2)=(t2,t1+t2)

fib=fib_generator()

def seq(n):
    return [next(fib) for i in range(n)]



# def fibonacci(n):
#     if(n==1):
#         return t1
#     if(n==2):             #This function returns the nth term
#         return t2
    
#     return fibonacci(n-1)+fibonacci(n-2)

    
# def seq(n):
#     return [fibonacci(i+1) for i in range(n)] # This function creates the fibonacci sequence 
     

print(seq(n))  