import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

def ucitaj():
    knjiga = epub.read_epub("Halo_the_flood.epub")

    pocetak_split = "index_split_006.html" # odavde krece sadrzaj knjige posto pre toga ima intro i acknowledgements
    kraj_split = "index_split_024.html" # zadnji split

    pasus=[]
    read=False

    for item_id, _ in knjiga.spine:
        item = knjiga.get_item_with_id(item_id) # split iz knjige
        ime = item.get_name().split("/")[-1] # da ne stoji text/

        if ime.endswith(pocetak_split):
            read=True # krece da cita tek kad treba
        if read:
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            for p in soup.find_all('p'): #p zato sto je tu tekst
                tekst = p.get_text(' ', strip=True)
                if tekst:
                    pasus.append((ime, tekst)) # tuple u obliku index_split_nesto i tekst pasusa
        if ime.endswith(kraj_split):
            break

    #debugging
    # print(len(pasus), "pasusa\n----------\n")
    # for i in range(10):
    #     print(pasus[i],"\n")
    # print(pasus[-10])
    pasus = pasus[:-9] # izbacuje zadnji 9 pasusa zato sto imaju informacije od knjzi npr copyright, isbn itd.
    #print(pasus[-1])
    return pasus