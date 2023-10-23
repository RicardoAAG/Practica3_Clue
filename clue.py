import json
import random
respuestas_correctas=0

def elegir_testimonio(buscar,tipo):
    global respuestas_correctas
    equivocado="No deduciste correctamente"
    correcto="Deduciste correctamente"
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
        if buscar in (1,2,3,4):
            return equivocado
        if buscar in (5,6,7):
            respuestas_correctas=respuestas_correctas+1
            return correcto

def cargar_base_de_datos(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data  

def buscar(sospechosos,revisar,tipo):
    revisar=int(revisar)-1
    if 0 <= revisar < len(sospechosos):
        objetivo=sospechosos[revisar]
        if objetivo in testimonios:
            print(elegir_testimonio(testimonios[objetivo],tipo))
        y=1
        return y
    else:
        print("\nInsertar el numero de la opcion\n")
        y=0
        return y

def investigar_personaje():
    y=0
    sospechosos=list(personajes.keys())
    
    while y==0:
        revisar=input("Selecciona un sospechoso a interrogar: \n1) Ingeniero\n2) Espia\n3) Medico\n4) Soldado\n5) Francotirador\n")
        y=buscar(sospechosos,revisar,0)
    
def investigar_locacion():
    y=0
    sospechosos=list(locaciones.keys())
    
    while y==0:
        revisar=input("Selecciona un lugar a investigar: \n1) Casa\n2) Tunel\n3) Barracones\n4) Puesto de guardia\n5) Enfermeria\n")
        y=buscar(sospechosos,revisar,0)
    
    
def investigar_arma():
    y=0
    sospechosos=list(armas.keys())
    
    while y==0:
        revisar=input("Selecciona un arma a inspeccionar: \n1) Papel de regalo\n2) Katana\n3) Cuchillo mariposa\n4) Guante de box\n5) Llave inglesa\n")
        y=buscar(sospechosos,revisar,0)
    

def alazar_borrar_personaje(numero):
    borrar=random.choice(list(personajes2.keys()))
    del informacion2["evidencia"][0]["personajes"][borrar]
    testimonios[borrar]=numero
    return borrar

def alazar_borrar_locacion(numero):
    borrar=random.choice(list(locaciones2.keys()))
    del informacion2["evidencia"][1]["locaciones"][borrar]
    testimonios[borrar]=numero
    return borrar

def alazar_borrar_arma(numero):
    borrar=random.choice(list(armas2.keys()))
    del informacion2["evidencia"][2]["armas"][borrar]
    testimonios[borrar]=numero
    return borrar

informacion: dict = cargar_base_de_datos('clue_base_de_datos.json')

#informacion 2 se va a terminar borrando
informacion2: dict = cargar_base_de_datos('clue_base_de_datos.json')


#Se cambio un valor de cada categoria a True para denotar el asesino, el lugar y el arma#
personajes = informacion['evidencia'][0]['personajes']
asesino = random.choice(list(personajes.keys()))
informacion["evidencia"][0]["personajes"][asesino] = True    

locaciones = informacion['evidencia'][1]['locaciones']
escena_crimen = random.choice(list(locaciones.keys()))
informacion["evidencia"][1]["locaciones"][escena_crimen] = True    

armas = informacion['evidencia'][2]['armas']
arma_homicida = random.choice(list(armas.keys()))
informacion["evidencia"][2]["armas"][arma_homicida] = True    
##


#Se crean los testimonios de los inocentes, y la informacion del culpable, el arma y el lugar#
testimonios={}

personajes2 = informacion2['evidencia'][0]['personajes']
locaciones2 = informacion2['evidencia'][1]['locaciones']
armas2 = informacion2['evidencia'][2]['armas']

sospechoso=asesino+" no se presentó a hacer testimonio"
testimonios[asesino]=5
lugar="Nadie recuerda haber estado en "+escena_crimen
testimonios[escena_crimen]=6
arma="Nadie recuerda haber visto o usado el/la "+arma_homicida
testimonios[arma_homicida]=7
final_resultado=asesino+" mato al Jefe usando "+arma_homicida+" en la/el "+escena_crimen

del informacion2["evidencia"][0]["personajes"][asesino]
del informacion2["evidencia"][1]["locaciones"][escena_crimen]
del informacion2["evidencia"][2]["armas"][arma_homicida]

testimonio1= alazar_borrar_personaje(1)+" estaba en "+alazar_borrar_locacion(1)+" usando "+alazar_borrar_arma(1)
testimonio2= alazar_borrar_personaje(2)+" estaba en "+alazar_borrar_locacion(2)+" usando "+alazar_borrar_arma(2)
testimonio3= alazar_borrar_personaje(3)+" estaba en "+alazar_borrar_locacion(3)+" usando "+alazar_borrar_arma(3)
testimonio4= alazar_borrar_personaje(4)+" estaba en "+alazar_borrar_locacion(4)+" usando "+alazar_borrar_arma(4)
##


print("Parece que hay un asesino entre nosotros porque mataron al Jefe\n")
print("Pudo haber sido cualquiera de los 5 mercenarios, en cualquier lugar de la base usando alguno de estas 5 armas")
print("Interrogemos a los sospechos para ver que estuvieron haciendo, o indagemos mas en la informacion que sabemos de las armas y los lugares")
print("El tiempo es limitado antes de que escape, solo podemos realizar 5 busquedas o interrogaciones")

x=5

while x!=0:
    a_investigar= input("Quedan "+str(x)+" intentos\nSelecciona que quieres investigar\n 1. Personaje\n 2. Locacion\n 3. Arma\n")
    
    switch = {
        '1': investigar_personaje,
        '2': investigar_locacion,
        '3': investigar_arma
    }
    
    if a_investigar in switch:
        switch[a_investigar]()
        x=x-1
    else:
        print("Opción no válida")
        
print("\nSe te acabaron los intentos, ahora tienes que decidir al culpable, su arma y el lugar del asesinto\n")

y=0

while y==0:
    final_culpable=input("Selecciona un culpable: \n1) Ingeniero\n2) Espia\n3) Medico\n4) Soldado\n5) Francotirador\n")
    y=buscar(list(personajes.keys()),final_culpable,1)
    
y=0
while y==0:
    final_lugar=input("Selecciona el lugar del asesinato: \n1) Casa\n2) Tunel\n3) Barracones\n4) Puesto de guardia\n5) Enfermeria\n")
    y=buscar(list(locaciones.keys()),final_lugar,1)
    
y=0
while y==0:
    final_arma=input("Selecciona el arma homicida: \n1) Papel de regalo\n2) Katana\n3) Cuchillo mariposa\n4) Guante de box\n5) Llave inglesa\n")
    y=buscar(list(armas.keys()),final_arma,1)
   
print("\n"+final_resultado+"\n")
print("Deduciste "+str(respuestas_correctas)+" parte(s) del asesinato")
if respuestas_correctas == 3:
    print("\nGanaste!!!")
else:
    print("\nPerdiste :c")
