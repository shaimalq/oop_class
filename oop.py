class car ():
    def __init__(self , name , model , speed , color , number ,engine_power) :
        self.name = name
        self.model =model
        self.speed = speed
        self.color =color
        self.number= number
        self.engine_power= engine_power


    def info(self):
        print (f"   car {self.name}:\nmodel:{self.model}\nspeed:{self.speed}km/h\number:{self.number} \ncolor:{self.color}\nengine_power:{self.engine_power}")  
car1= car("range rover","2018","340" ," black","3","4400cc")
car2= car("lamborguini","2015","340" ," black","3","4400cc")
 
car1.info()
car2.info()
      