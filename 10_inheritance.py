class Parent():
    def __init__(self, last_name, eye_color, skin_shade):
        print("welcome in Parent constructor")
        self.last_name = last_name
        self.eye_color = eye_color
        self.skin_shade = skin_shade

    def show_info(self):
        print("Parent Method")
        print("last name:" + self.last_name)
        print('Eye color:' + self.eye_color)
        print('Skin Shade:' + self.skin_shade)      

# inherit from Parent class
class Child(Parent):
    def __init__(self, last_name, eye_color, skin_shade, number_of_toys, hair_type):
        print("welcome in Child Constructor")
        Parent.__init__(self, last_name, eye_color, skin_shade)
        self.number_of_toys = number_of_toys
        self.hair_type = hair_type

    def show_info(self):
        print("Method Overriding...")
        print("last name:" + self.last_name)
        print('Eye color:' + self.eye_color)
        print('Skin Shade:' + self.skin_shade)
        print('Number of toys:' + str(self.number_of_toys))                # convert no to string using str()
        print('Hair Type:' + self.hair_type) 

sobhit = Child("Kumar", "brown", "dark", 5, "brown")
sobhit.show_info()
    
        
