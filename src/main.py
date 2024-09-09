import random

class SATPrep:
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
            return False, "Question not found."
        correct_answer = self.questions[question]["answer"]
        is_correct = user_answer.lower() == correct_answer.lower()
        explanation = self.questions[question]["explanation"]
        return is_correct, explanation

    def practice_session(self):
        if len(self.questions) < 10:
            print("Not enough questions for a full practice session. Please add more questions.")
            return

        score = 0
        questions_asked = set()

        for i in range(10):
            while True:
                question = self.get_random_question()
                if question not in questions_asked:
                    questions_asked.add(question)
                    break

            print(f"\nQuestion {i+1}: {question}")
            user_answer = input("Your answer: ")
            
            is_correct, explanation = self.check_answer(question, user_answer)
            if is_correct:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer is: {self.questions[question]['answer']}")
                print(f"Explanation: {explanation}")

        percentage = (score / 10) * 100
        print(f"\nPractice session complete.")
        print(f"Your score: {score}/10")
        print(f"Percentage: {percentage:.1f}%")

def main():
    sat_prep = SATPrep()

    # Adding sample questions with explanations
    sat_prep.add_question("What is the capital of France?", "Paris", "Paris is the capital and most populous city of France, known for its iconic Eiffel Tower and rich history.")
    sat_prep.add_question("What is 2 + 2?", "4", "This is a basic arithmetic addition. 2 + 2 = 4 is one of the fundamental equations in mathematics.")
    sat_prep.add_question("Who wrote 'Romeo and Juliet'?", "William Shakespeare", "William Shakespeare, an English playwright and poet, wrote 'Romeo and Juliet' around 1595. It's one of his most famous tragedies.")
    sat_prep.add_question("What is the largest planet in our solar system?", "Jupiter", "Jupiter is the largest planet in our solar system. It's a gas giant with a mass more than two and a half times that of all the other planets combined.")
    sat_prep.add_question("In which year did World War II end?", "1945", "World War II ended in 1945, with Germany surrendering in May and Japan in August following the atomic bombings of Hiroshima and Nagasaki.")
    sat_prep.add_question("What is the chemical symbol for gold?", "Au", "The chemical symbol for gold is Au, which comes from the Latin word 'aurum', meaning 'shining dawn' or 'glow of sunrise'.")
    sat_prep.add_question("What is the square root of 64?", "8", "The square root of 64 is 8 because 8 * 8 = 64. In mathematical notation, √64 = 8.")
    sat_prep.add_question("Who painted the Mona Lisa?", "Leonardo da Vinci", "The Mona Lisa was painted by Leonardo da Vinci, an Italian Renaissance polymath. It's one of the most famous paintings in the world.")
    sat_prep.add_question("What is the capital of Japan?", "Tokyo", "Tokyo is the capital and largest city of Japan. It's a major global economic and cultural center.")
    sat_prep.add_question("What is the largest ocean on Earth?", "Pacific Ocean", "The Pacific Ocean is the largest and deepest ocean on Earth, covering an area of about 63 million square miles.")

    while True:
        print("\n1. Add a question")
        print("2. Practice (10 questions)")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            question = input("Enter the question: ")
            answer = input("Enter the answer: ")
            explanation = input("Enter the explanation: ")
            sat_prep.add_question(question, answer, explanation)
            print("Question added successfully!")

        elif choice == '2':
            sat_prep.practice_session()

        elif choice == '3':
            print("Thank you for using the SAT Prep Program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
