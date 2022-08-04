frases=["Los lunes son los mejores dias para programar", "Python es moderno", "Veremos inteligencia artificial más adelante", "Lambda simplifica el código"]

frases.sort(reverse=True, key=lambda f: len(f.split()))  
    
print(frases)    