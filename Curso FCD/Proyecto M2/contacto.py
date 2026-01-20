import re #librería que nos permitirá hacer un match de expresiones regulares para
            #verificar que los mails sean mails realmente (no verifica la existencia,
            #sólo verifica si tienen un "@"" y un ".")
def chk_mail(mail):
    MAIL_EXPREG = r"^[^@]+@[^@]+\.[^@]+$" # definición de expresión regular al que se comparará cada
                                          # mail a validar. se divide en 4 partes:
                                          # parte 1: ^[^@]+    inicio de texto que no permite "@"
                                          # Parte 2: @[^@]+     1 sólo "@" seguido de texto sin "@"
                                          # Parte 3: \.[^@]+   1 sólo ppunto seguido de texto sin "@"
                                          # Parte 4: $        expresión para finalizar 
                                          # Hay casos que no considera correctamente, pero lo evidente,
                                          # lo valida

    if not re.match(MAIL_EXPREG, mail):
        return 0
    else:
        return mail
    
def chk_tel(telefono):
    TELEFONO_EXPREG = r"^\+\d{7,15}$"      # del mismo modo, esta expresión regular servirá para
                                            # validar número de teléfono con 1 sólo "+" 
                                            # seguido de sólo números (entre 7 y 15 números)

    if not re.match(TELEFONO_EXPREG, telefono):
        return 0
    else:
        return telefono
def datosPruebaContacto():              #se define una función que retorna datos de prueba para un contacto
    return ("Lucas","+5699999999","lucas@ale.cl","Camino 1559")
    
class Contacto:                     #se define la clase contacto basado en nombre, teléfono, mail y dirección

    def __init__(self, nombre: str, telefono: str, mail: str, direccion: str):
        self.nombre = nombre
        self.telefono = telefono
        self.mail= mail
        self.direccion = direccion

    def mostrar(self):          #función para mostrar los datos del contacto. retorna un string con los datos en lugar de imprimirlos
        #print(f"Nombre: {self.nombre} | Teléfono: {self.telefono} | Mail: {self.mail} | Dirección: {self.direccion}")
        return (f"Nombre: {self.nombre} | Teléfono: {self.telefono} | Mail: {self.mail} | Dirección: {self.direccion}")
        
    def getTelefono(self):    #función que retorna el teléfono del contacto. será útil por cómo la agenda usa el teléfono como clave única
        return(self.telefono)
