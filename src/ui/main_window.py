import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import os
from PIL import Image, ImageTk

class SATApp:
    def __init__(self, master, question_bank):
        self.master = master
        self.question_bank = question_bank
        self.master.title('Crafting Scholars SAT Prep')
        self.master.geometry('800x600')
        self.current_question = None
        self.questions_asked = 0
        self.correct_answers = 0
        self.remaining_time = 0

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.configure_styles()

        self.create_widgets()

    def configure_styles(self):
        self.style.configure('TFrame', background='#121212')
        self.style.configure('TLabel', background='#121212', foreground='#FFFFFF')
        self.style.configure('TButton', background='#1DB954', foreground='#121212', font=('Helvetica', 10, 'bold'))
        self.style.map('TButton', background=[('active', '#1ED760')])
        self.style.configure('Sidebar.TFrame', background='#000000')
        self.style.configure('Sidebar.TButton', background='#000000', foreground='#B3B3B3', font=('Helvetica', 12))
        self.style.map('Sidebar.TButton', background=[('active', '#1DB954')], foreground=[('active', '#FFFFFF')])

    def create_widgets(self):
        self.main_frame = ttk.Frame(self.master, style='TFrame')
        self.main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.create_sidebar()
        self.create_content_area()

    def create_sidebar(self):
        sidebar = ttk.Frame(self.master, width=200, style='Sidebar.TFrame')
        sidebar.pack(side=tk.LEFT, fill=tk.Y)

        logo_path = os.path.join('resources', 'images', 'logo.png')
        if os.path.exists(logo_path):
            logo = Image.open(logo_path)
            logo = logo.resize((150, 150), Image.Resampling.LANCZOS)
            logo = ImageTk.PhotoImage(logo)
            logo_label = ttk.Label(sidebar, image=logo, background='#000000')
            logo_label.image = logo
            logo_label.pack(pady=20)
        else:
            ttk.Label(sidebar, text="Crafting Scholars", style='Sidebar.TButton', font=('Helvetica', 14, 'bold')).pack(pady=20)

        ttk.Button(sidebar, text="Practice", style='Sidebar.TButton', command=self.start_practice).pack(pady=10, padx=20, fill=tk.X)
        ttk.Button(sidebar, text="Add Question", style='Sidebar.TButton', command=self.add_new_question).pack(pady=10, padx=20, fill=tk.X)
        ttk.Button(sidebar, text="Stats", style='Sidebar.TButton').pack(pady=10, padx=20, fill=tk.X)

    def create_content_area(self):
        self.content_frame = ttk.Frame(self.main_frame, style='TFrame')
        self.content_frame.pack(padx=40, pady=40, fill=tk.BOTH, expand=True)

        self.question_label = ttk.Label(self.content_frame, text='Welcome to SAT Prep!', 
                                        font=('Helvetica', 16), wraplength=500)
        self.question_label.pack(pady=20)

        self.answer_entry = ttk.Entry(self.content_frame, width=50, font=('Helvetica', 12))
        self.answer_entry.pack(pady=10)

        self.submit_button = ttk.Button(self.content_frame, text='Submit Answer', command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.next_button = ttk.Button(self.content_frame, text='Next Question', command=self.next_question)
        self.next_button.pack(pady=10)
        self.next_button.pack_forget()  # Hide initially

        self.explanation_text = tk.Text(self.content_frame, height=8, width=60, wrap=tk.WORD, 
                                        font=('Helvetica', 12), bg='#282828', fg='#FFFFFF')
        self.explanation_text.pack(pady=20)

        self.timer_label = ttk.Label(self.content_frame, text="Time: 00:00", font=('Helvetica', 14))
        self.timer_label.pack(pady=10)

    def start_practice(self):
        self.questions_asked = 0
        self.correct_answers = 0
        self.remaining_time = 600  # 10 minutes in seconds
        self.update_timer()
        self.next_question()

    def update_timer(self):
        if self.remaining_time > 0:
            minutes, seconds = divmod(self.remaining_time, 60)
            self.timer_label.config(text=f"Time: {minutes:02d}:{seconds:02d}")
            self.remaining_time -= 1
            self.master.after(1000, self.update_timer)
        else:
            self.show_results()

    def next_question(self):
        if self.questions_asked < 10:
            self.current_question = self.question_bank.get_random_question()
            self.question_label.config(text=f"Question {self.questions_asked + 1}: {self.current_question}")
            self.answer_entry.delete(0, tk.END)
            self.explanation_text.delete('1.0', tk.END)
            self.questions_asked += 1
            self.next_button.pack_forget()  # Hide the next button
            self.submit_button.pack()  # Show the submit button
        else:
            self.show_results()

    def check_answer(self):
        if self.current_question and self.remaining_time > 0:
            user_answer = self.answer_entry.get()
            is_correct, correct_answer, explanation = self.question_bank.check_answer(self.current_question, user_answer)
            if is_correct:
                self.correct_answers += 1
                self.explanation_text.insert(tk.END, f"Correct!\n{explanation}")
            else:
                self.explanation_text.insert(tk.END, f"Incorrect. The correct answer is: {correct_answer}\n{explanation}")
            self.submit_button.pack_forget()  # Hide the submit button
            self.next_button.pack()  # Show the next button
        elif self.remaining_time <= 0:
            self.show_results()

    def show_results(self):
        percentage = (self.correct_answers / 10) * 100
        messagebox.showinfo("Practice Results", 
                            f"Practice session complete.\nYour score: {self.correct_answers}/10\nPercentage: {percentage:.1f}%")
        self.question_label.config(text='Practice session complete. Click "Practice" to begin a new session.')
        self.next_button.pack_forget()  # Hide the next button
        self.submit_button.pack_forget()  # Hide the submit button
        self.timer_label.config(text="Time: 00:00")

    def add_new_question(self):
        question = simpledialog.askstring("New Question", "Enter the question:")
        if question:
            answer = simpledialog.askstring("New Question", "Enter the answer:")
            if answer:
                explanation = simpledialog.askstring("New Question", "Enter the explanation:")
                if explanation:
                    self.question_bank.add_question(question, answer, explanation)
                    messagebox.showinfo("Success", "New question added successfully!")
