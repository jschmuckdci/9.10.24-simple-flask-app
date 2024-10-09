from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Route for Home Page
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/result', methods=['POST'])
def result():
    # Get the bear choice from the form
    bear_choice = request.form['bear_choice']
    return render_template('result.html', bear=bear_choice)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

if __name__=="__main__":
    app.run(debug=True)