#Os formatos de data e hora são diversos. Leia hora, minuto, dia, mês e ano e imprima no formato hh:mm dd/mm/aa.
# Você deve certificar-se de imprimir um 0 à esquerda para garantir que todas as informações tenham 2 dígitos. A hora de entrada poderá aparecer no formato 24 horas,mas apresente-a na saída no formato 12h.

def main():
    
    hora = int(input())
    minut = int(input())
    dia = int(input())
    mes = int(input())
    ano = int(input())
    x = "0"
    
    if (hora >= 12):
        if(hora == 24):
            hora = 0
            hora = str(hora)
            hora = x + hora
        else:
            hora -=12
            if(hora < 10):
                hora = str(hora)
                hora = x + hora
            
    else:
        hora = str(hora)
        hora = x + hora
    if (minut < 10):
        minut = str(minut)
        minut = x + minut
    if (dia < 10):
        dia = str(dia)
        dia = x + dia
    if(mes < 10):
        mes = str(mes)
        mes = x + mes
    
    ano = str(ano)
    ano = ano[2:4]
   
        
    print("%s:%s %s/%s/%s" %(hora, minut, dia, mes, ano))
    
main()