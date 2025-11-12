def dechiffre_cesar(text, key):
    decrypted_text = ''
    for char in text:
        decrypted_text += chr((ord(char) - key) % 256)
    return decrypted_text


#Texte chiffré à tester
texte_chiffre = "ixlev"

#Brute force sur tous les décalages possibles
for key in range(1, 26):  # de 1 à 25 inclus
    resultat = dechiffre_cesar(texte_chiffre, key)
    print(f"Clé {key} : {resultat}")