import os

class QuizBaseQuestions:
    def __init__(self, filename="quiz_questions.txt"):
        self.filename =  filename
        self.check_file()
    
    def check_file(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w'):  # Open the file in write mode ('w') to create or clear its contents
                pass
    
    def load_questions(self):
        with open (self.filename, 'r') as file:   # Open the file in read mode ('r') so we can load and read its contents
            lines = file.readlines()

        questions = []
        current = {}

        for line in lines:
            line = line.strip()
            if line.startswith("Question:"):
                current = {"question":line}
            elif line.startswith("A."):
                current["choice_a"] =  line
            elif line.startswith("B."):
                current["choice_b"] = line
            elif line.startswith("C."):
                current["choice_c"] = line
            elif line.startswith("D."):
                current["choice_d"] = line
            elif line.startswith("Answer:"):
                current["answer"] = line.split(":")[1].strip().upper()
                questions.append(current)

        return questions
