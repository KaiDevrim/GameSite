from flask import Flask, render_template, Response, request
from functools import wraps
import sqlite3
import os

DB = "./steam.sqlite"

def get_row():
    conn = sqlite3.connect('./steam.sqlite')
    cur = conn.cursor()
    select = cur.execute('SELECT * FROM Games')
    result = [dict(ID=row[0],
                    Time=row[1],
                    Name=row[2],
                    Score=row[3],
                    TimeType=row[4],
                    Review=row[5],
                    AppID=row[6],
                    Image=row[7]) for row in select.fetchall()]
    conn.close()

    return result

def update_review(score, review, appid):
    conn = sqlite3.connect('./steam.sqlite')
    cur = conn.cursor()
    query = cur.execute('UPDATE Games SET Score = {}, SET Review = {} WHERE AppID = {}'.format(score, review, appid))

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == os.getenv('ADMIN_NAME') and password == os.getenv('ADMIN_PASS')

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

app = Flask(__name__)

@app.route("/")
def render():
    return render_template('index.html', items=get_row())

@app.route("/admin", methods=['POST'])
@requires_auth
def review():
    return render_template('admin.html')


if __name__ == '__main__':
    app.run(debug=True)