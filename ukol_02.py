#sklad součástek a jeho aktuální množství
sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
#software se nejprve zeptá na kód součástky
kod = input("Zadej kód součástky: ")
#pokud je kód součástky na skladě, zeptá se na požadované množství
if kod in sklad:
    zadane_mnozstvi = int(input("Zadej množství: "))
    #pokud je na skladě menší než požadované množstí, vypíše kolik je na skladě
    if sklad[kod] < zadane_mnozstvi:
      print (f"Lze prodat pouze omezené množství - {sklad[kod]} ks")
      #a smaže kod součástky ze skladu
      sklad.pop(kod)
      #kontrola jestli je smazáno
      print(sklad)    
    #pokud je na skladě a je jí dostatek, vypíše, že je skladem a sníží počet součástek na skladě o požadované množství
    else:
      print ("Poptávku lze uspokojit v plné výši.") 
      sklad[kod] = sklad[kod] - zadane_mnozstvi 
      print(sklad)
#kód součástky není na skladě
else:
    print("Součástka není skladem.")
