# Tkinter - Funciones de Tkinter en diseño

### __1 - Que es :__ 
tkinter es la biblioteca estándar de Python para crear interfaces gráficas de usuario (GUI). Es una envoltura del toolkit Tcl/Tk y permite construir ventanas, botones, cuadros de texto, menús y más de forma sencilla....
### __2 - Como usarla :__
Para poder usarla debemos poner en la parte de import, donde debemos poner:  
```python  
import tkinter
```
de esto podemos empezar a programar común y corriente
### __3 - Funciones :__

|Import |Funcion                              | Informacion de la funcion               |
|--------|-----------------------------|-----------------------------------------|
|Entry| → tk.Entry(parent)             |Caja de entrada para escribir texto.     |
|Label| → tk.Label(parent, text="...") |Muestra texto o imágenes en la ventana.  |
|Text| → tk.Text(parent)               |Área de texto más grande con varias líneas.|
|Frame| → tk.Frame(parent)             |Contenedor para organizar otros widgets.|
|Canvas| → tk.Canvas(parent, width, height)|Dibuja gráficos y formas.|
|Checkbutton| → tk.Checkbutton(parent, text="...")|Casilla de verificación.|
|Radiobutton| → tk.Radiobutton(parent, text="...", variable=var, value=1)|Botones de opción para elegir una sola opción de varias.|
|Scale| → tk.Scale(parent, from_=0, to=100, orient="horizontal")|Barra deslizante para seleccionar un valor.|
|Scrollbar| → tk.Scrollbar(parent, orient="vertical")|Barra de desplazamiento.|
|Listbox| → tk.Listbox(parent)|Lista de elementos seleccionables.|
|Spinbox| → tk.Spinbox(parent, from_=0, to=10)|Cuadro de selección numérica con flechas arriba/abajo.|
|Menu| → tk.Menu(parent)|Crea un menú desplegable.|
|Messagebox| → tk.messagebox.showinfo("Título", "Mensaje")|Muestra cuadros de diálogo emergentes.|
|Toplevel| → tk.Toplevel(parent)|Crea una nueva ventana secundaria.|
