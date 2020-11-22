from flask import Flask, request
from flask import render_template, redirect,url_for
from .conection import connect, conn_cursor

app = Flask(__name__)



@app.route('/')
def index():
    #connect() test de conecion postgres
    return render_template('create.html')

@app.route('/create')
def create():
    if request.method == 'POST':
        no_vendedor = request.form['no_vendedor']
        fecha_ingreso = request.form['fecha_ingreso']
        cursor =conn_cursor()
        # cursor.execute(
        #     'INSERT INTO respartner (name, display_name) \
        #     VALUES (%s, %s)',
        #     (no_vendedor, fecha_ingreso)
        # )
        
        cursor.execute("select name, create_date from respartner;")
        return redirect(url_for('create'))
    return render_template('devoluciones.html')

@app.route('/list')
def list():
    return 'lista'


if __name__ == '__main__':
    app.run(port = 3000, debug = True)


