#!/usr/bin/env python3

class Animal(object):
   owner = 'jack'
   def __init__(self,name):
       self._name = name
   def get_name(self):
       return self._name
#   def set_name(self,value):
#       self._name = value
   @property
   def name(self):
       return self._name
   @name.setter
   def name(self,value):
       self._name = value
   def make_sound(self):
       pass
   @classmethod
   def get_owner(cls):
       return cls.owner
   @staticmethod
   def order_animal_food():
       print('ording...')
       print('OK')

class Cat(Animal):
   def make_sound(self):
       print(self.get_name() + ' is making sound miu miu miu...')


class Dog(Animal):
   def make_sound(self):
       print(self.get_name() + ' is making sound wang wang wang...')

dog = Dog('wangcai')
cat = Cat('Kittty')
print(cat.name)

dog.make_sound()
cat.make_sound()

print(Animal.get_owner())
print(Cat.get_owner())

Animal.order_animal_food()

animals = [Dog('wangcai'),Cat('Kitty'),Dog('laifu'),Cat('Berry')]

for animal in animals:
    animal.make_sound()
