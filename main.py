MEM = []
PCODE = []
PC = 0
def charge(file):
    """
    Charge le fichier contenant les instructions MEM
    """
    with open('INST.txt') as f:
  
        for line in f:
            line = line.rstrip()
            if " " in line:
                line = line.split(" ")
                PCODE.append(line)
            else:
                PCODE.append([line])
            if 'str' in line:
                break
    interprete()
        

def interprete():
    """ Lance les instructions a partir de leurs nom """
    global MEM
    global PC
    global PCODE
    while PC < len(PCODE):
        inst = PCODE[PC]
        try:
            if len(inst) == 1:eval(inst[0]+"()")
            else:eval(inst[0]+"("+inst[1]+")")
            print(MEM)
   
        except NameError:
            print("ERREUR : "+str(inst[0])+" n'existe pas (Ligne : "+str(PC)+")")
        PC+=1
       
        


def ADD():
    """Additionne le sous-sommet de pile et le sommet, laisse
    le résultat au sommet."""
    MEM.append(MEM[-1]+MEM[-2])

def SUB():
    """Soustrait le sous-sommet de pile et le sommet, laisse
    le résultat au sommet. """
    MEM.append(MEM[-2]-MEM[-1])

def MUL():
    """Multiplie le sous-sommet de pile et le sommet, laisse
    le résultat au sommet."""
    MEM.append(MEM[-1]*MEM[-2])

def DIV():
    """Divise le sous-sommet de pile et le sommet, laisse
    le résultat au sommet. """
    MEM.append(MEM[-2]//MEM[-1])

def EQL():
    """Laisse 1 au sommet de pile si sous-sommet = sommet, 0 sinon"""
    if MEM[-1] == MEM[-2]: MEM.append(1)
    else: MEM.append(0)
 

def NEQ():
    """Laisse 1 au sommet de pile si sous-sommet != sommet, 0 sinon"""
    if MEM[-1] != MEM[-2]: MEM.append(1)
    else: MEM.append(0)

def GTR():
    """Laisse 1 au sommet de pile si sous-sommet > sommet, 0 sinon"""
    if MEM[-1] > MEM[-2]: MEM.append(1)
    else: MEM.append(0)

def LSS():
    """Laisse 1 au sommet de pile si sous-sommet < sommet, 0 sinon"""
    if MEM[-1] < MEM[-2]: MEM.append(1)
    else: MEM.append(0)


def GEQ():
    """Laisse 1 au sommet de pile si sous-sommet >= sommet, 0 sinon"""
    if MEM[-1] >= MEM[-2]: MEM.append(1)
    else: MEM.append(0)

def LEQ():
    """Laisse 1 au sommet de pile si sous-sommet <= sommet, 0 sinon"""
    if MEM[-1] <= MEM[-2]: MEM.append(1)
    else: MEM.append(0)

def PRN():
    """ Imprime le sommet et dépile """
    print(MEM[-1])

def INN(): 
    """Lit un entier, le stocke à l'adresse trouvée au sommet de
    pile, dépile """
    MEM[MEM[-1]] = int(input("Saisi d'un entier :"))
    MEM.pop(-1)

def INT(p):
    """Incrémente de la constante p le pointeur de pile"""
    global PC
    for p in range(p):
        MEM.append(0)
        pass

def LDI(p):
    """Empile la valeur p"""
    MEM.append(p)


def LDA(p):
    """Empile l'adresse p"""
    MEM.append(p)

def LDV():
    """Remplace le sommet par la valeur trouvée à l'adresse
    indiquée par le sommet (déréférence) """
    MEM.append(MEM[MEM[-1]])
    MEM.pop(-2)


def STO():
    """Stocke la valeur au sommet à l'adresse indiquée par le
    sous-sommet, dépile 2 fois """
    MEM[MEM[-2]] = MEM[-1]
    MEM.pop(-1)
    MEM.pop(-1)


def BRN(p):
    """Branchement inconditionnel à l'instruction p"""
    PC = p


def BZE(p):
    """Branchement à l'instruction p si le sommet = 0, dépile"""
    if MEM[-1] == 0:
        PC = p
    


def HLT():
    """Halte"""
    return None

charge("INST.txt")
