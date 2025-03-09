import json
import random


def read_file():
    with open("./db.json") as file:
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


def append_order():
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

    with open("./db.json") as file:
        contents = json.load(file)
        contents.append(order)
    with open("./db.json", "w") as file:
        json.dump(contents, file)


def sum_money():
    with open("./db.json") as file:
        data = json.load(file)
        total = sum(entry["price"] for entry in data)

        print(f"All moni: {total}")


def search_by_name():
    name = input("enter name: ")

    with open("./db.json") as file:
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


def search_by_type():
    pizza_type = input("enter type: ")

    with open("./db.json") as file:
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


def remove_order():
    name = input("meno: ")

    data = []

    with open("./db.json") as file:
        data = json.load(file)

    result = list(filter(lambda x: x["name"] != name, data))

    with open("./db.json", "w") as file:
        json.dump(result, file)


def main_loop():
    try:
        with open("./db.json", "x") as file:
            file.write("[]")
    except FileExistsError:
        pass

    key = input(
        """r = read
a = add new order
s = search by name
p = search by pizza type
d = remove order by name
$ = moni
x = exit
"""
    )
    while key != "x":
        if key == "r":
            read_file()
        elif key == "a":
            append_order()
        elif key == "$":
            sum_money()
        elif key == "s":
            search_by_name()
        elif key == "p":
            search_by_type()
        elif key == "d":
            remove_order()
        else:
            print("Unkown action")

        key = input(
            """r = read
a = add new order
s = search by name
p = search by pizza type
d = remove order by name
$ = moni
x = exit
"""
        )


main_loop()
