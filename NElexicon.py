#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
import pickle
file=open("C:/Users/Pc/Desktop/NAMED-ENTITY.TXT",encoding="utf-8").readlines()
file=file[1:]
NElexiconDic={}
for line in file:
    words=line.split()
    if words!=[]:
        name=words.pop(0)
    for word in words:
        if word in NElexiconDic.keys():
            NElexiconDic[word].append(name)
        else:
            NElexiconDic[word]=[]
            NElexiconDic[word].append(name)
tag={}
for l in file:
    l=l.split()
    cle=l[0]
    l=l[1:]
    if cle in tag.keys():
       for x in l:
            if x not in tag[cle]:
                tag[cle].append(x)
    else:
        tag[cle]=l            
            
            
with open('C:/Users/Pc/Desktop/NAMED-ENTITY_TAG-NAMES.p','wb') as fp:
    pickle.dump(NElexiconDic,fp,protocol=pickle.HIGHEST_PROTOCOL)
with open('C:/Users/Pc/Desktop/NAMED-ENTITY_NAME-TAGS.p','wb') as fp:
    pickle.dump(tag,fp,protocol=pickle.HIGHEST_PROTOCOL)



with open('C:/Users/Pc/Desktop/NAMED-ENTITY_TAG-NAMES.p','rb') as fp:
    a=pickle.load(fp)
with open('C:/Users/Pc/Desktop/NAMED-ENTITY_NAME-TAGS.p','rb') as fp:
    b=pickle.load(fp)
    
    
