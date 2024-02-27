from flask import Flask


# main.py file number 2. File path: application/book_information/main.py
app = Flask(__name__)

#... create endpoints etc
@app.route('/')
def home():
    return 'hi from main.py at book_info'