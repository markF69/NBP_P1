from pomocne.ucitavanje import ucitaj, fiksni_split
from pomocne.embedding import embeduj
from pomocne.indeksiranje import indeksiraj
from pomocne.pretraga import pretrazi
from pomocne.groq import configure_groq_client, generate_llm_answer

pitanje1 = "Which staff sergeant's dog tags did the Chief find on the mangled body in the Library?" # fiksni pristup daje tacan odgovor, zato sto pasusu fali kontekst scene
# u knjizi je odg u jednom pasusu (chapter 9)
# MOBUTO, MARVIN, STAFFSERGEANT,followed by a service number.
pitanje2 = "What did the timer read while the Master Chief was driving the warthog toward the longsword?" # oba poredjenja imaju tacan odg. kao top 1
# chapter 12, odg 01:10:20
pitanje3 = "Since the enemy had taken to watching the humans, what else did they do?"
# ch 7 - odg je "making note of which routes they took, and setting ambushes along the way"
# poredjenje pasusa ovde daje tacan(i brzi) odgovor zato sto je fiksnoj celini kontekst presecen na pola, samim tim prvi deo krene dobro al onda izhalucinira ostatak odgovora
# glavni prikaz mane secenja na fiksne delove

pitanja_list = [pitanje1,pitanje2,pitanje3]
odg_list = ["MOBUTO, MARVIN, STAFFSERGEANT",
            "01:10:20",
            "making note of which routes they took, and setting ambushes along the way"]

# poredice se pasus sa fiksnim delom od 100 reci
pasusi = ucitaj()
lista_fiksnih_delova = fiksni_split(pasusi, 100) # 1034 frag

lista_pasusa=[] # oko 2900 frag

for ime_splita, pasus in pasusi:
    lista_pasusa.append(pasus)

#print(len(lista_pasusa), len(lista_fiksnih_delova))

vektori_pasusa = embeduj(lista_pasusa)
vektori_fiksno = embeduj(lista_fiksnih_delova)

indeks_pasusa = indeksiraj(vektori_pasusa)
indeks_fiksno = indeksiraj(vektori_fiksno)

#print(indeks_pasusa.ntotal,"\n----\n",indeks_fiksno.ntotal)
groq_client = configure_groq_client()
print("\n\n")
for i, pitanje in enumerate(pitanja_list):
    print("-----------Pasusi-----------")
    top_pasusi = pretrazi(pitanje, indeks_pasusa, lista_pasusa)
    print("-----------Fiksni-----------")
    top_fiksni = pretrazi(pitanje, indeks_fiksno, lista_fiksnih_delova)

    odgovor_a = generate_llm_answer(pitanje, top_pasusi, groq_client)
    odgovor_b = generate_llm_answer(pitanje, top_fiksni, groq_client)

    print("\n\nPitanje: ", pitanje)
    print("Odgovor: ", odg_list[i])
    print("\nLLM odgovor A(pasus): ", odgovor_a)
    print("LLM odgovor B(fiksne celine): ", odgovor_b)

    print("\n"*2)
    print("_"*60)
    print("\n"*2)
