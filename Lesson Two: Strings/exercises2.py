# jtyurkovich, 2014

# coding: utf-8

# In[1]:

# Write a function that takes a string as input and outputs the reverse
# of the string (e.g., input 'James is awesome' and output 'emosewa si 
# semaJ').
def reverse(string):
    newstr = ''
    
    for letter in reversed(string):
        newstr += letter
    
    print string
    print newstr
    
reverse('James is awesome')


# In[2]:

# Write a function that takes as input two DNA sequences of arbitrary 
# but equal length and returns the positions of any SNPs that exist. Test
# with 'ACTCTATCGGCTACG' and 'ACTCTATCGACTACG' where a SNP has occurred 
# at position 9 (zero-based indexing). Also report the SNP that occurred 
# (i.e., which base was mutated to which base). Make sure your function 
# can handle multiple SNPs.
def snp_finder(seq1,seq2):
    snp = []
    bases = []
    count = 0
    
    for index in range(0,len(seq1)):
        if seq1[index] != seq2[index]:
            snp.append(index)
            bases.append([seq1[index],seq2[index]])
            count += 1

    if len(snp) > 0:
        for index in range(0,len(snp)):
            print 'SNP at position %(snp)s (%(bases1)s is replaced with %(bases2)s)' %{"snp":snp[index],"bases1":bases[index][0],"bases2":bases[index][1]}

    else:
        print 'No SNPs present'

seq1 = 'ACTCTATCGGCTACA'
seq2 = 'ACTCTATCGACTACG'

snp_finder(seq1,seq2)


# In[7]:

# Write a function that determines whether an input phrase is a pangram (a
# sentence that contains all the letters in the alphabet). Test it with
# 'The quick brown fox jumps over the lazy dog' which is a pangram. If the 
# input is not a pangram, report which letter(s) is/are missing.
def ispangram(sentence):
    sentence.replace(' ','')
    abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    #flag = True
    missingletters = ''
    
    for letter in abc:
        if letter not in sentence:
            #flag = False
            missingletters += letter
            #break  

    if missingletters == '':
        print '"' + sentence + '" is a pangram'
    elif len(missingletters) == 1:
        print '"' + sentence + '" is not a pangram; "%s" is missing.' %missingletters
    else:
        print '"' + sentence + '" is not a pangram; "%s" are missing.' %missingletters

sentence = 'The quick brown fox jumps over the lazy dog'
output = ispangram(sentence)

sentence = 'This is not a pangram'
output = ispangram(sentence)


# In[32]:

# Determine if the two strings are equal: 'AATAGATCGCTAGCT' and 
# 'AATAGATCGCTAGCT'.
str1 = 'AATAGATCGCTAGCT'
str2 = 'AATAGATCGCTAGCT'

if str1 == str2:
    print 'Strings equal'
else:
    print 'Strings not equal'


# In[15]:

# Determine if the substrings 'AATA' and 'TTT' are present in the larger 
# string 'AATAGATCGCTAGCT'.
def issubstringpresent(str1,str2):
    index = str1.find(str2)

    if index >= 0:
        print str2 + ' found in ' + str1 + ' at index %s' %index
    else:
        print str2 + ' not found in ' + str1
        
issubstringpresent('AATAGATCGCTAGCT','CGC')
issubstringpresent('AATAGATCGCTAGCT','TTT')


# In[19]:

# Now try the same problem again, but look for a substring that appears 
# multiple times, such as 'TAG'. Report the position within the string 
# (zero-based indexing) at which the substring appears. 
str1 = 'AATAGATCGCTAGCT'
str2 = 'TAG'

flag = False

for index in range(0,len(str1)-2):
    if str1[index:(index+2)] == str2:
    	flag = True
        print str2 + ' found in ' + str1 + ' at index %s' %index

if not flag:
    print str2 + ' not found in ' + str1


# In[29]:

# That can be fairly inefficient, especially for large strings. We can 
# instead use something called a regular expression to quickly and 
# efficiently do the same search.

# You will need to install Python's regular expression module to run this
# block of code.
import re

str1 = 'AATAGATCGCTAGCT'
str2 = 'TAG'

indices = [m.start() for m in re.finditer(str2,str1)]

for index in indices:
    print str2 + ' found in ' + str1 + ' at index %s' %index
if len(indices) == 0:
    print str2 + ' not found in ' + str1


# In[94]:

# Importing a package may not be preferable, especially if you don't have
# that particular package already. In that case, we can implement more 
# complex solutions.
def locations_of_substring(string,substring):
    substring_length = len(substring)  
    
    def recurse(locations_found,start):
        location = string.find(substring,start)
        
        if location != -1:
            return recurse(locations_found + [location],location + substring_length)
        else:
            return locations_found

    return recurse([], 0)

indices =  locations_of_substring('AATAGATCGCTAGCT','TAG')

for index in indices:
    print str2 + ' found in ' + str1 + ' at index %s' %index
if len(indices) == 0:
    print str2 + ' not found in ' + str1


# In[103]:

# Or, we could use a built-in method for strings in Python to find the 
# number of occurrences. Ultimately, we see that although this may be the
# easiest, we would need to use additional methods to find the location of
# these occurrences. Experiment with the different string methods to find
# similarly easy implementations for various problems.
str1 = 'AATAGATCGCTAGCT'
str2 = 'TAG'

print str2 + ' occurs ' + str(str1.count(str2)) + ' times in ' + str1

