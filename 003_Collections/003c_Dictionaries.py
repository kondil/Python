#!/usr/bin/env python


print ">> dict1 = { 'item1': 'value1', 'item2': 'value2' }"
dict1 = { 'item1': 'value1', 'item2': 'value2' }

print ">> print dict1"
print dict1

print ">> print dict1['item1']"
print dict1['item1']

print ">> print dict1['item2']"
print dict1['item2']

print "dict2 = { \
          'dict2a': {'item1': 'value1', 'item2': 'value2'} \
        , 'dict2b': {'item1': 'value1', 'item2': 'value2'} \
        , 'dict2c': {'item1': 'value1', 'item2': 'value2'} \
        }"

dict2 = {
          'dict2a': {'item1': 'value1', 'item2': 'value2'}
        , 'dict2b': {'item1': 'value1', 'item2': 'value2'}
        , 'dict2c': {'item1': 'value1', 'item2': 'value2'}
        }

print ">> print dict2"
print dict2

print ">> print dict2['dict2a']"
print dict2['dict2a']

print ">> print dict2['dict2a']['item1']"
print dict2['dict2a']['item1']

