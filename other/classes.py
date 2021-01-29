class myClass():
  def method1(self):
    print("myClass Method1")

  def method2(self, someString):
    print("myClass Method2" + someString)

class anotherClass(myClass):
  def method(self):
    myClass.method1(self)
    print("anotherClass method1")


def main():
    c = myClass()
    c.method1()
    c.method2("hello")
    

main()