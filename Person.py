class Person:
    def __init__(self, name, age, adress, children):
        self.name=name
        self.age=age
        self.adress=adress
        self.children=children
    def add_child(self,newchild):
        self.children.append(newchild)
    def print_children_names(self):
       for i in self.children:
         print(i.name)
    def print_details(self):
        print(self.name,self.age,self.address)