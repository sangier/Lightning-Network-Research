f = open("output_c_3.txt", "r")

now=f.read()

if now.startswith("[lncli]"):
    print("errore trovato fraaa")
elif now.startswith("{"):
    print("Il canale è stato montato a buon fine")
