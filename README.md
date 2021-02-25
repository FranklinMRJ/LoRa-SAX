# LoRa-SAX
LoRa-SAX
Documento escrito por Franklin MRJ
# Para compactar os pacotes LoRa do 'arquivoEntrada.txt' utilize o código em "compactar_LoRa-SAX.py"

#intervalo = quantidade de linhas do arquivoEntrada
#qtdSimbolos = 150 em todos os experimentos   

intervalo=200 
compactarLoRaSAX('arquivoEntrada.txt', 150, 'arquivoComprimido.lorasax', intervalo)



# Para descompactar utilize o código em "descompactar_LoRa-SAX.py"
#exemplo de descompactação com o gateway = 1876585532657073

descompactarLoRaSAX('arquivoComprimido.lorasax','arquivoDescomprimido.txt', '1876585532657073')
