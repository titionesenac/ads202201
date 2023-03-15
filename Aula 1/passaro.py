class Passaro:

    def intro(self):
        print("Existem muitos tipos de pássaros.")

    def voar(self):
        print("A maioria dos pássaros pode voar, outros não.")


class Pardal(Passaro):

    def voar(self):
        print("Pardais voam.")


class Avestruz(Passaro):

    def voar(self):
        print("Avestruzes não voam.")


obj_passaro = Passaro()
obj_pardal = Pardal()
obj_avestruz = Avestruz()

obj_passaro.intro()
obj_passaro.voar()

obj_pardal.intro()
obj_pardal.voar()

obj_avestruz.intro()
obj_avestruz.voar()


