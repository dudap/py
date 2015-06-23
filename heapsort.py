import time
#sortowanie stogowe
def heap_sort(L):

    for start in range(int((len(L)-2)/2), -1, -1):
        shiftdown(L, start, len(L)-1)

    #sortowanie
    for end in range(len(L)-1, 0, -1):
     #   print("[LOG] Zamiana: "+str(L[end])+" z "+str(L[0]))
        L[end], L[0] = L[0], L[end] #swap
        shiftdown(L, 0, end - 1) #przywracanie wlasnosci kopca
    return L
 
#spusc element pod indeksem start w dol - tak by byl zachowany warunek kopca
def shiftdown(lst, start, end):
    """Metoda do produkcji kopca"""
    root = start
    #print("[LOG] Przywracanie wlasnosci kopca")
   # print("[LOG] Ustalamy korzen: "+str(root))
    while True:
        child = root * 2 + 1
        if child > end: break
        if child + 1 <= end and lst[child] < lst[child + 1]:
            child += 1
        if lst[root] < lst[child]:
            lst[root], lst[child] = lst[child], lst[root]
            root = child
        else:
            break


czas1=time.time()
p=[9,1,2,5,561,6,231,3,456,798,9,42,13,456,0,47,987,4,231,32,456,498,798,7,984,51,34,654,94,987,1,13,2,64,64,9,5,561,6,231,3,456,798,9,42,13,456,0,47,987,4,231,32,456,498,798,7,984,51,34,654,94,987,1,13,2,64,64,9,5,561,6,231,3,456,798,9,42,13,456,0,47,987,4,231,32,456,498,798,7,984,51,34,654,94,987,1,13,2,64,64,9,5,561,6,231,3,456,798,9,42,13,456,0,47,987,4,231,32,456,498,798,7,984,51,34,654,94,987,1,13,2,64,64,9,5,561,6,231,3,456,798,9,42,13,456,0,47,987,4,231,32,456,498,798,7,984,51,34,654,94,987,1,13,2,64,64,9,5,561,6,231,3,456,798,9,42,13,456,0,47,987,4,231,32,456,498,798,7,984,51,34,654,94,987,1,13,2,64,64,9,5,561,6,231,3,456,798,9,42,13,456,0,47,987,4,231,32,456,498,798,7,984,51,34,654,94,987,1,13,2,64,64,9,5,561,6,231,3,456,798,9,42,13,456,0,47,987,4,231,32,456,498,798,7,984,51,34,654,94,987,1,13,2,64,64,9,5,561,6,231,3,456,798,9,42,13,456,0,47,987,4,231,32,456,498,798,7,984,51,34,654,94,987,1,13,2,64,64,9,5,561,6,231,3,456,798,9,42,13,456,0,47,987,4,231,32,456,498,798,7,984,51,34,654,94,987,1,13,2,64,64,9]
print (p)
p=heap_sort(p)
czas2=time.time()
print(len (p),p)
print(czas2-czas1)
