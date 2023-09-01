from flask import Flask, render_template
import pyodbc
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\cuc\Downloads\Database2.accdb;')
cursor = conn.cursor()
cursor.execute('select * from personas')
   
for row in cursor.fetchall():
    print (row)
cursor.close
conn.close
app = Flask(__name__)

@app.route('/estudiantes')
def listar_estudiantes():
    # Ejemplo de consulta a la base de datos de Access
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Estudiantes')
    estudiantes = cursor.fetchall()
    return render_template('estudiantes.html', estudiantes=estudiantes)

@app.route('/cursos')
def listar_cursos():
    # Ejemplo de consulta a la base de datos de Access
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Cursos')
    cursos = cursor.fetchall()
    return render_template('cursos.html', cursos=cursos)

if __name__ == '__main__':
    app.run()
