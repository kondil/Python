#!/usr/bin/env python
# Infos retrieved from ::
# 1. https://docs.python.org/2/library/json.html
# 2. http://pymotw.com/2/json/


import json

json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]) 
# '["foo", {"bar": ["baz", null, 1.0, 2]}]'

print json.dumps("\"foo\bar")
# "\"foo\bar"

print json.dumps(u'\u1234')
# "\u1234"

print json.dumps('\\')
# "\\"

print json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)
# {"a": 0, "b": 0, "c": 0}

json.dumps([1,2,3,{'4': 5, '6': 7}], separators=(',',':'))
# '[1,2,3,{"4":5,"6":7}]'

print json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4, separators=(',', ': '))
{
    "4": 5,
    "6": 7
}


