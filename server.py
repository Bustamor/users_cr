# WHAT STARTS MY SERVER Bring in flask
# relevant code snippet from server.py
from flask_app import app
from flask_app.controllers import user_controller

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5001)

