Gestión de Contactos en Python

Descripción general

Este proyecto implementa una agenda de contactos en Python, ejecutable desde consola, que permite agregar, editar, eliminar, buscar y listar contactos.
El sistema está diseñado de forma modular, separando la lógica de negocio, los modelos de datos y la interfaz de usuario (CLI).

Cada contacto se identifica de forma única por su número de teléfono, lo que permite búsquedas y operaciones eficientes utilizando diccionarios.

Estructura del proyecto

Proyecto M2/
│
├── contacto.py
├── agenda.py
└── gestion_contactos_main.py

Módulos y responsabilidades
contacto.py — Modelo de contacto y validaciones

Este módulo define:

Clase Contacto
Representa un contacto individual con los siguientes atributos:

nombre

teléfono

mail

dirección

Métodos principales:

mostrar() → retorna un string con los datos del contacto

getTelefono() → retorna el teléfono

Funciones de validación

chk_mail(mail)
Valida formato de correo electrónico usando expresiones regulares.

chk_tel(telefono)
Valida formato de teléfono internacional (+ seguido de 7 a 15 dígitos).

Datos de prueba

datosPruebaContacto()
Retorna una tupla con datos simulados para pruebas rápidas.

agenda.py — Lógica de la agenda

Este módulo contiene la clase central del sistema.

Clase Agenda

La agenda utiliza un diccionario para almacenar contactos:

self.contactos = {
    telefono: Contacto
}


El teléfono actúa como clave única.

Métodos principales:

agregarRegistro(contacto)

Agrega un contacto si el teléfono no existe.

quitarContacto(telefono)

Elimina un contacto usando su teléfono.

editarContacto(...)

Permite modificar nombre, teléfono, mail o dirección.

El cambio de teléfono reindexa el diccionario.

mostrar()

Muestra todos los contactos registrados.

buscarPorNombre(texto)

Búsqueda parcial, no sensible a mayúsculas.

buscarPorTelefonoParcial(texto)

Búsqueda por coincidencia parcial del número.

Datos de prueba de agenda

datosPruebaAgenda(usar_datos_prueba)

Retorna una lista de contactos si el parámetro es 1.

Retorna None si se desea iniciar con agenda vacía.

gestion_contactos_main.py — Interfaz de usuario (CLI)

Este archivo es el punto de entrada de la aplicación.

Responsabilidades:

Crear la agenda (con o sin datos de prueba)

Mostrar el menú principal

Gestionar la entrada del usuario

Delegar operaciones a la clase Agenda

Funcionalidades disponibles:

Agregar nuevo contacto

Editar contacto existente

Eliminar contacto

Buscar contacto por nombre

Buscar contacto por número

Ver lista completa de contactos

Salir del programa

🏗 Arquitectura del proyecto

El proyecto sigue una arquitectura simple y clara:

Usuario
  ↓
Interfaz CLI (gestion_contactos_main.py)
  ↓
Lógica de negocio (Agenda)
  ↓
Modelo de datos (Contacto)

Principios aplicados:

Separación de responsabilidades

Modularidad

Uso de estructuras de datos eficientes (dict)

Validaciones centralizadas

Código legible y extensible

Instrucciones para ejecutar en entorno local
Requisitos

Python 3.8 o superior

No se requieren librerías externas salvo re que viene precargada en python

Pasos

1-Abrir una terminal en la carpeta del proyecto
2-Ejecutar:

python gestion_contactos_main.py


Interactuar con el menú desde la consola

Datos de prueba

Para iniciar la agenda con contactos de ejemplo, en gestion_contactos_main.py:

usar_datos_prueba = 1


Para iniciar vacía:

usar_datos_prueba = 0

El programa indicará siempre las opciones del menú.