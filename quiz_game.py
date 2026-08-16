import random

# Each dictionary contains the question text, answer choices, and correct option.
questions = [
    {
        "question": "What is Python?",
        "options": {
            "A": "A Programming Language",
            "B": "An Operating System",
            "C": "A Database",
            "D": "A Web Browser"
        },
        "answer": "A"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": {
            "A": "function",
            "B": "def",
            "C": "func",
            "D": "define"
        },
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": {
            "A": "//",
            "B": "/* */",
            "C": "#",
            "D": "<!-- -->"
        },
        "answer": "C"
    },
    {
        "question": "Which data type stores True or False?",
        "options": {
            "A": "String",
            "B": "Boolean",
            "C": "Integer",
            "D": "Float"
        },
        "answer": "B"
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": {
            "A": "display()",
            "B": "show()",
            "C": "print()",
            "D": "output()"
        },
        "answer": "C"
    },
    {
        "question": "Which function is used to get input from the user?",
        "options": {
            "A": "input()",
            "B": "get()",
            "C": "read()",
            "D": "scan()"
        },
        "answer": "A"
    },
    {
        "question": "Which data structure stores multiple values in an ordered collection?",
        "options": {
            "A": "List",
            "B": "Integer",
            "C": "Boolean",
            "D": "String"
        },
        "answer": "A"
    },
    {
        "question": "Which method converts a string to uppercase?",
        "options": {
            "A": ".upper()",
            "B": ".uppercase()",
            "C": ".up()",
            "D": ".capital()"
        },
        "answer": "A"
    },
    {
        "question": "Which loop is commonly used to iterate over a sequence?",
        "options": {
            "A": "if",
            "B": "for",
            "C": "try",
            "D": "def"
        },
        "answer": "B"
    },
    {
        "question": "Which keyword is used to create a loop that continues while a condition is true?",
        "options": {
            "A": "repeat",
            "B": "loop",
            "C": "while",
            "D": "during"
        },
        "answer": "C"
    },
    {
        "question": "Which operator is used for exponentiation in Python?",
        "options": {
            "A": "^",
            "B": "**",
            "C": "//",
            "D": "%%"
        },
        "answer": "B"
    },
    {
        "question": "What does len() return?",
        "options": {
            "A": "The largest value",
            "B": "The smallest value",
            "C": "The length or number of items",
            "D": "The data type"
        },
        "answer": "C"
    },
    {
        "question": "Which module is used to generate random values?",
        "options": {
            "A": "math",
            "B": "random",
            "C": "number",
            "D": "choice"
        },
        "answer": "B"
    },
    {
        "question": "Which keyword is used to handle exceptions?",
        "options": {
            "A": "catch",
            "B": "error",
            "C": "try",
            "D": "handle"
        },
        "answer": "C"
    },
    {
        "question": "Which file mode is used to read a file?",
        "options": {
            "A": "w",
            "B": "a",
            "C": "r",
            "D": "x"
        },
        "answer": "C"
    },
    {
        "question": "Which file mode is used to append data to a file?",
        "options": {
            "A": "r",
            "B": "w",
            "C": "a",
            "D": "x"
        },
        "answer": "C"
    },
    {
        "question": "Which collection stores data as key-value pairs?",
        "options": {
            "A": "List",
            "B": "Tuple",
            "C": "Dictionary",
            "D": "Set"
        },
        "answer": "C"
    },
    {
        "question": "Which keyword is used to exit a loop?",
        "options": {
            "A": "stop",
            "B": "exit",
            "C": "break",
            "D": "end"
        },
        "answer": "C"
    },
    {
        "question": "Which keyword skips the current iteration of a loop?",
        "options": {
            "A": "skip",
            "B": "continue",
            "C": "pass",
            "D": "next"
        },
        "answer": "B"
    },
    {
        "question": "Which symbol is used to compare two values for equality?",
        "options": {
            "A": "=",
            "B": "!=",
            "C": "==",
            "D": "=>"
        },
        "answer": "C"
    }
]


def ask_question(question):
    # Update shared score and progress values for this question.
    global score, correct, wrong, percentage, grade, n

    # Track and display the current question number.
    n+=1
    print("\n" + "-" * 50)
    print(f'Q.{n} ',question["question"])
    print("-" * 50)

    # Display each available answer choice.
    for option, text in question["options"].items():
        print(f"{option}. {text}")

    # Keep prompting until the player enters a valid option.
    while True:

        answer = input("\nYour answer (A/B/C/D): ").strip().upper()

        if answer in ["A", "B", "C", "D"]:

            # Check whether the selected option is correct.
            if answer == question["answer"]:
                print("Correct!")
                score += 1
                correct += 1
            else:
                wrong += 1

            break

        else:
            print("Invalid input. Please enter A, B, C, or D.")
            continue

    
    # Calculate the final percentage and grade after the last question.
    if correct + wrong == len(questions):

        percentage = (score / len(questions)) * 100

        if percentage >= 90:
            grade = "A"
        elif percentage >= 80:
            grade = "B"
        elif percentage >= 70:
            grade = "C"
        elif percentage >= 60:
            grade = "D"
        else:
            grade = "F"

def load_high_score():
    # Return the saved high score, or zero when no record exists yet.
    try:
        with open("highscore.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0
    
def save_high_score(score):
    # Save the latest high score to a local text file.
    with open("highscore.txt", "w") as file:
        file.write(str(score))
        
def high_score():
    # Show the previous record and save the score if it was beaten.
    high_score = load_high_score()
    print(f"Previous High Score: {high_score}/{len(questions)}")
    if score > high_score:
        print("New High Score!")
        save_high_score(score)
    else:
        print("High score not beaten.")

def play_game():
    # Reset all statistics before starting a new game.
    global score, correct, wrong, percentage, grade, n
    score = 0
    correct = 0
    wrong = 0
    percentage = 0
    grade = ""
    n = 0
    # Randomize question order for each round.
    random.shuffle(questions)
    for question in questions:
        ask_question(question)
    high_score()

def main():
    # Ask whether the player wants to start the quiz.
    choice = input("Do you want to play the quiz game? (Y/N): ").strip().upper()
    if choice == "Y":
        print("Welcome to the Python Quiz Game!")
        print("You will be asked 20 questions.")
        print("Type A, B, C, or D to answer each question.")
        # Continue offering rounds until the player chooses to quit.
        while True:
            play_game()
            print("---------------Final Score---------------")
            print(f"Total Questions: {len(questions)}")
            print(f"Correct Answers: {correct}")
            print(f"Wrong Answers: {wrong}")
            print(f"Score: {score}/{len(questions)}")
            print(f"Percentage: {percentage:.2f}%")
            print(f"Grade: {grade}")
            print("-" * 41)
            # Validate the replay response before acting on it.
            while True:
                choice = input("\nDo you want to play again? (Y/N): ").strip().upper()
                if choice == "Y":
                    break
                elif choice == "N":
                    print("Thanks for playing! Goodbye!")
                    print("-" * 50)
                    exit()
                else:
                    print("Invalid input. Please enter Y or N.")
    else:
        exit()

if __name__ == "__main__":
    # Start the game only when this script is run directly.
    main()
