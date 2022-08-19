from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.numero import Numero
from utils.db import db

numeros = Blueprint('numeros', __name__)

@numeros.route('/')
def index():
    numeros = Numero.query.all()
    return render_template('index.html', numeros = numeros)
    
@numeros.route('/agregar_numero', methods = ['POST'])
def agregar_numero():
    numero = request.form['numero'] 
    

    nuevo_numero = Numero(numero)

    db.session.add(nuevo_numero)
    db.session.commit()

    flash("¡Numero añadido satisfactoriamente!")

    return redirect(url_for('numeros.index'))

@numeros.route('/actualizar_numero/<id>', methods = ['POST','GET'])
def actualizar_numero(id):
    numero = Numero.query.get(id)

    if request.method == 'POST':       
        numero.numero = request.form["numero"]
        db.session.commit()
        return redirect(url_for('numeros.index'))
     
    numero = Numero.query.get(id)

    flash("¡Numero actualizado satisfactoriamente!")

    return render_template('actualizar_numero.html', numero = numero)

@numeros.route("/eliminar_numero/<id>")
def eliminar_numero(id):
    numero = Numero.query.get(id)
    db.session.delete(numero)
    db.session.commit()

    flash("¡Numero eliminado satisfactoriamente!")

    return redirect(url_for('numeros.index'))
    
    
@numeros.route("/about")
def about():
    return render_template('about.html')


def fibo(n: int):
    """
    Calculating the fibonacci numbers
    """
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

# The actual route
@numeros.route("/fibonacci/get")
def send_fibo():
    
    """
    Sending the fibonacci number to the user, telling him if
    he uses improper input
    """
    fibo_number = str(fibo(int(request.args['n'])))
   
    try:
        return {'number' : fibo_number}
         
    except ValueError:
        return "Please use a number as the 'n' argument"

#@numeros.route("/calcular_numero", methods=['POST'])
#def calcular_numero():
 #   num1 = request.form['numero']

  #  resultado = fibo(int(num1))
    
    
   # return render_template('numeros.index', resultado = resultado)
   # return resultado


@numeros.route('/calcular_numero/<id>', methods = ['POST','GET'])
def calcular_numero(id):
    numero = Numero.query.get(id)

         
    if request.method == 'POST':       
        numero.numero = request.form["numero"]
        #db.session.commit()
        num1 = request.form['numero']
        resultado = fibo(int(num1))
        return render_template('calcular_numero_2.html', resultado = resultado)
     
    numero = Numero.query.get(id)

    flash("¡Numero actualizado satisfactoriamente!")

    return render_template('calcular_numero.html', numero = numero)
     
    #num1 = Numero.query.get(id)

    #flash("¡Numero actualizado satisfactoriamente!")

    #return render_template('actualizar_numero.html', resultado = resultado)
   

    #if request.method == 'POST':       
    #    numero.numero = request.form["numero"]
    #    db.session.commit()
    #    return redirect(url_for('numeros.index'))
     
    #numero = Numero.query.get(id)

    #flash("¡Numero actualizado satisfactoriamente!")

    #return render_template('actualizar_numero.html', numero = numero)
