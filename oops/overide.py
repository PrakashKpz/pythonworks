class parent:

    vehicles=["pasnpro00","swift"]

    def properties(self):
        return self.vehicles
    
class child(parent):

    def properties(self):
        self.veh=super().properties()
        self.veh.append("hunter")
        return self.veh
    
ch=child()
print(ch.properties())