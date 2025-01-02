list1 = [4, 5, 1, 0, 7, 9]

# summer
sum = 0
for i in list1:
    sum += i


print(f"Summer ={sum}")

# ungerade
list_ungerade = []
for i in list1:
    if i % 2 != 0:
        list_ungerade.append(i)
print(f"ungerade liste {list_ungerade}")

# die größte Zahl
nb = 0
for i in list1:
    if nb < i:
        nb = i
print(f"die größte Zahl ist: {nb}")
