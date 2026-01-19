from contacto import Contacto
from contacto import chk_mail, chk_tel
def datosPruebaAgenda(usar_datos_prueba: int):
    if usar_datos_prueba==1:
        return [
            ("Juan", "+56912341234", "juan@gmail.com", "Casa de Juan 100"),
            ("Ana",  "+56912351235", "ana@gmail.com",  "Casa de Ana 101")
        ]
    else:
        return None

class Agenda:
    def __init__(self, datos_prueba=None):
        self.contactos = {}  # diccionario teléfono -> Contacto

        if datos_prueba:
            for nombre, telefono, mail, direccion in datos_prueba:
                self.agregarRegistro(
                Contacto(nombre, telefono, mail, direccion)
                )

    def agregarRegistro(self, contacto: Contacto):
        if contacto.telefono in self.contactos:
            print("Ya existe un contacto con ese teléfono ")
            return False

        self.contactos[contacto.telefono] = contacto
        print("Contacto agregado correctamente ")
        return True
    
    def quitarContacto(self, telefono: str):
        contacto = self.contactos.pop(telefono, None)

        if contacto is None:
            print("Contacto no encontrado")
            return False

        print("Contacto eliminado correctamente")
        return True

    def mostrar(self):
        if not self.contactos:
            print("Agenda vacía ")
            return

        print("\nLista de contactos: ")
        for contacto in self.contactos.values():
            print(contacto.mostrar())
            
    def editarContacto(
        self,
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
            if chk_tel(nuevo_telefono) == 0:
                print("Teléfono inválido")
                return False

            if nuevo_telefono in self.contactos:
                print("Ya existe un contacto con ese teléfono")
                return False

            # reindexar
            del self.contactos[telefono_actual]
            contacto.telefono = nuevo_telefono
            self.contactos[nuevo_telefono] = contacto
            telefono_actual = nuevo_telefono

        if nuevo_nombre:
            contacto.nombre = nuevo_nombre

        if nuevo_mail:
            if chk_mail(nuevo_mail) == 0:
                print("Mail inválido")
                return False
            contacto.mail = nuevo_mail

        if nueva_direccion:
            contacto.direccion = nueva_direccion

        print("Contacto editado correctamente")
        return True
    
    def buscarPorNombre(self, texto: str):
        texto = texto.lower().strip()
        resultados = []

        for contacto in self.contactos.values():
            if texto in contacto.nombre.lower():
                resultados.append(contacto)

        return resultados
    
    def buscarPorTelefonoParcial(self, texto: str):
        texto = texto.strip()
        resultados = []

        for telefono, contacto in self.contactos.items():
            if texto in telefono:
                resultados.append(contacto)

        return resultados