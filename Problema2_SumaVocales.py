import re
def ContadorVocales(string):
    vocal = re.findall('[aeiou]', string, re.IGNORECASE)
    return len(vocal)
string = input("Ingresa palabra:")
print (ContadorVocales(string))