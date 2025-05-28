from colorama import Fore, Style, init
from quiz_creator_class import QuizCreate
from quiz_viewer import QuizViewer


init(autoreset=True)

def main():
    creator = QuizCreate()
    viewer = QuizViewer()

    while True:
        print(Style.BRIGHT + "\nWelcome to Quiz Creator!")
        print("A. Add question")
        print("B. View questions")
        print("C. Remove question")
        print("D. Exit")

        choice = input("Choose an option (A/B/C/D): ").strip().upper()

        if choice == 'A':
            creator.add_questions()
        elif choice == 'B':
            viewer.view_questions()
        elif choice == 'C':
            viewer.remove_question()
        elif choice == 'D':
            print(Fore.MAGENTA + "Thank you!")
            break
        else:
            print(Fore.RED + "Invalid input. Please try again.")

if __name__ == "__main__":
    main()