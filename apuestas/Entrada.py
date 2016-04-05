from gi.repository import Gtk
from ApuestasDeportivas import Apuestas

class Entrada:
    def __init__(self):
        self.builder2 = Gtk.Builder()
        self.builder2.add_from_file("VentanaEntrada.glade")

        #Muestra una ventana de Entra con nombre (entry1) y password (entry2)
        self.entry1 = self.builder2.get_object("entry1")
        self.entry2 = self.builder2.get_object("entry2")
        self.ventanaEntrada = self.builder2.get_object("window2")

        sinal = {"on_button1_clicked": self.abrir_apuestas,
                 "delete-event": Gtk.main_quit}

        self.builder2.connect_signals(sinal)

        self.ventanaEntrada.show_all()

    #En caso de que el login sea correcto (diego/abal) abrirá la ventana apuestas
    def abrir_apuestas(self, widget):
        if self.entry1.get_text() == "diego" and self.entry2.get_text() == "abal":
           apuestas = Apuestas()
           self.ventanaEntrada.destroy()
        else:
            self.notificar_error("Usuario o clave incorrecta.")



    def notificar_error(self, mensaje):
        """"
        Mensaje para avisar de
        errores mediante una ventana emergente
        """
        window = Gtk.Window()
        label = Gtk.Label(mensaje)
        label.set_padding(15, 15)
        window.add(label)
        window.connect("delete-event", self.cerrar)
        window.set_position(Gtk.PositionType.RIGHT)

        window.show_all()

    #Metodo para cerrar la ventana emergente de error
    def cerrar(self, widget):
        widget.destroy()



Entrada()
Gtk.main()