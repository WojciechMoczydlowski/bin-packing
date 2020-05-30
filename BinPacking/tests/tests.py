# Wojciech Moczydlowski bin packing problem
import math

from BinPacking.algorithms.brutal_bin_packing import brutal_bin_packing
from BinPacking.algorithms.first_fit_bin_packing import first_fit_bin_packing
from BinPacking.dataController.data import DataController
from BinPacking.view.view import View

BRUTAL_C = 0.00000023
FIRST_FIT_C = 0.000000065

class Tests:
    def __init__(self):
        self.dataController = DataController()
        self.view = View()

    def test_algorithms(self, test_type, algorithm_type):
        if test_type == 1:
            self.console_test(algorithm_type)
        elif test_type == 2:
            self.random_test(algorithm_type)
        else:
            self.complexity_test(algorithm_type)

    def console_test(self, algorithm_type):
        items = self.dataController.get_items_from_console()
        self.correctness_test(algorithm_type, items)

    def random_test(self, algorithm_type):
        items = self.dataController.rand_items()
        print(f"items: {items}")
        self.correctness_test(algorithm_type, items)

    def correctness_test(self, algorithm_type, items):
        if algorithm_type == 1:
            result = brutal_bin_packing(items)
            self.view.print_result(result)

        if algorithm_type == 2:
            result = first_fit_bin_packing(items)
            self.view.print_result(result)

        if algorithm_type == 3:
            result = brutal_bin_packing(items)
            self.view.print_result(result)

            first_fit_result = first_fit_bin_packing(items)
            self.view.print_result(first_fit_result)

    def complexity_test(self, algorithm_type):
        if algorithm_type == 1:
            self.brutal_complexity_test()
        if algorithm_type == 2:
            self.first_fit_complexity_test()
        if algorithm_type == 3:
            self.brutal_complexity_test()
            self.first_fit_complexity_test()

    def brutal_complexity_test(self):
        step = 1
        print("Brutal algorithm for 10 sets of items")
        for itemsAmount in range(1, 11, step):
            items_for_algorithm = self.dataController.rand_items_for_complexity(itemsAmount)
            result = brutal_bin_packing(items_for_algorithm)

            time = result.time
            items = result.items
            q = time / (items * math.factorial(items) * BRUTAL_C)

            self.view.print_complexity_results(items, result.time, q)

    def first_fit_complexity_test(self):
        step = 1000
        print("First fit algorithm for 15 sets of items")

        for itemsAmount in range(1000, 16000, step):
            items_for_algorithm = self.dataController.rand_items_for_complexity(itemsAmount)
            result = first_fit_bin_packing(items_for_algorithm)

            items = result.items
            time = result.time
            q = time / ((items - 1) * 1/2 * items * FIRST_FIT_C )
            self.view.print_complexity_results(items, time, q)
