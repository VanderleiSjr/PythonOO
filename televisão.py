class Televisao():

    def __init__(self):
        self.ligada = False
        self.canal = 5
        self.volume = 0
    
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def increase_channel(self):
        self.canal += 1

    def increase_sound(self):
        self.canal += 1
    

televisao = Televisao()
televisao.power()

print('Televisão está ligada: {}'.format(televisao.ligada))
print('Canal: {}'.format(televisao.canal))
televisao.increase_channel()
televisao.increase_channel()
print('Canal: {}'.format(televisao.canal))