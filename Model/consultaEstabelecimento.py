import populartimes
import time
import logging

def queryLatitudeLongitude(l1,l2,l3,l4):
    result = populartimes.get("AIzaSyDVhgI-kGsNiDaWjTt6Tl0B2mskdPqAVMA", 
        [""], (l1, l2),(l3, l4),radius=10, all_places=True)
    return result


def readcluster():
    with open("/home/semantix/Documentos/Poligono.csv","r") as zafile:
        return [int(line.split(',')[0]) for n,line in enumerate(zafile) if n > 0]


def readLatLong():
    with open("/home/semantix/Documentos/Poligono.csv","r") as zafile:
        lista = list() # lati, longe
        for n,line in enumerate(zafile):
            if n > 0:
                lista_in = list()
                lista_in.append(float(line.split(',')[2])) 
                lista_in.append(float(line.split(',')[3]))
                lista.append(lista_in)
        return lista
                
            
# def readLineByLine():
#     with open("/home/semantix/Documentos/Semantix/zonaAzul/zonaAzulDouble.csv","r") as zafile:
#         for line in zafile:
#             yield [float(l.strip()) for l in line.split(',')]


def manipulandoQuery():
    lines = readLatLong()
    lista2 = []
    recebe_ultima_posicao, count = None, 0
    for line in lines:
        logging.info("*******************valor da PRIMEIRA LINHA no for {}****************".format(line))
        if recebe_ultima_posicao:
            try:
                lista2.append(queryLatitudeLongitude(*(recebe_ultima_posicao + line)))
                print("****************valor da lista depois do append :{}*************** tamanho({})".format(lista2,len(lista2)))
                time.sleep(100)
            except KeyError as e:
                logging.error("**********ERRO NA CHAVE {} **********".format(e))
        logging.warning("######## PROSSEGUINDO COM O PROCESSO ########")
        recebe_ultima_posicao = line
        logging.info("*******valor da ultima posição depois da verificação {}***********".format(recebe_ultima_posicao))
        print()
        count+= 1
        print("COUNT {}".format(count))
        print()
    return lista2
       

def read_cluster_by_cluster():
    populartimes = manipulandoQuery()
    read_cluster = readcluster()



# print(d)


