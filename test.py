class Test:
    def __init__(self):
        self.someAttribute = 'some initial value'

    @property
    def someAttribute(self): 
        print("through the getter!")
        return self._someAttribute

    @someAttribute.setter
    def someAttribute(self, value): # This is the "setter" method.
        self._someAttribute = value
    
    
    
