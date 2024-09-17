// Sample questions (you'll expand this with your full question set)
const questions = {
    math: [
        {
            question: "What is 2 + 2?",
            options: ["3", "4", "5", "6"],
            correctAnswer: "4"
        }
    ],
    verbal: [
        {
            question: "What is the opposite of 'hot'?",
            options: ["Warm", "Cool", "Cold", "Tepid"],
            correctAnswer: "Cold"
        }
    ],
    writing: [
        {
            question: "Which sentence is grammatically correct?",
            options: [
                "Their going to the store.",
                "There going to the store.",
                "They're going to the store.",
                "There're going to the store."
            ],
            correctAnswer: "They're going to the store."
        }
    ]
};

let currentQuiz = null;
let currentQuestionIndex = 0;

function startQuiz(type) {
    currentQuiz = type;
    currentQuestionIndex = 0;
    showQuestion();
}

function showQuestion() {
    const quizContainer = document.getElementById('quiz-container');
    const currentQuestion = questions[currentQuiz][currentQuestionIndex];
    
    let html = `<h2>${currentQuestion.question}</h2>`;
    currentQuestion.options.forEach((option, index) => {
        html += `<button onclick="checkAnswer(${index})">${option}</button>`;
    });
    
    quizContainer.innerHTML = html;
}

function checkAnswer(selectedIndex) {
    const currentQuestion = questions[currentQuiz][currentQuestionIndex];
    const selectedAnswer = currentQuestion.options[selectedIndex];
    
    if (selectedAnswer === currentQuestion.correctAnswer) {
        alert("Correct!");
    } else {
        alert(`Incorrect. The correct answer is: ${currentQuestion.correctAnswer}`);
    }
    
    currentQuestionIndex++;
    if (currentQuestionIndex < questions[currentQuiz].length) {
        showQuestion();
    } else {
        alert("Quiz completed!");
        document.getElementById('quiz-container').innerHTML = "";
    }
}
