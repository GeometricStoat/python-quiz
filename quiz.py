import random

class Answer:
    def __init__(self, answer, c = False):
        self.answer = answer
        self.correct = c

    def check(self, a):
        if self.correct == True and self.answer == a:
            return True

        return False

class Question:
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers

    def ask(self):
        print(self.question)

    def check(self, a):
        for x in self.answers:
            if x.check(a):
                print("Correct!")
                return True

        print("Incorrect.")
        return False

class Quiz:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def getInput(self):
        return input("Your answer: ")

    def check(self):
        qCopy = self.questions.copy()
        random.shuffle(qCopy)
        correct = 0

        for q in qCopy:
            q.ask()
            i = self.getInput()
            correct += q.check(i)

        print("You scored " + str(correct) + "/" + str(len(self.questions)) + "!")

def getBinary(q, t, f):
    return Question(q, [Answer(str(t), True), Answer(str(f))])

#example quiz
questions = [
    getBinary("What is 3 + 4 * 2?", 11, 14),
    getBinary("What is the color of the sky?", "blue", "yellow"),
    getBinary("Are you subscribed to Geometric Stoat?", "yes", "no")
]

quiz = Quiz("Random Quiz", questions)
quiz.check()
