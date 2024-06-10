# se definen las funciones interfaz
# para este caso se usara aws bedrock

import boto3
import json
import logging

def constructor_de_prompt(historia_de_paciente):
	# se define el prompt
	prompt_base = ''
	with open('src/prompt_base.txt','r',encoding='utf-8') as file:
		prompt_base = file.read()

	prompt = prompt_base + "\nHistoria de Paciente: " + historia_de_paciente
	# se agrega las preguntas de extraccion
	# importar form prompt_tail.txt
	prompt_tail = ''
	with open('src/prompt_tail.txt','r',encoding='utf-8') as file:
		prompt_tail = file.read()

	prompt += prompt_tail	
	logging.info(f'Se estara usando el prompt siguiente:\n {prompt[-100:]}')
	return prompt
	
def llamar_modelo(proveedor_modelo, prompt, regex_resultado):
	pass