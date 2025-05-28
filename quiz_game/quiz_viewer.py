from base_quiz_game import BaseGame
from colorama import Fore, Style
import random

class QuizViewer(BaseGame):
    
    def quiz_user(self):
        questions = self.load_questions()
        if not questions:
            print(Fore.YELLOW + "No questions available to quiz.")
            return

        score = 0
        total_questions = min(5, len(questions))
        asked_questions = random.sample(questions, total_questions)

        print(Style.BRIGHT + Fore.YELLOW + "\n ☆Quiz Time! ☆ ---")

        for index, question in enumerate(asked_questions, 1):
            print(f"\nQuestion {index}:")
            print(Style.BRIGHT + Fore.GREEN + question['question'])
            print(f"A. {question['A']}")
            print(f"B. {question['B']}")
            print(f"C. {question['C']}")
            print(f"D. {question['D']}")
            user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()

            if user_answer == question['answer']:
                print(Fore.GREEN + "Correct! ⚡︎")
                score += 1
            else:
                print(Fore.RED + f"Wrong! The correct answer was {question['answer']}.")

        print(Style.BRIGHT + Fore.BLUE + f"\nYou got {score} out of {total_questions} correct!")


    