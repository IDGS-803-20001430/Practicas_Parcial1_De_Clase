from flask import Flask,render_template,request
import math
import distancia
import resistencia

app = Flask(__name__)

@app.route("/diccionario", methods=["GET", "POST"])
def diccionario():
    espanol = ""
    ingles = ""
    buscar = ""
    traduccion = ""
    diccionario_form = resistencia.DiccionarioForm(request.form)
    busqueda_form = resistencia.BusquedaForm(request.form)

    if request.method == 'POST' and diccionario_form.validate():
        espanol = diccionario_form.espanol.data
        ingles = diccionario_form.ingles.data
        
        with open("diccionario.txt", "a") as archivo:
            archivo.write(f"{ingles.upper()}={espanol.upper()}\n")

    elif request.method == 'GET':
        palabraBuscada = str(request.args.get('buscar'))
        palabraBuscada = palabraBuscada.upper()
        idioma=request.args.get('opcionIdioma')

        print(palabraBuscada)
        print(idioma)
        
        if palabraBuscada:
            diccionario = {}
            
            # Haz algo con el idioma seleccionado (por ejemplo, imprimirlo)
            print("Idioma seleccionado:", idioma)            

            with open("diccionario.txt", "r") as archivo:
                for linea in archivo:
                    if "=" in linea:
                        palabra_ingles, palabra_espanol = linea.strip().split("=")
                        
                        if idioma == '1':
                            diccionario[palabra_espanol] = palabra_ingles
                        else:
                            diccionario[palabra_ingles] = palabra_espanol
                            

            resultado = diccionario.get(palabraBuscada, "No se encontró traducción")

    return render_template("diccionario.html", diccionario_form=diccionario_form, busqueda_form=busqueda_form, espanol=espanol, ingles=ingles, buscar=buscar, traduccion=resultado)
    

color_css_mapping = {
    'Negro': 'negro',
    'Cafe': 'cafe',
    'Rojo': 'rojo',
    'Naranja': 'naranja',
    'Amarillo': 'amarillo',
    'Verde': 'verde',
    'Azul': 'azul',
    'Violeta': 'violeta',
    'Gris': 'gris',
    'Blanco': 'blanco'
}

@app.route("/resistencias",methods=["GET","POST"])
def res():
    multiplicadores = {
        0: 1,
        1: 10,
        2: 100,
        3: 1000,
        4: 10000,
        5: 100000,
        6: 1000000,
        7: 10000000,
        8: 100000000,
        9: 1000000000
    }
    color_nombres = {
        0: 'Negro',
        1: 'Cafe',
        2: 'Rojo',
        3: 'Naranja',
        4: 'Amarillo',
        5: 'Verde', 
        6: 'Azul',
        7: 'Violeta',
        8: 'Gris',
        9: 'Blanco',
    }
    
    color1_nombre = ""
    color2_nombre = ""
    color3_nombre = ""
    tolerancia_display = ''
    tolerancia_color = ''
    tolerancia = 0
    resistenciaT = 0
    resistenciaMin = 0
    resistenciaMax = 0
    porcentaje_tolerancia = 0.0
    resistencia_form = resistencia.ResistenciaForm(request.form)
    
    if request.method == 'POST':
        color1 = int(resistencia_form.color1.data)
        color2 = int(resistencia_form.color2.data)
        color3 = int(resistencia_form.color3.data)
        tolerancia = int(resistencia_form.tolerancia.data)
        
        color1_nombre = color_nombres[color1]
        color2_nombre = color_nombres[color2]
        color3_nombre = color_nombres[color3]
        
        concat = str(color1) + str(color2)
        resistenciaT = int(concat) * multiplicadores.get(color3, 1)
        porcentaje_tolerancia = resistenciaT * (tolerancia / 100)
        resistenciaMin = resistenciaT - porcentaje_tolerancia
        resistenciaMax = resistenciaT + porcentaje_tolerancia

    if tolerancia == 5:
        tolerancia_display = 'Dorado'
        tolerancia_color = 'goldenrod'  # Color para Dorado
    elif tolerancia == 10:
        tolerancia_display = 'Plata'
        tolerancia_color = 'silver'  # Color para Plata

    return render_template("resistencias.html", form=resistencia_form, color1=color1_nombre, color2=color2_nombre, color3=color3_nombre, tolerancia=tolerancia, resistenciaT=resistenciaT, resistenciaMin=resistenciaMin, resistenciaMax=resistenciaMax, tolerancia_display=tolerancia_display, tolerancia_color=tolerancia_color, color_css_mapping=color_css_mapping)
    

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

# @app.route("/resistencias")
# def resistencias():
#     return render_template("resistencias.html")


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