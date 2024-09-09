import random
import json

class QuestionBank:
    def __init__(self):
        self.questions = {}

    def add_question(self, question, answer, explanation):
        self.questions[question] = {"answer": answer, "explanation": explanation}

    def get_random_question(self):
        if not self.questions:
            return "No questions available."
        return random.choice(list(self.questions.keys()))

    def check_answer(self, question, user_answer):
        if question not in self.questions:
            return False, "Question not found.", ""
        correct_answer = self.questions[question]["answer"]
        is_correct = user_answer.lower() == correct_answer.lower()
        explanation = self.questions[question]["explanation"]
        return is_correct, correct_answer, explanation

    def load_sample_questions(self):
        sample_questions = [
            {
                "question": "What is the capital of France?",
                "answer": "Paris",
                "explanation": "Paris is the capital and most populous city of France."
            },
            {
                "question": "What is 2 + 2?",
                "answer": "4",
                "explanation": "This is a basic arithmetic addition. 2 + 2 = 4 is one of the fundamental equations in mathematics."
            },
            {
                "question": "Who wrote 'Romeo and Juliet'?",
                "answer": "William Shakespeare",
                "explanation": "William Shakespeare, an English playwright and poet, wrote 'Romeo and Juliet' around 1595."
            }
        ]
        for q in sample_questions:
            self.add_question(q["question"], q["answer"], q["explanation"])

    def save_questions(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.questions, f)

    def load_questions(self, filename):
        with open(filename, 'r') as f:
            self.questions = json.load(f)
