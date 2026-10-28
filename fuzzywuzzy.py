#pip install fuzzywuzzy
#pip install python-Levenshtein
# Python code showing all the ratios together, 
# make sure you have installed fuzzywuzzy module 
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 
s1 = "I love fuzzys forfuzzys"
s2 = "I am loving fuzzys for fuzzys"

print ("Ratio:", fuzz. ratio (s1, s2))
print("Partial Ratio:", fuzz.partial_ratio (s1, s2)) 
print ("Token Sort Ratio:", fuzz.token_sort_ratio (s1, s2)) 
print ("Token Set Ratio:", fuzz.token_set_ratio (s1, s2)) 
print ("Weighted Ratio: ", fuzz.WRatio (s1, s2))

query = "fuzzys for fuzzys"
choices = ["fuzzy for fuzzy", "fuzzy fuzzy", "g. for fuzzys"]

print("All matches:", process.extract (query, choices)) 
print ("Best match:", process.extractOne (query, choices))