# 1. Print all even numbers from 10 to 20 (inclusive) using range() without any loop
print(*range(10, 21, 2))

# 2. Keep asking the user to enter a positive number until they enter 0 (simulate do-while)
number = -1
while number != 0:
    number = int(input("Enter a positive number (0 to stop): "))

# 3. Calculate the factorial of a number using a while loop
num = int(input("Enter a number to calculate its factorial: "))
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print(f"The factorial is: {factorial}")

# 4. Assign a grade based on the score using nested if-else
score = int(input("Enter the score: "))
if score > 90:
    grade = 'A'
else:
    if score > 80:
        grade = 'B'
    else:
        if score > 70:
            grade = 'C'
        else:
            if score > 60:
                grade = 'D'
            else:
                grade = 'F'
print(f"Your grade is: {grade}")

# 5. Ask the user to enter a number from 1 to 7 and print the day of the week using match-case
day_number = int(input("Enter a number from 1 to 7: "))
match day_number:
    case 1: print("Monday")
    case 2: print("Tuesday")
    case 3: print("Wednesday")
    case 4: print("Thursday")
    case 5: print("Friday")
    case 6: print("Saturday")
    case 7: print("Sunday")
    case _: print("Invalid input")

# 6. Manage a list of student scores and perform operations
scores = []
scores.append(85)
scores.append(90)
scores.append(78)
scores.append(92)
scores.append(88)

scores.insert(2, 80)
scores.remove(92)
scores.sort()
scores.reverse()

print(f"Maximum score: {max(scores)}")
print(f"Minimum score: {min(scores)}")

if 90 in scores:
    print("90 is in the list")

print(f"Total number of scores: {len(scores)}")
print(f"First three scores: {scores[:3]}")

for score in scores:
    print(score)

print(f"Last element: {scores[-1]}")
scores[2] = 95
scores_copy = scores.copy()

print(f"Original scores: {scores}")
print(f"Copied scores: {scores_copy}")
