import json
import regex

def extractor(res_prompt: str) -> str:
	#regex patter to capture the json
	regex = r'{*}'
	# apply regex 
	res_regex = regex.