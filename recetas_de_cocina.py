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
            "paso_1":"Preparar la salsa, junte el zumo de limon, la sal, el ajo y la pimienta negra; y revuelva.",
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
            "paso_1":"Preparar la salsa, junte el zumo de limon, la sal, el ajo y la pimienta negra; y revuelva.",
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
            "paso_1":"Preparar la salsa, junte el zumo de limon, la sal, el ajo y la pimienta negra; y revuelva.",
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

def preparar_salsa_cesar ():

    while True:
        pimienta = input("¿Desea la ensalada con pimienta?(S/N)\n")
        if pimienta.upper() != "S" or pimienta.upper() != "N":
            print("Elija una opción valida")
        else:
            break

    if pimienta == "si":
        receta["ensalada_cesar_con_pollo"]["salsa"]["pimienta_negra"] = "Sí"
        receta["sandwich_clasico_pollo"]["salsa"]["pimienta_negra"] = "Sí"
        receta["warp_de_pollo_con_salsa_cesar"]["salsa"]["pimienta_negra"] = "Sí"
    elif pimienta == "no":
        receta["ensalada_cesar_con_pollo"]["salsa"]["pimienta_negra"] = "No"
        receta["sandwich_clasico_pollo"]["salsa"]["pimienta_negra"] = "No"
        receta["warp_de_pollo_con_salsa_cesar"]["salsa"]["pimienta_negra"] = "No"