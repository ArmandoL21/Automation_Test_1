def sumar(a, b):
  return a + b 
def restar(a, b):
  return a - b 
def multiplicar(a, b):
  return a * b 
def dividir(a, b):
  if b == 0:
    raise ZeroDivisionError("No se puede dividir por cero.")
  return a / b 

def calculadora_simple():
   print("\n--- CALCULADORA SIMPLE---")
   try:
      # Las entradas de usuario ahora están dentro del try para que asi tome el vlueError
      a = float(input("Primer número: "))
      b = float(input("Segundo número: "))
      
      print("Tipo de Operacion: 1) Sumar 2) Restar 3) Multiplicar 4) Dividir")
      operacion = input("Elije (1-4): ")

      if operacion == '1':
          resultado = sumar(a, b) 
      elif operacion == '2':
          resultado = restar(a, b)
      elif operacion == '3':
          resultado = multiplicar(a, b)
      elif operacion == '4':
          resultado = dividir(a, b)
      else:
        print("Opción inválida.") 
        return
      
      print(f"Resultado: {resultado}")
      
   except ZeroDivisionError:
     print('Error: No se puede dividir por 0.')
   except ValueError:
     print("Error: Deben ser valores numéricos.")

calculadora_simple()