class parent:
    phone="samsung"
    vehicle="duke"

    def mobile(self):
        print(self.phone)

    def bike(self):
        print(self.vehicle)

class child(parent):
        pass

obj=child()
obj.mobile()
obj.bike()