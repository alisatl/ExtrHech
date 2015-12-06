# README #
 
##Description##
**ExtrHech** is an Open Information Extraction system for Spanish language based on matching sequences of Part-of-Speech tags. 
It has been created as a part of my [PhD thesis](http://nlp.cic.ipn.mx/~alisa/papers/PhDThesis_AlisaZhila.pdf) in the Center for Computing Research of Instituto Politécnico Nacional [(CIC-IPN)](http://www.cic.ipn.mx) in Mexico City, Mexico. "*Orgullosamente politécnico*."

Essentially, it is a system for detection and extraction of potentially infromative verb-based triples, i.e., relations along with their arguments, from arbitrary texts in Spanish language. Of course, the text must be pre-processed correspondingly (see below).  

You can read more about the details and theoretical background in my paper [Open Information Extraction for Spanish Language based on Syntactic Constraints](http://www.aclweb.org/anthology/P/P14/P14-3011.pdf) co-authored with my advisor [Prof.  Alexander Gelbukh](http://www.gelbukh.com)

Currently, ExtrHech definitely lacks industrial strength but it works... or more precisely, worked a few times.
 
###Keywords###
Natural Language Processing, Open Information Extraction, Part-of-Speech tags, Relation Extraction, PhD thesis 
 
### What do we have here? ###
 
The `./src` folder contains all files ever related to the project, a lot of which are outdated and not necessary but I keep them all as a history and push them diligently.     
 
In the `./data` folder there are couple files for testing: 

* news-v6.es-en.300.es      - 300 sentences from Reuters news corpus  
* news-v6.es-en.300.es.pos  - same 300 sentences POS-tagged according to EAGLES POS tag set. POS-tagging was done using Freeling-2.2 POS-tagger (see below)

In the `./output` folder: 

* output.extr               - what to expect as output 
 
### How to run it? ###
 
If you happen to have your texts POS-tagged with EAGLES POS-tages and formatted one sentence per line then all you need is to run: 

```
> python ./src/fact_extr_regexp4.py  ./src/facts_extr.config your_input.pos > your_output.extr
```

To try it out, you can  just blindly run 

```
python ./src/fact_extr_regexp4.py ./src/facts_extr.config  ./data/news-v6.es-en.300.es.pos > ./output/my_output.extr
```

which is equivalent to the `ExtrHech.bat` file. 

However, if you do need to POS-tag your dataset first: 

* download [Freeling](http://devel.cpl.upc.edu/freeling/downloads?order=time&desc=1)  
* to get the idea how to proceed, check ./extraction_pipeline.bat ... yes, it's .bat.   
   
### Who to talk to? ###
 
* talk to [me](http://nlp.cic.ipn.mx/~alisa/)