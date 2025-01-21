import numpy as np
import scipy.stats as stats
from scipy.stats import ttest_ind

# 1. Somers' D (Utilisation pour les variables ordinales)
def somers_d(x, y):
    """
    Calcule le Somers' D pour deux variables ordinales.

    Paramètres:
    x (array-like) : Première variable ordinale.
    y (array-like) : Deuxième variable ordinale.

    Retourne:
    float : Valeur de Somers' D.
    """
    result = stats.somersd(x, y)
    return result.statistic

# 2. Test d'Équivalence avec marge définie
def equivalence_test(x, y, alpha=0.05, equivalence_margin=0.2):
    """
    Effectue un test d'équivalence entre deux échantillons indépendants.

    Paramètres:
    x (array-like) : Premier échantillon.
    y (array-like) : Deuxième échantillon.
    alpha (float) : Niveau de signification (par défaut 0.05).
    equivalence_margin (float) : Marge d'équivalence.

    Retourne:
    None
    """
    # Calcul de la différence moyenne entre les deux groupes
    mean_diff = np.mean(x) - np.mean(y)
    
    # Calcul de la statistique du test t et de la p-value
    t_stat, p_value = ttest_ind(x, y)  # On calcule t_stat et p_value
    
    # Affichage de la statistique t et de la p-value
    print(f"Statistique t: {t_stat:.4f}, p-value: {p_value:.4f}")
    
    # Utilisation de alpha pour déterminer si la p-value est significative
    if p_value < alpha:
        print("Les groupes sont statistiquement différents (H0 rejetée).")
    else:
        print("Les groupes ne sont pas statistiquement différents (H0 acceptée).")
    
    # Vérification de l'équivalence si la p-value n'est pas significative
    if -equivalence_margin <= mean_diff <= equivalence_margin:
        print("Les groupes sont équivalents (différence dans la marge d'équivalence).")
    else:
        print("Les groupes ne sont pas équivalents (différence hors marge).")

# 3. Test Kolmogorov-Smirnov (pour tester si deux échantillons suivent la même distribution)
def ks_test(x, y, alpha=0.05):
    """
    Effectue un test Kolmogorov-Smirnov pour comparer deux distributions.

    Paramètres:
    x (array-like) : Premier échantillon.
    y (array-like) : Deuxième échantillon.
    alpha (float) : Niveau de signification (par défaut 0.05).

    Retourne:
    None
    """
    ks_stat, p_value = stats.ks_2samp(x, y)
    print(f"Statistique KS: {ks_stat:.4f}, p-value: {p_value:.4f}")
    if p_value < alpha:
        print("Les distributions sont significativement différentes (H0 rejetée).")
    else:
        print("Les distributions ne sont pas significativement différentes (H0 acceptée).")

# Exemple d'utilisation
np.random.seed(45)

# Données d'exemple (variables ordinales pour Somers' D)
x_ord = np.random.randint(0, 5, size=100)
y_ord = np.random.randint(0, 5, size=100)

# Calcul de Somers' D
print("Somers' D (variables ordinales):", somers_d(x_ord, y_ord))

# Données normales pour les autres tests
x_norm = np.random.normal(loc=0, scale=1, size=100)
y_norm = np.random.normal(loc=0, scale=1, size=100)

# Test d'Équivalence
equivalence_test(x_norm, y_norm, equivalence_margin=0.1)

# Test Kolmogorov-Smirnov
ks_test(x_norm, y_norm)

