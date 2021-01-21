
from src.bowling import Bowling


def execute_bowling():

    score = input('Escribe tu score de la partida de bowling: ')

    print('*'*50)

    bowling_object = Bowling(score)

    total_score_bowling = bowling_object.total_score()

    if total_score_bowling == False:

        print('El score de la partida de bowling que ingresaste no es valido')
    else:

        print(
            f'El resultado de tu partida de bowling es: {total_score_bowling}')

    program_reload = input(
        'Quieres ingresar un score de una nueva partida: 1. Si 2.No')

    if program_reload == '1':
        reload_program(True)
    else:
        reload_program(False)
        print('Gracias por usar nuestro programa')


def reload_program(active=False):

    while active == True:

        execute_bowling()


if __name__ == "__main__":

    execute_bowling()
