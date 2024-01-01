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

@app.route('/queue_dequeue')
def queue_deque():  
    return render_template('q_dq.html')\


queue = []
@app.route('/queue_dequeue', methods=['GET', 'POST'])
def queue_operations():
    Enqueue = None
    Dequeue = None

    if request.method == 'POST':

        if request.form.get('enqueue', ''):
            data = str(request.form.get('inputString', ''))
            queue.append(data)

        elif request.form.get('dequeue', ''):
            if queue:
                Dequeue = queue.pop(0)

    return render_template('q_dq.html', Enqueue=queue, Dequeue=Dequeue)
    

if __name__ == "__main__":
    app.run(debug=True)