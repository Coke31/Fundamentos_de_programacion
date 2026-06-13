def motrar_menu():
    print("[1] °C -> °F \n [2] °F -> °C \n [3] Salir")

def pedir_temperatura():
    temperatura = float(input("¿Cual es la temperatura?"))
    return temperatura

def mostar_resultado(orig,conv,ud):
    print(orig)
    print(conv)
    print(ud)
mostar_resultado(3.0, 40, "CF")

c = float(input("¿Cual es la temperatura en celcius?"))
def celcius_a_farenheit(c):
    return (c * 9/5) +32
print(f"el resultado es:{celcius_a_farenheit(c)}")
        
f = float(input("¿Cual es la temeperatura en farenheit?"))
def farenheit_a_celcius(f):
    return(f -32) *5/9
print(f"el resultado es:{farenheit_a_celcius(f)}")
    