correctUserName = "abc123"
correctPwd = "secretPassword"

while True:
    userName = input("Ange användarnamn")
    pwd = input("Ange password")
    if userName == correctUserName and pwd == correctPwd:
        print("Du är inloggad")
        break
    if userName != correctUserName:
        print("Fel användarnamn")
    if pwd != correctPwd:
        print("Fel lösen")
    if input("Vill du fortsätta") != "J":
        break