from typing import Dict, List, Union, Optional

def add(a: Union[float, int], b: Union[float, int]) -> float:
    return a + b

def foo(x: Dict[str, str]) -> int:
    return len(x)


print(add(2, 3))
# print(add("asdf", "sdsd"))

# foo({1:2})
