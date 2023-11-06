class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km, dostupne=True):
      self.znacka = registracni_znacka
      self.typ = typ_vozidla
      self.km = najete_km
      self.dostupne = dostupne
    

#zkontroluje, jestli je vozidlo aktuálně volné. Pokud je volné, změní hodnotu atributu dostupne, který určuje, zda je vozidlo půjčené, a vrátí text "Potvrzuji zapůjčení vozidla". Pokud je vozidlo již půjčené, vrátí text "Vozidlo není k dispozici"
    def pujc_auto(self):
        if self.dostupne:
            self.dostupne = False
            return f"Potvrzuji zapůjčení vozidla "
        else:
           return f"vozidlo není k dispozici "
        
    def get_info(self):
      return f"Registrační značka: {self.znacka}, Typ vozidla: {self.typ}, Najeté kilometry: {self.km}, dostupnost {self.dostupne}"
#metoda vrat auto
    
    def vrat_auto(self, stav_tachometr, pocet_dni):
       self.stav_tachometr = stav_tachometr
       self.pocet_dni = pocet_dni
       self.dostupne = True
       if pocet_dni < 7:
            cena_na_den = 400
       else:
            cena_na_den = 300
       celkova_cena = cena_na_den * pocet_dni   
       return f"celková cena za půjčení je {celkova_cena} Kč."
          
auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253)

#dotaz na uživatele, jakou značku si přeje půjčit      
zadana_znacka = input("Jakou značku auta si přejete vypůjčit: ")

if zadana_znacka == "Peugeot":
   print(auto1.get_info())
   print(auto1.pujc_auto())
elif zadana_znacka == "Škoda":
   print(auto2.get_info())
   print(auto2.pujc_auto())
else:
   print("naplatná značka ")

#vrat auto
pocet_dni = int(input("Počet dní zapůjčení auta: "))
stav_tachometr = int(input("zadej stav tachometru: "))
print(auto1.vrat_auto(stav_tachometr, pocet_dni))
