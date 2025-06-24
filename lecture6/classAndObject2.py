# Private function
class Person:
    __name = "Anonymous"

    def __hello(self):
        print("Hello from Private function!!")

    def welcome(self):
        self.__hello() # Private function can only be called inside any other public function. We don't directly called that private function!!

p1 = Person()
print(p1.welcome())
