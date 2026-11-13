from pomocne.ucitavanje import ucitaj, fiksni_split
from pomocne.embedding import embeduj
from pomocne.indeksiranje import indeksiraj
from pomocne.pretraga import pretrazi
from pomocne.groq import configure_groq_client, generate_llm_answer

pitanje1 = "Which staff sergeant's dog tags did the Chief find on the mangled body in the Library?" #odg u fiksnim, 3. rez
# u knjizi je odg u jednom pasusu (chapter 9)
# MOBUTO, MARVIN, STAFFSERGEANT,followed by a service number.


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

#print(indeks_pasusa.ntotal,"\n----\n",indeks_fiksno.ntotal)

#print("-----------Pasusi-----------")
top_pasusi = pretrazi(pitanje1, indeks_pasusa, lista_pasusa)
#print("-----------Fiksni-----------")
top_fiksni = pretrazi(pitanje1, indeks_fiksno, lista_fiksnih_delova)

groq_client = configure_groq_client()

odgovor_a = generate_llm_answer(pitanje1, top_pasusi, groq_client)
odgovor_b = generate_llm_answer(pitanje1, top_fiksni, groq_client)

print("Odgovor a: ", odgovor_a)
print("Odgovor b: ", odgovor_b)