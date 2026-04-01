def greet_names(names: list[str]) -> list[str]:
    result = []
    for name in names:
        result.append(f"Hello, {name}!")
    return result