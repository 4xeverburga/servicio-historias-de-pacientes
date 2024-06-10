import boto3
import json
import src.constructor_de_prompt as constructor
import src.extractor as extractor
import src.llm_connection as conector
import logging
logging.getLogger().setLevel(logging.INFO)

def lambda_handler(event, context):
	pass

def test_main(input_object):
	historia_paciente = input_object['historia_paciente']
	
	prompt = constructor.constructor_de_prompt(historia_paciente)
	completion = conector.llamar_modelo("gpt-3.5-turbo",prompt)
	logging.info(f'la rpta del llm es {completion}')
	res = extractor.extractor_json(completion)
	# save the res
	with open('./out/output_test.json', 'w', encoding='utf-8') as f:
		json.dump(res, f)
	return res

if __name__ == '__main__':
	# load input file
	with open('./in/input_test.json', 'r') as f:
		json_input = json.load(f)
	# out the res
	res = test_main(json_input)
	