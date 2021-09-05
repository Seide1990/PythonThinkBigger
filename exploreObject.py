#[PythonThinkBigger] Aşağıdakı tapşırıqları ayrı ayrı python faylları olaraq yazın
##exploreObject(obj) adında bir metod yazın. Bu metod argument olaraq verilən istənilən obyektin bütün xüsusiyyətlərini
#hansı property-ləri olduğunu və onların value-sunu
#hansı metodlarının olduğunu və nə return etdiyini
class User():
    def __init__(self):
        self.ad= 'Islam'
        self.soyad = 'Serifli'
        self.age = 4

def exploreObject(obj):

       a=type(obj)
       pro_siyahi=[]
       for i in obj:
              pro_siyahi.append(property(i))
       dir_siyahi=[]
       for x in obj:
              gotur=dir(x)
              for i in gotur:
                     if i.startswith('__'):
                          continue
                     else:
                                dir_siyahi.append(i)
                       

       

       return(print('\n return=  ',obj,'  \n tipi=   ',a,' \n xususiyyet=  ',pro_siyahi,' \n dir = ',dir_siyahi))

ARREY=[1,5,7,6,9]
exploreObject(ARREY)     

user=User()
userProperties = vars(user) 
exploreObject(userProperties)



