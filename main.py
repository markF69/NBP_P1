from ucitavanje import ucitaj, fiksni_split
# poredice se pasus sa fiksnim delom od 100 reci
lista_pasusa = ucitaj()
lista_fiksnih_delova = fiksni_split(lista_pasusa, 100) # 1034 frag
#print(lista_pasusa[-1])
lista_fragmenata=[]

for ime_splita, pasus in lista_pasusa:
    lista_fragmenata.append(pasus)

print(len(lista_fragmenata), len(lista_fiksnih_delova))
# for i, (ime, tekst) in enumerate(lista_pasusa):
#     if "MOBUTO, MARVIN" in tekst:
#         print(i, ime)