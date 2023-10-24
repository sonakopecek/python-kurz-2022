teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

#seznam průměrných teplot pro každý den
prumer_teplot = [[sum(teplota)/len(teplota)] for teplota in teploty]

#seznam ranních teplot
ranni_teploty = [teplota[0] for teplota in teploty]

#seznam nočních teplot
nocni_teploty = [teplota[3] for teplota in teploty]

#seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu
poledni_a_nocni_teploty = [[teplota[1], teplota[3]] for teplota in teploty]

#slovník, který bude mít následující formát, kde klíčem bude den v týdnu, a hodnotou průměrná teplota ten den.
teploty = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]
import statistics

novy_slovnik = {teplota[0]: sum(teplota[1:])/(len(teplota)-1) for teplota in teploty}
#novy_slovnik = {teplota[0]: statistics.mean(teplota[1:]) for teplota in teploty}
print(novy_slovnik)