from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# LINTING ERROR TO TEST 888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888

# In-memory database
items = []

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:
        items.append(item)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_item(index):
    if index < len(items):
        items.pop(index)
    return redirect(url_for('index'))

@app.route('/update/<int:index>', methods=['POST'])
def update_item(index):
    if index < len(items):
        items[index] = request.form.get('new_item')
    return redirect(url_for('index'))




def create_app():
    app = Flask(__name__)

    @app.route('/health')
    def health():
        return {"status": "ok"}

    return app

#PYTHON FUNCTION FOR UNTIT TESTS
def add_numbers(a, b):
    """Function that adds two numbers."""
    return a + b

if __name__ == '__main__':
    app.run(debug=True)