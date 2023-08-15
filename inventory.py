from collections import Counter

def main():

    inventory = Counter(STAA001=20, SAL002=50, ENT004=60)
    sales = Counter(STAA001=10, SAL002=34, ENT004=20)
    inventory = inventory - sales
    new_inventory = {"STAOO1": 35, "SAL002":35, "ENT004": 23}
    inventory.update(new_inventory)

    print(inventory)


if __name__ == "__main__":
    main()