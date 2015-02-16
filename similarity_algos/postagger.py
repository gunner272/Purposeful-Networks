'''
Pos tagging done
'''

from nltk.tag.stanford import POSTagger

tagger= POSTagger('/usr/share/stanford-postagger/models/english-bidirectional-distsim.tagger',
	        '/usr/share/stanford-postagger/stanford-postagger.jar')

def tagtext(text):  
    '''return nouns from text'''
    text=text.split()

    retob=[]
    try:
     taggedlist=tagger.tag(text)
     for i in tagger.tag(text):
	    if i[1] in ('NN','NNS','NNP','NNPS'):
		    retob.append(i[0])
    except Exception as e:
     print "returning nothing due to a",    
     print e

    return retob

def rmtags(taggedline):
	takeout=['RT','via','http']
	deconcat=["#","@"]
	i=0;
	try:
	 for word in taggedline:
		for it in takeout:
			if it in word :
				taggedline.remove(word)
				i-=1
		if len(taggedline)>0:
		 for t in deconcat:
			 taggedline[i]=taggedline[i].replace(t,'')
		i+=1
	except Exception as e:
		 print "->>>>",taggedline
		 print e
	return taggedline




	
	


def main():
	pass

if __name__=='__main__':
	main()




    
 

