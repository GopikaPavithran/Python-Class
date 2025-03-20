class Encapsulation:
    def example(self,name,salary,address):
        self.name=name         # public data member
        self.__salary=salary   # private data member ( add double underscore)
        self._address=address  # protected data member ( add single underscore)

                # Access modifiers are also applicable for functions