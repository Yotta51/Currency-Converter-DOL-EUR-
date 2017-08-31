dol_rate = 0.84072
eur_rate = 1.18957
what = input("Select (A) DOL->EUR or (B) EUR->DOL: ")
if what == "A" or what == "a":
    price1 = input("Enter a certain amount of US dollars: ")
    doltoeur = int(price1) * dol_rate
    print(doltoeur,"€")
elif what == "B" or what == "b":
    price2 = input("Enter a certain amount of EUROS: ")
    eurtodol = int(price2) * eur_rate
    print(eurtodol,"$")
else:
    print("Please enter one of the two options")
