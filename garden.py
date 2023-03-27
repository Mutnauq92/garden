import spacy

""" 
This program is used to tokenize sentences and perform entity recognition
on each one of them.
"""

nlp = spacy.load("en_core_web_sm")

gardenpathSentences = [
    u"the horse Kelso raced past the barn fell",
    u"the old man the boat",
    u"the florist Kacy sent the flowers was pleased",
    u"the cotton clothing is made of grows in Newyork",
    u"the sour drink from the ocean",
    u"I know the words to that song about the King Moswati don't rhyme"
]

def tokenizer(sentence_list):
    """This enumerates all sentences in a sentence list
        and tokenize each one.
        
    :param list sentence_list: A list of sentences
    
    :returns: Prints tokens for each sentence
    
    :rtype: Prints tokens for each sentence
    """
    
    for pos, sentence in enumerate(sentence_list):
        doc = nlp(sentence)
        # tokenizing sentence
        print(f"SENTENCE #{pos + 1} TOKENS")
        print([(token, token.orth_, token.orth) for token in doc if not token.is_punct | token.is_space])
        print()
        
        # entity recognition
        print(f"SENTENCE #{pos + 1} ENTITIES")
        print([(i, i.label_, i.label) for i in doc.ents if len(i) > 0])

        print()
    
    
tokenizer(gardenpathSentences)

entities = ["FAC", "GPE"]

for ent in entities:
    print(f"{ent} : {spacy.explain(ent)}")
    
print()

warning = "NB!!! EMPTY ENTITY LIST MEANS NO ENTITY WAS FOUND !"
print(warning + "\n")

# Looked up "FAC" and "GPE" entities
# FAC -> Buildings, airports, highways, bridges, etc. 
#   Makes no sense why the king is classified as "FAC"
# GPE -> Countries, cities, states
#   Makes perfect sense, since Newyork is indeed a city.



