# Задание 1
print("Задание 1")
print("В строке есть слово Строка?", "Строка" in "В строке есть слово Строка?")

# Задание 2

print()
print("Задание 2")
number = int(input("Enter number: "))

if number % 2 == 0 and number % 3 == 0:
    print("Yes")
else:
    print("No")

# Задание 3

print()
print("Задание 3")
print("Winter" if int(input("Enter number of month: ")) in {1, 2, 12} else "Not winter")

# Задание 4
print()
print("Задание 4")
print("Morning" if 6 <= int(input("Enter hour: ")) <= 12 else "Not morning")

# Задание 5
print()
print("Задание 5")
print([4, 8] in [5, 6, 7, 8, 9])