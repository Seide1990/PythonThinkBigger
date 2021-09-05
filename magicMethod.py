#magicMethod(param) adında bir metod yazın.Bu ele bir metod olsun ki argument olaraq verilən param
#arraydirsə onun içindəki bütün elementləri ekrana çap elesin
#obyektdirsə onun properylerini ekrana cap etsin
#rəqəmdirsə kvadratını ekrana çap etsin
#stringdirsə cüt yerdə duran hərfləri böyük hərfə çevirsin

def magicMethod(param):
    a=type(param)
    if a==list:
       return param
    elif a==type:

       return property(param),dir(param)
    elif a==int:
        return param*param
    elif a==str:
        boyut=param[0]
        for i in range(1,len(param)):
            if i%2==0:
             boyut=boyut+param[i].upper()
           
            else:
               boyut=boyut+param[i]
        return boyut
        
obj=[1,3,5,7]
print(magicMethod(obj))
obj="salamazerbaycan"
print(magicMethod(obj))
obj=list
print(magicMethod(obj))
obj=25
print(magicMethod(obj))