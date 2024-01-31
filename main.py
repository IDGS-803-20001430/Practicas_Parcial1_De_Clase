from flask import Flask,render_template,request
import math
import distancia

app = Flask(__name__)

@app.route("/distancia",methods=["GET","POST"])
def distan():
    x1=0
    y1=0
    x2=0
    y2=0
    operacion=0
    distancia_form=distancia.CalcularForm(request.form)
    if request.method=='POST':
        x1=distancia_form.x1.data
        x2=distancia_form.x2.data
        y1=distancia_form.y1.data
        y2=distancia_form.y2.data
        operacion = math.sqrt((x2-x1)** 2 + (y2-y1)** 2)
        
    return render_template("distancia.html", form=distancia_form, x1=x1, y1=y1, x2=x2, y2=y2, operacion=operacion)

# @app.route("/")
# def index():
#     # escuela="UTL!!!"
#     # alumnos=["Mario","Pedro","Luis","Dario"]
#     return render_template("index.html")

# @app.route("/alumnos")
# def alumnos():
#     return render_template("alumnos.html")

# @app.route("/maestros")
# def maes():
#     return render_template("maestros.html")

@app.route("/multiplicar",methods=["GET","POST"])
def mult():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        return "<h1>La multiplicacion es: {}</h1>".format(str(int(num1)*int(num2)))
    else:    
        return'''
            <form action="/multiplicar" method="POST">
            <label>N1:</label>
            <input type="text" name="n1"/><br>
            <label>N2:</label>
            <input type="text" name="n2"/><br>
            <input type="submit"/>
            </form>
        '''
@app.route("/formulario1")
def formulario():
    return render_template("formulario1.html")

@app.route("/")
def operaciones():
    return render_template("operaciones.html")

@app.route("/cine")
def cine():
    return render_template("cine.html")

# @app.route("/resultado",methods=["GET","POST"])
# def resultado():
#     if request.method=="POST":
#         num1=request.form.get("n1")
#         num2=request.form.get("n2")
#         return "<h1>La multiplicacion es: {}</h1>".format(str(int(num1)*int(num2)))
    

@app.route("/resultado",methods=["GET","POST"])
def resultado():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        op=request.form.get("operation")

        if op=="suma":
            return "<h1>La suma es: {}</h1>".format(str(int(num1)+int(num2)))
        
        if op=="resta":
            return "<h1>La resta es: {}</h1>".format(str(int(num1)-int(num2)))
        
        if op=="multi":
            return "<h1>La mulltiplicacion es: {}</h1>".format(str(int(num1)*int(num2)))
        
        if op=="divi":
            return "<h1>La division es: {}</h1>".format(str(int(num1)/int(num2)))

@app.route("/calcular", methods=["POST"])
def calcular():
    nombre = request.form.get("nombre")
    cantidadCompradores = int(request.form.get("cantidadCompradores"))
    tarjetaCineco = request.form.get("tarjetaCineco")
    cantidadBoletos = int(request.form.get("cantidadBoletos"))

    print("Nombre:", nombre)
    print("Cantidad de compradores:", cantidadCompradores)
    print("Tarjeta Cineco:", tarjetaCineco)
    print("Cantidad de boletos:", cantidadBoletos)

    precio_boleto = 12
    costo_total = cantidadBoletos * precio_boleto

    if cantidadBoletos > 5:
        descuento = 0.15
    elif cantidadBoletos >= 3:
        descuento = 0.10
    else:
        descuento = 0

    costo_con_descuento = costo_total - (costo_total * descuento)

    if tarjetaCineco == "si":
        descuento_tarjeta_cineco = 0.10
        costo_con_descuento -= (costo_con_descuento * descuento_tarjeta_cineco)

    return str(costo_con_descuento)


if __name__=="__main__":
    app.run(debug=True)