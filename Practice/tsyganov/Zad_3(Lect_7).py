import random
import pickle
class Human:

    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
    def __repr__(self):
        res = self.name + ' ' + self.surname
        return res

def serialize(self):
        with open('myfile.py','ab') as f:
            res_ser=pickle.dump(self, f)
            return res_ser

def deserialize():
        with open("myfile.py", 'rb') as f:
                res_des = pickle.load(f)
                return res_des

def zavod(n):
    surname_box=['Lennon','Hendrix','Morrison']
    name_box= ['John','Jimi','Jim']
    res= [Human(random.choice(surname_box),random.choice(name_box)) for x in range(n)]
    return res

serialize(zavod(20))
deserialize()
