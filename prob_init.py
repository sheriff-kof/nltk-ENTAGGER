
#calcul des prob init
import nltk
import pickle
###clean the text from punctuation
def clean_string(query):
    table=str.maketrans('','','!ًُ"#$ّ%&ٓ\'ٰ(ٖ)ٌ*+,ٍ-./:ْ;<ٕ=>?@[\\ـٍَُِّْٰٖٕٓٔ]^_`{|}~َ،؛؟,ٔ’')
    query=[query.translate(table)]
    return str(query[0])
######## return a freqdist
def proba_init(list_tag,tagged_text):
    fd=nltk.FreqDist()
    for tag in list_tag:
        for w in tagged_text:
            if w[1]==tag:
                fd[tag]+=1
    for t in fd:
        fd[t]=fd[t]/len(tagged_text)
    return fd  
#### treat a tagged text into a liste of tuples  
def tagged_text(text):
    return [nltk.str2tuple(w) for w in text.split()]


####test
####load dictionary for tagging
with open('/storage/emulated/0/PROJET TAL/NAMED-ENTITY_TAG-NAMES.p','rb') as fp:
    a=pickle.load(fp)
with open('/storage/emulated/0/PROJET TAL/NAMED-ENTITY_NAME-TAGS.p','rb') as fp:
    b=pickle.load(fp)
tg_text=open("/storage/emulated/0/PROJET TAL/tagged text/tagged_text.txt",encoding="utf-8").read()
x=tagged_text(tg_text)

file=open("/storage/emulated/0/PROJET TAL/new 2",encoding="utf-8").read()
tg=nltk.UnigramTagger(model=b)
tg.tag(file.split())

p=proba_init(a.keys(),x)
print([(w, p[w] )for w in p])

#proba de trans
def prob_trans(list_tag,tagged_text):
    cfd=nltk.ConditionalFreqDist()
    for tag in list_tag:
        for w in tagged_text:
            if w[1]==tag:
                cfd[tag]+=1
    for t in cfd:
        cfd[t]=cfd[t]/len(tagged_text)
    return cfd  
for w in x:
 print(w)