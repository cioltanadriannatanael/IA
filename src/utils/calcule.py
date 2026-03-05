from scipy.spatial.distance import cityblock

def distanta_manhattan_manuala(x: list[float], y: list[float]) -> float:
    """Calculează distanța Manhattan manual între doi vectori.

    Args:
        x (list[float]): Primul vector.
        y (list[float]): Al doilea vector.

    Returns:
        float: Distanța Manhattan calculată manual.
        
    Raises:
        ValueError: Dacă vectorii nu au aceeași lungime.
    """
    if len(x) != len(y):
        raise ValueError("Vectorii trebuie să aibă aceeași dimensiune.")
    
    return sum(abs(a - b) for a, b in zip(x, y))

def distanta_manhattan_scipy(x: list[float], y: list[float]) -> float:
    """Calculează distanța Manhattan utilizând pachetul scipy.

    Args:
        x (list[float]): Primul vector.
        y (list[float]): Al doilea vector.

    Returns:
        float: Distanța Manhattan calculată prin funcția cityblock.
    """
    return cityblock(x, y)