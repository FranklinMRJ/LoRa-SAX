import time

def descompactarLoRaSAX(arquivoEntrada,arquivoSaida,nomeGateway):
    significadoSimbol=[]
    
    f=open(arquivoEntrada)
    lines=f.readlines()
    totalLinhas = len(lines)
    totalSimbolos = int(lines[0][:lines[0].find(':')])

    for i in range(totalSimbolos):
        separaIndice=int(lines[i].find(':'))
        significadoSimbol.append(lines[i][separaIndice+2:])
    for i in range(totalSimbolos+1,len(lines)):
        for j in range (totalSimbolos):
            lines[i]=lines[i].replace('|'+str(totalSimbolos-j)+'|',significadoSimbol[j])
        lines[i]=lines[i].replace('\n','')
    
    ArqApoio=open('formato.txt')
    apoio = ArqApoio.read()
    ArqApoio.close()
    
    parte1=apoio.find('phyPayload')+14
    parte2=apoio.find("txInfo")-4
    parte3=apoio.find('gatewayID')+13
    parte4=apoio.find("timestamp")-4
    parte5=apoio.find('timestamp')+12
    parte6=apoio.find("rssi")-3

    p1=(apoio[:parte1])
    p2=(apoio[parte2:parte3])
    p3=(apoio[parte4:parte5])
    p4=(apoio[parte6:])
    current_milli_time = lambda: int(round(time.time() * 1000))
    
    fFinal = open(arquivoSaida, "w")
    for i in range (totalSimbolos+1,len(lines)):
        
        timeAUX = str(current_milli_time())
        linhaFinal=p1+lines[i]+p2+nomeGateway+p3+str(timeAUX[:10])+p4+'\n'
        fFinal.write(linhaFinal)
    fFinal.close()