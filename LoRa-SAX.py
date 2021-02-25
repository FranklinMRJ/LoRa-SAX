#os arrays simbolo e significadoSimbol formam o dicionário
#simbolo é o array de símbolos de fato
#significadoSimbol é o conjunto de caracteres que aquele símbolo representa
def simbolizar(v, simbolo, significadoSimbol, intervalo):
    linhasSaida=[]
    k=0
    if (intervalo%2!=0):
        intervaloAUX=intervalo-1
    else:
        intervaloAUX=intervalo
    while (k<intervaloAUX):
        s1=v[k]
        s2=v[k+1]
        c=0
        # verificar se existem simbolos no s1
        for y in range (len(simbolo)):
            if (significadoSimbol[y]!=''):
                s1=s1.replace(significadoSimbol[y],simbolo[y])
                s2=s2.replace(significadoSimbol[y],simbolo[y])
        if (len(s1)<len(s2)):
            max=len(s1)
        else:
            max=len(s2)
        for i in range(max):
                if s2[i] == s1[i]: #compara se o caractere da string s2 == ao caractere da string s1
                    if (c==0):
                        Sini=i
                    c=c+1
                else:
                    if (c>5):# se achou 5 ou mais caracteres iguais
                    # marcar com um símbolo de significado que ainda esteja vazio, ele armazena no array significadoSimbol
                        Sfini=i
                        if (c>84): # em nosso experimento não existem mais de 85 ou 86 caracteres iguais, mas esse IF pode ser apagado
                            Sfini=85 #
                        for w in range (len(simbolo)):
                            if (not significadoSimbol[w]):
                                significadoSimbol[w]=s1[Sini:Sfini]
                                break
                    c=0

        for y in range (len(simbolo)):
            if (significadoSimbol[y]!=''):
                s1=s1.replace(significadoSimbol[y],simbolo[y])
                s2=s2.replace(significadoSimbol[y],simbolo[y])

        k=k+2
        linhasSaida.append(s1)
        linhasSaida.append(s2)
        
    if (intervalo!=intervaloAUX):
        for y in range (len(simbolo)):
            if (significadoSimbol[y]!=''):
                v[-1]=v[-1].replace(significadoSimbol[y],simbolo[y])
        linhasSaida.append(v[-1])
    return linhasSaida, significadoSimbol

    
#intervalo = quantidade de linhas do arquivoEntrada
#qtdSimbolos = 150 em todos os experimentos    
def compactarIoTSAX(arquivoEntrada, qtdSimbolos, arquivoSaida, intervalo):
    v=[]
    simbolo=[]
    significadoSimbol=[]
    
    for i in range (qtdSimbolos):
        simbolo.append('|'+str(i+1)+'|')
        significadoSimbol.append('')

    f=open(arquivoEntrada)
    lines=f.readlines()
    tamanho = len(lines)

    for i in range (0,tamanho):
        stringAux=lines[i]
        ini = stringAux.find("phyPayload")+14
        fim = stringAux.find("txInfo")-4
        v.append(stringAux[ini:fim])

    saida, significadoSimbol = simbolizar(v, simbolo, significadoSimbol, intervalo)
    header =''
    for i in range (len(simbolo)): 
        if (significadoSimbol[i]!=''):
            header=str(i+1)+ ': ' +significadoSimbol[i] +'\n'+ header
    print()
    out =''
    for i in range (len(saida)): 
        out =out+'\n'+str(saida[i])
    a=header+out
    f = open(arquivoSaida, "w")
    f.write(a)
    f.close()

