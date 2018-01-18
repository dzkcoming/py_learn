#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

'这里是注释信息'

__author__ = 'Dou Zhongkang'

# class 学习

class Student(object):

	def __init__ (self, name, score):
		self.name  = name
		self.score = score

	def print_score (self):
		print ("name : ", self.name, 'score : ', self.score)

douzhk  = Student("douzhk", 10)
zhengli = Student("zhengli", 100)

douzhk.print_score()
zhengli.print_score()

douzhk.age = 24

print (douzhk.age)

# 私有变量
class Persion(object):
	def __init__ (self, sex, age):
		self.__sex = sex
		self.__age = age

	def print_info (self):
		print (self.__sex, self.__age)
		
douzhk  = Persion('male', 24)
zhengli = Persion('male', 26)

douzhk.print_info()
zhengli.print_info()

class Animal(object):
	def run (self):
		print ("animal is runing")

class Dog(Animal):
	def run (self):
		print ("Dog is running");

class Cat(Animal):
	def run (self):
		print ("Cat is running");

dog = Dog()
cat = Cat()

dog.run()
cat.run()

# hasattr getattr setattr

hasattr(dog, 'run')

fn=getattr(dog, 'run')
fn()

if hasattr(dog, 'name') == False:
	setattr(dog, 'name', 'wangcai')

print ('have name ?  ', hasattr(dog, 'name'))
print ('dog\'name : ', getattr(dog, 'name'))

# 类的成员

class Student(object):
	name = 'student'

a = Student()
print (a.name, Student.name)

a.name = 'lala'
print (a.name, Student.name)

del a.name
print (a.name, Student.name)

# 类的多重继承

class Animal(object):
	def live(self):
		print ("Living ...")

class Runable(object):
	def run(self):
		print ("runing ...")
	

class Dog(Animal, Runable):
	def __init__(self):
		self.live()
		self.run()
		print ("Boom, God Create a dog")

	def yell(self):
		print ("汪汪汪...")

class People(Animal, Runable):
	def __init__(self):
		self.live()
		self.run()
		print ("Boom, God Create a person")

	def joke(self):
		print ("HaHa")

dog=Dog()

dog.yell()

print ("dog is animal ? ", isinstance(dog, Animal))
print ("dog can run ? ", isinstance(dog, Runable))

person = People()
person.joke()
print ("dog is People ? ", isinstance(dog, People));
