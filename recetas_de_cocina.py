receta = {
    "ensalada_cesar_con_pollo":{
        "ingredientes":(
            "1. Lechuga romana.",
            "2. Pan.",
            "3. Pechuga de pollo.",
            "4. Aceite de oliva.",
            "5. Zumo de limon.",
            "6. Sal.",
            "7. Ajo.",
            "8. Pimienta negra."
        ),
        "paso_a_paso":{
            "paso_1":"Paso 1: Preparar la salsa, junte el zumo de limon, la sal, el ajo y revuelva.",
            "paso_2":"Paso 2: Lavar y escurrir la lechuga, cortar y guadar en la nevera durante 30 minutos.",
            "paso_3":"Paso 3: Añadir un poco de acite en un sarten y colocar la pechuga de pollo a dorar.",
            "paso_4":"Paso 4: Freir los lados del pan en aceite o tostar en el horno. y cortar en trozos.",
            "paso_5":"Paso 5: Emplatar y disfrutar."
        },
        "pollo":"",
        "salsa":{
            "pimienta_negra":"",
            "zumo_limon":"Una cucharada.",
            "sal":"Al gusto.",
            "ajo":"1 diente."
        }
    },
    "warp_de_pollo_con_salsa_cesar":{
        "ingredientes":(
            "1. Lechuga romana.",
            "2. Tortillas.",
            "3. Pechuga de pollo.",
            "4. Aceite de oliva.",
            "5. Zumo de limon.",
            "6. Sal.",
            "7. Ajo.",
            "8. Pimienta negra."
        ),
        "paso_a_paso":{
            "paso_1":"Paso 1: Preparar la salsa, junte el zumo de limon, la sal, el ajo y revuelva.",
            "paso_2":"Paso 2: Añadir un poco de acite en un sarten y colocar la pechuga de pollo a dorar.",
            "paso_3":"Paso 3: Calentar torilla, sobre esta colocar una hoja de lechuga y añadir el pollo y la salsa.",
            "paso_4":"Paso 4: Emplatar y disfrutar."
        },
        "pollo":"",
        "salsa":{
            "pimienta_negra":"",
            "zumo_limon":"Una cucharada.",
            "sal":"Al gusto.",
            "ajo":"1 diente."
        }
    },
    "sandwich_clasico_pollo":{
        "ingredientes":(
            "1. Lechuga romana.",
            "2. Pan tajado.",
            "3. Pollo.",
            "4. Aceite de oliva.",
            "5. Zumo de limon.",
            "6. Sal.",
            "7. Ajo.",
            "8. Pimienta."
        ),
        "paso_a_paso":{
            "paso_1":"Paso 1: Preparar la salsa, junte el zumo de limon, la sal, el ajo y revuelva.",
            "paso_2":"Paso 2: Añadir un poco de acite en un sarten y colocar la pechuga de pollo a dorar. y luego agregar la salsa",
            "paso_3":"Paso 3: Freir los lados del pan tajado en aceite o tostar en el horno.",
            "paso_4":"Paso 4: Emplatar y disfrutar."
        },
        "pollo":"",
        "salsa":{
            "pimienta_negra":"",
            "zumo_limon":"Una cucharada.",
            "sal":"Al gusto",
            "ajo":"1 diente."
        }
    }
}

def preparar_pollo_a_la_plancha (presentacion):
    tipos = ("En tiras.","Normal.")
    presentacion = tipos[presentacion]
    receta["ensalada_cesar_con_pollo"]["pollo"] = presentacion
    receta["warp_de_pollo_con_salsa_cesar"]["pollo"] = presentacion
    receta["sandwich_clasico_pollo"]["pollo"] = presentacion

def preparar_salsa_cesar (pimienta):
    receta["ensalada_cesar_con_pollo"]["salsa"]["pimienta_negra"] = pimienta
    receta["warp_de_pollo_con_salsa_cesar"]["salsa"]["pimienta_negra"] = pimienta
    receta["sandwich_clasico_pollo"]["salsa"]["pimienta_negra"] = pimienta
    if pimienta:
        salsa_ensalada = receta["ensalada_cesar_con_pollo"]["paso_a_paso"]["paso_1"]
        receta["ensalada_cesar_con_pollo"]["paso_a_paso"]["paso_1"] = f"{salsa_ensalada} Con pimienta."
        salsa_warps = receta["warp_de_pollo_con_salsa_cesar"]["paso_a_paso"]["paso_1"]
        receta["warp_de_pollo_con_salsa_cesar"]["paso_a_paso"]["paso_1"] = f"{salsa_warps} Con pimienta."
        salsa_sandwich = receta["warp_de_pollo_con_salsa_cesar"]["paso_a_paso"]["paso_1"]
        receta["sandwich_clasico_pollo"]["paso_a_paso"]["paso_1"] = f"{salsa_sandwich} Con pimienta."
    else:
        salsa_ensalada = receta["ensalada_cesar_con_pollo"]["paso_a_paso"]["paso_1"]
        receta["ensalada_cesar_con_pollo"]["paso_a_paso"]["paso_1"] = f"{salsa_ensalada} Sin pimienta."
        salsa_warps = receta["warp_de_pollo_con_salsa_cesar"]["paso_a_paso"]["paso_1"]
        receta["warp_de_pollo_con_salsa_cesar"]["paso_a_paso"]["paso_1"] = f"{salsa_warps} Sin pimienta."
        salsa_sandwich = receta["warp_de_pollo_con_salsa_cesar"]["paso_a_paso"]["paso_1"]
        receta["sandwich_clasico_pollo"]["paso_a_paso"]["paso_1"] = f"{salsa_sandwich} Sin pimienta."

def preparar_ensalada_cesar():
    while True:
        choice = input("\n¿Desea pimienta en la preparación de su salsa?(S/N)\n")
        if choice.upper() == "S" or choice.upper() == "N":
            break
        else:
            print("\n¡ERROR!, por favor elija una opción valida\n")
        
    if choice.upper() == "S":
        choice = True
    elif choice.upper() == "N":
        choice = False

    preparar_salsa_cesar(choice)
    print("\nPreparación\n")
    pasos = receta["ensalada_cesar_con_pollo"]["paso_a_paso"]
    for paso in pasos.values():
        print(paso)

def preparar_warp_cesar():
    while True:
        choice = input("\n¿Desea pimienta en la preparación de su salsa?(S/N)\n")
        if choice.upper() == "S" or choice.upper() == "N":
            break
        else:
            print("\n¡ERROR!, por favor elija una opción valida\n")
        
    if choice.upper() == "S":
        choice = True
    elif choice.upper() == "N":
        choice = False

    preparar_salsa_cesar(choice)
    print("\nPreparación\n")
    pasos = receta["warp_de_pollo_con_salsa_cesar"]["paso_a_paso"]
    for paso in pasos.values():
        print(paso)

def preparar_sandwich_pollo():
    while True:
        choice = input("\1¿Desea pimienta en la preparación de su salsa?(S/N)\n")
        if choice.upper() == "S" or choice.upper() == "N":
            break
        else:
            print("\n¡ERROR!, por favor elija una opción valida\n")
        
    if choice.upper() == "S":
        choice = True
    elif choice.upper() == "N":
        choice = False

    preparar_salsa_cesar(choice)

    print("\nPreparación\n")
    pasos = receta["sandwich_clasico_pollo"]["paso_a_paso"]
    for paso in pasos.values():
        print(paso)
    
def emplatado(plato):
    if plato.lower() == "a":
        print(receta["ensalada_cesar_con_pollo"])
    elif plato.lower() == "b":
        print(receta["warp_de_pollo_con_salsa_cesar"])
    elif plato.lower() == "c":
        print(receta["sandwich_clasico_pollo"])

print("\nBienvani@ al recetario.\n")

while True:
    eleccion_receta = input("¿Qué desea preparar?\na) Ensalada César con pollo.\nb) Warp de pollo con salsa César.\nc) Sándwich clásico de pollo.\n")
    if eleccion_receta.lower() == "a" or eleccion_receta.lower() == "b" or eleccion_receta.lower() == "c":
        break
    else:
        print("\n¡ERROR!, por favor elija una opción valida\n")


if eleccion_receta.lower() == "a":
    receta["ensalada_cesar_con_pollo"]["ingredientes"] = str(receta["ensalada_cesar_con_pollo"]["ingredientes"]).replace("(","").replace(")","").replace(",","\n").replace("'","")
    a = receta["ensalada_cesar_con_pollo"]["ingredientes"]
    print(f"\nLos ingrecientes que necesitas son:\n {a}\n")
elif eleccion_receta.lower() == "b":
    receta["warp_de_pollo_con_salsa_cesar"]["ingredientes"] = str(receta["warp_de_pollo_con_salsa_cesar"]["ingredientes"]).replace("(","").replace(")","").replace(",","\n").replace("'","")
    print(f"\nLos ingrecientes que necesitas son:\n {receta['sandwich_clasico_pollo']['ingredientes']}\n")
elif eleccion_receta.lower() == "c":
    receta["sandwich_clasico_pollo"]["ingredientes"] = str(receta["sandwich_clasico_pollo"]["ingredientes"]).replace("(","").replace(")","").replace(",","\n").replace("'","")
    print(f"\nLos ingrecientes que necesitas son:\n {receta['sandwich_clasico_pollo']['ingredientes']}\n")

while True:
    try:
        tipo_pollo = int(input("¿En qué presentación desea el pollo?\n1) En tiras.\n2) Normal.\n"))
        if tipo_pollo == 1 or tipo_pollo == 2:
            break
        else:
            print("\n¡ERROR!, por favor elija una opción valida.\n")
    except:
        print("\n¡ERROR!, por favor ingrese un caracter valido.\n")

if tipo_pollo == 1:
    tipo_pollo = 0
    preparar_pollo_a_la_plancha(tipo_pollo)
elif tipo_pollo == 2:
    tipo_pollo = 1
    preparar_pollo_a_la_plancha(tipo_pollo)

if eleccion_receta.lower() == "a":
    preparar_ensalada_cesar()
elif eleccion_receta.lower() == "b":
    preparar_warp_cesar()
elif eleccion_receta.lower() == "c":
    preparar_sandwich_pollo()

while True:
    mostrar_emplatado = input("\n¿Desea ver el emplatado?(S/N)\n")
    if mostrar_emplatado.upper() == "S" or mostrar_emplatado.upper() == "N":
        break
    else:
        print("\n¡ERROR!, por favor elija una opción valida.\n")

if mostrar_emplatado.upper() == "S":
    print("\n")
    print(emplatado(eleccion_receta))
    print("\n¡DISFRUTE DE SU RECETA!\n")
elif mostrar_emplatado.upper() == "N":
    print("\n¡DISFRUTE DE SU RECETA!\n")