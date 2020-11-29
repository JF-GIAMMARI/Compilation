PCODE = [1,2,3,5,6,98,7,4]
PC = 0
def charge(file):
    """
    Charge le fichier contenant les instructions PCODE
    """
    with open('INST.txt') as f:
        INST = []
        for line in f:
            line = line.rstrip()
            if " " in line:
                line = line.split(" ")
                INST.append(line)
            else:
                INST.append([line])
            if 'str' in line:
                break
    return INST
        

def interprete(INST):
    """ Lance les instructions a partir de leurs nom """
    global PCODE
    global PC
    while PC < len(INST):
        line = INST[PC]
        try:
            if len(line) == 1:eval(line[0]+"()")
            else:eval(line[0]+"("+line[1]+")")
   
        except NameError:
            print("ERREUR : "+str(line[0])+" n'existe pas (Ligne : "+str(PC)+")")
        PC+=1
        print("PC : "+str(PC))
        


def ADD():
    """Additionne le sous-sommet de pile et le sommet, laisse
    le résultat au sommet."""
    PCODE.append(PCODE[-1]+PCODE[-2])

def SUB():
    """Soustrait le sous-sommet de pile et le sommet, laisse
    le résultat au sommet. """
    PCODE.append(PCODE[-2]-PCODE[-1])

def MUL():
    """Multiplie le sous-sommet de pile et le sommet, laisse
    le résultat au sommet."""
    PCODE.append(PCODE[-1]*PCODE[-2])

def DIV():
    """Divise le sous-sommet de pile et le sommet, laisse
    le résultat au sommet. """
    PCODE.append(PCODE[-2]//PCODE[-1])

def EQL():
    """Laisse 1 au sommet de pile si sous-sommet = sommet, 0 sinon"""
    if PCODE[-1] == PCODE[-2]: PCODE.append(1)
    else: PCODE.append(0)
 

def NEQ():
    """Laisse 1 au sommet de pile si sous-sommet != sommet, 0 sinon"""
    if PCODE[-1] != PCODE[-2]: PCODE.append(1)
    else: PCODE.append(0)


def PRN():
    """ Imprime le sommet et dépile """
    print(PCODE[-1])
    print("F")

def INN(): #####################
    """Lit un entier, le stocke à l'adresse trouvée au sommet de
    pile, dépile """
    PCODE.append(int(input("Saisi d'un entier :")))

def INT(p):
    """Incrémente de la constante p le pointeur de pile"""
    global PC
    PC += p
    print(p)
    
def LDI(p):
    """Empile la valeur p"""
    PCODE.append(p)


def LDA(p):
    """Empile l'adresse p"""
    PCODE.append(PCODE[p])

def LDV():
    """Remplace le sommet par la valeur trouvée à l'adresse
    indiquée par le sommet (déréférence) """
    PCODE.append(PCODE[PCODE[-1]])
    PCODE.pop(-2)


def STO():
    """Stocke la valeur au sommet à l'adresse indiquée par le
    sous-sommet, dépile 2 fois """
    print("F")

def BRN(p):
    """Branchement inconditionnel à l'instruction p"""


def BZE(p):
    """Branchement à l'instruction p si le sommet = 0, dépile"""


def HLT():
    """Halte"""
    return None

interprete(charge("INST.txt"))
