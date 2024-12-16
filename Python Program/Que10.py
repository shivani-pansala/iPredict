'''Define a class, which have a class parameter and have a same instance parameter.
Hints:
Define a instance parameter, need add it in __init__ method
You can init a object with constructor parameter or set the value later'''

class MyClass:
     def __init__(self, instance_param):
          self.instance_param = instance_param
          self.class_param = 'Class parameter'
         
     def print_values(self):
          print('Instance parameter:', self.instance_param)
          print('Class parameter:', self.class_param)


obj1 = MyClass('Instance parameter 1')

obj1.print_values()

'''Output
Instance parameter 1
Class parameter: Class parameter
'''
  