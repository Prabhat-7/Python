li_smallest=[]
n=input("Enter a multiple digit number:")

for i in n:
   li_smallest.append(i)

li_greatest=li_smallest.copy()
li_greatest.sort(reverse=True)
li_smallest.sort(reverse=False)

def confirm(list,idx):
   
    if list[idx]=="0":
        confirm(list,idx+1)
        list[idx]=list[idx+1]
        list[idx+1]="0"
          
    else:
        return   
   
confirm(li_smallest,0)
n=""
for i in li_smallest:
    n+=i
smallest=n
print("The smallest number with those digits=",smallest)    
n=""
for i in li_greatest:
    n+=i
greatest=n
print("The greatest number with those digits=",greatest)  