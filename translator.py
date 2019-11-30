comps = []
node_number = [1]
class Fonte:
    def __init__(self, T, I ):
        self.T = T
        self.I = I
        self.catodo = None
        self.anodo = None
        self.registro = None
    def setCatodo(self, catodo):
        self.catodo = catodo
    def setAnodo(self, anodo):
        self.anodo = anodo
    def setRegistro(self, registro):
        self.registro = registro
    def printComp(self):
        return "Fonte: " + self.T + "V e " + self.I + "A."

class Resistor:
    def __init__(self, R, W ):
        self.R = R
        self.W = W
    # sei que n existe anodo e catodo num resistor, mas apra simplificar essa PoC usarei anodo e catodo para perna 1 e 2
        self.catodo = None
        self.anodo = None
        self.registro = None
    def setCatodo(self, catodo):
        self.catodo = catodo
    def setAnodo(self, anodo):
        self.anodo = anodo
    def setRegistro(self, registro):
        self.registro = registro
    def printComp(self):
        return "Resistor: " + self.R + "ohms e " + self.W + "W."

class Led:
    def __init__(self, T, I ):
        self.T = T
        self.I = I
        self.catodo = None
        self.anodo = None
        self.registro = None
    def setCatodo(self, catodo):
        self.catodo = catodo
    def setAnodo(self, anodo):
        self.anodo = anodo
    def setRegistro(self, registro):
        self.registro = registro
    def printComp(self):
        return "Led: " + self.T + "V e " + self.I + "A."

def getNodeNumber():
    ret = node_number[0]
    node_number[0] = node_number[0] + 1 
    return ret

def find_node_to_connect (term1, term2):
    if (term1 is None and term2 is None):
        n = getNodeNumber()
        return n
    else:
        return term1 if not none else term2
    
        

def printComps():
    for comp in comps:
        print(comp.printComp())

def stringComps( posToIgnore ):
    ret = ""
    n = 1
    for comp in comps:
        if (posToIgnore >= 0):
            if (comp != comps[posToIgnore]):
                ret += str(n) + " para " + comp.printComp() + "\n"
                n+=1
        else:
            ret += str(n) + " para " + comp.printComp() + "\n"
            n+=1
    return ret

def ploterNodes():
    blacklist = []
    for comp in comps:
        if (comp.anodo != None  or comp.catodo != None):
            node = comp.anodo if comp.anodo != None else comp.atodo
            if node in blacklist:
                continue
            else:
                blacklist.append(node)
            for comp2 in comps:
                if (comp == comp2 ):
                    continue
                else:
                   if (comp2.anodo == node  or comp2.catodo == node):
                        print(comp.printComp())
                        print ("anodo: ", comp.anodo)
                        print ("catodo: ", comp.catodo)
                        print(comp2.printComp())
                        print ("anodo: ", comp2.anodo)
                        print ("catodo: ", comp2.catodo) 
                        print( "______________///________________")

def addHandle():
    while(True):
        action =  input("Digite:\n\
                1 para adição de fonte\n\
                2 para adição de resistor\n\
                3 para adição de LED\n\
                4 para listar componentes\n\
                Qualquer oura coisa para voltar \n")
        if( action == str(1) ):
            T = input("Digite a tensão em Volts: \n")
            I = input("Digite a corrente em Amperes: \n")
            comps.append(Fonte(T,I))
        elif( action == str(2) ):
            R = input("Digite a resistencia em ohms: \n")
            W = input("Digite a potencia em Watts: \n")
            comps.append(Resistor(R, W))
           
        elif( action == str(3) ):
            T = input("Digite a tensão em Volts: \n")
            I = input("Digite a corrente em Amperes:\n")
            comps.append(Led(T,I))

        elif( action == str(4) ):
            printComps()
        else:
            break

def cosntructHandle():
    text = ""
    
    action =  int(float(input("Digite quem você quer conectar:\n "+ stringComps(-1) + 
            " 0 para voltar\n")))
    if action == 0 :
        return
    action2 = int(float(input("Digite com quem você quer conectar:\n "+ stringComps(-1) + 
            " 0 para voltar\n")))
    
    if ( type(comps[action -1]) is Resistor ):
        a2 = input ("Qual perna de " + comps[action-1].printComp() + " vocer quer conectar: \n\
            1 para Perna1\n \
            2 para Perna 2 \n" )
    else:
        a1 = input ("Qual perna de " + comps[action-1].printComp() + " vocer quer conectar: \n\
            1 para anodo\n \
            2 para catodo \n" )
    if action2 == 0 :
        return

    if ( type(comps[action2 -1]) is Resistor ):
        a2 = input ("Qual perna de " + comps[action2-1].printComp() + " vocer quer conectar: \n\
            1 para Perna1\n \
            2 para Perna 2 \n" )
    else:
        a2 = input ("Qual perna de " + comps[action2-1].printComp() + " vocer quer conectar: \n\
            1 para anodo\n \
            2 para catodo \n" )

    
    if (a1 == str(1)):
        if(a2 == str(1)):
            node = find_node_to_connect(comps[action-1].anodo, comps[action2-1].anodo )
            comps[action-1].setAnodo(node)
            comps[action2-1].setAnodo(node)
        else:
            node = find_node_to_connect(comps[action-1].anodo, comps[action2-1].catodo )
            comps[action-1].setAnodo(node)
            comps[action2-1].setCatodo(node)
    else:
        if(a2 == str(1)):
            node = find_node_to_connect(comps[action-1].catodo, comps[action2-1].anodo )
            comps[action-1].setCatodo(node)
            comps[action2-1].setAnodo(node)
        else:
            node = find_node_to_connect(comps[action-1].catodo, comps[action2-1].catodo )
            comps[action-1].setCatodo(node)
            comps[action2-1].setCatodo(node)

def ResistorRdfMaker(comp):
    ret = ""
    resistVal = comps.index(comp)
    comp.setRegistro("Resistor"+str(resistVal) )
    ret += "ex:Resistor" + str(resistVal) + " a  dbr:Resistor;\n"
    ret += "\t ex:Resistencia " + "\"" + comp.R + "\";\n"
    ret += "\t ex:Potencia " + "\"" + comp.W + "\".\n"
    return ret

def FonteRdfMaker(comp):
    ret = ""
    fonteVal = comps.index(comp)
    comp.setRegistro("Fonte" + str(fonteVal) )
    ret += "ex:Fonte" + str(fonteVal) + " a  dbr:Regulated_power_supply;\n"
    ret += "\t ex:Tensao " + "\"" + comp.T + "\";\n"
    ret += "\t ex:Corrente " + "\"" + comp.I + "\".\n"
    return ret

def LedRdfMaker(comp):
    ret = ""
    ledVal = comps.index(comp)
    comp.setRegistro("Led" + str(ledVal))
    ret += "ex:Led" + str(ledVal) + " a  dbr:Light-emitting_diode;\n"
    ret += "\t ex:Tensao " + "\"" + comp.T + "\";\n"
    ret += "\t ex:Corrente " + "\"" + comp.I + "\".\n"
    return ret



def NodeRdfMaker():
    ret = "ex:Node_of_circuit a rdfs:Class.\n"
    aux = node_number[0]
    max = 0
    for i in range(1, aux):
        ret += "ex:Node" + str(i) + "  a " + "ex:Node_of_circuit.\n"
        counter = 1
        for comp in comps:
            if max < counter:
                max = counter
                res_aux = "ex:pin" + str(counter) + " a rdfs:Property;\n\
\trdfs:label \"Pin" + str(counter) + "\".\n" 
                ret = res_aux + ret
            if type(comp) is not Resistor:
                if comp.anodo == i:
                    ret += "ex:Node" + str(i) + " ex:pin" + str(counter) + " ex:" + comp.registro + ".\n"
                    ret += "ex:Node" + str(i) +" ex:pin" + str(counter)  + " \"anodo\".\n"
                    counter += 1 
                elif comp.catodo == i:
                    ret += "ex:Node" + str(i) + " ex:pin" + str(counter)   + " ex:" + comp.registro + ".\n"
                    ret += "ex:Node" + str(i) + " ex:pin" + str(counter)   + " \"catodo\".\n"
                    counter  += 1
            else: 
                if comp.anodo == i:
                    ret += "ex:Node" + str(i) + " ex:pin" + str(counter)   + " ex:" + comp.registro + ".\n"
                    ret += "ex:Node" + str(i) + " ex:pin" + str(counter)   + " \"pino1\".\n"
                    counter += 1
                elif comp.catodo == i:
                    ret += "ex:Node" + str(i) + " ex:pin" + str(counter)  + " ex:" + comp.registro + ".\n"
                    ret += "ex:Node" + str(i) + " ex:pin" + str(counter)   + " \"pino2\".\n"
                    counter += 1
    return ret


        
            






def compsRDFMaker():
    ret = "@prefix ex: <http://example.org/>.\n\
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>.\n\
@prefix dbr: <http://dbpedia.org/resource/>.\n\
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.\n\
@prefix dbo: <http://dbpedia.org/ontology/>.\n\n\
ex:Tensao a rdfs:Property;\n\
\trdfs:label \"Tensao\";\n\
\trdfs:Range rdfs:Literal.\n\
ex:Corrente  a rdfs:Property;\n\
\trdfs:label \"Corrente\";\n\
\trdfs:Range rdfs:Literal.\n\
ex:Resistencia  a rdfs:Property;\n\
\trdfs:label \"Resistencia\";\n\
\trdfs:Range rdfs:Literal.\n\
ex:Potencia  a rdfs:Property;\n\
\trdfs:label \"Potencia\";\n\
\trdfs:Range rdfs:Literal.\n"

    for comp in comps:
        if type(comp) is Resistor:
            ret += ResistorRdfMaker(comp)
        if type(comp) is Fonte:
            ret += FonteRdfMaker(comp)
        if type(comp) is Led:
            ret += LedRdfMaker(comp)
    ret += NodeRdfMaker()
    
    
        
    print(ret)
    


def ploter():
    compsRDFMaker()
    return



def menuHandle():
    while(True):
        action =  input("Digite:\n\
                1 para entrar no menu de adição de componente.\n\
                2 para adicionar um nó de circuito\n\
                3 para plotar RDF-Turttle\n\
                4 para listar nós de circuito\n\
                Qualquer outra coisa para sair\n")
        if( action == str(1) ):
            addHandle()
        elif( action == str(2) ):
            cosntructHandle()
        elif( action == str(3) ):
            ploter()
        elif( action == str(4) ):
            ploterNodes()
        else:
            break

menuHandle()
