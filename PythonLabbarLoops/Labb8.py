def GetIntValue():
    while True:
        try:
            val = int(input("Ange ett värde"))
            return val
        except:
            print("Ange ett TAL för sjutton")
    

tal = GetIntValue()
if tal > 30:
    print("Du har matat in ett ogiltigt tal")
else:
    for i in range(tal,30):
        print(i+1)

