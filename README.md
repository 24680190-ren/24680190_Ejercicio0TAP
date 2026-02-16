**24680190_Ejercicio0TAP renta**

<br>Cómo crear botones que,al dar clic, realicen una acción y la muestren en un display, así como también uno que limpie la pantalla.</br>
<br>Para iniciar,debemos instalar Python y Flet; en mi caso,usaré también Git Bash en lugar del CMD.</br>
<br>Para instalar Python desde la página oficial, no se requiere tener muchos conocimientos. Podemos verificar que la instalación fue exitosa colocando en el CMD lo siguiente:</br>
```bash
python --version 
o
py --version
```
<br>Dado que el CMD no reconoce un comando necesario para la instalación de Flet, haremos uso de Git Bash. Al igual que con la instalación anterior, solo necesitamos descargarlo de la página oficial y seleccionar la versión más adecuada para nuestro sistema operativo.</br>
<br>Cuando esté descargado, solo lo ejecutamos y damos clic en "Next". Teniendo lista la instalación, buscaremos la aplicación Git Bash, la cual se verá un poco parecida al CMD pero con más colores.</br>

<br>Pasamos a la creación de un enotono virtual para dentro de este hacer la isntalación de flet </br>
<br>Crear una carpeta en la que se va a crear el entorno. </br>
<br>En mi caso accedere al escritorio</br>
```bash
cd Desktop
```
<br>Creo una carepta con el comando mkdir seguido del nombre de la carpeta</br>
```bash
mkdir tap
```
Accedemos a esta con el mismo comando de cd
```bash
cd tap 
```
<br>Luego de hacer lo anterior creamos y activamos el entrono virtual con los siguiente comandos:</br>
Dentro de la carpeta se crearan varios archivos de los cuales dos son importantes para la instalación de flet, estos serián la carpeta Scripts y el archivo activate 
```bash
python -m venv .venv o py -m venv .venv 
source .venv/Scripts/activate
```
LLegamos a la parte en la que instalaremos flet usando los siguientes comandos 
```bash
pip install 'flet[all]'
```
Para verifcar que todo salio bien en la instalación usa el siguiente comando, el cual te debe arrojar la verión del flet 
```bash
flet doctor 
```
Creamos nuetra primer app con el comando 
```bash
flet create  
```
<br>Veremos en la pantalla una interfaz con un número en la pantalla y un botón que la darle clic aumenta el número que esta en el centro.</br>
<br>Para inicial la creación de nuestro código abrimos Visual Studio Code seleccionando la carpeta de tap en la que encontraremos una subcarpeta llamada src esta contiene un main pero nosotros crearemos uno nuevo main.</br>
Lo primero que haremos sera exportar flet, seguido de la configuración de la pantalla principal, determinaremos su tamaño (ancho=width y alto=height)y titulo. 
```python
import flet as ft 
def main(page: ft.Page): #Se define la función priciapl que sera main

  #Configuración de la pantalla
  page.title = "Calculadora TAP"
  page.window_width=600
  page.window_height=600
  page.padding=50  
```
Seguimos con la creación del display en el que se mostrara el resultado de dar clic en uno de los botones:
```python
#Displey donde se mostrara cada acción del botón
  display=ft.Container(
    content=ft.Text("0",size=30),
    bgcolor=ft.Colors.BLACK12,
    border_radius=15,
    alignment=ft.alignment.Alignment(1,2),
    padding=10,
    width=300, #Forzamos el ancho manualmente
    height=70
   )
```
<br>En este recuadro se inciara con un texto que sera 0, debemos asignar un formato que es indicarel cuantos pixeles tentra de ancho, alto, el redondeo de borde, color y alineación del texto.</br> 
Este display esta dentro de un contenedor el cual se esta heredando de una clase predeterminada por flet por eso se usa <ins>**ft.Container** </ins> 
Para agregar los botones heredaremos la clase GridView <ins>**ft.GridView** </ins>	, se hereda de la misma menera que en contenedor. El grid es una estructura para organizar elementos en un interfaz, osea que dentro de este vamos a ordenar los botones.
```python
 #grid para los botones
  r= ft.GridView(
    runs_count=2, #Crea dos columnas 
    spacing=10,
    run_spacing=10,
    width=300, #Ancho fijo igual al del display
    height=500, #Alto fijo para que no crezca
    expand=False 
  )
```
Como lo hemos visto también en este grid tenemos que darle un formato: ancho, alto, número de columnas y el espacio que se dejara entre cada una. 
Veremos como crear un botón y que configuracion tenemos que darle pero también crearemos la funcion del on_click:
```python
#Función para manejar los clicks de los botones 
  def click_boton(e):
    inicial_valor=display.content.value
    valor_click=e.control.data
    #Evalua el valor que tiene el display(valor 0) y lo resplaza por el valor del click
    if inicial_valor=="0":
      display.content.value=valor_click
    #Si el valor no es sero el nuvo se agrega al valor del click anterior 
    else: 
      display.content.value+=valor_click
    page.update()

```
Esta fución es la encargada de mostrar lo que hace nuestro botón al dar clic:
1. Se asigan el valor que tiene el display (isplay.content.value) a la variable valor_inicial.
2. La variable (e) se le asigana a valor_click
3. Se utliza la condición <ins>**if** </ins> que dice si inicial_valor es igual a 0 ahora.
4. De lo cotrario si no cumple el valor se suman.
5. Es importante agregar <ins>**page.update** </ins> para refrescar y mostrar algo en la patalla.
Seguimos con la configuracion de los botenes:
```python
r.controls.append(
    ft.ElevatedButton(
      content=ft.Text("1",size=20),
      data="1",
      on_click=click_boton, 
      height=20, 
      bgcolor=ft.Colors.PINK_100))
```
El botón esta compuesto por un color,un alto, ancho , un dato el cual e simportante en la función on_click y  el texto que se muestra en botón. Ese mismo codigo se copia para los otros 3 botones, la unica modificaión es data y el texto que se muestra.
```python
 r.controls.append(
    ft.ElevatedButton(
      content=ft.Text("1",size=20),
      data="1",
      on_click=click_boton, 
      height=20, 
      bgcolor=ft.Colors.PINK_100))
  
  r.controls.append(
    ft.ElevatedButton(
    content=ft.Text("2",size=20), 
    data="2",
    on_click=click_boton, 
    height=20, 
    bgcolor=ft.Colors.PINK_100))
  
  r.controls.append(
    ft.ElevatedButton(
      content=ft.Text("3",size=20), 
      data="3",
      on_click=click_boton, 
      height=20, 
      bgcolor=ft.Colors.PINK_100))
  
  r.controls.append(
    ft.ElevatedButton(
      content=ft.Text("4",size=20),
      data="4",
      on_click=click_boton,
      height=20, 
      bgcolor=ft.Colors.PINK_100))
```
Para el botón que limpia la pantalla tambien debemos definir una función para que pueda realizar la acción deseada.
Como hacer la función:
1. Creamos la función que llaremos limpiar_pantalla
2. A la variable display.content.value le asiganmos el valor de 0
3. Imporate agregar el page.update
```python
def limpiar_pantalla(e):
    # Cambiamos el texto directamente a "0"
    display.content.value = "0"
    # Refrescamos la pantalla para que se vea el cambio
    page.update()
```
Formato del botón AC :
```python
r.controls.append(
    ft.ElevatedButton(
      content=ft.Text("AC", size=20),
      on_click=limpiar_pantalla, 
      bgcolor=ft.Colors.RED_200))
```
Para terminar creamos una variable llamada layout_principal y le asignamos un objeto tipo Columna. Imagina que esto es un estante vertical donde iremos colocando tus componentes desde arriba hacia abajo.
Esta es la parte más importante. La propiedad controls recibe una lista de los elementos que queremos que aparezcan dentro de esa columna.
1. display: Es el primer elemento de la lista, por lo que aparecerá en la parte superior.
2. r: Es el segundo elemento, por lo que aparecerá justo debajo del display.
<br>Esta propiedad (tight=True) ajusta el tamaño de la columna:</br>
<br>Por defecto, una columna intenta ocupar todo el espacio vertical disponible.</br>
<br>Al poner tight=True, le decimos a la columna que solo ocupe el espacio necesario para cubrir sus elementos hijos (display y r). Es como si el contenedor se "encogiera" para ajustarse perfectamente al contenido.</br>
```python
layout_principal=ft.Column(
    controls=[
      display,
      r
    ],
    tight=True
  )
```
Al final agregamos la pasrte que hara que nuestro código compile:
```python
page.add(display,r)
  page.update()
if __name__=="__main__":  
 ft.app(target=main)
```
Código completo:
```python
import flet as ft 
def main(page: ft.Page): #Se define la dunción priciapl que sera main

  #Configuración de la pantalla
  page.title = "Calculadora TAP"
  page.window_width=600
  page.window_height=600
  page.padding=50

  #Funcion para manejar los clicks de los botones 
  def click_boton(e):
    inicial_valor=display.content.value
    valor_click=e.control.data
    #Evalua el valor que tiene el display(valor 0) y lo resplaza por el valor del click
    if inicial_valor=="0":
      display.content.value=valor_click
    #Si el valor no es sero el nuvo se agrega al valor del click anterior 
    else: 
      display.content.value+=valor_click
    page.update()

  def limpiar_pantalla(e):
    # Cambiamos el texto directamente a "0"
    display.content.value = "0"
    # Refrescamos la pantalla para que se vea el cambio
    page.update()
  
  #Displey donde se mostrara cada acción del botón
  display=ft.Container(
    content=ft.Text("0",size=30),
    bgcolor=ft.Colors.BLACK12,
    border_radius=15,
    alignment=ft.alignment.Alignment(1,2),
    padding=10,
    width=300, #Forzamos el ancho manualmente
    height=70
   )
  
  #grid para los botones
  r= ft.GridView(
    runs_count=2, #Crea dos columnas 
    spacing=10,
    run_spacing=10,
    width=300, #Ancho fijo igual al del display
    height=500, #Alto fijo para que no crezca
    expand=False 
  )

  r.controls.append(
    ft.ElevatedButton(
      content=ft.Text("1",size=20),
      data="1",
      on_click=click_boton, 
      height=20, 
      bgcolor=ft.Colors.PINK_100))
  
  r.controls.append(
    ft.ElevatedButton(
    content=ft.Text("2",size=20), 
    data="2",
    on_click=click_boton, 
    height=20, 
    bgcolor=ft.Colors.PINK_100))
  
  r.controls.append(
    ft.ElevatedButton(
      content=ft.Text("3",size=20), 
      data="3",
      on_click=click_boton, 
      height=20, 
      bgcolor=ft.Colors.PINK_100))
  
  r.controls.append(
    ft.ElevatedButton(
      content=ft.Text("4",size=20),
      data="4",
      on_click=click_boton,
      height=20, 
      bgcolor=ft.Colors.PINK_100))
  
  r.controls.append(
    ft.ElevatedButton(
      content=ft.Text("AC", size=20),
      on_click=limpiar_pantalla, 
      bgcolor=ft.Colors.RED_200 
    )
  )
  
  layout_principal=ft.Column(
    controls=[
      display,
      r
    ],
    tight=True
  )
  page.add(display,r)
  page.update()
if __name__=="__main__":  
 ft.app(target=main)
```
<br>Resultado del código:</br>

<img width="267" height="511" alt="image" src="https://github.com/user-attachments/assets/6746be58-5d53-42b9-a011-9a5f44e81ec8" />

