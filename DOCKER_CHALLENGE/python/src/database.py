import mysql.connector
import utils
import hashlib

#Conectarse a la BD
def open():
    connection = mysql.connector.connect(
        user='root', password='root', host='mysql', port='3306', database='db', auth_plugin='mysql_native_password')
    return connection

def getAllSalesValidAdmin():
    connect = open()
    cursor = connect.cursor(dictionary=True)
    cursor.execute("Select fec_alta,user_name,codigo_zip,credit_card_num,credit_card_type,cuenta_numero,direccion,geo_latitud,geo_longitud,color_favorito,foto_dni,ip,auto,auto_modelo,auto_tipo,auto_color,cantidad_compras_realizadas,avatar,id FROM sales where credit_card_type<>'Invalid...'")
    sales = cursor.fetchall()
    connect.close()
    return sales

def getAllSalesValid():
    connect = open()
    cursor = connect.cursor(dictionary=True)
    cursor.execute("Select fec_alta,user_name,codigo_zip,credit_card_num,credit_card_type,cuenta_numero,direccion,geo_latitud,geo_longitud,color_favorito,foto_dni,ip,auto,auto_modelo,auto_tipo,auto_color,cantidad_compras_realizadas,avatar,id FROM sales where credit_card_type<>'Invalid...'")
    sales = cursor.fetchall()
    connect.close()
    return sales

def getAllSalesLog():
    connect = open()
    cursor = connect.cursor(dictionary=True)
    cursor.execute("Select fec_alta,user_name,codigo_zip,credit_card_num,credit_card_type,cuenta_numero,direccion,geo_latitud,geo_longitud,color_favorito,foto_dni,ip,auto,auto_modelo,auto_tipo,auto_color,cantidad_compras_realizadas,avatar,id FROM sales where credit_card_type='Invalid...'")
    sales = cursor.fetchall()
    connect.close()
    return sales


#Consultas para generar los APIs REST - GET

def getAllSales():
    connect = open()
    cursor = connect.cursor(dictionary=True)
    cursor.execute('Select user_name,codigo_zip,credit_card_num,credit_card_type,cuenta_numero,direccion,geo_latitud,geo_longitud,color_favorito,foto_dni,ip,auto,auto_modelo,auto_tipo,auto_color,cantidad_compras_realizadas,avatar,id FROM sales')
    sales = cursor.fetchall()
    connect.close()
    return sales


def getSale(id):
    connect = open()
    cursor = connect.cursor(dictionary=True)
    #cursor.execute("Select user_name,codigo_zip,credit_card_num,cuenta_numero,direccion,geo_latitud,geo_longitud,color_favorito,foto_dni,ip,auto,auto_modelo,auto_tipo,auto_color,cantidad_compras_realizadas,avatar,id FROM sales where id='"+id+"'")
    cursor.execute("Select user_name,codigo_zip,credit_card_num,cuenta_numero,direccion,geo_latitud,geo_longitud,color_favorito,foto_dni,ip,auto,auto_modelo,auto_tipo,auto_color,cantidad_compras_realizadas,avatar,id FROM sales where id = %(id)s", {'id': id})
    sales = cursor.fetchall()
    connect.close()
    return sales

# Sentencia para eliminar los datos de la tabla sales para volver a cargarlos (dado el error del id)
def truncateSales():
    connect = open()
    cursor = connect.cursor(dictionary=True)
    sql = "TRUNCATE TABLE sales"
    cursor.execute(sql)
    connect.commit()
    cursor.close()

def insertJsonIntoSales(respuestaJson):
    connect = open()
    cursor = connect.cursor(dictionary=True)
    for resp in respuestaJson:
        #sql = "INSERT INTO sales (fec_alta,user_name,codigo_zip,credit_card_num,cuenta_numero,direccion,geo_latitud,geo_longitud,color_favorito,foto_dni,ip,auto,auto_modelo,auto_tipo,auto_color,cantidad_compras_realizadas,avatar,fec_birthday,id) VALUES ('"+str(resp['fec_alta'])+"','"+resp['user_name']+"','"+resp['codigo_zip']+"','"+resp['credit_card_num']+"','"+str(resp['cuenta_numero'])+"','"+resp['direccion']+"','"+str(resp['geo_latitud'])+"','"+str(resp['geo_longitud'])+"','"+resp['color_favorito']+"','"+resp['foto_dni']+"','"+resp['ip']+"','"+resp['auto']+"','"+str(resp['auto_modelo'])+"','"+resp['auto_tipo']+"','"+resp['auto_color']+"','"+str(resp['cantidad_compras_realizadas'])+"','"+resp['avatar']+"','"+resp['fec_birthday']+"','"+str(resp['id'])+"')"
        #sql = "INSERT INTO sales (fec_alta,user_name,codigo_zip,credit_card_num,cuenta_numero,direccion,geo_latitud,geo_longitud,color_favorito,foto_dni,ip,auto,auto_modelo,auto_tipo,auto_color,cantidad_compras_realizadas,avatar,fec_birthday,id) VALUES ('"+utils.formatDate(resp['fec_alta'])+"','"+resp['user_name']+"','"+resp['codigo_zip']+"','"+utils.truncatePAN(resp['credit_card_num'])+"','"+str(resp['cuenta_numero'])+"','"+resp['direccion']+"','"+str(resp['geo_latitud'])+"','"+str(resp['geo_longitud'])+"','"+resp['color_favorito']+"','"+resp['foto_dni']+"','"+resp['ip']+"','"+resp['auto']+"','"+str(resp['auto_modelo'])+"','"+resp['auto_tipo']+"','"+resp['auto_color']+"','"+str(resp['cantidad_compras_realizadas'])+"','"+resp['avatar']+"','"+utils.formatDate(resp['fec_birthday'])+"','"+str(resp['id'])+"')"
        sql = "INSERT INTO sales (fec_alta,user_name,codigo_zip,credit_card_num,credit_card_type,cuenta_numero,direccion,geo_latitud,geo_longitud,color_favorito,foto_dni,ip,auto,auto_modelo,auto_tipo,auto_color,cantidad_compras_realizadas,avatar,fec_birthday,id) VALUES ('"+utils.formatDate(resp['fec_alta'])+"','"+resp['user_name']+"','"+resp['codigo_zip']+"','"+utils.hashingPAN(resp['credit_card_num'])+"','"+utils.validcard(resp['credit_card_num'])+"','"+str(resp['cuenta_numero'])+"','"+resp['direccion']+"','"+str(resp['geo_latitud'])+"','"+str(resp['geo_longitud'])+"','"+resp['color_favorito']+"','"+resp['foto_dni']+"','"+resp['ip']+"','"+resp['auto']+"','"+str(resp['auto_modelo'])+"','"+resp['auto_tipo']+"','"+resp['auto_color']+"','"+str(resp['cantidad_compras_realizadas'])+"','"+resp['avatar']+"','"+utils.formatDate(resp['fec_birthday'])+"','"+str(resp['id'])+"')"
        cursor.execute(sql)
    connect.commit()
    cursor.close()

#Validación del usuario y el password
def validateUser(u, p):
    connect = open()
    cursor = connect.cursor(dictionary=True)
    #sql = "select count(1) from user where name='"+u+"' and password='"+u+"'"
    #cursor.execute(sql)

    pHashed = hashlib.sha256(p.encode('utf-8')).hexdigest()
    pHashedStr = str(pHashed)

    cursor.execute("select resposibility from user where name = %(u)s and password = %(p)s", {'u': u, 'p':pHashedStr})
    result = cursor.fetchone()
    connect.close()
    return result
    




