class Penguin():
    def __init__(self):
        pass

    def animal(self):
        print("Penguin")

    def hi(self):
        print("Penguin says hi.")

class pappu(Penguin):
    def __init__(self):
        super().__init__()
        pass

    def hi(self):
        print('pappu says hi.')


a=pappu()
pappu.animal(pappu)
pappu.hi(pappu)

            