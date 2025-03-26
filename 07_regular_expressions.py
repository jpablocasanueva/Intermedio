### Regular Expressions ###

import re 

#match

my_string = "Esta es la leccion numero 7: Expresiones regulares"
my_other_string = "Esta no es leccion 6: manejo de ficheros"

match = re.match("Esta es la leccion numero", my_string, re.I)
# print(match)
# start, end = match.span()
# print(my_string[start:end])

if not(match != None):
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

#search

search = re.search("Esta es la leccion numero", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])