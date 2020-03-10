from vector import Vector

if __name__ == "__main__":
    #test1 = Vector(-1)
    #print(test1)
    v1 = Vector((10, 15))
    v1b = Vector ((0, 5))
   # v2 = v1 + 4
    #print("V1 = ", v1, "V1bis = ", v1b)
    v3 = v1 + v1b
    print("ICI", v3.__str__())
    #test2.display()
    #test3 = Vector([0.0, 1.0, 2.0, 3.0, 40])
    #test3.display()


"""class Met(object):
 
    def __init__(self, nom):
        self.nom = nom
 
    def __str__(self):
        return self.nom
    
    def __add__(self, other):
            Override l'opérateur 
        print(other)
        return Met(str(self) + ' et ' + str(other))
 
    def __sub__(self, other):
            Override l'opérateur 
        return Met(str(self) + ' sans ' + str(other))
 
    def __mul__(self, other):
            Override l'opérateur 
        return Met(str(self) + ' avec plein de ' + str(other))
 
    def __truediv__(self, other):
            Override l'opérateur 
        return Met(str(self) + ' avec très peu de ' + str(other))
 
    def __mod__(self, other):
            Override l'opérateur 
        return Met(str(self) + ' servi dans ' + str(other))
 
    def __pow__(self, other):
            Override l'opérateur **
        return Met(str(self) + ' relevé avec ' + str(other))
 
    def __lshift__(self, other):
            Override l'opérateur <<
        return Met(str(self) + ' après ' + str(other))
 
    def __and__(self, other):
        
            Override l'opérateur &
        
        return  Met(str(self) + ' accompagné de ' + str(other))
 
    def __or__(self, other):
        
            Override l'opérateur |
        
        return Met(str(self) + ' à la place de ' + str(other))


    def __pr__(self):
        print("coucou")
    

 
 
plat = Met('Canard laqué') + Met('son fond de volaille')
# plat2 = plat - (Met('vinaigrette')) * Met('frites') / Met('sel') ** Met('du piment') << Met('une entrée de chorizo')
#plat2 = plat2 
print(plat)
#Met.__pr__()"""