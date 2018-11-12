# pylint: disable=c0111
import numpy as np

from nbautoeval.exercise_function import ExerciseFunctionNumpy
from nbautoeval.args import Args


# @BEG@ name=checkers
def checkers(size, corner_0_0=True):
    """
    Un damier
    le coin (0, 0) vaut 1 ou 0 selon corner_0_0
    se souvenir que False == 0 et True == 1
    """
    # disons pour fixer les idées que 0=blanc et noir=1
    # on crée un tableau d'entiers
    # par défaut tout est blanc
    result = np.zeros(shape=(size, size), dtype=int)
    # on remplit les cases blanches en deux fois
    # avec un slicing astucieux; c'est le ::2 qui fait le travail
    result[1::2, 0::2] = 1
    result[0::2, 1::2] = 1
    # on renverse si corner_0_0 est False
    if corner_0_0:
        result = 1 - result
    return result
# @END@


# faux parce qu'on ignore corner_0_0
# voir aussi si la correction est contente avec des float
def checkers_ko(size, ignored=True):
    result = np.ones(shape=(size, size), dtype=float)
    # on remplit les cases blanches en deux fois
    result[1::2, 0::2] = 0
    result[0::2, 1::2] = 0
    return result


checkers_inputs = [
    Args(3),
    Args(3, False),
    Args(1),
    Args(2),
    Args(4),
]


exo_checkers = ExerciseFunctionNumpy(
    checkers,
    checkers_inputs,
    nb_examples=2,
    )
