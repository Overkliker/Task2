from flask import Flask, render_template

app = Flask(__name__)

@app.route('/training/<templates>')
def nextlvl(templates):
    if 'инженер' in templates.lower() or 'строитель' in templates.lower():
        return render_template('nextlvl.html', name=templates)

    else:
        return render_template('index.html', name=templates)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)

