list=[]

def myfunction(inp):
    list.append(inp)
    

print("How many Items in List")
n=int(input())
print("Add Items in List")
for i in range(0,n):
    inp=input()
    myfunction(inp)

print(list)