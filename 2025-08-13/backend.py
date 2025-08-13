# ==============================
# 📚 WHAT I HAVE LEARNED TODAY
# ==============================
# 1. Type Casting → int(), float(), str() to convert values.
# 2. Random Module →
#    - random.randrange(a, b) → random int in range
#    - random.choice(list) → random list item
#    - random.shuffle(list) → shuffle in-place
#    - random.random() → random float 0.0–1.0
# 3. if / elif / else →
#    - elif = else if
#    - Indentation is critical
# 4. while loop →
#    - while <condition>: ...
#    - Can have else clause
# 5. Loop Control →
#    - break → exit loop
#    - continue → skip iteration
#    - pass → placeholder

# ==============================
# 🎯 CHALLENGE
# ==============================
# Create a program that:
# 1. Asks the user for their name.
# 2. Asks the user for a number.
# 3. Uses a while loop to count from 1 up to that number.
# 4. If the current count is equal to a random number between 1 and the user’s number:
#       - Print "Lucky number hit!"
#       - Use break to stop the loop.
# 5. If the loop finishes without hitting the lucky number:
#       - Print "Better luck next time!"
#
# Bonus:
# - Use continue to skip printing even numbers.

import random
user_input = (input("What is your name: "))
user_int = int(input("What is your number: "))
num = 1
check = False
while num != user_int:
    if num == random.randint(1, 1000):
        print("Lucky number hit!")
        check = True
        break
    elif num % 2 == 0:
        num = num+1
        continue
    else:
        print(num)
        num = num+1

if check == False:
    print("Better luck next time")


# this is a just a working code first thing tomorrow i will work on making this code better
