# Implementações de fatorial em Python

o objetivo desse repósitorio e mostrar duas diferentes versões de algoritims para a resolução de fatorial.

## Fatorial Iterativo

Fatorial Iterativo consiste da implementação da versão iterativa do algoritimo fatorial.
Nesta abordagem utiliza-se de *loops* condicionais e **armazenamento esplicito em varíaveis**.

*Exemplo: 
``` python
def fatorial(n: int) -> int : 
  res = 1
  for i in range(1, n + 1):
    res *= i
  return res
```
## Fatorial Recursivo

Fatorial recursivo consistem da implementação da versão recursiva do algoritimo fatorial.
Nesta abordagem utiliza-se do recurso de chamada da propia função para quebrar o problema em problemas menores ate o caso base (parada).

**Exemplo**:
``` python
def fatorial_rec(n:int) -> int:
  if (n <=1):
    return 1 
  else:
   return n * fatorial_rec(n-1)
```
