




class Tab:
    def __init__(self,t):
        self.t = t
    def __str__(self):
        mA = 0
        mB = 0
        mC = 0
        nA = 0
        nB = 0
        nC = 0
        for i,v in enumerate(self.t):
            if isinstance (v,B):
                mB += v.m1() 
                nB += 1
            elif isinstance(v,C):
                mC += v.m1() 
                nC += 1
            else : 
                mA += v.m1()
                nA += 1
        return ("A: ({},{})\nB: ({},{})\nC: ({},{})".format(nA,mA,nB,mB,nC,mC))     
        
        
                
                
        
    
class A:
    def __init__(self,a):
    
        self.__a = a
    def m1(self):
        return self.a
    @property
    def a(self):
        return self.__a 
    @a.setter
    def a(self,a):
        self.__a = a
    
class B(A):
    def __init__(self,a,b):
        super().__init__(a)
        self.__a = a
        self.__b = b
    def m1 (self):
        return self.b + self.a
    @property
    def b(self):
        return self.__b
    @b.setter
    def b(self,b):
        self.__b = b
    
class C(A):
    def __init__(self,a,c):
        super().__init__(a)
        self.__a = a
        self.__c = c
    def m1(self):
        return self.c + self.a
    @property
    def c(self):
        return self.__c
    @c.setter
    def c(self,c):
        self.__c = c
        
        
        
choix = [2,1,1,0,1,1,0,2,0,2,2,1,0,0,2,2,2,2,2,0] 
vA = [-3,-5,0,4,0,2,1,-1,-4,2,-5,1,-3,2,-4,-4,2,-3,-3,1]
vB = [-1,3,2,0,4,2,2,5,4,-1,-5,1,-3,1,-3,0,-4,-4,0,-3]
vC = [-5,4,-4,2,-2,3,1,4,4,-5,-1,4,1,5,5,-3,-2,-2,-3,-5]

tab = []
for i,c in enumerate(choix):
    if c == 0:
        tab.append(A(vA[i]))
    if c == 1:
        tab.append(B(vA[i],vB[i]))
    if c == 2:
        tab.append(C(vA[i],vC[i]))
        

TAB = Tab(tab)
    
print(TAB)
    
    
