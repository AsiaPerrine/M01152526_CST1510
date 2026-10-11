# Week 3 — Extra Practice Projects

---

## Rock, Paper, Scissors

# step 1 
import random

# Step 2
def get_computer_choice():

# step 3 and 4
    number = random.randint(0, 2)
    if number == 0:
        return "rock"
    elif number == 1:
        return "paper"
    else:
        return "scissors"

# Step 5 to 8
def decide_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "rock" and computer_choice == "scissors") or
         (user_choice == "paper" and computer_choice == "rock") or 
         (user_choice == "scissors" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"


# Step 9
user_choice = input("Enter rock, paper, or scissors: ").lower()

# Step 10
computer_choice = get_computer_choice()

# Step 11
print(f"Computer picked: {computer_choice}")

# Step 12
winner = decide_winner(user_choice, computer_choice)

# Step 13
if winner == "draw":
    print("It's a draw!")
elif winner == "user":
    print("You win!")
else:
    print("Computer wins!")



**Uses:** functions, `return`, `random.randint()`

1. At the top of your file, write `import random`.
2. Define a function called `get_computer_choice()`.
3. Inside it, create a variable `number` and set it to `random.randint(0, 2)`.
4. Use `if`/`elif`/`else` to check `number`:
   - if it is `0`, return `"rock"`
   - if it is `1`, return `"paper"`
   - otherwise, return `"scissors"`
5. Define a function called `decide_winner(user_choice, computer_choice)`.
6. Inside it, if `user_choice` equals `computer_choice`, return `"draw"`.
7. Add an `elif` that returns `"user"` if the user wins
   (rock beats scissors, paper beats rock, scissors beats paper).
8. Add an `else` that returns `"computer"`.
9. Outside the functions, use `input()` to ask the user for their choice
   and store it in a variable called `user_choice`.
10. Call `get_computer_choice()` and store the result in `computer_choice`.
11. Print the computer's choice.
12. Call `decide_winner(user_choice, computer_choice)` and store the result
    in `winner`.
13. Print who won.

---

## Calculator

# Step 1 to 4
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Step 5
n1 = float(input("Enter first number: "))

# Step 6
keep_going = True

# Step 7
while keep_going:
    # Step 8 to 9 
    operator = input("Pick an operator (+ - * /): ")
    n2 = float(input("Enter next number: "))

    # Step 10
    if operator == "+":
        result = add(n1, n2)
    elif operator == "-":
        result = subtract(n1, n2)
    elif operator == "*":
        result = multiply(n1, n2)
    elif operator == "/":
        result = divide(n1, n2)
    else:
        print("Invalid operator!")
        continue

    # Step 11
    print(f"{n1} {operator} {n2} = {result}")

    # Step 12 to 14
    choice = input(f"Type 'y' to continue with {result}, or 'n' to start over: ").lower()
    
    if choice == "y":
        n1 = result
    else:
        n1 = float(input("Enter new first number: "))



**Uses:** functions, parameters, `return`, calling one function from another

1. Define a function `add(n1, n2)` that returns `n1 + n2`.
2. Define a function `subtract(n1, n2)` that returns `n1 - n2`.
3. Define a function `multiply(n1, n2)` that returns `n1 * n2`.
4. Define a function `divide(n1, n2)` that returns `n1 / n2`.
5. Use `input()` to ask for the first number. Convert it with `float()` and
   store it in `n1`.
6. Create a variable `keep_going` and set it to `True`.
7. Start a `while keep_going:` loop.
8. Inside the loop, ask for an operator (`+ - * /`) and store it in
   `operator`.
9. Ask for the second number, convert it with `float()`, and store it in `n2`.
10. Use `if`/`elif` to call the matching function and store the answer in
    `result`. For example, if `operator == "+"`, then `result = add(n1, n2)`.
11. Print the calculation and the result.
12. Ask the user: `"Type 'y' to continue with the result, or 'n' to start over:"`
13. If they type `"y"`, set `n1 = result`.
14. Otherwise, ask for a new first number and store it in `n1`.

**Extension, once you've done Week 4:** replace the `if`/`elif` in step 10
with a dictionary:
`operations = {"+": add, "-": subtract, "*": multiply, "/": divide}`
Then call `result = operations[operator](n1, n2)`.

---

## Number Guessing Game, upgraded

**Uses:** `random.randint()`

1. Open your Week 2 guessing game.
2. Add `import random` at the top of the file.
3. Find the line where you set the secret number.
4. Replace the fixed number with `random.randint(1, 100)`.
5. Run the game a few times and check that the secret number changes each time.

---

Stuck on why a function returning nothing gives you `None`? That's
`01 - Defining and Calling Functions`, section 4, in this folder.