c1, c2, c3 , c4, c5 ,c6 ,c7 , c8, c9 =('1','2','3','4','5','6','7','8','9')

def print_tab(c1, c2, c3 , c4, c5 ,c6 ,c7, c8, c9):
    print((' %s | %s | %s   \n'+ \
          '---+----+---- \n'+ \
          ' %s | %s | %s  \n' + \
          '---+----+----\n' + \
          ' %s | %s | %s ')% (c1, c2, c3, c4, c5, c6, c7, c8, c9))

def tem_ganhador(vez):
    if c1 == c2 == c3 or c4 == c5 == c6 or c7 == c8 == c9 or \
       c1 == c4 == c7 or c2 == c5 == c8 or c3 == c6 == c9 or \
       c1 == c5 == c9 or c3 == c5 == c7:
        print('Esse é o ganhador: ' % vez)
        print(print_tab())
        return True
    print_tab(c1, c2, c3 , c4, c5 ,c6 ,c7, c8, c9)
    return False

def deu_velha(c1, c2, c3 , c4, c5, c6, c7, c8, c9):
    if c1 != '1' and c2 != '2' and c3 != '3'and \
       c4 != '1' and c5 != '5' and c6 != '6'and \
       c7 != '7' and c8 != '8' and c9 != '9':
        print('Deu velha! ')
        return True
    return False

def valida_jogada(c):
    if (c == '1' and c1 != '1') or \
       (c == '2' and c2 != '2') or \
       (c == '3' and c3 != '3') or \
       (c == '4' and c4 != '4') or \
       (c == '5' and c5 != '5') or \
       (c == '6' and c6 != '6') or \
       (c == '7' and c7 != '7') or \
       (c == '8' and c8 != '8') or \
       (c == '9' and c9 != '9'):
        return False
    return True

vez = 'X'

while not tem_ganhador('O' if vez == 'X' else 'x') and \
      not deu_velha(c1, c2, c3 , c4, c5, c6, c7, c8, c9):

    c = input('Jogador %s escolha sua jogada:'% vez)

    if(valida_jogada(c)):
        if (c == '1'): c1 = vez
        elif (c == '2'): c2 = vez
        elif (c == '3'): c3 = vez
        elif (c == '4'): c4 = vez
        elif (c == '5'): c5 = vez
        elif (c == '6'): c6 = vez
        elif (c == '7'): c7 = vez
        elif (c == '8'): c8 = vez
        elif (c == '9'): c9 = vez
        if vez == 'X':
            vez ='O'
        else:
            vez = 'X'
    else:
            print('Jogada invalida!')
else:
        
        (print_tab)
