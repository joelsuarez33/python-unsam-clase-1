frase = 'cómo transmitir a los otros el infinito Aleph'
palabras = frase.split();
for palabra in palabras:
    if len(palabra) == 1:
        print("");
    else:
        if palabra[-2] == "o":
            a = list(palabra);
            a.pop(-2);
            a.insert(-1,"e");
            strA ="".join(a)
            b = palabras.index(palabra);
            palabras.pop(b);
            palabras.insert(b,strA);
frase_t =" ".join(palabras)        
print(frase_t);
