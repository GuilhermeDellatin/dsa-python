"""Insertion sort (CLRS, seção 2.1)."""

from collections.abc import MutableSequence
from typing import Any


def insertion_sort[T: Any](items: MutableSequence[T]) -> MutableSequence[T]:
    """Ordena `items` in-place em ordem crescente e retorna a mesma sequência.

    Tempo: O(n²) no pior caso, O(n) no melhor caso (já ordenada).
    Espaço: O(1) extra. Estável.
    """
    for j in range(1, len(items)):
        key = items[j]
        i = j - 1
        while i >= 0 and items[i] > key:
            items[i + 1] = items[i]
            i -= 1
        items[i + 1] = key
    return items
