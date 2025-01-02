sum = 0
zaehler_ungerade = 0
zahl1 = int(input("gib eine Zahl ein: "))
zahl2 = int(input("gib eine Zahl ein: "))
for i in range(zahl1, zahl2 + 1):
    if i % 2 != 0:
        zaehler_ungerade += 1
        sum += i


print(f"die summer ist {sum}")
print(f"die Anzahl der ungeraden Zahlen {zaehler_ungerade}")
