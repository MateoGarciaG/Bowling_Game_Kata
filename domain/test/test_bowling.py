
from domain.src.bowling import Bowling
import pytest

#* 1 partida: 10 cuadros
#* Cda cuadro tiene tres secciones: 1. Primer tiro 2. Segundo tiro 3. Suma total
#* Tendremos 2 tiros en cada cuadro para derribar los 10 bolos
#* STRIKE : Si en un cuadrado, a la 1 oportunidad derribas los 10 bolos, es un STRIKE: X. Cuando en un cuadro tenemos un STRIKE, la sección/casilla del segundo tiro se deja en blanco, y se pasa al siguiente cuadro
#* SPARE/SEMIPLENO: Si en las dos oportunidades de un cuadro, se derriban los 10 bolos es un SPARE, donde se marca el número de bolos derribados en la primera tirada y en la segunda tirada no colocamos el resto, sino que colocamos "/"
#* En el caso de que no se marque ningún bolo en algun tiro, se marca con: -
#* Suma total de un cuadro: El total de puntos de ese cuadrado es la suma de sus 2 tiros y la suma del siguiente cuadro, es decir, la suma de los dos siguientes tiros. Solo en el caso de que los dos siguiente tiros sean STRIKE, recordemos que si hay strike el segundo tiro se deja en blanco.
#* Ejm: tenemos 3 STRIKES, el total del cuadro del 1 STRIKE sería entonces 30
#* SUMA SPARE: La suma total en un cuadro con resultado SPARE, es sumar ambos tiros, es decir, 10. Más la suma del siguiente tiro, este siguiente tiro puede ser el primer tiro o segundo tiro del siguiente cuadro.
#* Ejm: En un cuadro tenemos 6 / = 10, y el siguiente cuadro tenemos 4 / . Por lo cual se suma 6 7 = 10 . Y el siguiente tiro que es 4 = 14. 14 sería la suma total del cuadro de 6 /

def test_all_strikes():
    
    assert Bowling("XXXXXXXXXXXX").total_score() == 300

def test_spare():
    
    assert Bowling("5/5/5/5/5/5/5/5/5/5/5").total_score() == 150

def test_heartbreak():
    
    assert Bowling("9-9-9-9-9-9-9-9-9-9-").total_score() == 90

def test_random_score():
    
    assert Bowling("12345123451234512345").total_score() == 60