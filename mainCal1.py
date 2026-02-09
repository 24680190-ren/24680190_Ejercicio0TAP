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