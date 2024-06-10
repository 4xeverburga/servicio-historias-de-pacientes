import json
import logging
import re
logging.getLogger().setLevel(logging.INFO)

def _extractor_texto(res_prompt: str) -> str:
	#regex patter to capture the json
	regex = r'{(.|\n)*}'
	# apply regex 
	res_regex = re.search(regex, res_prompt)
	print("hi")
	logging.info(res_regex)
	return res_regex.group(0)

def extractor_json(res_prompt: str) -> dict:
	res = json.loads(_extractor_texto(res_prompt))
	logging.info(res)	
	return res	

if __name__ == '__main__':
	test_str = """
	ddfasdf
	asdfasdf
	{
    "sintomas_extraidos": [
        {
            "descripcion": "fiebre",
            "cita_textual": "Desde que me desperté he tenido fiebre"
        },
        {
            "descripcion": "escalofríos",
            "cita_textual": "Desde que me desperté he tenido... escalofríos"
        },
        {
            "descripcion": "dolor de cabeza",
            "cita_textual": "Desde que me desperté he tenido... dolor de cabeza"
        },
        {
            "descripcion": "cansancio",
            "cita_textual": "Ahora que me despierto estoy bastante cansada"
        }
    ],
    "eventos_en_la_historia": [
        {
            "descripcion": "salió a caminar con amigos",
            "cita_textual": "Salí a caminar con mis amigos"
        },
        {
            "descripcion": "fue de compras",
            "cita_textual": "Fui de compras"
        },
        {
            "descripcion": "realizó tareas cotidianas",
            "cita_textual": "Mis tareas cotidianas"
        },
        {
            "descripcion": "se fue a dormir",
            "cita_textual": "A dormir"
        }
    ]
}
"""
	print(extractor_json(test_str))
