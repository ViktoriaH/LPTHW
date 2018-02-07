from flask import Flask, session, request, flash
from flask import url_for, redirect, render_template
import map

app = Flask(__name__)

@app.route('/game', methods=['GET'])
def game_get():
    if 'scene' in session:
        thescene = map.SCENES[session['scene']]
        return render_template('show_scene.html', scene=thescene)
    else:

        return redirect(url_for('start'))
@app.route('/game', methods=['POST'])
def game_post():
    userinput = request.form.get('userinput')
    if 'scene' in session:
        if userinput is None:

           return redirect(url_for('start'))

        else:
            currentscene = map.SCENES[session['scene']]
            nextscene = currentscene.go(userinput)
            if nextscene is None:

                return redirect(url_for('start'))

            else:
                session['scene'] = nextscene.urlname
                return render_template('show_scene.html', scene=nextscene)
    else:

        return redirect(url_for('start'))

@app.route('/start')
def start():
    return render_template('welcome_screen.html')
@app.route('/')
def index():
    session['scene'] = map.START.urlname
    return redirect(url_for('start'))

app.secret_key = 'hallo'

if __name__ == "__main__":
    app.run()
