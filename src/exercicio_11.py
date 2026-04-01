def modify_guest_list(
    guests: list[str],
    unavailable: str,
    new_guest: str
) -> list[str]:
    """
    Substitui um convidado indisponível por outro.
    """
    return [new_guest if guest == unavailable else guest for guest in guests]