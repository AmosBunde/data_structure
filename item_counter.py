from collections import Counter

def get_items(product_purchased):

    counter = Counter(product_purchased)
    recurring_products = counter.most_common(3)
    return recurring_products



def main():

    product_purchased = ["DES005",
"EV003",
"ES004",
"DES001",
"DES002",
"DES003",
"DES002",
"DES002",
"STA004",
"SAL004",
"ENT005",
"BEV003",
"SAL002",
"ENT0052",
"SAL004",
"ENT004",
"ENT0041",
"DES004",
"BEV001",
"STA001",
"STA003",
"BEV002",
"STA003",
"DES005",
"BEV002",
"ENT004",
"ENT001",
"DES005",
"ENT004",
"STA005",
"ENT005",
"DES002",
"ENT001",
"SAL001",
"BEV001",
"DES002",
"EV0011",
"DES004",
"ENT004",
"DES001",
"STA005",
"DES004",
"ENT002",
"ES0012",
"ENT0022",
"ENT003",
"BEV001",
"DES004",
"STA005",
"STA003",
"SAL002",
"ENT001",
"SAL0042",
"STA005",
"ENT002",
"DES004",
"DES004",
"SAL001",
"BEV003",
"DES001"
    ] 
    print(get_items(product_purchased))




if __name__ == "__main__":
    main()