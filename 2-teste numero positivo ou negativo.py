# verificar se o numero digitado é positivo ou negativo
from pyfirmata import Arduino
import lcd
import time

board=Arduino ('COM6')
lcd.escrever(board, 0, 0, '2 DIA PYTHON')
time.sleep(10.0)

variavel1 = input(lcd.escrever(board, 0, 0, 'DIGITE UM NUMERO'))
if variavel1 >= str(0):
    lcd.escrever(board, 0, 1, f'NUM POSITIVO ')
    lcd.escrever(board, 13, 1, f'{variavel1}')
else:
    lcd.escrever(board, 0, 1, f'NUM NEGATIVO ')
    lcd.escrever(board, 13, 1, f'{variavel1}')
time.sleep(100.0)
lcd.limpar(board)
board.exit()