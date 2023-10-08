# =============================================================================
# Title             PyHacks - Typing in Python
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      25/10/2022
# Usage:            mypy 33_typing_in_python.py
# =============================================================================
# Basic implementation of types - documenting code
x: str = "Gary" 

# Function annotations
def add_nums(a: int,b: int,c: int) -> int:
    # Arrow indicates return type
    return a + b + c

result = add_nums(10,20,30)
print(result)

# List types
from typing import List
my_list: List[List[int]] = [[1,2,3], [4,5,6]]

# Dictionary types
from typing import Dict
my_dict: Dict[str, str] = {"a":'Gary'}

# Set types
from typing import Set
my_set: Set[str] = {"I", "love", "type", "setting"}
my_bool:Set[bool] = {True, False, True, False}
print(my_set)

# Create custom types

# Example 1 
Vector = List[float]
print(type(Vector))

def vector_test(v:Vector) -> Vector:
    return v

# Example 2
Vectors = List[Vector]

# Special types
# Optional type
from typing import Optional
def optional_foo(output: Optional[bool]=False):
    pass

optional_foo()

# Any type
from typing import Any
def any_foo(output: Any):
    pass

# Sequence types - anything that can be indexed
from typing import Sequence
def seq_foo(seq: Sequence[str]):
    pass

seq_foo(('a', 'b', 'c'))
seq_foo(['a', 'b', 'c'])
seq_foo('This is a sequence as well')

# Tuple type
my_tup: tuple = (1,2,3, "Gary")
print(my_tup)

from typing import Tuple
my_typed_tuple: Tuple[int, int, int, str] = (1,2,3,"Gary")

# Callable type
# Function as a parameter
from typing import Callable

def add(x:int, y:int) -> int:
    return x + y

def call_func(func: Callable[[int, int], int]) -> None:
    func(1,2)

# Do this for a return value
def returnable_foo() -> Callable[[int, int], int]:
    def add_stuff(x:int, y:int) -> int:
        return x + y 
    return add_stuff

returnable_foo()

# Do this for a lambda
def lambda_foo() -> Callable[[int, int], int]:
    func: Callable[[int, int], int] = lambda x, y: x+y+y
    return func

lambda_foo()

# Generics
from typing import TypeVar
T = TypeVar('T')
# Placeholder for a generic type
def get_item(lst: List[T], index:int) -> T:
    return lst[index]

print(get_item([1,2,3], 0))
