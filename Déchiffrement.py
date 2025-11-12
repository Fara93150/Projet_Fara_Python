def dechiffre_cesar(text, key):
    decrypted_text = ''
    for char in text:
        decrypted_text += chr((ord(char) - key) % 256)
    return decrypted_text


texte_chiffre = "ixlev"
key = 4

print(dechiffre_cesar(texte_chiffre, key))