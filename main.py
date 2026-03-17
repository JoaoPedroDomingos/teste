def fatorial_rec(n:int) -> int:


#Caso base 
  if (n <=1):
    return 1 
  else:
   return n * fatorial_rec(n-1)


def fatorial(n: int) -> int :
  '''    algorotimo interativo para resover fatorial
      input:
         n: int - Um valor inteiro Qualquer >0
      output:
         result - Um valor inteiro >0
  '''
  
    
  res = 1
  for i in range(1, n + 1):
    res *= i
  return res

try: 
    print("==================FATORIAL========================")
    print("")
    n = int(input("Informe um numero "))
    print(f'Resultado interativo:{fatorial(n)}')
    print(f'Resultado Recursivo:{fatorial_rec(n)}')

except ValueError:
 print("Isso não e um numero")

