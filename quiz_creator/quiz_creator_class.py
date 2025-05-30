from quiz_base_questions import QuizBaseQuestions
from colorama import Fore

class QuizCreate(QuizBaseQuestions):
    def add_questions(self):
        while True:
            print(Fore.GREEN + "\nAdding a new question")
            question = input("Enter the question: ")
            choice_a = input("a.")
            choice_b = input("b.")
            choice_c = input("c.")
            choice_d = input("d.")
            answer = input("Correct answer a/b/c/d/:").strip().lower()

            if answer not in ('a', 'b', 'c', 'd'):
                print(Fore.RED + "Invalid answer")
                continue

            with open(self.filename, 'a') as file:
               file.write(f"Question:{question}\n")
            file.write(f"A. {choice_a}\n")
            file.write(f"B. {choice_b}\n")
            file.write(f"C. {choice_c}\n")
            file.write(f"D. {choice_d}\n")
            file.write(f"Answer: {answer.upper()}\n\n")
            
            again = input("Add a new question? (yes/no):").strip().lower()
            if again != 'yes.':
                break 

