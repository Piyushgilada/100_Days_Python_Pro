from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a question bank from data
question_bank = []
for item in question_data:
    ques = item["text"]
    answer = item["answer"]
    new_question = Question(ques, answer)  # Use the Question class
    question_bank.append(new_question)

# Initialize the QuizBrain object
quiz = QuizBrain(question_bank)

# Run the quiz
while quiz.still_has_question():
    quiz.next_question()
