# **Proyecto de aprendizaje y practica para python**

## **Pynventario**

### *1. Lógica de sistemas Inventario:*
Todos sistemas de inventario basan en tres conceptos
básicos : Maestros, detalles y salida de información, que son los maestros: son las
entidades principal que describen la actividades del sistemas ejemplo Maestro de Ficha
de productos, grupo productos, marcas de productos etc. Que son los detalles: Son los
objetos encargados de darle movimientos a los maestros ejemplo detalle de carga de
inventario inicial , allí se ponemos las cantidades de productos que están en nuestro
almacenes y por último la salida de información este es más sencillo de explicar en donde
vemos todas las información suministradas por los maestro detalles ejemplo salida de
información del valor de nuestro inventario que es costo por cantidad de existencia.

#### *2. Herramientas y paradigmas a utilizar:*
Debemos utilizar para realizar el proyecto una o
varios modelos de base datos Ejemplo Mysql, MogonDb ,progress etc. Además un tipo de
vistas ejemplo Tkinterm,PyQT, Pyside, WinPy ,GTK y otras , también debemos aprender
Modelo Vista Controlador y para una fase mas avanzada a prototipar, UML, API ,
microservícios entre otras.

#### *3. Ejemplo de los que se quiere alcanzar:*
App de inventario , aquí tenemos los maestros:

###### *Productos:*
Datos contenidos en este id productos, Nombre de productos, Precios, costos, Tipo de
Impuesto, Utilización del producto descripción amplia de producto, Imagen(CRUD), opción de
Ingresar, Leer datos, modificar o actualizar y eliminar.

###### *Grupo:*
Datos contenidos Id grupo, Descripción. (Todos los maestros hay que hacer un CRUD).

###### *Documentos de transacción de Inventario (Maestro detalles):*
Datos contenidos Id o número de
documentos ,fecha de elaboración, usuario o persona que los realizo, descripción de transacción,
en detalle id de productos , descripción de productos , costo, precio, cantidad entrada o salida es
este documentos.

##### ***Ejemplo:***

Modulos Documentos de Transacción de Inventario:

Documentos : 0001 Fecha 01/03/2019 Usuario: Pedro Perez
Descripcion : Cargar de inventario inicial

***************** Detalle *************************************
#### **Tabla:**
|  Id Producto  |  Descripcion Producto  |  Costo  |  Precio  |      Tipo       |  Cantidad  |
| :-----------: | :--------------------: | :-----: | :------: | :-------------: | :--------: |
|    0001XA     |  Tarjeta madre foxcon  |   12$   |    23$   |  Entrada invent |    12,00   |
|    999911     |  Mouse Generico  |   2$   |    3$   |  Entrada invent |    120,00   |
|    19999A     |  Teclado USB Español  |   2$   |    4$   |  Entrada invent |    130,00   |
|    19999A     |  Teclado USB Español  |   2$   |    4$   |  Salida invent |    1,00   |
