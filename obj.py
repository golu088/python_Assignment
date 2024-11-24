# object orinted programming /useof class in python
class dog:
    #class atrribute (shared by all instance )
    species = "cnies familiars"

    def __init__(self,name,age):
        #instance atrribute (unique to each  instance)
        self.name=name
        self.age=age
    # instance method
    def bark(self):
        return f"{self.name} say woof"
    #another instance methdoo
    def get_age(self):
        return f"{self.name} is {self.age} years old"

# creating a object of this dog 
dog1 =dog("buddy",3)
dog2 =dog("charlie",5)

print(dog1.bark())
print(dog2.get_age())
print(dog1.species)




# create the class for cat
class cat:
    
    species = "cnies familiars"

    def __init__(self,name,age):
        
        self.name=name
        self.age=age
    
    def meu(self):
        return f"{self.name} say meu"

    def get_age(self):
        return f"{self.name} is {self.age} years old"

 
cat1 =cat("buddy",3)


print(dog1.bark())
print(dog2.get_age())
print(dog1.species)


