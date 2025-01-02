# list1 = [4, 5, 1, 0, 7, 9]

# # summer
# sum = 0
# for i in list1:
#     sum += i


# print(f"Summer ={sum}")

# # ungerade
# list_ungerade = []
# for i in list1:
#     if i % 2 != 0:
#         list_ungerade.append(i)
# print(f"ungerade liste {list_ungerade}")

# # die größte Zahl
# nb = 0
# for i in list1:
#     if nb < i:
#         nb = i
# print(f"die größte Zahl ist: {nb}")

imp_liste = []
sum = 0
zaehler_ungerade = 0
zahl1 = int(input("gib eine Zahl ein: "))
zahl2 = int(input("gib eine Zahl ein: "))
for i in range(zahl1, zahl2 + 1):
    if i % 2 != 0:
        zaehler_ungerade += 1
        imp_liste.append(i)
        sum += i


print(f"die summer ist {sum}")
print(f"die Anzahl der ungeraden Zahlen {zaehler_ungerade}")
print(imp_liste)
