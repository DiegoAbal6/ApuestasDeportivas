import sqlite3 as dbapi
from gi.repository import Gtk
from lxml.html import _element_name
#import Generarpdf as pdf


class Apuestas:
    def __init__(self):


        self.db = dbapi.connect("basededatosapuestas.dat")

        self.cursor = self.db.cursor()

        fichero = "VentanaApuestas.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(fichero)

        self.entry1 = self.builder.get_object("entry1")
        self.entry2 = self.builder.get_object("entry2")
        self.entry3 = self.builder.get_object("entry3")
        self.entry4 = self.builder.get_object("entry4")
        self.ventana = self.builder.get_object("window1")

        sinais = {"on_insertar_clicked": self.on_insertar_clicked,
                  "on_consultar_clicked": self.on_consultar_clicked,
                  "on_borrar_clicked": self.on_borrar_clicked,
                  "on_modificar_clicked": self.on_modificar_clicked,
                  "on_imprimir_clicked": self.imprimir,
                  "on_ayuda_clicked": self.on_ayuda_clicked,
                  "delete-event": Gtk.main_quit}

        self.builder.connect_signals(sinais)

        self.ventana.show_all()

    def on_ayuda_clicked(self,widget):
        self.notificar("La práctica abusiva de apuestas, puede generar ludopatía, juegue con responsabilidad")

    def on_consultar_clicked(self, widget):
        """
        Evento de consulta
        """
        self.ver_resultados()

    def ver_resultados(self):
        """
        Ventana de resultados
        Muestra todo
        """
        ventana = Gtk.Window(title = "Contenido de la base de datos.")
        ventana.connect("delete-event", self.cerrar)

        codigo = Gtk.Label("CODIGO")
        evento = Gtk.Label("EVENTO")
        pronostico = Gtk.Label("PRONOSTICO")
        cuota = Gtk.Label("CUOTA")

        titulos = Gtk.Box()
        titulos.set_homogeneous(True)

        titulos.add(codigo)
        titulos.add(evento)
        titulos.add(pronostico)
        titulos.add(cuota)

        grid = Gtk.VBox()
        ventana.add(grid)
        grid.add(titulos)

        self.cursor.execute("Select * from apuestas")

        for fila in self.cursor:
            caja = Gtk.Box()
            caja.set_homogeneous(True)
            for c, elemento in enumerate(fila):
                label = Gtk.Label()
                label.set_text(str(elemento))
                caja.add(label)
            grid.add(caja)
            #print("Codigo: " + str(resultado[0]) + ", Evento: " + str(resultado[1]) + ", Pronostico: " + str(resultado[2]) + ", Cuota: " + str(resultado[3]))
        ventana.show_all()

    def on_borrar_clicked(self, widget):
        """
        Evento de borrado
        """
        entry1 = self.entry1.get_text()
        self.cursor.execute("delete from apuestas where codigo ='" + entry1 + "'")
        self.db.commit()
        self.notificar("Borrado")

    def on_modificar_clicked(self, widget):
        """
        Metodo modificar
        """
        entry2 = self.entry2.get_text()
        entry3 = self.entry3.get_text()
        entry4 = self.entry4.get_text()
        entry1 = self.entry1.get_text()
        if entry1.isdigit and len(entry2)==10 and entry3.isdigit and len(entry4)==3:
            self.boolean = True
        else:
            self.notificar("Datos invalidos.")
            self.boolean = False

        if(self.boolean):
            try:

                self.db.execute(
                    "update apuestas set Evento ='" + entry2 + "',Pronostico='" + entry3 + "',Cuota='" + entry4 + "'" +
                    " where Codigo='" + entry1 + "'")
                self.notificar("Modificado")
                self.db.commit()
                self.ver_resultados()
            except dbapi.IntegrityError:
                    self.notificar("La matricula ya existe")

    def on_insertar_clicked(self, widget):
        """
        Metodo insertar, tiene 4 campos (entry 1,2,3 y 4)
        """
        entry1 = self.entry1.get_text()
        entry2 = self.entry2.get_text()
        entry3 = self.entry3.get_text()
        entry4 = self.entry4.get_text()

        if entry1.isdigit and len(entry2)==10 and entry3.isdigit and len(entry4)==3:
            self.boolean = True
        else:
            self.notificar("Datos invalidos.")
            self.boolean = False

        if(self.boolean==True):
            try:
                self.db.execute(
                    "insert into apuestas values('" + entry1 + "','" + entry2 + "','" + entry3 + "','" + entry4 + "')")

                self.notificar("Insertado")
                self.db.commit()
                self.ver_resultados()
            except dbapi.IntegrityError:
                self.notificar("La matricula ya existe")

    def notificar(self, mensaje):
        """
        Mensaje para avisar de errores mediante un ventana emergente

        """
        window = Gtk.Window()
        label = Gtk.Label(mensaje)
        label.set_padding(15, 15)
        window.add(label)
        window.connect("delete-event", self.cerrar)
        window.set_position(Gtk.PositionType.RIGHT)

        window.show_all()

    def cerrar(self, widget):
        """
        Metodo para cerrar las ventanas


        """
        widget.destroy()

    def imprimir(self,widget):
        """
        Metodo Imprimir, hace llamada a la clase GenerarPDF para que cree el informe

        """
        #obj = pdf.PDF()
        #obj.pdf()



