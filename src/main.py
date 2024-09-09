import tkinter as tk
from question_bank import QuestionBank
from ui.main_window import SATApp

def main():
    question_bank = QuestionBank()
    question_bank.load_sample_questions()
    
    root = tk.Tk()
    app = SATApp(root, question_bank)
    root.mainloop()

if __name__ == "__main__":
    main()
