"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi! This is the home page.</title>
      </head>
    <body>
      <h1>Hi! This is the home page.</h1>
      <a href="http://localhost:5000/hello">Hello</a>
    </body>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
      <form action="/greet">
          What's your name? <input type="text" name="person">
          <!--<form action="/greet">-->
            <label for="compliment-select">Choose your compliment!</label>
            <select name="compliment" id="compliment-select">
            <option value="ducky">Ducky</option>
            <option value="neato">Neato</option>
            <option value="oh-so-not-meh">Oh-so-not-meh</option>
            </select>
          <!--</form>-->
          <!--<form action="/greet">-->
          <input type="submit" value="Submit">
          <!--</form>-->
      </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
