pase = []

while True:
    print("\nVad vill du göra?")
    print("1. Visa saker")
    print("2. Lägg till en sak")
    print("3. Ta bort en sak")
    print("4. Avsluta")

    val = input("Välj 1-4: ")

    if val == "1":
        if len(pase) == 0:
            print("Påsen är tom.")
        else:
            print("I påsen finns:")
            for nummer in range(len(pase)):
                print(str(nummer + 1) + ". " + pase[nummer])

    elif val == "2":
        sak = input("Vad vill du lägga i påsen? ")
        pase.append(sak)
        print(sak + " lades i påsen.")

    elif val == "3":
        if len(pase) == 0:
            print("Påsen är tom.")
        else:
            print("Skriv numret på saken du vill ta bort:")
            for nummer in range(len(pase)):
                print(str(nummer + 1) + ". " + pase[nummer])

            val = input("Nummer: ")

            if val.isdigit():
                nummer = int(val)
                if nummer >= 1 and nummer <= len(pase):
                    sak = pase.pop(nummer - 1)
                    print(sak + " togs bort.")
                else:
                    print("Det numret finns inte.")
            else:
                print("Skriv ett nummer.")

    elif val == "4":
        print("Hej då!")
        break

    else:
        print("Välj en siffra mellan 1 och 4.")
