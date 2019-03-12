def readCsv():
    with open("/home/semantix/Documentos/Poligono.csv","r") as zafile:
        return [int(line.split(',')[0]) for n,line in enumerate(zafile) if n > 0]
            


def readLineByLine():
    with open("/home/semantix/Documentos/Semantix/zonaAzul/zonaAzulDouble.csv","r") as zafile:
        for line in zafile:
            yield [float(l.strip()) for l in line.split(',')]