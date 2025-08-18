from flask import Flask, render_template, request, redirect, url_for
from expense_tracker import Expense, ExpenseTracker

app = Flask(__name__)
tracker = ExpenseTracker()

@app.route('/')
def index():
    expenses = tracker.view_expenses()
    total = tracker.total_expenses()
    return render_template('index.html', expenses=expenses, total=total)

@app.route('/add', methods=['POST'])
def add():
    date = request.form['date']
    description = request.form['description']
    amount = float(request.form['amount'])
    tracker.add_expense(Expense(date, description, amount))
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    tracker.remove_expense(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
