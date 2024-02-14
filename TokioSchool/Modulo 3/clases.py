class Galleta():
    
    def __init__(self, sabor=None, forma=None, chocolate=False):
        self.sabor = sabor
        self.forma = forma
        self.chocolate = chocolate
    
    def chocolatear(self):
        self.chocolate = True
        
    def tiene_chocolate(self):
        if (self.chocolate):
            print("Soy una galleta chocolateada :-D")
        else:
            print("Soy una galleta sin chocolate :-(")
            
if __name__ == "__main__":
    g = Galleta("dulce","cuadrada",True)
    print("-------- g1 ----------")
    print(g.sabor, g.forma, g.chocolate)
    g2 = Galleta("salada")
    print("-------- g2 ----------")
    print(g2.sabor, g2.forma, g2.chocolate)