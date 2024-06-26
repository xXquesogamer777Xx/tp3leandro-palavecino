
frutas = ("manzana", "banana", "cereza", "durazno", "kiwi")

print("Frutas encontradas:", frutas)


coordenadas_lago = (35.123, -118.456)


print("Coordenadas del lago:", coordenadas_lago)
def cartesianas_a_polares(x, y):
    
    r = math.hypot(x, y)
    
  
    theta = math.atan2(y, x)
    
   
    theta_grados = math.degrees(theta)
    
    return r, theta_grados


x = 3
y = 4
r, theta_grados = cartesianas_a_polares(x, y)
print(f"Coordenadas cartesianas: ({x}, {y})")
print(f"Coordenadas polares: (r={r}, θ={theta_grados}°)")
