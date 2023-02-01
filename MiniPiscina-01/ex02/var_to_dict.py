def var_to_dict():
    dictionary = {}
    d = [
        ('Hendrix' , '1942'),
        ('Allman' , '1946'),
        ('King' , '1925'),
        ('Clapton' , '1945'),
        ('Johnson' , '1911'),
        ('Berry' , '1926'),
        ('Vaughan' , '1954'),
        ('Cooder' , '1947'),
        ('Page' , '1944'),
        ('Richards' , '1943'),
        ('Hammett' , '1962'),
        ('Cobain' , '1967'),
        ('Garcia' , '1942'),
        ('Beck' , '1944'),
        ('Santana' , '1947'),
        ('Ramone' , '1948'),
        ('White' , '1975'),
        ('Frusciante', '1970'),
        ('Thompson' , '1949'),
        ('Burton' , '1939')
    dict_temp = dict(d) 
    for pos1, pos2 in dict_temp:
        if not dct[pos2] == None:
            dct[pos2] += " " + pos1
        else:
            dct[pos2] = pos1
    for year, name in dct.items():
        print(f"{year} : {name}")

if __name__ == '__main__':
    var_to_dict()
