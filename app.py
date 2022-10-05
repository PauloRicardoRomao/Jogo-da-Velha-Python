class JogodaVelha:
    posicoes_tabuleiro = {"7":" ", "8":" ", "9":" ",
                          "4":" ", "5":" ", "6":" ",
                          "1":" ", "2":" ", "3":" "
                          }
    turno = None
    def __init__(self, jogador_inicial): #):
        self.turno = jogador_inicial
        
    def exibir_tabuleiro(self):
        print("┌───┬───┬───┐")
        print(f"| {self.posicoes_tabuleiro['7']} | {self.posicoes_tabuleiro['8']} | {self.posicoes_tabuleiro['9']} |")
        print("├───┼───┼───┤")
        print(f"| {self.posicoes_tabuleiro['4']} | {self.posicoes_tabuleiro['5']} | {self.posicoes_tabuleiro['6']} |")
        print("├───┼───┼───┤")
        print(f"| {self.posicoes_tabuleiro['1']} | {self.posicoes_tabuleiro['2']} | {self.posicoes_tabuleiro['3']} |")
        print("└───┴───┴───┘")
    
    def verificar_jogada(self, jogada):
        if jogada in self.posicoes_tabuleiro.keys():
            if self.posicoes_tabuleiro[jogada] == " ":
                return True
        return False
    
    def verificar_tabuleiro(self):
        if self.posicoes_tabuleiro['7'] == self.posicoes_tabuleiro['8'] == self.posicoes_tabuleiro['9']:
            return self.posicoes_tabuleiro['7']
        elif self.posicoes_tabuleiro['4'] == self.posicoes_tabuleiro['5'] == self.posicoes_tabuleiro['6']:
            return self.posicoes_tabuleiro['4']
        elif self.posicoes_tabuleiro['1'] == self.posicoes_tabuleiro['2'] == self.posicoes_tabuleiro['3']:
            return self.posicoes_tabuleiro['1']
        
        if self.posicoes_tabuleiro['7'] == self.posicoes_tabuleiro['4'] == self.posicoes_tabuleiro['1']:
            return self.posicoes_tabuleiro['7']
        elif self.posicoes_tabuleiro['8'] == self.posicoes_tabuleiro['5'] == self.posicoes_tabuleiro['2']:
            return self.posicoes_tabuleiro['8']
        elif self.posicoes_tabuleiro['9'] == self.posicoes_tabuleiro['6'] == self.posicoes_tabuleiro['3']:
            return self.posicoes_tabuleiro['9']
        
        if self.posicoes_tabuleiro['7'] == self.posicoes_tabuleiro['5'] == self.posicoes_tabuleiro['6']:
            return self.posicoes_tabuleiro['5']
        elif self.posicoes_tabuleiro['9'] == self.posicoes_tabuleiro['5'] == self.posicoes_tabuleiro['1']:
            return self.posicoes_tabuleiro['5']
        
        #empate
        if [*self.posicoes_tabuleiro.values()].count(" ") == 0:
            return "Empate!"
        else:
            return [*self.posicoes_tabuleiro.values()].count(" ")
        
    def jogar(self):
        while True:
            self.exibir_tabuleiro()
            print(f"Turno atual: {self.turno}")
            while True:
                jogada = input("Jogada: ").strip()
                if self.verificar_jogada(jogada):
                    break
                else:
                    print("Jogada inválida, tente novamente.")
                    
            self.posicoes_tabuleiro[jogada] = self.turno
            
            estado = self.verificar_tabuleiro()
            if estado == "X":
                print("X é o vencedor!")
                break
            elif estado == "O":
                print("O é o vencedor!")
                break
            elif estado == "Empate":
                print("EMPATE!")
                break
            
            self.turno = "X" if self.turno == "O" else "O"
            


jogador = input("Qual você escolhe 'X' ou 'O'? ").strip().upper()
while True:
    if jogador != 'X' and jogador != 'O':
        print("Opção inválida.")
        break
    elif jogador == 'X':
        print("Você escolheu 'X'.")
        print("*=*"*10)
        jogo = JogodaVelha(jogador)
        jogo.jogar()
        break
    elif jogador == "O":
        print("Você escolheu 'O'.")
        print("*=*"*10)
        jogo = JogodaVelha(jogador)
        jogo.jogar()
        break
    
print("*=*"*10)





