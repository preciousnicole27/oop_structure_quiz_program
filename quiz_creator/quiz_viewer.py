from quiz_base_questions import QuizBaseQuestions
from colorama import Fore

class QuizViewer(QuizBaseQuestions):
    def view_questions(self):
        questions = self.load_questions()
        if not questions:
            print(Fore.BLUE +"No questions found")
            return
        for idx, question in enumerate(questions):
            print(Fore.GREEN + f"[{idx}] {question['question'][9:]}")

    def remove_question(self):
        questions = self.load_questions()
        if not questions:
            print(Fore.YELLOW + "No questions to remove")
            return
        self.view_questions()
        
        try:
            idx = int(input("Enter the number of questions to remove:"))
            if 0 <= idx < len(questions):
                del questions[idx]
                with open(self.filename, 'w') as file:
                    for question in questions[idx]:
                            file.write(f"{question['question']}\n")
                            file.write(f"{question['A']}\n")
                            file.write(f"{question['B']}\n")
                            file.write(f"{question['C']}\n")
                            file.write(f"{question['D']}\n")
                            file.write(f"Answer: {question['answer']}\n\n")
                    print(Fore.GREEN + "Question removed successfully.")
            else:
                print (Fore.RED + "Invalid index.")
                
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")
