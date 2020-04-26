from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect(url_for('login'))

@app.route('/login')
def login():
   return 'login'

@app.route('/<user>/profile')
def profile(user):
    return f"{user} profile"

@app.route('/<user>/pull')
def pull(user):
    return f"{user} pull"

@app.route('/<user>/builder')
def builder(user):
    return f"{user} deck builder"

@app.route('/<user>/new_deck')
def new_deck(user):
    return f"{user} new_deck"

@app.route('/<user>/stats')
def stats(user):
    return f"{user} stats"

@app.route('/<user>/packs')
def packs(user):
    return f"{user} packs"

@app.route('/<user>/pack/<pack_name>')
def edit_pack(user,pack_name):
    return f"{user} editing {pack_name}"

@app.route('/<user>/new_pack')
def new_pack(user):
    return f"{user} new_pack"

@app.route('/<user>/ccreate')
def ccreate(user):
    return f"{user} card creator"


if __name__ == '__main__':
   app.run(debug=True)
