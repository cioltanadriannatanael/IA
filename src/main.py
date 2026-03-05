from utils.calcule import distanta_manhattan_manuala, distanta_manhattan_scipy

def citeste_vectori(nume_fisier: str) -> tuple[list[float], list[float]]:
    """Citește doi vectori din fișierul de intrare."""
    with open(nume_fisier, 'r') as f:
        linii = f.readlines()
        v1 = [float(val.strip()) for val in linii[0].split(',')]
        v2 = [float(val.strip()) for val in linii[1].split(',')]
    return v1, v2

if __name__ == "__main__":
    fisier = "../input.txt"
    
    try:
        vector_X, vector_Y = citeste_vectori(fisier)
        print(f"Vector X: {vector_X}")
        print(f"Vector Y: {vector_Y}")
        
        dist_manuala = distanta_manhattan_manuala(vector_X, vector_Y)
        print(f"Distanța Manhattan (Calcul manual): {dist_manuala}")
        
        dist_scipy = distanta_manhattan_scipy(vector_X, vector_Y)
        print(f"Distanța Manhattan (Scipy cityblock): {dist_scipy}")
        
    except FileNotFoundError:
        print(f"Eroare: Fișierul '{fisier}' nu a fost găsit.")
    except Exception as e:
        print(f"A apărut o eroare: {e}")