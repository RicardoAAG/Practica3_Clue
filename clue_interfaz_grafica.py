import json
import random
import tkinter as tk
from tkinter import simpledialog, messagebox

intentos_restantes = 5
respuestas_correctas = 0

def elegir_testimonio(buscar, tipo):
    global respuestas_correctas
    equivocado = "No deduciste correctamente"
    correcto = "Deduciste correctamente"
    if tipo == 0:
        if buscar == 1:
            return testimonio1
        if buscar == 2:
            return testimonio2
        if buscar == 3:
            return testimonio3
        if buscar == 4:
            return testimonio4
        if buscar == 5:
            return sospechoso
        if buscar == 6:
            return lugar
        if buscar == 7:
            return arma
    else:
        if buscar in (1, 2, 3, 4):
            return equivocado
        if buscar in (5, 6, 7):
            respuestas_correctas += 1
            return correcto

def cargar_base_de_datos(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data  

def buscar(sospechosos, revisar, tipo):
    revisar = int(revisar) - 1
    if 0 <= revisar < len(sospechosos):
        objetivo = sospechosos[revisar]
        if objetivo in testimonios:
            messagebox.showinfo("Testimonio", elegir_testimonio(testimonios[objetivo], tipo))
            return True
    else:
        messagebox.showerror("Error", "Insertar el número de la opción")
        return False

def investigar_personaje():
    global intentos_restantes
    if intentos_restantes > 0:
        sospechosos = list(personajes.keys())
        revisar = simpledialog.askinteger("Investigar Personaje", "Selecciona un sospechoso a interrogar: \n1) Ingeniero\n2) Espia\n3) Medico\n4) Soldado\n5) Francotirador\n")
        while revisar is not None:
            if buscar(sospechosos, revisar, 0):
                intentos_restantes -= 1
                break
            revisar = simpledialog.askinteger("Investigar Personaje", "Selecciona un sospechoso a interrogar: \n1) Ingeniero\n2) Espia\n3) Medico\n4) Soldado\n5) Francotirador\n")
    else:
        messagebox.showinfo("Fin de juego", "Se te han agotado los intentos.")
        investigar_personaje_button.config(state="disabled")

def investigar_locacion():
    global intentos_restantes
    if intentos_restantes > 0:
        sospechosos = list(locaciones.keys())
        revisar = simpledialog.askinteger("Investigar Locación", "Selecciona un lugar a investigar: \n1) Casa\n2) Tunel\n3) Barracones\n4) Puesto de guardia\n5) Enfermeria\n")
        while revisar is not None:
            if buscar(sospechosos, revisar, 0):
                intentos_restantes -= 1
                break
            revisar = simpledialog.askinteger("Investigar Locación", "Selecciona un lugar a investigar: \n1) Casa\n2) Tunel\n3) Barracones\n4) Puesto de guardia\n5) Enfermeria\n")
    else:
        messagebox.showinfo("Fin de juego", "Se te han agotado los intentos.")
        investigar_locacion_button.config(state="disabled")

        
def investigar_arma():
    global intentos_restantes
    if intentos_restantes > 0:
        sospechosos = list(armas.keys())
        revisar = simpledialog.askinteger("Investigar Arma", "Selecciona un arma a inspeccionar: \n1) Papel de regalo\n2) Katana\n3) Cuchillo mariposa\n4) Guante de box\n5) Llave inglesa\n")
        while revisar is not None:
            if buscar(sospechosos, revisar, 0):
                intentos_restantes -= 1
                break
            revisar = simpledialog.askinteger("Investigar Arma", "Selecciona un arma a inspeccionar: \n1) Papel de regalo\n2) Katana\n3) Cuchillo mariposa\n4) Guante de box\n5) Llave inglesa\n")
    else:
        messagebox.showinfo("Fin de juego", "Se te han agotado los intentos.")
        investigar_arma_button.config(state="disabled")
        
def alazar_borrar_personaje(numero):
    borrar = random.choice(list(personajes2.keys()))
    del informacion2["evidencia"][0]["personajes"][borrar]
    testimonios[borrar] = numero
    return borrar

def alazar_borrar_locacion(numero):
    borrar = random.choice(list(locaciones2.keys()))
    del informacion2["evidencia"][1]["locaciones"][borrar]
    testimonios[borrar] = numero
    return borrar

def alazar_borrar_arma(numero):
    borrar = random.choice(list(armas2.keys()))
    del informacion2["evidencia"][2]["armas"][borrar]
    testimonios[borrar] = numero
    return borrar

def finalizar_juego():
    global intentos_restantes
    if intentos_restantes == 0:
        final_culpable = simpledialog.askinteger("Culpable", "Selecciona un culpable: \n1) Ingeniero\n2) Espia\n3) Medico\n4) Soldado\n5) Francotirador\n")
        final_lugar = simpledialog.askinteger("Lugar", "Selecciona el lugar del asesinato: \n1) Casa\n2) Tunel\n3) Barracones\n4) Puesto de guardia\n5) Enfermeria\n")
        final_arma = simpledialog.askinteger("Arma Homicida", "Selecciona el arma homicida: \n1) Papel de regalo\n2) Katana\n3) Cuchillo mariposa\n4) Guante de box\n5) Llave inglesa\n")
        
        y = buscar(list(personajes.keys()), final_culpable, 1)
        if not y:
            return
    
        y = buscar(list(locaciones.keys()), final_lugar, 1)
        if not y:
            return
    
        y = buscar(list(armas.keys()), final_arma, 1)
        if not y:
            return
    
        resultado = final_resultado
        messagebox.showinfo("Resultado", resultado)
        if respuestas_correctas==3:
            resultado_label.config(text=resultado+"\nDeduciste correctamente "+str(respuestas_correctas)+" veces GANASTE")
            intentos_restantes=-1
        else:
            resultado_label.config(text=resultado+"\nDeduciste correctamente "+str(respuestas_correctas)+" veces PERDISTE")
            intentos_restantes=-1
    else:
        messagebox.showinfo("Advertencia", "Debes utilizar los 5 intentos antes de finalizar el juego.")
    

# Crear una ventana Tkinter
root = tk.Tk()
root.title("Clue - Juego de detectives")
root.minsize(300,200)

personajes = {}
locaciones = {}
armas = {}
testimonios = {}
personajes2 = {}
locaciones2 = {}
armas2 = {}

# Cargar datos del archivo
informacion = cargar_base_de_datos('clue_base_de_datos.json')
informacion2 = cargar_base_de_datos('clue_base_de_datos.json')

personajes = informacion['evidencia'][0]['personajes']
locaciones = informacion['evidencia'][1]['locaciones']
armas = informacion['evidencia'][2]['armas']

asesino = random.choice(list(personajes.keys()))
informacion["evidencia"][0]["personajes"][asesino] = True
escena_crimen = random.choice(list(locaciones.keys()))
informacion["evidencia"][1]["locaciones"][escena_crimen] = True
arma_homicida = random.choice(list(armas.keys()))
informacion["evidencia"][2]["armas"][arma_homicida] = True

personajes2 = informacion2['evidencia'][0]['personajes']
locaciones2 = informacion2['evidencia'][1]['locaciones']
armas2 = informacion2['evidencia'][2]['armas']

sospechoso = asesino + " no se presentó a hacer testimonio"
testimonios[asesino] = 5
lugar = "Nadie recuerda haber estado en " + escena_crimen
testimonios[escena_crimen] = 6
arma = "Nadie recuerda haber visto o usado el/la " + arma_homicida
testimonios[arma_homicida] = 7
final_resultado = asesino + " mató al Jefe usando " + arma_homicida + " en la/el " + escena_crimen

del informacion2["evidencia"][0]["personajes"][asesino]
del informacion2["evidencia"][1]["locaciones"][escena_crimen]
del informacion2["evidencia"][2]["armas"][arma_homicida]

testimonio1 = alazar_borrar_personaje(1) + " estaba en " + alazar_borrar_locacion(1) + " usando " + alazar_borrar_arma(1)
testimonio2 = alazar_borrar_personaje(2) + " estaba en " + alazar_borrar_locacion(2) + " usando " + alazar_borrar_arma(2)
testimonio3 = alazar_borrar_personaje(3) + " estaba en " + alazar_borrar_locacion(3) + " usando " + alazar_borrar_arma(3)
testimonio4 = alazar_borrar_personaje(4) + " estaba en " + alazar_borrar_locacion(4) + " usando " + alazar_borrar_arma(4)

label_titulo = tk.Label(root, text="CLUE Team Fortress 2")
label_titulo.pack()

label_intentos = tk.Label(root, text="Intentos restantes: ")
label_intentos.pack()

resultado_label = tk.Label(root, text="", padx=10, pady=10)
resultado_label.pack()

investigar_personaje_button = tk.Button(root, text="Investigar Personaje", command=investigar_personaje)
investigar_personaje_button.pack()

investigar_locacion_button = tk.Button(root, text="Investigar Locación", command=investigar_locacion)
investigar_locacion_button.pack()

investigar_arma_button = tk.Button(root, text="Investigar Arma", command=investigar_arma)
investigar_arma_button.pack()

finalizar_button = tk.Button(root, text="Finalizar Juego", command=finalizar_juego)
finalizar_button.pack()

root.mainloop()