from flask import Flask, request, render_template, redirect, session, jsonify, flash
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

boggle_game = Boggle()

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


"""No confusions here"""
@app.route('/')
def make_board():
    board = boggle_game.make_board()
    session['board'] = board
    return render_template('create_board.html', board=board)

"""
- Note board is created in make_board(). 
- Word is the submitted value from form. When form is submitted 
 """
@app.route('/check')
def check_answer():
    word = request.args['word']
    board = session['board']
    """Returns OK if valid word and on board, returns 'not-on-board' if word is valid, if neither or returns not-word"""
    response = boggle_game.check_valid_word(board, word)
    """I recall colt mentioning that axios needs to receive JSON. Confused at this part as"""
    return jsonify({'result': response})


