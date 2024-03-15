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





    idade = int(input("Digite sua idade: "))
  
    if idade <= 12:
        print("Criança")
    elif 13 <= idade <= 19:
        print("Adolescente")
    elif 20 <= idade <= 59:
        print("Adulto")
    else:
        print("Idoso")

 



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
    nota = int(input("Digite sua nota:"))
    

    if nota >= 90 and nota <= 100:
         print("A")
    elif nota >= 80 and nota <= 89:
        print("B")
    elif nota >= 70 and nota <= 79:
        print("C")
    elif nota >= 60 and nota <= 69:
        print("D")
    elif nota >= 50 and nota <= 59:
        print("E")
    else:
        print("F")
    

def q8():
    """
    8. Validação de Login: Crie um programa que pede ao usuário um nome 
    de usuário e uma senha. Se o nome de usuário for "admin" e a senha for 
    "12345", exiba "Acesso concedido", caso contrário, exiba "Acesso negado".
    """
    login = input("Digite seu login:")
    senha = input("Digite sua senha:")
    ADMIN = "admin"
    PASSAWORD = "12345"
    

    if login == ADMIN and senha == PASSAWORD:
        print ("Acesso concedido")

    else:
        print("Acesso negado")

      

def q9():
    """
    9. Calculadora de IMC: Peça ao usuário sua altura e peso e calcule o
      índice de massa corporal (IMC). Em seguida, mostre uma mensagem 
      indicando se a pessoa está: Abaixo do peso, Peso normal, Sobrepeso, 
      Obesa ou Muito obesa.
    """
    h = float(input(""))
    peso = int(input(""))
    imc = peso/h**2
    

    match imc:
        case imc if imc < 18.5:
            print("Abaixo do peso")
        case imc if imc > 18.5 and imc < 25:
            print("Peso normal")
        case imc if imc > 26 and imc < 30:
            print("Sobrepeso")
        case imc if imc > 30 and imc < 35:
            print("Obeso")
        case imc if imc > 35 :
            print("Muito obeso")








    


def q10():
    """
    10. Verificação de Ano Bissexto: Escreva um programa que verifica 
    se um ano fornecido pelo usuário é bissexto ou não.
    """
 

