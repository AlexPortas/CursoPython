# + ->suma, - -> resta, * -> multiplicación, / -> división flotante, // -> división entera, % -> módulo de una división, ** -> potencia

print(2 * 4 - (7 - 2) / 4 + 1, 5 / 4, 7 // 3, 2**10)

# = -> asignación simple, += -> suma, -= -> resta, *= -> multiplicación, **= -> exponente
# /= -> división flotante, //= -> división entera, %= -> módulo


# == -> igual a, != -> distinto de, < -> menor que, <= -> menor o igual que, > -> mayor que, >= -> mayor o igual que

# and -> AND (conjunción lógica), or -> OR (disyunción lógica), not -> NOT (negación lógica)

# Prioridad: paréntesis, las expresiones aritméticas, las expresiones relacionales (comparación), las expresiones lógicas

print(type(54), type(5.4), type(5-4j), type('54'))

print(isinstance(5, float), isinstance(5, int))

#casting

cadena = str(4)
print(cadena, type(cadena))
cadena = int("12345")
print(cadena, type(cadena))
cadena = float(4)
print(cadena, type(cadena))
cadena = complex(4) 
print(cadena, type(cadena))