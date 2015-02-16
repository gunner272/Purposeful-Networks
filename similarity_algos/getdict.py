import json
import sys

def gdict(jfile):
 with open(jfile) as fp:
	data=json.load(fp)
	return data


