from rios import *

def test_carga_rios(rios:list[Rio])->None:
    print("\n1. Test_carga_rios")
    longitud = len(rios)
    n = 0
    while n < longitud:
        print(carga_rios()[n])
        n = n+1

def test_filtra_rios_de_continente(rios, continente):
    print("\n2. Test_filtra_rios_de_continente")
    print(f'Para el continente {continente} --> {filtra_rios_de_continente(rios, continente)}')

def test_obtener_continentes_y_rios(rios):
    print('\n3. Test_obtener_continentes_y_rios')

    longitud = len(obtener_continentes_y_rios(rios))
    n = 0
    while n < longitud:
        print(obtener_continentes_y_rios(rios)[n])
        n = n+1



if __name__=='__main__':
    rios = carga_rios()
    #test_carga_rios(rios)
    #test_filtra_rios_de_continente(rios, 'Asia')
    test_obtener_continentes_y_rios(rios)
