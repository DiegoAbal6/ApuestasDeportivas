from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate,Table,TableStyle,Paragraph,Spacer,Image
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

import time
import datetime
import sqlite3 as dbapi
from gi.repository import Gtk
class PDF():
    """
    Esta clase GenerarPDF esta creada para poner generar un informe PDF sobre los datos de la base

    """
    def __init__(self):
        """
        Conexion con la base de datos
        """
        self.bd = dbapi.connect("basededatosapuestas.dat")
        self.cursor = self.bd.cursor()
        #foto = Image("./imagen.jpg")
        self.elementos = []

    def pdf(self):
        """
        Metodo pdf:
        Este metodo genera el pdf, y en el nombre

        """
        historialpdf ="Apuestas"+ str(datetime.date.today()) +"_.pdf"
        c = canvas.Canvas(historialpdf, pagesize=A4)
        c.drawString(20,800,"Lista de apuestas realizadas")

        #c.drawImage(foto,200,800)
        #c.drawImage(self.foto, 1*cm, 26*cm, 19*cm, 3*cm)

        tabla = self.tabla()
        tabla.wrapOn(c, 20, 30)
        tabla.drawOn(c, 20, 600)
        c.save()

        self.notificar("PDF Generado")
        #self.elements.append(tabla)
        #doc.build(elements)

    def tabla(self):
        """
        Metodo tabla:
        Este metodo genera la tabla en el pdf metiendo el contenido de la tabla

        """
        apuestas = list(self.cursor.execute("select * from apuestas"))
        titulos = [["CODIGO","EVENTO", "PRONOSTICO", "CUOTA"]]

        apuestas = titulos + apuestas
        tabla = Table(apuestas)

        tabla.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 2, colors.white),
                                   ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                   ('LEFTPADDING', (0, 0), (-1, -1), 3),
                                   ('RIGHTPADDING', (0, 0), (-1, -1), 3),
                                   ('FONTSIZE', (0, 1), (-1, -1), 10),
                                   ('BACKGROUND', (0,1),(-1,-1), colors.lightblue),
                                   ('BACKGROUND', (0, 0), (-1, 0), colors.blue)]))

        return tabla
    def cerrar(self, widget):
        """"
        Metodo cerrar:
        Destruye la ventana emergente que nos
        muestra el mensaje de informacion
        """
        widget.destroy()

    def notificar(self, texto):
        """
        Metodo que saca una ventana emergente
        """
        window = Gtk.Window(title="Oye!")
        label = Gtk.Label(texto)
        label.set_padding(15,15)
        window.add(label)
        window.connect("delete-event", self.cerrar)
        window.set_position(Gtk.PositionType.RIGHT)
        window.show_all()
#PDF().pdf()