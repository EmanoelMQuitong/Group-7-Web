from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/profile')
def profile():  
    return render_template('profile.html')

@app.route('/contact')
def contact():
    return "Contact Page. please create me an html page with dummy contact info"

@app.route('/search_algo')
def search_algo():  
    return render_template('search_algo.html')

@app.route('/merge_linkedlist')
def merge_linkedlist():  
    return render_template('merge_linkedlist.html')

@app.route('/queue_deque')
def queue_deque():  
    return render_template('queue_deque.html')

if __name__ == "__main__":
    app.run(debug=True)