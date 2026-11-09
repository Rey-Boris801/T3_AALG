import random
import math

def simulacion_monte_carlo_interseccion():
    print("=== MÉTODO DE MONTE CARLO: INTERSECCIÓN ELIPSE E HIPÉRBOLA ===")
    
    a = float(input("Ingrese el valor de a (elipse): "))
    b = float(input("Ingrese el valor de b (elipse): "))
    c = float(input("Ingrese el valor de c (hipérbola): "))
    d = float(input("Ingrese el valor de d (hipérbola): "))
    cantidad = int(input("Ingrese la cantidad de puntos aleatorios: "))
    
    puntos_elipse = 0
    puntos_interseccion = 0
    

    for _ in range(cantidad):
        x = random.uniform(-a, a)
        y = random.uniform(-b, b)
        
        cond_elipse = (x**2 / a**2) + (y**2 / b**2) <= 1
        
        if cond_elipse:
            puntos_elipse += 1
            
            cond_hiperbola = (x**2 / c**2) - (y**2 / d**2) >= 1
            
            if cond_hiperbola:
                puntos_interseccion += 1
                
    area_elipse_formula = math.pi * a * b
    
    if puntos_elipse > 0:
        area_interseccion_mc = (puntos_interseccion / puntos_elipse) * area_elipse_formula
    else:
        area_interseccion_mc = 0.0

    print("\n================ RESULTADOS ================")
    print(f"1. Puntos aleatorios dentro de la elipse: {puntos_elipse:,}")
    print(f"2. Puntos aleatorios en la intersección (elipse e hipérbola): {puntos_interseccion:,}")
    print(f"3. Área teórica de la elipse: {area_elipse_formula:.4f}")
    print(f"4. Área aproximada de la zona de intersección: {area_interseccion_mc:.4f}")

if __name__ == "__main__":
    simulacion_monte_carlo_interseccion()