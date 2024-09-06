def flatten_list(l):
    flattened_list = []
    def flatten(l): # List eleman kalmayana kadar recursive bir fonksiyon donecek
        for e in l:
            if isinstance(e, list): # List olanlar bir daha flatten fonksiyonuna girecek
                flatten(e)
            else:
                flattened_list.append(e)
    flatten(l)
    return flattened_list
l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5] # Örnek liste
print(flatten_list(l))