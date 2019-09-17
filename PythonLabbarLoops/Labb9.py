
namn=""
gatuadress=""
postnummer=""
postort=""

while(namn == "" or gatuadress == "" or postnummer=="" or postort==""):
    if namn == "":
        namn = input("Ange namn")
    if gatuadress == "":
        gatuadress = input("Gatuadress")
    if postnummer == "":
        postnummer = input("Postnummer")
    if postort=="":
        postort = input("Postort")

print("Alla uppgifter ifyllda")