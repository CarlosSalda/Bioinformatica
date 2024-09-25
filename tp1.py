import random;

aminoacids_dict = {
    "Glu": {"alpha": 1.59, "beta": 0.52, "loop": 1.01},
    "Ala": {"alpha": 1.41, "beta": 0.72, "loop": 0.82},
    "Leu": {"alpha": 1.34, "beta": 1.22, "loop": 0.83},
    "Met": {"alpha": 1.30, "beta": 1.14, "loop": 0.67},
    "Gln": {"alpha": 1.27, "beta": 0.98, "loop": 1.10},
    "Lys": {"alpha": 1.23, "beta": 0.69, "loop": 0.97},
    "Arg": {"alpha": 1.21, "beta": 0.84, "loop": 0.90},
    "His": {"alpha": 1.05, "beta": 0.80, "loop": 0.81},
    "Val": {"alpha": 0.90, "beta": 1.87, "loop": 0.41},
    "Ile": {"alpha": 1.00, "beta": 1.67, "loop": 0.47},
    "Tyr": {"alpha": 0.74, "beta": 1.45, "loop": 0.76},
    "Cys": {"alpha": 0.79, "beta": 1.30, "loop": 1.19},
    "Trp": {"alpha": 1.02, "beta": 1.35, "loop": 0.59},
    "Phe": {"alpha": 1.12, "beta": 1.30, "loop": 0.59},
    "Thr": {"alpha": 0.76, "beta": 1.17, "loop": 0.90},
    "Gly": {"alpha": 0.43, "beta": 0.58, "loop": 1.77},
    "Asn": {"alpha": 0.67, "beta": 0.76, "loop": 1.56},
    "Pro": {"alpha": 0.34, "beta": 0.31, "loop": 1.32},
    "Ser": {"alpha": 0.57, "beta": 0.77, "loop": 1.32},
    "Asp": {"alpha": 0.99, "beta": 0.39, "loop": 1.24}
}

def perform_random_action_for_aminoacid(aminoacid_data):
    # Extraemos valores de probabilidad de cada aminoácido
    alpha_prob = aminoacid_data['alpha']
    beta_prob = aminoacid_data['beta']
    loop_prob = aminoacid_data['loop']
    
    # Calculamos la suma de las probabilidades
    total_prob = alpha_prob + beta_prob + loop_prob
    
    # Normalizamos las probabilidades
    # Realmente la normalizacion loop no se considera, pero se incluye para ilustrar la idea
    normalized_alpha = alpha_prob / total_prob
    normalized_beta = beta_prob / total_prob
    normalized_loop = loop_prob / total_prob
    
    # Generamos un valor random entre 0 y 1
    random_number = random.random()
    
    # Se compara el valor random con las probabilidades normalizadas y se toma la acción correspondiente
    if random_number <= normalized_alpha:
        return "H"
    elif random_number <= normalized_alpha + normalized_beta:
        return "B"
    else:
        return "L"

def predict_structure(aminoacid):
    if aminoacid in aminoacids_dict:
        aminoacid = aminoacids_dict[aminoacid]
        return perform_random_action_for_aminoacid(aminoacid)
    else:
        print(f"Unknown amino acid: {aminoacid}")
        return
sequence = ["Glu", "Ala", "Asp", "Val"]

# Predicción de la estructura secundaria para cada aminoácido
possible_structure = [predict_structure(aminoacid) for aminoacid in sequence]
print(f"Secuencia: {'-'.join(sequence)}")
print(f"Estructura Posible: {'-'.join(possible_structure)}")