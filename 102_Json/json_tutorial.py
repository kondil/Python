#!/usr/bin/env python

import json

print 'json_string = \'{"first_name": "Guido", "last_name":"Rossum"}\''
json_string = '{"first_name": "Guido", "last_name":"Rossum"}'

print 'parsed_json = json.loads(json_string)'
parsed_json = json.loads(json_string)

print 'print(parsed_json[\'first_name\'])'
print(parsed_json['first_name'])

d = {
	'first_name': 'Guido',
	'second_name': 'Rossum',
	'titles': [{'BDFL': 'Developer'}, {'BDFL': 'Analyst'}],
}

print 'print(json.dumps(d))'
print(json.dumps(d))

print 'print d[\'titles\'][0][\'BDFL\']'
print d['titles'][0]['BDFL']

print 'print d[\'titles\'][1][\'BDFL\']'
print d['titles'][1]['BDFL']

