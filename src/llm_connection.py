import logging
import json
import openai
import os 

openai.api_key= os.getenv("OPENAI_API_KEY")

def llamar_modelo(tipo_modelo, prompt: str) -> str:
	if tipo_modelo == "gpt-3.5-turbo":
		message = {
			'role': 'user',
			'content': prompt
		}

		response = openai.chat.completions.create(
			model="gpt-3.5-turbo",
			messages=[message]
		)
		return response.choices[0].message.content	
	logging.warning("No se ha encontrado un case para tipo_modelo")	
	return None