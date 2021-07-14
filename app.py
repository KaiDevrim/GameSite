from flask import Flask, render_template
import sqlite3

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

    # conn.commit()
    conn.close()

    return result


app = Flask(__name__)

@app.route("/")
def render():
    return render_template('index.html', items=get_row())


if __name__ == '__main__':
    app.run(debug=True)