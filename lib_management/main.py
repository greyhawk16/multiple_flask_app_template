from flask import Flask


# main.py file number 1. File path: application/lib_management/main.py
app = Flask(__name__)


#... create endpoints etc
@app.route('/')
def home():
    return 'hi from main.py at lib_manage'