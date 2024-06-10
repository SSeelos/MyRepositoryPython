# base class
class MySuperClass:
    mySuperProperty: str = "value"
    def super_function(self):
        raise NotImplementedError()
class MyClass(MySuperClass):
    myDict: dict[int, str] = {1: "A", 2: "B", 3: "C"}
    def __init__(self):
        super.__init__(self)
        raise NotImplementedError("constructor notimplemented")

    def my_function(self) -> None:
        """
        my comment
        :return:
        """
        print("hi from class function" + self.__str__())

    def my_function(self) -> dict[int, str]:
        return self.myDict
    def my_function(self, param: dict[int,str]) -> None:
        print(param)

    # there are no private fcts to define a private method prefix the member name with "__"
    def __my__private_function(self):
        print("hi from private function")

    # raise exception instead of pass
    def not_implemented(self):
        raise NotImplemented("todo")
