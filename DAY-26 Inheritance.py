#3.Multi-level---->This occurs when a class inherits from a child class, creating a grandparent---> Parent--->child in this structure
'''
class GrandParent:
    def Show_GrandParent(self):
        print("I'm GrandParent")
class Parent(GrandParent):
    def Show_Parent(self):
        print("I'm Parent")
class child(Parent):
    def Show_child(self):
        print("I'm child")
any = child()
any.Show_GrandParent()
any.Show_Parent()
any.Show_child()
'''

'''
class mobile:
    def basic_features(self):
        print("Can make calls and send messages")
class smartphone(mobile):
    def smart_features(self):
        print("Can use apps and access internet")
class androidphone(smartphone):
    def android_features(self):
        print("Runs on android OS with Google services")
phone = androidphone()
phone.basic_features()
phone.smart_features()
phone.android_features()
'''

#4.Hierarchical---->This occurs when multiple child classes inherit from a single parent class, this process is called hierarchical
'''
class Parent:
    def Parent_(self):
        print("I am Parent")
class child_1(Parent):
    def child_(self):
        print("I am 1st child")
class child_2(Parent):
    def _child(self):
        print("I am 2nd child")
class child_3(child_1, child_2):
    def child(self):
        print("I am the child")
thing = child_3()
thing.Parent_()
thing.child_()
thing._child()
thing.child()
'''

#5.Hybrid Inheritance----> This is a combination of two or more types of inheritance, such as single multiple, multi-level,
#or hierarchical all this in a single class
'''
class GrandParent:
    def Show_GrandParent(self):
        print("I'm GrandParent")
class Parent(GrandParent):
    def Show_Parent(self):
        print("I'm Parent")
class child(Parent):
    def Show_child(self):
        print("I'm child")
any = child()
any.Show_GrandParent()
any.Show_Parent()
any.Show_child()
class Parent:
    def Parent_(self):
        print("I am Parent")
class child_1(Parent):
    def child_(self):
        print("I am 1st child")
class child_2(Parent):
    def _child(self):
        print("I am 2nd child")
class child_3(child_1, child_2, GrandParent):
    def child(self):
        print("I am inherited from Grandparent class and child_1, child_2")
thing = child_3()
thing.Show_GrandParent()
thing.Parent_()
thing.child_()
thing._child()
thing.child()
'''


