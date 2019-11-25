
class Numery():
    def __init__(self,numer):
        
        numer= str(numer)
        self.numer=numer
        self.slownik_cyfr = {"0":'zero', "1":'jeden', "2":'dwa', "3":'trzy', "4":'cztery',
                                 "5":'pięć', "6":'sześć', "7":'siedem', "8":'osiem', "9":'dziewięć'}
        self.slownik_kodow = {"42":"Łódź", "62":"Kolo"}
     
        if len(numer)==9  :
            print("Numer jest poprawny")
            if self.numer[:2] in self.slownik_kodow:
                print("Podany numer jest z " + self.slownik_kodow[self.numer[:2]])
            else:
                print ("Podany numer jest numerem komorkowym")
        else:
            print("Podales zly numer")
 
        slownie=""
        for i in self.numer:
            slownie+= (self.slownik_cyfr[i]+" ")
        print(slownie)
     

           
numer=Numery(622656251)
