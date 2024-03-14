def q1():
    """
    1. Escreva um programa que solicita um número ao usuário e determina se 
    é positivo, negativo ou zero. 
    """
    n = int(input("Digite um numero"))
    if n > 0:
        print("positivo")
    elif n < 0:
        print("negativo")
    else:
        print("zero")

def q2():
    """
    2. Verificação de Número Par/Ímpar: Crie um programa que pede ao usuário 
    um número e imprima se ele é par ou ímpar.
    """
    numero = int(input("Digite um numero"))
    if numero % 2 == 0:
        print("par")

    else:
        print("ímpar")






def q3():
    """
    3. Calculadora Simples: Faça uma calculadora que pede ao usuário dois 
    números e uma operação (+, -, *, /) e imprima o resultado dessa operação.
    """
    num1 = float(input("Digite o primeiro número"))
    num2 = float(input("Digite o segundo número"))
    opr = input("Qual é a operação")

    if opr == "+":
        print (num1+num2)

    elif opr == "-":
        print (num1-num2) 
    
    elif opr == "*":
        print (num1*num2)

    elif opr == "/":
        print (num1/num2)

    else:
        print("Resolva novamente")    

        

     
 
 
 


def q4():
    """
    4. Maior de Três Números: Escreva um programa que solicita três números 
    ao usuário e imprima o maior dentre eles.
    """
    n1 = float(input("Digite um número"))
    n2 = float(input("Digite segundo número"))
    n3 = float(input("Digite terceiro número"))

    if n1 >= n2 and n1 >= n3:
        print(n1)
    elif n2 >= n1 and n2 >= n3:
        print(n2)
    else:
        print(n3)




               


def q5():
    """
    5. Classificação de Idade: Peça a idade do usuário e imprima a classificação
    em "Criança" (0-12), "Adolescente" (13-19), "Adulto" (20-59) ou "Idoso" (60+).
    """
    #criança = int(input(""))
    #adolescente = int(input(""))
    #adulto = int(input(""))
    #idoso = int(input(""))

    idade = int(input("Digite sua idade:"))

    if idade <= 12:
        print("criança")
    elif idade == 13 >= 19:
        print ("Adolescente")

    elif idade == 20 >= 59:
        print("Adulto")

    elif idade == 60 >= 90:
        print("idoso") 



def q6():
    """
    6. Verificação de Triângulo: Peça ao usuário o comprimento de três 
    lados e verifique se eles podem formar um triângulo. Se sim, determine 
    se é um triângulo equilátero, isósceles ou escaleno.
    """
    

def q7():
    """
    7. Conversão de Notas: Escreva um programa que converte uma nota 
    de 0 a 100 em uma escala de conceitos: 
    A (90-100), B (80-89), C (70-79), D (60-69), E (50-59).e F (0-49)
    """
    

def q8():
    """
    8. Validação de Login: Crie um programa que pede ao usuário um nome 
    de usuário e uma senha. Se o nome de usuário for "admin" e a senha for 
    "12345", exiba "Acesso concedido", caso contrário, exiba "Acesso negado".
    """
    

def q9():
    """
    9. Calculadora de IMC: Peça ao usuário sua altura e peso e calcule o
      índice de massa corporal (IMC). Em seguida, mostre uma mensagem 
      indicando se a pessoa está: Abaixo do peso, Peso normal, Sobrepeso, 
      Obesa ou Muito obesa.
    """


def q10():
    """
    10. Verificação de Ano Bissexto: Escreva um programa que verifica 
    se um ano fornecido pelo usuário é bissexto ou não.
    """


