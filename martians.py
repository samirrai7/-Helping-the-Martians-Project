import random



kg = [300, 250, 163]
locations = [random.randint(1, 10) for _ in range(3)]


print("Hello!")
print("Your need to find locations of 3 boxes.")
print("Each time you guess wrong, the boxes relocate!")



while True:
    chance = []
    for i in range(3):
        user = int(input(f"Enter your guess for box {i + 1} (1-10): "))
        chance.append(user)
    
    if chance == locations:
        print("Good job,you found the boxes")
        print(f"Total weight recovered: {sum(kg)} kg")
        break
    else:
        print("Wrong answers,try again.")
        locations = [random.randint(1, 10) for _ in range(3)]
