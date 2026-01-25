def main():
    item = input("Item: ").title()

    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    while True:
        try:
            if item == menu["Baja Taco"]:
                return menu.get("Bajo Taco")
            elif item == menu["Bowl"]:
                return menu.get("Bowl")
            elif item == menu["Burrito"]:
                return menu.get("Burrito")
            elif item == menu["Nachos"]:
                return menu.get("Nachos")
            elif item == menu["Quesadilla"]:
                return menu.get("Quesadilla")
            elif item == menu["Super Burrito"]:
                return menu.get("Super Burrito")
            elif item == menu["Super Quesadilla"]:
                return menu.get("Super Quesadilla")
            elif item == menu["Taco"]:
                return menu.get("Taco")
            elif item == menu["Tortilla Salad"]:
                return menu.get("Tortilla Salad")
            
        except:
            continue


main()