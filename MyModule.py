def my_static_function(self) -> None:
    """
    my comment
    """
    print("hi from static function")

# * forces caller to use keyword parameters for all following params
def force_keyword_args(*, param_a, param_b):
    print(param_a, param_b)

def join(*strings, separator: str) -> str:
    return separator.join(strings)
