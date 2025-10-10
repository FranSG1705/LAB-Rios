from rios import *

def test_carga_rios(rios:list[Rio])->None:
    print("\n1. Test_carga_rios")
    longitud = len(rios)
    n = 0
    while n < longitud:
        print (carga_rios()[n])
        n = n+1

def




if __name__=='__main__':
    rios=carga_rios()
    test_carga_rios(rios)