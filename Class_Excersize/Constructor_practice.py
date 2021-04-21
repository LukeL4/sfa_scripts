class Animal(object):
    def __init__(self, sound):
        self.sound = sound

    def vocalize(self):
        print(str(self.sound))

tiger = Animal("roar")
tiger.vocalize()

cat = Animal ("meow")
cat.vocalize()

