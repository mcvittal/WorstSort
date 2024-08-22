import terriblesort 

x = input("Enter a value (Leave blank to end input): ")
l = []
while x != "":
    try:
        xint = int(x)
        l.append(xint)
        x = input("Enter a value (Leave blank to end input): ")

    except:
        break

print(terriblesort.sort(l))



