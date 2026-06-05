class Telefon:
    def __init__(self, model):
        self.__model = model

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

t = Telefon("Samsung")
print(t.get_model())

t.set_model("iPhone")
print(t.get_model())
