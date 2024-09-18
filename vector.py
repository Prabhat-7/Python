
class vector:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    def format_component(self, value, suffix):
        return {
            (value == 0): "",                  
            (value == 1): suffix,
            (value == -1): f"-{suffix}",
            (value > 1): f"+{value}{suffix}",
            (value < -1): f"{value}{suffix}"#The .get(True) method checks each condition in the dictionary
        }.get(True)                         # and executes the corresponding code for the first True condition.
        

    def __str__(self):
        components = {
            'a': ('i', self.a),
            'b': ('j', self.b),
            'c': ('k', self.c)
        }

        formatted_components = [self.format_component(value, suffix) for suffix, value in components.values()]

        result= "".join(formatted_components)
        if(result.startswith("+")):
           result= result[1:]
        return result
    

    def __add__(self,vect2):
        new_a=self.a+vect2.a    
        new_b=self.b+vect2.b    
        new_c=self.c+vect2.c 
        return vector(new_a,new_b,new_c)  


    def __sub__(self,vect2):
        new_a=self.a-vect2.a    
        new_b=self.b-vect2.b    
        new_c=self.c-vect2.c 
        return vector(new_a,new_b,new_c)
    

    def dot(self,vect2):
        dot_prod=self.a*vect2.a +self.b*vect2.b+self.c*vect2.c
        return dot_prod
    


    @staticmethod
    def detrmt(a,b,c,d):
        return a*d-b*c
    

    def __mul__(self,vect2):
        new_a=vector.detrmt(self.b,self.c,vect2.b,vect2.c)
        new_b=-vector.detrmt(self.a,self.c,vect2.a,vect2.c)
        new_c=vector.detrmt(self.a,self.b,vect2.a,vect2.b)
        return vector(new_a,new_b,new_c)
