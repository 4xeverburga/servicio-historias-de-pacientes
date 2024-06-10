import boto3
import json


def lambda_handler(event, context):
	pass

def test_main(input_object):
	# 
	pass

if __name__ == '__main__':
	# load input file
	with open('/in/input.json', 'r') as f:
		json_input = json.load(f)
	# out the res
	res = test_main(json_input)
	