
while True:
    tal = int(input("Ange ett tal"))

    if tal > 10:
        print("Talet är för stort")
    elif tal < 10:
        print("Talet är för litet")
    else:
        print("Du matade in rätt tal")
        break