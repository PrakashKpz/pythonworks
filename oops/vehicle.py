class bike:

    def start(self):
        print("kicker start")

    def breaking(self):
        print("drum brake")

class ktmduke(bike):
    def start(self):
      print("self start")

    def breaking(self):
         print("abs breaking")

hobj=ktmduke()
hobj.start()
