# 1 vytvoření emailové adresy
jmeno = "sona"
email = "@czechitas.cz"
print (jmeno + email)

# 2 bonus 
jmeno_a_prijmeni = input("Zadej své jméno a příjmení: ")
#všechna velká
print (jmeno_a_prijmeni.upper())
# všechna malá
print (jmeno_a_prijmeni.lower())

# první velké ostatní malá
jmeno = input("Zadej jmeno:" )
prijmeni = input("Zadej prijmeni:" )
print (jmeno.capitalize() + " " + prijmeni.capitalize())

# iniciáy
print(jmeno[0].upper() + ". " +  prijmeni[0].upper() + ". ")

#zkrácené
if len(jmeno) > 5:
    print(jmeno[0].upper() + ". " + prijmeni.capitalize())
else:
    print (jmeno.capitalize() + " " + prijmeni.capitalize())