def generar_estructura(names,goals,goals_avoided,assists):
    '''Este modulo devuelve una estructura unica para las 4 variables de entrada.
        La estructura es un Diccionario de Tuplas.
    '''
    #le quito los caracteres no deseados
    
    names1= names.replace(' ','')
    names2= names1.replace('\n','')
    
    names_list = list(names2.split(','))
    
    return dict(zip(names_list, zip(goals,goals_avoided,assists)))