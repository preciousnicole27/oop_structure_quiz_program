from colorama import init, Fore, Style
from quiz_viewer import QuizViewer

init(autoreset=True)

def main():
    quiz_viewer = QuizViewer()

    while True:
        print(Style.BRIGHT + "\n--⋆⭐︎.°✹ Welcome to the Quiz Program!𑕚---")
        print("A. Start Quiz")
        print("B. Exit")

        user_choice = input("Please choose an option (A/B): ").strip().upper()

        if user_choice == "A":
            quiz_viewer.quiz_user()
        elif user_choice == "B":
            print(Fore.BLUE + "Thank you for using the Quiz Program.")
            break
        else:
            print(Fore.RED + "Invalid input. Please try again.")

if __name__ == "__main__":
    main()
