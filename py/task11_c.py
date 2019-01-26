ui = int(input("Enter potential prime number here: "))
if ui > 1:
    for i in range(2, ui):
        if ui % i == 0:
            print(ui, "is not prime")
        else:
            print(ui, "is a prime number")
