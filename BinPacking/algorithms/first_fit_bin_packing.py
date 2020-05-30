import time

from BinPacking.algorithms.result import AlgorithmResult


def first_fit_bin_packing(items):

    algorithm_start = time.time()

    boxes = []

    for item in items:
        if len(boxes) == 0:
            boxes.append(0)

        item_is_packed = False

        for i in range(len(boxes) - 1):
            if boxes[i] + item <= 1:
                boxes[i] += item
                item_is_packed = True
                break

        if not item_is_packed:
            boxes.append(item)

    algorithm_end = time.time()

    algorithm_time = algorithm_end - algorithm_start

    result = AlgorithmResult("first fit algorithm", len(items), len(boxes), algorithm_time)

    return result
