import os

class BaseGame:
    def __init__(self, filename="quiz_questions.txt"):
        self.filename= filename

    def check_file(self):
        if not os.path.exists(self.filename):
            print("Quiz file not found")
            return False
        return True
    def load_questions(self):
        if not self.check_file():
            return []
        with open(self.filename, 'r')as file:
            lines = file.readlines()

        questions = []
        current = {}
        for line in lines:
            line = line.strip()
            if line.startswith("Question:"):
                current = {"question": line[9:].strip()}
            elif line.startswith("A."):
                current["A"] = line[2:].strip()
            elif line.startswith("B."):
                current["B"] = line[2:].strip()
            elif line.startswith("C."):
                current["C"] = line[2:].strip()
            elif line.startswith("D."):
                current["D"] = line[2:].strip()
            elif line.startswith("Answer:"):
                current["answer"] = line.split(":")[1].strip().upper()
                questions.append(current)
        return questions
        