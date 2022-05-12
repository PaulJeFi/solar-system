from flask import Flask
from flask import render_template
from flask import request
import webbrowser

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

def main():
    webbrowser.open('http://127.0.0.1:5000/')
    app.run(debug=True, threaded=True)
    
if __name__ == '__main__':
    main()