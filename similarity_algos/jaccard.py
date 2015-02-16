def jaqq(query,taggedline):# taggedline is a list of nouns
 simlimit=0.001 #return true if query and taggedline 30% similar
 squery=query.split()
 inter=0
 union=len(squery)+len(taggedline)
 for match in squery:
		if match in taggedline:
			inter=inter+1
 print query,union,inter
 if(union>0):
	if (inter/float(union)) >simlimit:
		return True
	else:
		return False
 else:
	return False

def main():
	pass

if __name__=='__main__':
	main()


