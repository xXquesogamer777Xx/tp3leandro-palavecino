facil

suma_total= sum (monedas)
promedio = suma_total / len (monedas) if monedas else 0
return suma_total, promedio, moneda_mas_valiosa


monedas = [10, 20, 5, 50, 100]
suma_total, promedio, moneda_mas_valiosa = analizar_monedas(monedas)
print(f"Suma total: {suma_total}")
print(f"Promedio: {promedio}")
print(f"Moneda más valiosa: {moneda_mas_valiosa}")

intermedio

def eliminar_duplicados(cristales):
    
    cristales_unicos = list(set(cristales))
    return cristales_unicos


cristales = ['rubí', 'zafiro', 'esmeralda', 'diamante', 'rubí', 'esmeralda']
cristales_unicos = eliminar_duplicados(cristales)
print(f"Cristales únicos: {cristales_unicos}")

dificil

def monedas_comunes(cofre1, cofre2):
   
    comunes = list(set(cofre1) & set(cofre2))
    return comunes


cofre1 = [10, 20, 30, 40, 50]
cofre2 = [30, 40, 50, 60, 70]
monedas_comunes_en_cofres = monedas_comunes(cofre1, cofre2)
print(f"Monedas comunes en ambos cofres: {monedas_comunes_en_cofres}")
