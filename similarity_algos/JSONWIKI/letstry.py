import sys,os
from postagger import tagtext,rmtags
from jaccard import jaqq
from getdict import gdict
import pickle
def done():#text written in txt file
	cnt=0
	ncnt=0
	query="life"
	#print "yeh"
	with open('tweets20131103-154451.txt','r') as fptr:
		#print "oh"	
	 lines=fptr.read()
	 #print lines
	 lines=lines.split('\n')
	 for line in lines:
		 line=tagtext(line)
		 line=rmtags(line)
		 if len(line)==0:
			 ncnt+=1
			 print "hihi",ncnt

			 continue
		 elif jaqq(query,line)==True:
		     print query,'->',line
		     cnt+=1
	              

def openingdicts():
	cnt=0
	ncnt=0
	#query="life mother krishna karma guru"
	with open('queryfile','r') as fptr:
	 lines=fptr.read()
	 lines=lines.split('\n')
	 try:
		mydict=gdict('extracted_AA_wiki_00.json')
		final=mydict.items()
		for query in lines:
		 for line in final:
			print "a",len(line[1]) 
			print jaqq(query,line[1])
	 except Exception as e:
		print e
	
def createshelve():
	 try:
		 d=open("perdict","rb+")
		 l=['extracted_AA_wiki_00.json','extracted_AA_wiki_01.json','extracted_AA_wiki_02.json','extracted_AA_wiki_03.json']
		 for i in l: 
			mydict=gdict(i)
			for j in mydict.items():
				pickle.dump(j,d)	

		
	 except Exception as e:
		print e
	
if __name__=='__main__'	:
	createshelve()
	#	done()	
	#openingdicts()


