# 참고 코드: https://oieivind.medium.com/run-multiple-flask-applications-at-the-same-time-c73dd21f7d9


from flask import Flask
from lib_management.main import app as flask_app_1
from book_information.main import app as flask_app_2

from werkzeug.middleware.dispatcher import DispatcherMiddleware  # use to combine each Flask app into a larger one that is dispatched based on prefix
from werkzeug.serving import run_simple  # werkzeug development server


if __name__ == "__main__":
    application = DispatcherMiddleware(flask_app_1, {'/book_info': flask_app_2})
    run_simple('localhost', 5002, application, use_reloader=True, use_debugger=True, use_evalex=True)
