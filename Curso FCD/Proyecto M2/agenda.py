from contacto import Contacto
from contacto import chk_mail, chk_tel
def datosPruebaAgenda(usar_datos_prueba: int): #función que retorna datos de prueba para la agenda
    if usar_datos_prueba==1:
        return [
            ("Juan", "+56912341234", "juan@gmail.com", "Casa de Juan 100"),
            ("Ana",  "+56912351235", "ana@gmail.com",  "Casa de Ana 101")
        ]
    else:
        return None

class Agenda:
    def __init__(self, datos_prueba=None):
        self.contactos = {}  # se define un diccionario para almacenar los contactos
                            # la clave será el teléfono (único) y el valor será el objeto Contacto
                            #pero eso se ve en agregarRegistro
        if datos_prueba:
            for nombre, telefono, mail, direccion in datos_prueba:
                self.agregarRegistro( #se llama a la función agregarRegistro para agregar cada contacto de prueba
                Contacto(nombre, telefono, mail, direccion)
                )

    def agregarRegistro(self, contacto: Contacto): #se define la función para agregar un contacto
        if contacto.telefono in self.contactos: #verifica si el teléfono ya existe en la agenda
            print("Ya existe un contacto con ese teléfono ")
            return False

        self.contactos[contacto.telefono] = contacto #agrega el contacto al diccionario usando el teléfono como clave
        print("Contacto agregado correctamente ")
        return True
    
    def quitarContacto(self, telefono: str): #se define la función para eliminar un contacto según su teléfono
        contacto = self.contactos.pop(telefono, None)

        if contacto is None:
            print("Contacto no encontrado")
            return False

        print("Contacto eliminado correctamente")
        return True

    def mostrar(self):          #se define la función para mostrar todos los contactos de la agenda
        if not self.contactos: #a diferencia de contacto.mostrar, esta función imprime directamente
            print("Agenda vacía ") #se hizo así porque es más práctico para este caso
            return

        print("\nLista de contactos: ")
        for contacto in self.contactos.values():
            print(contacto.mostrar())
            
    def editarContacto( #se define la función para editar un contacto existente
        self,               #debido al uso de teléfono como clave única, la edición de teléfono es un caso especial
        telefono_actual: str,
        nuevo_nombre: str = None,
        nuevo_telefono: str = None,
        nuevo_mail: str = None,
        nueva_direccion: str = None
        ):
        contacto = self.contactos.get(telefono_actual)

        if not contacto:
            print("Contacto no encontrado")
            return False

        # Caso especial: cambio de teléfono (clave del diccionario)
        if nuevo_telefono and nuevo_telefono != telefono_actual:
            if chk_tel(nuevo_telefono) == 0: #se llama a la función chk_tel definida en contacto.py para validar el teléfono
                print("Teléfono inválido")
                return False

            if nuevo_telefono in self.contactos:
                print("Ya existe un contacto con ese teléfono")
                return False

            # reindexar el contacto con el nuevo teléfono, eliminando la antigua clave
            del self.contactos[telefono_actual] # y agregando el contacto con el nuevo teléfono
            contacto.telefono = nuevo_telefono
            self.contactos[nuevo_telefono] = contacto
            telefono_actual = nuevo_telefono

        if nuevo_nombre: #a diferencia del cambio de teléfono, los otros campos son simples atributos del objeto Contacto
            contacto.nombre = nuevo_nombre

        if nuevo_mail:
            if chk_mail(nuevo_mail) == 0: #se llama a la función chk_mail definida en contacto.py para validar el mail
                print("Mail inválido")
                return False
            contacto.mail = nuevo_mail

        if nueva_direccion:
            contacto.direccion = nueva_direccion

        print("Contacto editado correctamente")
        return True
    
    def buscarPorNombre(self, texto: str): #se define la función para buscar contactos por nombre
        texto = texto.lower().strip()       #acá se convierte el texto a minúsculas y se eliminan espacios en blanco
        resultados = []                     

        for contacto in self.contactos.values(): #ciclando por todos los contactos
            if texto in contacto.nombre.lower(): #se hace de este modo para buscar matches parciales en el nombre
                resultados.append(contacto)

        return resultados
    
    def buscarPorTelefonoParcial(self, texto: str): #se define la función para buscar contactos por teléfono parcial
        texto = texto.strip()       #acá se eliminan espacios en blanco del texto
        resultados = []

        for telefono, contacto in self.contactos.items(): #ciclando por todos los contactos
            if texto in telefono:                   #se busca si el texto tiene match parcial en el teléfono
                resultados.append(contacto)        

        return resultados