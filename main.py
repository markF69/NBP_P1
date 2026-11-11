from ucitavanje import ucitaj
# poredice se pasusi od npr 80 reci sa fiksnim secenjem od nzm kolko reci (trenutno)
lista_pasusa = ucitaj()
#print(lista_pasusa[-1])

fragment = "" # 80 reci chunkovi
lista_fragmenata=[]
for ime_splita, pasus in lista_pasusa:
    if len(fragment.split()) < 80:
        fragment += pasus
    else:
        #print(fragment_od_80,"\n",len(fragment_od_80.split()))
        lista_fragmenata.append(fragment)
        fragment = ""
        break