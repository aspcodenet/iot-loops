
#Alt 1
tal = int(input("Ange ett tal"))

for i in range(1,tal):
    print(i)


for i in range(tal-1,0,-1):
    print(i)

#Alt 2
tal = int(input("Ange ett tal"))

num =tal-1
while num > 0:
    print(num)
    num=num-1