from wtforms import Form
from wtforms import SelectField, RadioField,StringField
from wtforms import validators

class ResistenciaForm(Form):
    colores = [
        (0, 'Negro'),
        (1, 'Cafe'),
        (2, 'Rojo'),
        (3, 'Naranja'),
        (4, 'Amarillo'),
        (5, 'Verde'), 
        (6, 'Azul'),
        (7, 'Violeta'),
        (8, 'Gris'),
        (9, 'Blanco'),
        ]
    tolerancias = [
        (5, 'Dorado'), 
        (10, 'Plata')
        ]

    color1 = SelectField('Color 1', choices=colores)
    color2 = SelectField('Color 2', choices=colores)
    color3 = SelectField('Color 3', choices=colores)
    tolerancia = RadioField('Tolerancia', choices=tolerancias)
    
class DiccionarioForm(Form):
    espanol=StringField('espanol',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=1, max=20, message='ingrese nombre valido')
    ])
    ingles=StringField('ingles',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=1, max=20, message='ingrese apellido valido')
    ])
    
class BusquedaForm(Form):
    opcionIdioma = RadioField('opcionIdioma', [
        validators.DataRequired(message='el campo es requerido'),
    ], choices=[(2, 'Español'), (1, 'Inglés')], default='espanol')
    buscar = StringField('buscar',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=1, max=20, message='ingrese apellido valido')
    ])