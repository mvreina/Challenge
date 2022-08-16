from flask import Flask, request, render_template, redirect, flash
from flask_restful import Resource, Api
from flask_login import login_user, login_required, current_user, LoginManager, logout_user, UserMixin
import base64
import requests
import mysql.connector
import json
import database
import collections

app = Flask(__name__)
app.secret_key = "Melissa"
api = Api(app)

#login_manager = LoginManager()
#login_manager.login_view = 'login'
#login_manager.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = "Por favor inicie sesión para poder acceder a esta página."
login_manager.login_message_category = "info"


@login_manager.user_loader
def load_user(id):
    return User.get_by_id(id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
@login_required
def admin():
    #Conectarse a la BD
    ventas = database.getAllSalesValidAdmin()
    return render_template('admin.html', ventas=ventas)

@app.route('/log')
@login_required
def log():
    #Conectarse a la BD
    ventas = database.getAllSalesLog()
    return render_template('log.html', ventas=ventas)

@app.route('/batch')
@login_required
def batch():
    return render_template('batch.html')

@app.route('/user')
@login_required
def user():
    ventas = database.getAllSalesValid()
    return render_template('user.html', ventas=ventas)

@app.route('/authorized')
@login_required
def authorized():
    #Conectarse a la BD
    ventas = database.getAllSalesValidAdmin()
    return render_template('authorized.html', ventas=ventas)


#Consumir Endpoint de Usuarios y Cargarlos en la Base de datos
@app.route('/runBatch')
@login_required
def runBatch():
    #Bajar los datos desde el API REST
    url = 'https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios'
    respuesta = requests.get(url)
    respuestaJson = respuesta.json()

    #Borrar los datos de la tabla actual
    database.truncateSales()

    #Insertar la información del API REST en la BD
    database.insertJsonIntoSales(respuestaJson)

    flash('Finalizó el proceso de carga satisfactoriamente.')
    return render_template('batch.html')

#API REST GET SALES
class getSales(Resource):
    def get(self):
        ventas = database.getAllSales()
        return ventas

#API REST GET SALES BY ID
class getSalesById(Resource):
    def get(self, id):
        venta = database.getSale(id)
        return venta
    
api.add_resource(getSales, '/sales')
api.add_resource(getSalesById, '/sales/<id>')


####################################################
#                   AUTENTICACIÓN
####################################################
class User(UserMixin):
    def __init__(self, id, user, password) -> None:
        self.id = id
        self.user = user
        self.password = password

    def get_by_id(id):
        user = User(1,"Meli","Meli")
        return user

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    result = database.validateUser(username,password)
    
    try:
        numRows = len(result) #Extrae la posición 1 {'count(1)': 0} 
    except:
        numRows = 0    

    if (numRows==0):
        flash('Por favor revise su nombre de usuario y password e ingrese nuevamente.')
        return redirect('/login') # Si el usuario no existe recarga la página
    else:
        # if the above check passes, then we know the user has the right credentials
        #user=User(username,username)
        user=User(1,username,password)
        login_user(user, remember=remember)
        #Ingresa a la app
        resposibility = result['resposibility']
        if(resposibility == 'Sales'):
            return redirect('/user')
        elif(resposibility == 'Administrator'):
            return redirect('/batch')
        elif(resposibility == 'Authorized'):
            return redirect('/authorized')
        else:
            return redirect('/home')





####################################################
#                   Ejecutar Aplicación
####################################################
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True, ssl_context='adhoc')