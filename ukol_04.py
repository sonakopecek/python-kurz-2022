#Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát
def spravne_tel_cislo(tel_cislo):

    if tel_cislo[0:3] == "+420" and len(tel_cislo) == 13:
        return True
    
    elif len(tel_cislo) == 9:
        return True
    
    else:
        return False
    
#Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát
def cena_sms(text):

    pocet_zprav = len(text) // 180
    if len(text) < 180:
        pocet_zprav = 1

    cena = pocet_zprav * 3

    return cena

tel_cislo = input("Zadej telefonní číslo pro zaslání sms: ")
if spravne_tel_cislo(tel_cislo):
    text = input("Zadej text pro sms: ")
    cena = cena_sms(text)
    print(f"cena sms je: {cena}.")
else:
    print("telefonní číslo je v neplatné ")
