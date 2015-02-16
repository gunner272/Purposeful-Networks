def jaqq(query,taggedline):# query ,taggedline are  list of nouns 
 simlimit=0.001 #return true if query and taggedline more  similar than this threshold
 inter=0
 union=len(squery)+len(taggedline)
 for match in query:
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


