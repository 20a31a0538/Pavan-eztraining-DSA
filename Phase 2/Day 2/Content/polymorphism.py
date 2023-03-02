class bhim():
    def placename(self):
        print("bhimavaram ")
    def person(self):
        print("pavan")

class hyd():
    def placename(self):
        print("Hyderabad ")
    def person(self):
        print("prince")

obj_bh =bhim()
obj_hyd =hyd()
for details in (obj_bh,obj_hyd):
    details.placename()   #getting two place names at a time
    details.person()    #getting all persons at a time
