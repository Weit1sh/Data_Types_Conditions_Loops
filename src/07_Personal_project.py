print("Hello! What is your name?")
name = input(">>> ")
print("Hello, " + name + "!")
print("Today we have products with barcodes 8790, 6734, 3298.")
print("Write the desired barcode: ")
products = int(input(">>> "))
if products == 8790:
    print("Its price 80 pounds.")
elif products == 6734:
    print("Its price 30 pounds.")
elif products == 3298:
    print("Its price 60 pounds.")
else:
    print("Today we don't have product with whis barcode.")
    exit()
another = input("Do you need anything else?: ")
another = another.lower()
while another == "yes":
    print("Write the desired barcode: (For stop type 10000)")
    products = int(input(">>> "))
    if products == 8790:
        print("Its price 80 pounds.")
    elif products == 6734:
        print("Its price 30 pounds.")
    elif products == 3298:
        print("Its price 60 pounds.")
    elif products == 10000:
        print("Bye, bye!")
        break
    else:
        print("Today we don't have product with whis barcode.")
if another == "no":
    print("Bye, bye!")
