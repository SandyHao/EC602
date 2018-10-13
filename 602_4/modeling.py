# Copyright 2018 SichunHao sichunh@bu.edu

class Polynomial():
#1.implement a constructor which takes a sequence and assigns the coefficients in the natural (descending order). So Polynomial([4,-9,5.6]) should make 4x2−9x+5.6
#8.implement accessing and modifying the coefficients using []. So p[2] should be the coefficient of x2 and p[8] = 12 should set the coefficent of x8 to 12.倒序
    def __init__(self,value={}):
        self.v = {}
        if isinstance(value,(list,tuple,range)):
            value=value[::-1]
            for i in range(len(value)):
               self.v[i] = value[i]
        elif isinstance(value,dict):
            for key in value:
               self.v[key] = value[key]
        else:
            pass
#-------------------------------------------------------------------
    def __str__(self):
        return str(self.v)
#2.implement addition and subtraction of polynomials using + and -
    def __add__(self,value):
        y={}
        for key in self.v:
            y[key]=self.v[key]
        for key in value.v:
            if key in self.v:
                y[key]=self.v[key]+value.v[key]
            else:
                y[key]=value.v[key]
        return Polynomial(y)
#-----------------------------------------------------------------
    def __sub__(self,value):
        y={}
        for key in self.v:
            y[key]=self.v[key]
        for key in value.v:
            if key in self.v:
                y[key]=self.v[key]-value.v[key]
            else:
                y[key]=-value.v[key]
        return y
#3.implement multiplication of polynomials using *
    def __mul__(self,value):
        y={}
        for key1 in self.v:
            for key2 in value.v:
               y[key1+key2]=0
        for key1 in self.v:
            for key2 in value.v:
               y[key1+key2] += self.v[key1]*value.v[key2]
        return y
#4.implement testing for equality of polynomials using ==
    def __eq__(self,value):
        return self.v == value
#7.implement evaluation of the polynomial using a eval method, like this: p.eval(2.1)   x=2.1
    def eval(self,value):
        y=0
        for key in self.v:
            y += self.v[key]*(value**(key))
        return y
#9.implement a derivative method p.deriv() which returns the derivative of the polynomial.导数
    def deriv(self):
        y={}
        for key in self.v:
            if key!=0:
                y[key-1]=key*self.v[key]
        return y
##set value & get value.........................................
    def __setitem__(self,key,value):
        self.v[key]=value
#----------------------------------------------------------------
    def __getitem__(self,key):
        l=len(self.v)
        if key>l:
            return 0
        else:
            return self.v[key]
##..............................................................
def main():
     "write your test code here"
     pass

if __name__=="__main__":
	main()






