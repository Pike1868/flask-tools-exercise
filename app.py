from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route("/")
def show_home_page():
    """Show the user the title of the survey, the instructions, and a button to start the survey. The button should serve as a link that directs the user to /questions/0 (the next step will define that route). """
    
    session['testing'] = "Do you see me over there?"
    
    return render_template("index.html")

@app.route("/questions/<int:question_index>")
def show_question(question_index):
    """Show the user the next question in the survey"""
    num_of_questions = len(satisfaction_survey.questions)
    curr_index = len(session["responses"])
    if question_index >= num_of_questions:
        return render_template("thanks.html")
    if question_index != curr_index:
        flash("Trying to access an invalid question, redirecting to next question in order")
        return redirect(f"/questions/{curr_index}")
    current_question = satisfaction_survey.questions[question_index]
    choices = current_question.choices
    
    
    return render_template("question.html", current_question= current_question, choices=choices, curr_index=curr_index)

@app.route("/answer/<int:question_index>", methods=["POST"])
def handle_answer(question_index):
    """Handle answer submission and redirect to the next question."""
    answer = request.form["answer"]
    answers_list = session["responses"]
    answers_list.append(answer)
    session["responses"] = answers_list
    print(session["responses"], "responses array")
    return redirect(f"/questions/{question_index + 1}")

@app.route("/start" , methods=["POST"])
def handle_session():
    session["responses"] = []
    start_index = len(session["responses"])
    print(start_index, "start index")
    return redirect(f"/questions/{start_index}")