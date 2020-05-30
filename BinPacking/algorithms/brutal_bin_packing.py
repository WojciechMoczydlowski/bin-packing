# Wojciech Moczydlowski bin packing problem

import itertools
import math
import time
from BinPacking.algorithms.result import AlgorithmResult


def brutal_bin_packing(items):
    if len(items) == 0:
        return AlgorithmResult("brutal bin packing", len(items), 0, 0)

    items_permutations = itertools.permutations(items)
    minimal_boxes_amount = math.inf

    algorithm_start = time.time()

    for permutation in items_permutations:
        boxes_amount = boxes_amount_for_permutation(permutation)
        if boxes_amount < minimal_boxes_amount:
            minimal_boxes_amount = boxes_amount

    algorithm_end = time.time()

    algorithm_time = algorithm_end - algorithm_start

    result = AlgorithmResult("brutal algorithm", len(items), minimal_boxes_amount, algorithm_time)

    return result


def boxes_amount_for_permutation(permutation):
    boxes_amount = 0
    degree_of_filling = float(0)

    for item in permutation:
        if boxes_amount == 0:
            boxes_amount = 1
            degree_of_filling = 0

        if degree_of_filling + item <= 1:
            degree_of_filling = degree_of_filling + item
        else:
            boxes_amount = boxes_amount + 1
            degree_of_filling = item

    return boxes_amount
