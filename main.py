receta = {
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
    }

for key in receta.keys():
    if type(receta[key]).__name__ == 'tuple':
        print(key)
        for valor in receta[key]:
            print(valor)
    elif type(receta[key]).__name__ == 'dict':
        print(key)
        for valor in receta[key]:
            print(receta[key][valor])
    elif type(receta[key]) == 'str':
        print(key)
        
    # print(receta[i])
