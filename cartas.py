import math
RS = float(input()) # quantia RS em dinheiro que uma pessoa tem para enviar cartas
PE = float(input()) # o preço PE de um envelope
PS = float(input()) # o preço PS de um selo
QS = int(input()) # a quantidade QS de selos que a pessoa já dispõe 6
QE = int(input()) # a quantidade de envelopes QE que a pessoa também já dispõe

# Quantas cartas a pessoa pode mandar?
if QS > QE: # comprar envelopes
    dif = QS - QE
    cndc1 = RS - dif * PE
    if cndcl < 0:
        tenho = QE
        comprarE = QE * PE
        cartas = tenho + math.floor(RS/comprarE)
    else:
        tenho = QS
        QE = QS - QE
        comprare = QE * PE
        novoRS = RS - comprare
        comprarCartas = math.floor(novoRS/(PE+PS))
        cartas = comprarCartas + tenho
if QE > QS: # comprar selos
    dif2 = QE - QS
    cndc2 = RS - dif2 * PS
    if cndc2 < 0:
        tenho = QS
        comprars = QS * PS
        cartas = tenho + math.floor(RS/comprars)
    else:
        tenho = QE
        QS = QE - OS
        comprars = QS * PS
        novoRS = RS - comprars
        comprarCartas = math.floor(novoRS/(PE+PS))
        cartas = comprarCartas + tenho
if QS == QE:
    tenho = QS
    precoC = PE + PS
    possocomprar = math.floor(RS/precoc)
    cartas = possocomprar + tenho

print(cartas)
