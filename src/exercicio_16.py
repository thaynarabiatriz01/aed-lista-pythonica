def odd_numbers(n: int) -> list[int]:
    """
    Retorna os números ímpares de 1 até n.
    """
    return [i for i in range(1, n + 1) if i % 2 != 0]