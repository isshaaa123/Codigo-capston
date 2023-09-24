import os
os.chdir("C:\\Users\\isado\\Documents\\IA\\Codigo what")

import pandas as pd
import pywhatkit
from datetime import datetime

# Lee el archivo CSV de participantes
participantes = pd.read_csv("participantes.csv", dtype="str")
links = pd.read_csv("links.csv")

for ind in participantes.index:
    nombre = participantes['Nombre'][ind]
    telefono = participantes['Telefono'][ind]
    link = links['Link'][ind]
    pedido_fecha =participantes['Fecha']  # Reemplaza con la fecha de entrega real
    pedido_valor = participantes['Valor']  # Reemplaza con el valor del pedido real

    mensaje = f"Hola {nombre}, te informamos que el pedido se entregará el {pedido_fecha}. El valor del pedido es {pedido_valor}. "
    mensaje += "¿Puedes recibir el pedido?\n"
    mensaje += "1. Sí\n"
    mensaje += "2. No"

    # Envía el mensaje
    pywhatkit.sendwhatmsg_instantly(telefono, mensaje, tab_close=True)
    print(f"Mensaje enviado a {nombre} al {telefono}")

    # Captura la respuesta del destinatario
    respuesta = input("Por favor, ingrese la respuesta (1 para Sí, 2 para No): ")

    # Guarda la respuesta en el DataFrame
    participantes.at[ind, 'Respuesta'] = respuesta

# Guarda el DataFrame actualizado en el archivo CSV
participantes.to_csv("participantes_con_respuestas.csv", index=False)
