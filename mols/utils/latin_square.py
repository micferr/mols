from typing import List

from mols.structures.square import Square

def all_distinct(elements: List[int]) -> bool:
    return len(set(elements)) == len(elements)

