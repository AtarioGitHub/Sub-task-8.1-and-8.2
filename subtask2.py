l1=[]

counter=int(input("Enter the length of your list: "))
print("Enter your list:")

for i in range(counter):
    m=int(input())
    l1.append(m)

l1.append(-1)

length=len(l1)    
s= sum(l1)
Max=max(l1)
avg=s/length

if length==0:
    m=-1
    a=-1

print("n=",length,"s=",s,"m=",Max,"a=",avg)
print("l1 is: ",l1)