from sys import flags


test = ['p', 'u', 'b', 'l', 'i', 'c', ' ', 'C', 'l', 'a', 's', 's', ' ', 'H', 'o', 'l', 'a', 's','{','}']


automata ={
    
    'Final': 'Q16',
    
    'delta': {
        ('Q0', 'p'):'Q1',
        ('Q1', 'u'):'Q2',
        ('Q2', 'b'):'Q3',
        ('Q3', 'l'):'Q4',
        ('Q4', 'i'):'Q5',
        ('Q5', 'c'):'Q6',
        ('Q6', ' '):'Q7',
        ('Q7', 'C'):'Q8',
        ('Q8', 'l'):'Q9',
        ('Q9', 'a'):'Q10',
        ('Q10', 's'):'Q11',
        ('Q11', 's'):'Q12',
        ('Q12', ' '):'Q13',
        ('Q13', 'A'):'Q14',
        ('Q13', 'B'):'Q14',
        ('Q13', 'C'):'Q14',
        ('Q13', 'D'):'Q14',
        ('Q13', 'E'):'Q14',
        ('Q13', 'F'):'Q14',
        ('Q13', 'G'):'Q14',
        ('Q13', 'H'):'Q14',
        ('Q13', 'I'):'Q14',
        ('Q13', 'J'):'Q14',
        ('Q13', 'K'):'Q14',
        ('Q13', 'L'):'Q14',
        ('Q13', 'M'):'Q14',
        ('Q13', 'N'):'Q14',
        ('Q13', 'O'):'Q14',
        ('Q13', 'P'):'Q14',
        ('Q13', 'Q'):'Q14',
        ('Q13', 'R'):'Q14',
        ('Q13', 'S'):'Q14',
        ('Q13', 'T'):'Q14',
        ('Q13', 'U'):'Q14',
        ('Q13', 'V'):'Q14',
        ('Q13', 'W'):'Q14',
        ('Q13', 'X'):'Q14',
        ('Q13', 'Y'):'Q14',
        ('Q13', 'Z'):'Q14',
        ('Q14', 'a'):'Q14',
        ('Q14', 'b'):'Q14',
        ('Q14', 'c'):'Q14',
        ('Q14', 'd'):'Q14',
        ('Q14', 'e'):'Q14',
        ('Q14', 'f'):'Q14',
        ('Q14', 'g'):'Q14',
        ('Q14', 'h'):'Q14',
        ('Q14', 'i'):'Q14',
        ('Q14', 'j'):'Q14',
        ('Q14', 'k'):'Q14',
        ('Q14', 'l'):'Q14',
        ('Q14', 'm'):'Q14',
        ('Q14', 'n'):'Q14',
        ('Q14', 'o'):'Q14',
        ('Q14', 'p'):'Q14',
        ('Q14', 'q'):'Q14',
        ('Q14', 'r'):'Q14',
        ('Q14', 's'):'Q14',
        ('Q14', 't'):'Q14',
        ('Q14', 'u'):'Q14',
        ('Q14', 'v'):'Q14',
        ('Q14', 'w'):'Q14',
        ('Q14', 'x'):'Q14',
        ('Q14', 'y'):'Q14',
        ('Q14', 'z'):'Q14',
        ('Q14', '{'):'Q15',
        ('Q15', '\n'):'Q16',
        ('Q16', '\n'):'Q16',
        ('Q16', '}'):'Q17',
        ('Q15', '}'):'Q17',
        
        
    },

    'estate' :[
        'Q0', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 'Q13', 'Q14', 'Q15', 'Q16'
    ],

    'lenguage': [
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q', 
        'R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h',
        'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',
        'z','{','}', ' '
    ]

}



#print(delta.get(('Q0', 'P')))

def validation(a,b):#funcion que evalua si existe el o los caracteres dentro del lenguaje
    try:
       assert(a in automata['estate'])
       assert(b in automata['lenguage'])
       return automata['delta'][a,b] #Retorno el estado de la transicion
    except:
        return False
    
def estate_validation(a):#Valida el estado de la función validation
    if a==False:
        return True
    else:
        return False
    
    
def bucle_state(p, q, c): #funcion para evaluar estados que se encuentren en bucle
    if p == q:
        return c
    else:
        return c+1

def test_array(a): #funcion que evaluará el texto Java
    pos = 0
    for index in a:
        
        #print(validation(state[pos],index))
        #print(index)
        #print("P",state[pos])
        if estate_validation(validation(state[pos],index)):
            break     
        pos = bucle_state(validation(state[pos], index), state[pos], pos)
        #print("P",pos)
        print(index)
    print(validation(state[pos], index))
    return validation(state[pos], index)
        
    
def final(a):
    if a == automata['Final']:
        return "Cumple"
    else:
        return "No cumple"

#print(validation(d, 'B'))

#print(automata['estate'][0])
#print(test[0])
state = automata['estate']


a = 'P'
print(test_array(test))
print(final(test_array(test)))

    
    
#print(validation(automata['estate'][0], test[0]))
#print(validation(i, a))

#for index, item in zip(automata['estate'], test):
#    if validation(index, item) == index:
#        index = validation(index, item)
#        print(index)
    
#    print(f"Hola {index}")
        
    #print(validation(index, item))
    #print(estate_validation(index,validation(index, item)))
    #print(validation(index, item))
    #print(index, item)
    #print(validation(index, item))
    #print(final(validation(index, item)))
    


