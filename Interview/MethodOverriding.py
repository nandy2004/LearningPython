class Family:
    def Elderdaughter(self):
        self.name="Nandhini"
        self.about="Have to carry all the responsibilities on her sholder"
        print("In every family elder daugter {0}-{1}".format(self.about,self.name))
class Family1(Family):
    def Elderdaughter(self):
        self.name="Sagarila"
        self.about="Have to carry all the responsibilities on her sholder"
        print("In every family elder daugter {0}-{1}".format(self.about,self.name))
parents=Family()
parents.Elderdaughter()
parent=Family1()
parent.Elderdaughter()
