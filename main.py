from pomocne.ucitavanje import ucitaj, fiksni_split
from pomocne.embedding import embeduj
from pomocne.indeksiranje import indeksiraj
# poredice se pasus sa fiksnim delom od 100 reci
pasusi = ucitaj()
lista_fiksnih_delova = fiksni_split(pasusi, 100) # 1034 frag

lista_pasusa=[]

for ime_splita, pasus in pasusi:
    lista_pasusa.append(pasus)

#print(len(lista_pasusa), len(lista_fiksnih_delova))

vektori_pasusa = embeduj(lista_pasusa)
vektori_fiksno = embeduj(lista_fiksnih_delova)

indeks_pasusa = indeksiraj(vektori_pasusa)
indeks_fiksno = indeksiraj(vektori_fiksno)

print(indeks_pasusa.ntotal,"\n----\n",indeks_fiksno.ntotal)

pitanje1 = "What is the name of the deceased marine whose body Master Chief found in the library?"
# odg je u jednom pasusu (chapter 9, stranica 244?)
# MOBUTO, MARVIN, STAFFSERGEANT,followed by a service number.
pitanje2 = ""
pitanje3 = ""


# for i, (ime, tekst) in enumerate(lista_pasusa):
#     if "MOBUTO, MARVIN" in tekst:
#         print(i, ime)