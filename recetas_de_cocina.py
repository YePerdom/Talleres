receta = {
    "ensalada_cesar_con_pollo":{
        "ingredientes":(
            "Lechuga romana",
            "Pan",
            "Pechuga de pollo",
            "Aceite de oliva",
            "Zumo de limon",
            "Sal",
            "Ajo",
            "Pimienta negra"
        ),
        "paso_a_paso":{
            "paso_1":"Preparar la salsa, junte el zumo de limon, la sal, el ajo y revuelva.",
            "paso_2":"Lavar y escurrir la lechuga, coratar y guadar en la nevera durante 30 minutos.",
            "paso_3":"Añadir un poco de acite en un sarten y colocar la pechuga de pollo a dorar.",
            "paso_4":"Freir los lados del pan en aceite o tostar en el horno.",
            "paso_5":"Emplatar y disfrutar"
        },
        "pollo":"",
        "salsa":{
            "pimienta_negra":"",
            "zumo_limon":"una cucharada",
            "sal":"al gusto",
            "ajo":"1 diente"
        }
    },
    "warp_de_pollo_con_salsa_cesar":{
        "ingredientes":(
            "Lechuga romana",
            "Tortillas",
            "Pollo",
            "Aceite de oliva",
            "Zumo de limon",
            "sal",
            "Ajo",
            "Piminta negra"
        ),
        "paso_a_paso":{
            "paso_1":"Preparar la salsa, junte el zumo de limon, la sal, el ajo y revuelva.",
            "paso_2":"Añadir un poco de acite en un sarten y colocar la pechuga de pollo a dorar.",
            "paso_3":"Calentar torilla, sobre esta colocar una hoja de lechuga y añadir la salsa",
            "paso_4":"Emplatar y disfrutar"
        },
        "pollo":"",
        "salsa":{
            "pimienta_negra":"",
            "zumo_limon":"una cucharada",
            "sal":"al gusto",
            "ajo":"1 diente"
        }
    },
    "sandwich_clasico_pollo":{
        "ingredientes":(
            "Lechuga romana",
            "Pan",
            "Pollo",
            "Queso rayado",
            "Parmesano",
            "Aceite de oliva",
            "Zumo de limon",
            "sal"
        ),
        "paso_a_paso":{
            "paso_1":"Preparar la salsa, junte el zumo de limon, la sal, el ajo y revuelva.",
            "paso_2":"Añadir un poco de acite en un sarten y colocar la pechuga de pollo a dorar. y luego agregar la salsa",
            "paso_3":"Freir los lados del pan en aceite o tostar en el horno.",
            "paso_4":"Emplatar y disfrutar"
        },
        "pollo":"",
        "salsa":{
            "pimienta_negra":"",
            "zumo_limon":"",
            "sal":"",
            "ajo":""
        }
    }
}


def preparar_pollo_a_la_plancha (presentacion):
    tipos = ("En tiras","Normal")
    presentacion = tipos[presentacion]
    return presentacion

def preparar_salsa_cesar (pimienta):
    receta["ensalada_cesar_con_pollo"]["salsa"]["pimienta_negra"] = pimienta
    if pimienta:
        salsa_ensalada = receta["ensalada_cesar_con_pollo"]["paso_a_paso"]["paso_1"]
        receta["ensalada_cesar_con_pollo"]["paso_a_paso"]["paso_1"] = f"{salsa_ensalada} Con pimienta"
        salsa_warps = receta["warp_de_pollo_con_salsa_cesar"]["paso_apaso"]["paso_1"]
        receta["warp_de_pollo_con_salsa_cesar"]["paso_apaso"]["paso_1"] = f"{salsa_warps} Con pimienta"
        salsa_sandwich = receta["warp_de_pollo_con_salsa_cesar"]["paso_apaso"]["paso_1"]
        receta["warp_de_pollo_con_salsa_cesar"]["paso_apaso"]["paso_1"] = f"{salsa_sandwich} Con pimienta"

def preparar_ensalada_cesar():
    pasos = receta["ensalada_cesar_con_pollo"]["paso_a_paso"]
    for paso in pasos.values():
        print(paso)
    # paso1 = [f"Primero: {receta["ensalada_cesar_con_pollo"]["paso_a_paso"]["paso_1"]}"]
    # paso2 = f"Segundo: {receta["ensalada_cesar_con_pollo"]["paso_a_paso"]["paso_2"]}"
    # paso3 = f"Tercero: {receta["ensalada_cesar_con_pollo"]["paso_a_paso"]["paso_3"]}"
    # paso4 = f"Cuarto: {receta["ensalada_cesar_con_pollo"]["paso_a_paso"]["paso_4"]}"
    # paso5 = f"Quinto: {receta["ensalada_cesar_con_pollo"]["paso_a_paso"]["paso_5"]}"
    
    # resultado = f"{paso1}\n{paso2}\n{paso3}\n{paso4}\n{paso5}"
    
    # return resultado
    
while True:
    choice = input("¿Desea pimienta en la preparación de su salsa?(S/N)\n")
    if choice.upper() == "S" or choice.upper() == "N":
        break
    else:
        print("Ingrese una opción valida.s")
    
if choice.upper() != "N":
     choice = False
     
    
tipo_de_salsa = preparar_salsa_cesar(choice)
receta_elejida = preparar_ensalada_cesar()