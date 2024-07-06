from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return 'Hello, World!'


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"

    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"

    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"

    return wrapper


# Different route using the app.route decorator
@app.route("/buy")
@make_bold
@make_emphasis
@make_underlined
def buy():
    return 'buy!'


# Creating variable path and converting the path to a specified data
@app.route("/username/<name>/<int:number>")
def great(name, number):
    return f"Hello there {name}; you are {number} years old."


if __name__ == "__main__":
    app.run(debug=True)

# running our local flask server manually
# set FLASK_APP=main.py
# flask --app main.py run
