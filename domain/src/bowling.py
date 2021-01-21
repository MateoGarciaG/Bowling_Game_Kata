

class BowlingScoreCard():
    
    """Class Bowling: This class let us obtain self.total_score of a Bowling's game
    """
    
    def __init__(self, score):
        
        self.score = score
        self.valid_score = False
        self.total_score = 0
        self.cont_frame = 0
        self.actual_char = self.score[0]
        
    def strike(self):
        
        #* Si X es el penúltimo o último caracter
        if self.cont_frame == len(self.score)-2 or self.cont_frame == len(self.score)-1:
            if self.score[self.cont_frame] == 'X':
                pass
        #* Si el siguiente caracter a partir de X, no es otra X
        elif self.score[self.cont_frame+1] != 'X':
            #* Si el segundo caracter a partir de X es /
            if self.score[self.cont_frame+2] == '/':
                self.total_score += 10 + 10
            else:
                self.total_score += 10 + int(self.score[self.cont_frame+1]) + int(self.score[self.cont_frame+2])
        #* Si el siguiente caracter a partir de X es otra X y el segundo caracter a partir de X no es una X
        elif self.score[self.cont_frame+1] == 'X' and self.score[self.cont_frame+2] != 'X':
            self.total_score += 10 + 10 + int(self.score[self.cont_frame+2])
        #* Si el siguiente caracter a partir de X es otra X y el segundo caracter a partir de X es de nuevo otra X
        elif self.score[self.cont_frame+1] == 'X' and self.score[self.cont_frame+2] == 'X':
            self.total_score += 10 + 10 + 10
        
        #* Agrega un cero entre el anterior caracter de X y de X
        self.score = self.score[:self.cont_frame] + '0' + self.score[self.cont_frame:]
        #* Suma al self.cont_frame += 1, porque asi permite al siguiente frame ser par, aunque como los indices empiezan desde 0, por eso está colocado como self.cont_frame % 2 == 1
        self.cont_frame += 1
        
    def spare(self):
        #* Al ser char = /, necesitamos saber el valor de este /, por lo cual lo restamos con el anterior caracter y menos 10. Porque son 10 bolos
        rest = 10 - int(self.actual_char)
        #* Si / es el ultimo caracter
        if self.cont_frame == len(self.score)-1:
            if self.score[self.cont_frame] == 'X':
                pass
        #* Si el siguiente caracter a partir de / es una X
        elif self.score[self.cont_frame+1] == 'X':
            self.total_score += int(self.actual_char) + rest + 10
        else:
            #* Si no, al no ser un strike, suma al total el siguiente caracter.
            self.total_score += int(self.actual_char) + rest + int(self.score[self.cont_frame+1])
            
    def check_valid_score(self):
        if self.score[0] == '/':
            return self.valid_score
        elif 'X/' in self.score:
            return self.valid_score
        else:
            self.valid_score = True
            
            
    def get_total_score(self):
        
        self.check_valid_score()
        
        self.score = self.score.replace('-', '0')
        print(self.score)
        
        # self.total_score = 0
        # self.actual_char = self.score[0]
        # self.cont_frame = 0
        for char in self.score:

            if char == '/':
                self.spare()
            elif char == 'X':
                self.strike()

            else:
                
                #* Si self.cont_frame % 2 == 1, quiere decir que self.actual_char y char forman un frame y este frame no tiene X o /. Por lo cual simplemente se suman al total, ambos números
                if self.cont_frame % 2 == 1:
                    if self.actual_char != 'X':
                        self.total_score += int(self.actual_char) + int(char)
                    
            self.actual_char = char
            self.cont_frame += 1
            
        print(self.total_score)
        return self.total_score


