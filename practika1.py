# Задание 1

print("The number of books on the media: %s" % (int(float(input("Enter the storage capacity (in MB): ")) * 1048576) // (
            int(input("Number of bytes per character: ")) * int(
        input("Enter the number of characters per line: ")) * int(input("Enter the number of lines per page: ")) * int(
        input("Enter the number of pages in the book: ")))))

# Задание 2

print()
mode = input("Enter calc mode(circle, square): ")
if mode == "circle":
    radius = float(input("Enter the radius(may in float): "))
    print("Area: %s " % float(3.1415 * radius ** 2.0))
    print("Length: %s" % float(2.0 * 3.1415 * radius))
elif mode == "square":
    side = float(input("Enter the side size(may in float): "))
    print(f"Perimeter: {float(4 * side)}")
    print(f"Area: {float(side ** 2)}")

# Задание 3

print()
print('0' * 20 + '1' * 50 + '2' * 30)

# задание 4

print()
paid_data = (500 - (float(input('Enter the speed in kb/s: ')) * float(input("Enter the download time: ")))) * float(
    input("Introduction the cost of one kilobyte: "))
print("You need to pay: %s" % paid_data if paid_data < 0 else "No payment is required")

# Задание 5

print()
length = float(input("Enter length: "))
width = float(input("Enter width: "))
perimetr = length * width
print(perimetr)

# Задание 7

print()
all_hour = int(input("Enter the number of hours: "))
days = all_hour // 24
hours = all_hour - (days * 24)
print(f"Days: {days}")
print(f"Hours: {hours}")

# Задание 8

print()
list_players = ['Frost', 'IvanGuy', 'Mood']
last_player = list_players[len(list_players) - 1]
reestr = {'First': 'Frost', 'Second': 'IvanGuy', 'Third': 'Mood'}
print(f"Last player: {last_player}")
print(f"First player: {reestr['First']}")

# Задание 9

print()
fruits = ["лимонка", "бананчик", "Яблочко", "лаймик"]
incorrect_word = fruits[2]
correct_word = "а" + incorrect_word[1:]
fruits[2] = correct_word
print(fruits)