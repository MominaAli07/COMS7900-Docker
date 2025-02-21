from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        operation = request.form.get('operation')

        if num1 and num2 and operation:
            try:
                num1, num2 = float(num1), float(num2)
                if operation == 'add':
                    result = num1 + num2
                elif operation == 'subtract':
                    result = num1 - num2
                elif operation == 'multiply':
                    result = num1 * num2
                elif operation == 'divide':
                    result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
            except ValueError:
                result = "Invalid input"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

