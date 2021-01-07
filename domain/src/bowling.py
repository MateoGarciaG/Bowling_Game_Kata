

class Bowling():
    
    def __init__(self, score):
        
        self.score = score
        self.valid_score = False
        
    
    def total_score(self):
        
        if self.score[0] == '/':
            return self.valid_score
        elif 'X/' in self.score:
            return self.valid_score
        else:
            self.valid_score = True
        
        self.score = self.score.replace('-', '0')
        print(self.score)
        
        total_score = 0
        actual_char = self.score[0]
        cont = 0
        for char in self.score:

            if char == '/':
                #* Al ser char = /, necesitamos saber el valor de este /, por lo cual lo restamos con el anterior caracter y menos 10. Porque son 10 bolos
                rest = 10 - int(actual_char)
                #* Si / es el ultimo caracter
                if cont == len(self.score)-1:
                    if self.score[cont] == 'X':
                        pass
                #* Si el siguiente caracter a partir de / es una X
                elif self.score[cont+1] == 'X':
                    total_score += int(actual_char) + rest + 10
                else:
                    #* Si no, al no ser un strike, suma al total el siguiente caracter.
                    total_score += int(actual_char) + rest + int(self.score[cont+1])
            elif char == 'X':
                #* Si X es el penúltimo o último caracter
                if cont == len(self.score)-2 or cont == len(self.score)-1:
                    if self.score[cont] == 'X':
                        pass
                #* Si el siguiente caracter a partir de X, no es otra X
                elif self.score[cont+1] != 'X':
                    #* Si el segundo caracter a partir de X es /
                    if self.score[cont+2] == '/':
                        total_score += 10 + 10
                    else:
                        total_score += 10 + int(self.score[cont+1]) + int(self.score[cont+2])
                #* Si el siguiente caracter a partir de X es otra X y el segundo caracter a partir de X no es una X
                elif self.score[cont+1] == 'X' and self.score[cont+2] != 'X':
                    total_score += 10 + 10 + int(self.score[cont+2])
                #* Si el siguiente caracter a partir de X es otra X y el segundo caracter a partir de X es de nuevo otra X
                elif self.score[cont+1] == 'X' and self.score[cont+2] == 'X':
                    total_score += 10 + 10 + 10
                
                #* Agrega un cero entre el anterior caracter de X y de X
                self.score = self.score[:cont] + '0' + self.score[cont:]
                #* Suma al cont += 1, porque asi permite al siguiente frame ser par, aunque como los indices empiezan desde 0, por eso está colocado como cont % 2 == 1
                cont += 1

            else:
                
                #* Si cont % 2 == 1, quiere decir que actual_char y char forman un frame y este frame no tiene X o /. Por lo cual simplemente se suman al total, ambos números
                if cont % 2 == 1:
                    if actual_char != 'X':
                        total_score += int(actual_char) + int(char)
                    
            actual_char = char
            cont += 1

        return total_score
