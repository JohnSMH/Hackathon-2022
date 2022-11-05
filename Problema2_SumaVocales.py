import re
def ContadorVocales(string):
    vocal = re.findall('[aeiou]', string, re.IGNORECASE)
    return len(vocal)
