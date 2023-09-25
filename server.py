from flask import Flask, render_template

app = Flask(__name__)

print(__name__)

@app.route('/')
@app.route('/tingod')
def tingod():
    return render_template('tingod.html')

@app.route('/')
@app.route('/gabby')
def gabby():
    return render_template('gabby.html')

if __name__== '__main__':
    app.run(debug=True)