# Parādīt ledusskapja saturu un piedāvāt ielikt kaut ko

my_list = ["Ābols", "Banāns", "Piens", "Maize", "Olas"]
print(f"Pašlaik ledusskapī ir {my_list}")

# Piedāvāt ielikt ledusskapī kādu produktu (Y/N)

def ledusskapis():

    ielikt = input("Vai Tu gribi ievietot ledusskapī produktu? Y/N ")
    if ielikt.upper() == "Y":
        added = input("Ievieto ledusskapī nopirko produktu! ")
        my_list.append(added)
        print(f"Tagad ledusskapī ir šādi produkti: {my_list}")


#Nevar izņemt to kā nav
    elif ielikt.upper() == "N":
        removed = input(f"Tagad ledusskapī ir šādi produkti: {my_list}, ko Tu gribi izņemt? ")
        print(my_list.index("Maize")) # hardcoded
        my_list.remove(removed.casefold().capitalize())
        print(my_list)


    else:
        print("Pieprasījums nav atpazīts!")
        ledusskapis()

ledusskapis()
# Parādīt ledusskapja saturu un piedāvāt izņemt laukā kaut ko
