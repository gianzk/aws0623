#definicion
def function1():
    print("hello now")

def function2(a):
    #manejo de excepciones
    try:
        print(1/a)
    except Exception as e:
        print(f"error {e}")
    else:
        print("se ejecuto correctamente")

