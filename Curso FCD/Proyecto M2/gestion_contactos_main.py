
## este será el archivo main que se ejecuta y maneja el menu

from contacto import Contacto, chk_mail, chk_tel, datosPruebaContacto
from agenda import Agenda, datosPruebaAgenda
#primero importamos las funciones y clases desarrolladas en los otros archivos para 
#mayor orden.

#creamos una agenda nueva con datos de prueba o vacía según se desee
#si usar_datos_prueba=0 se crea vacía, si usar_datos_prueba=1 se crea con datos de prueba
usar_datos_prueba=1
dp = datosPruebaAgenda(usar_datos_prueba)
agendaActual = Agenda(dp)

#se muestra el menú principal y se gestionan las opciones
while True:
    
    print("1. Agregar Nuevo Contacto")
    print("2. Editar Contacto")
    print("3. Eliminar Contacto")
    print("4. Búsqueda de Contacto por Nombre")
    print("5. Búsqueda de Contacto por Número")
    print("6. Ver Lista de Contactos")
    print("0. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        
        print("1. Agregar Nuevo Contacto")
        if(usar_datos_prueba==0):
            print("Agregando Nuevo Contacto ")
            nombre=input("Ingrese Nombre ")
            telefono=input("Ingrese Teléfono ")
            while(chk_tel(telefono)==0): #se valida el teléfono con la función chk_tel
                                        #definida en contacto.py
                telefono=input("Teléfono incorrecto,ingrese teléfono correctamente ")

            mail=input("Ingrese Mail ")
            while(chk_mail(mail)==0): #se valida el mail con la función chk_mail
                                        #definida en contacto.py
                mail=input("Mail incorrecto,ingrese mail correctamente ")
            direccion=input("Ingrese Dirección ")
            nuevo_contacto=Contacto(nombre, telefono, mail, direccion) #se crea el nuevo contacto
                                                                        #según la funcion definida en contacto.py
            print(nuevo_contacto.mostrar())
        else:
            nuevo_contacto=Contacto(datosPruebaContacto()[0],datosPruebaContacto()[1],
                                    datosPruebaContacto()[2], datosPruebaContacto()[3])
            print(nuevo_contacto.mostrar())

        agendaActual.agregarRegistro(nuevo_contacto)
        agendaActual.mostrar()

    elif opcion == "2":

        print("2. Editar Contacto")
   
        print("qué contacto editar: ")
        k=0
        lista_contactos = list(agendaActual.contactos.values()) 
        for c in lista_contactos:               #loop para mostrar los contactos con un índice
            print(str(k)+". "+c.mostrar())      #que servirá para seleccionar el contacto a editar
            k=k+1                               
        
        n = input("Opción: ")
        n=int(n)                                #este índice servirá para elegir el contacto a editar
        telefono_actual=lista_contactos[n].getTelefono()

        print("1. Editar Nombre")
        print("2. Editar Teléfono")
        print("3. Editar mail")
        print("4. Editar Dirección")
        m = input("Opción: ")
        m=int(m)
        if m==1:
            agendaActual.editarContacto(
            telefono_actual,
            nuevo_nombre=input("Nuevo nombre: "))

        elif m==2:
            agendaActual.editarContacto(
            telefono_actual,
            nuevo_telefono=input("Nuevo teléfono: "))

        elif m ==3:
            agendaActual.editarContacto(
            telefono_actual,
            nuevo_mail=input("Nuevo mail: "))
        
        elif m ==4:
            agendaActual.editarContacto(
            telefono_actual,
            nueva_direccion=input("Nueva dirección: "))

        agendaActual.mostrar()

    elif opcion == "3":
    

        print("3. Eliminar Contacto")

        print("qué contacto quitar: ")
        k=0
        lista_contactos = list(agendaActual.contactos.values()) 
        for c in lista_contactos:           #loop para mostrar los contactos con un índice
            print(str(k)+". "+c.mostrar())    #que servirá para seleccionar el contacto a eliminar
            k=k+1
        n = input("Opción: ")
        agendaActual.quitarContacto(lista_contactos[int(n)].getTelefono()) #se elimina el contacto seleccionado
        agendaActual.mostrar()                              #se llama según getTelefono definido en contacto.py
                                                            #ya que la agenda usa el teléfono como clave única

    elif opcion == "4":
        print("Búsqueda de Contacto por Nombre ")           #se gestiona la búsqueda por nombre
        texto = input("Buscar nombre: ")                    #usando la función buscarPorNombre definida en agenda.py
        resultados = agendaActual.buscarPorNombre(texto)

        if not resultados:
            print("No se encontraron contactos")
        else:
            print("Resultados:")
            for c in resultados:                            #se muestran los contactos encontrados
                print(c.mostrar())                          #usando for por si fueran varios

    elif opcion == "5":                                     #se gestiona la búsqueda por teléfono parcial
        print("Búsqueda de Contacto por Número ")           #usando la función buscarPorTelefonoParcial definida en agenda.py
        texto = input("Ingrese parte del teléfono: ")
        resultados = agendaActual.buscarPorTelefonoParcial(texto)

        if resultados:
            for c in resultados:
                print(c.mostrar())                          #se muestran los contactos encontrados
        else:                                               #usando for por si fueran varios
            print("No se encontraron contactos")

    elif opcion == "6":
        print("Ver Lista de Contactos ")                    #se muestra la agenda completa
        agendaActual.mostrar()

    elif opcion == "0":
        break
    else:
        print("Opción inválida")