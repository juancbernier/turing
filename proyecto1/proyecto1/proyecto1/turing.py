
from operator import concat
import re

lista_automata = str();

def eliminarCaracteres(automata):
    caracteres=" "
    for x in range(len(caracteres)):
        automata=automata.replace(caracteres[x],"")
    return automata


def inicio(automata):
    # ----------------- PARAMETROS DE LA MAQUINA DE TURING ------------------
    def turing_M (state = None, #estados de la maquina de turing
                blank = None, #simbolo blanco de el alfabeto de la cinta
                rules = [],   #reglas de transicion
                tape = [],    #cinta
                final = None,  #estado valido y/o final
                pos = 0):#posicion siguiente de la maquina de turing
        
        st = state #Obtengo los estados de la maquina
        if not tape: tape = [blank] #Si no hay elementos en la cinta; la cinta se llenará del simbolo blanco
        if pos <0 :
            pos += len(tape) #Obtengo el tamaño de mi cinta
        #if pos >= len(tape) or pos < 0 : raise  ("Se inicializa mal la posicion")
        
      

        #DEFINIENDO LAS REGLAS DE LA CINTA Y RECORRIENDO TODA LA CINTA
        rules = dict(((s0, v0), (v1, dr, s1))  for (s0, v0, v1, dr, s1) in rules) 

        # S0 = Estdo inicial; v0 = valor del simbolo que lee s0;  v1 = nuevo simbolo que reemplazará a v0; dr = direccion de la cinta; s1 = Nuevo estado 
        """Estado	Símbolo leído	Símbolo escrito	       Mov. 	Estado sig.
            p(s0)	       1(v0)	         x(v1)         R(dr)	     p(s1)
        """
    
        global lista_automata;
        while True:
            print (st, end=" --> ") #me imprime el estado y el señalamiento
            lista_automata = lista_automata+(st + " --> ")
            for i, v in enumerate(tape):
                if i==pos: 
                    print ("{%s}"%(v),end=" ")#me indica en tiempo real su posicion
                    lista_automata = lista_automata+("{%s}"%(v)+" ")
                    
                else: 
                    print (v, end=" ")#imprime el resto de datos
                    lista_automata = lista_automata+(v+" ")
                
            print()
            lista_automata = lista_automata+(" \n ")
            if st == final: #SI LLEGAMOS AL ESTADO DE ACEPTACION; SE CIERRE EL PROGRAMA
                break
            if (st, tape[pos]) not in rules: #SI LA CINTA ESTA VACIA; SE CIERRE EL PROGRAMA
                break
            
            (v1,dr,s1) = rules [(st, tape[pos])]#lee las reglas
            tape[pos]=v1 #rescribe el simbolo de la cinta
        
            #movimiento del cabezal
            if dr == 'L':
                if pos > 0:
                    pos -= 1
                else: tape.insert(0, blank)
            if dr == 'R':
                pos += 1
                if pos >= len(tape): tape.append(blank)
            st = s1

        return lista_automata.split("\n")

    #print(concat)
    automata=eliminarCaracteres(automata)
    patron=re.compile("^(a{1}|b{1})*")
    if re.fullmatch(patron,automata):
        print("la palabra es valida")

        cadena = automata.split()
        cad = "".join(cadena)
        return turing_M (state = 'q1', #estado inicial de la maquina de turing
                    blank = 'λ', #simbolo blanco de el alfabeto dela cinta
                    tape = list(cad),#inserta los elementos en la cinta
                    final = 'q3',  #estado valido y/o final
                    rules = map(tuple,#reglas de transicion
                                [
                                "q1 a a R q1".split(),
                                "q1 b b R q1".split(),
                                "q1 λ λ L q2".split(), 
                                "q2 a a L q2".split(),
                                "q2 b a L q2".split(),
                                "q2 λ λ R q3".split(),
                                
                                ]   
                                )
                    )   
    else:
        return -1;
       #return print("palabra no valida, por favor utiliza solo las letras [ a , b ]")
   
#inicio("ababa")