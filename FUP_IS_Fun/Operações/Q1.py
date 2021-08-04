#Leia dois números e imprima a soma, a subtração, a multiplicação, 
#a divisão e o resto da divisão entre eles respectivamente.

def main():
    num1 = int(input())
    num2 = int(input())
    
    result = num1 + num2
    print(result)
    
    result = num1 - num2
    print(result)
    
    result = num1 * num2
    print(result)
    
    result = float(num1 / num2)
    print("%.2f" %result)
    
    result = num1 % num2
    print("%i" %result)
    
main()