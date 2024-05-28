from flask import Flask, render_template, request
from get_answer import get_answer
from chi_square import chi_square
app = Flask(__name__)


@app.route('/', methods =['GET'])
def welcome():
    return render_template('first.html')

@app.route('/submission')
def submission():
    return render_template('welcome.html')

@app.route('/submit', methods=['POST'])
def submit():
    answers = []
    for index in range(1,6):
        answer = request.form.get(f'answer_{index}')
        answers.append(answer)
    print(answers)
    result , image_path = get_answer(answers)  # Call the function to print the list of results
    return render_template('index.html', result=result , image_path=image_path)

@app.route('/chisquare')
def display_dataframe():
    
    df1,df2,df3,r1,r2,r3,f1,f2,f3 = chi_square()
    df1_html = df1.to_html()
    df2_html = df2.to_html()
    df3_html = df3.to_html()

    return render_template('chisquare.html', table1=df1_html,table2=df2_html,table3=df3_html,res1 = r1,res2 = r2,res3 = r3,f1=f1,f2=f2,f3=f3)

@app.route('/text')
def by_text():
    return render_template('index.html' )

@app.route('/speech')
def by_speech():
    return render_template('speech.html')

@app.route('/submit_speech', methods=['POST'])
def submit_speech():
    answers_speech = []
    for index in range(1,6):
        speech = request.form.get(f'speech_{index}')
        answers_speech.append(speech)
    print(answers_speech)
    result , image_path = get_answer(answers_speech)  # Call the function to print the list of results
    return render_template('speech.html', result=result , image_path = image_path)

if __name__ == '__main__':
    app.run(debug=True)
