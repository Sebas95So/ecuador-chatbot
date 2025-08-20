# Importamos las bibliotecas necesarias
import os 
from openai import OpenAI  # Importamos la clase OpenAI para interactuar con la API de OpenAI

# Definimos el modelo que se utilizará para las respuestas
model = "gpt-4o-mini"

# Creamos una instancia del cliente de OpenAI
client = OpenAI()

# Función para obtener una respuesta de OpenAI
def get_response(messages):
    """
    Envía una lista de mensajes a la API de OpenAI y devuelve la respuesta del modelo.

    Args:
        messages (list): Lista de mensajes en formato [{"role": "user/system/assistant", "content": "texto"}].

    Returns:
        str: El contenido de la respuesta generada por el modelo.
    """
    response = client.chat.completions.create(
        model=model,  # Especificamos el modelo a usar
        messages=messages,  # Pasamos la conversación actual
        temperature=0.0,  # Controla la aleatoriedad de las respuestas (0.0 = determinista)
        max_tokens=100  # Límite de tokens en la respuesta
    )
    return response.choices[0].message.content  # Devolvemos solo el contenido del mensaje generado

# Inicializamos la conversación con un mensaje del sistema
conversation = [
    {
        "role": "system",  # Rol del mensaje (define el contexto inicial)
        "content": (
        "Eres un experto virtual en turismo de Ecuador 🇪🇨. "
        "Puedes proporcionar información valiosa sobre sus ciudades, "
        "parques naturales, cultura, gastronomía y lugares emblemáticos. "
        "Ofrecerás una experiencia inmersiva y atractiva para los viajeros."
        )  # Mensaje que define el propósito del asistente, en este caso un guia turístico virtual de Ecuador.
    }
]

# Lista de preguntas que el usuario quiere hacer al asistente
questions = [
    "Que tan lejos esta la mitad del mundo del aeropuerto internacional de Quito? Toma en cuenta que voy manejando",
    "Donde está el panecillo?",
    "Dime 3 platos típicos que puedo comer en Quito"
]

# Iteramos sobre cada pregunta para obtener respuestas del asistente
for q in questions:
    # Agregamos la pregunta del usuario a la conversación
    conversation.append({"role": "user", "content": q})
    
    # Obtenemos la respuesta del asistente llamando a la función get_response
    response = get_response(conversation)
    
    # Agregamos la respuesta del asistente a la conversación
    conversation.append({"role": "assistant", "content": response})

# Imprimimos toda la conversación (preguntas y respuestas)
for msg in conversation:
    print(f"{msg['role'].upper()}: {msg['content']}\n")