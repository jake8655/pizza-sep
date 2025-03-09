# Práca so súborom
Naprogramoval som program, ktorý spravuje systém na objednávanie pizze z reštaurácie.

## Obsah
1. [Úvod](#úvod)
1. [Zobrazenie objednávok](#zobrazenie-objednávok)
1. [Pridanie objednávky](#pridanie-objednávky)
1. [Hľadanie objednávky podľa mena](#hľadanie-objednávky-podľa-mena)
1. [Hľadanie objednávky podľa typu pizze](#hľadanie-objednávky-podľa-typu-pizze)
1. [Odstránenie objednávky podľa mena](#odstránenie-objednávky-podľa-mena)
1. [Zobrazenie celkovej sumy](#zobrazenie-celkovej-sumy)
1. [Záver](#záver)

### Úvod
Zadanie je vytvoriť program, ktorý v **CLI** forme umožňuje užívateľom nasledovať nasledovné operácie:
- Zobraziť všetky objednávky
- Pridať novú objednávku
- Hľadať objednávky podľa mena objednávateľa
- Hľadať objednávky podľa typu pizze
- Odstrániť objednávku podľa mena objednávateľa
- Zobraziť celkovú sumu všetkých objednávok

Program som vytváral v jazyku **Python** vo vývojovom prostredí _Visual Studio Code_ a _Neovim_.
Na ukľadanie údajov som použil súbor typu `JSON` uložený na disku.
Využívam modul kňižnicu `json` pre čítanie a zápis JSON súborov.

### Zobrazenie objednávok
Na zobrazenie všetkých objednávok potrebujeme prečítať súbor databázy a vypísať správne údaje pre každú objednávku.
```py
with open(umiestnenie_do_súboru) as file:
    data = json.load(file)
    for entry in data:
        print(
            f"""Meno: {entry["name"]}
Adresa: {entry["address"]}
Typ: {entry["type"]}
Velkost: {entry["size"]}
Cena: {entry["price"]}
Telefon: {entry["phone"]}"""
        )
        print("----------------")
```

### Pridanie objednávky
Pre pridanie novej objednávky potrebujeme vyžiadať užívateľa o príslušné údaje.
Tieto údaje zložíme do slovníka pridáme na koniec dát v súbore databázy.
```py
name = input("name: ")
address = input("address: ")
phone = input("phone: ")
typ = input("type: ")
size = input("size: ")
price = random.randint(8, 19)
order = {
    "name": name,
    "address": address,
    "type": typ,
    "size": size,
    "price": price,
    "phone": phone,
}
contents = []

with open(umiestnenie_do_súboru) as file:
    contents = json.load(file)
    contents.append(order)
with open(umiestnenie_do_súboru, "w") as file:
    json.dump(contents, file)
```

### Hľadanie objednávky podľa mena
Pre hľadanie objednávky podľa mena potrebujeme vyžiadať užívateľa o meno, ktoré chce vyhľadať.
Následne načítáme súbor databázy do pamäte a vypíšeme vhodné údaje všetkých objednávok so zadaným menom.
```py
name = input("enter name: ")

with open(umiestnenie_do_súboru) as file:
    data = json.load(file)

    for entry in data:
        if entry["name"] == name:
            print(
                f"""Meno: {entry["name"]}
Adresa: {entry["address"]}
Typ: {entry["type"]}
Velkost: {entry["size"]}
Cena: {entry["price"]}
Telefon: {entry["phone"]}"""
            )
            print("----------------")
```

### Hľadanie objednávky podľa typu pizze
Táto funkcionalita je veľmi podobná predošlej.
Potrebujeme vyžiadať užívateľa o typ pizze, podľa ktorého chce hľadať.
Potom rovnako načítame súbor databázy a vypíšeme údaje vhodných objednávok.
```py
pizza_type = input("enter type: ")

with open(umiestnenie_do_súboru) as file:
    data = json.load(file)

    for entry in data:
        if entry["type"] == pizza_type:
            print(
                f"""Meno: {entry["name"]}
Adresa: {entry["address"]}
Typ: {entry["type"]}
Velkost: {entry["size"]}
Cena: {entry["price"]}
Telefon: {entry["phone"]}"""
            )
            print("----------------")
```

### Odstránenie objednávky podľa mena
Pre túto funkcionalitu potrebujeme vyžiadať užívateľa o meno, ktoré chce odstrániť.
Načítame súbor databázy do pamäte a odstránime objednávky, ktoré obsahujú zadané meno.
Následne uložíme vyfiltrované dáta do súboru.
```py
name = input("meno: ")

data = []

with open(umiestnenie_suboru) as file:
    data = json.load(file)

result = filter(lambda x: x["name"] != name, data)

with open(umiestnenie_suboru, "w") as file:
    json.dump(result, file)
```

### Zobrazenie celkovej sumy
Na zobrazenie celkovej sumy všetkých objednávok potrebujeme načítať súbor databázy do pamäte.
Následne sčítame cenu všetkých objednávok a do jednej premennej uložíme výsledok.
Tento výsledok napokon vypíšeme.
```py
with open(umiestnenie_suboru) as file:
    data = json.load(file)
    total = sum(entry["price"] for entry in data)

    print(f"Celková suma: {total}")
```

### Záver
Program som otestoval a funguje podľa očakávaných výsledkov.

V tomto stave program načíta celý obsah súboru databázy pri každej operácii.
Táto metóda vyzerá byť pohodlná a jednoduchá, a pri takomto množstve dát slúží bez problémov.
Pri väčšóm množstve dát by táto metóda nebola vhodná a praktická.
Súborový typ `JSON` funguje na princípe, kde na jeho čítanie a upravenie je potrebné prečítať celý obsah súboru a väčsinou aj ho uložiť do pamäte programu.
Ak sa chceme vyhnúť týmto problémom, môžeme použiť inú metódu na ukladanie dát, ako napríklad súbor typu `CSV` alebo skutočnú databázu napríklad `SQLite`.

V zdrojovom kóde samotného programu tiež vidím príležitosť na prečistenie kódu lepšie zorganizovanie.
Keďže náročnosť a veľkosť tohto projektu je veľmi malá, tak som sa rozhodol nechať kód v takom stave, v akom je.

V programe vidím príležitosť na zlepšenie užívateľského rozhrania.
V tomto stave program funguje výhradne v móde `CLI` a jeho nie je triviálne pre priemerného užívateľa.
Na vylepšenie by som tento stav programu upravil na server, ktorý spracuváva žiadosti užívateľov a odpovedá na nich.
Následne by som vytvoril webové/desktop/mobilové rozhranie, ktoré by užívateľom pomohlo viac efektívne a priaznivo vykonať svoju prácu.

Celkovo som s úlohou nemal problémy a aj som sa naučil veľmi základné metódy na pracovanie s `JSON` dátami v programovacom jazyku `Python`.
