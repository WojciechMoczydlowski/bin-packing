# Wojciech Moczydlowski bin packing problem

import math
from BinPacking.utils.utils import get_input_from_range





class View:


    @staticmethod
    def display_welcome_screen():
        print("This is bin packing problem\n")

    @staticmethod
    def get_test_type():
        print("Choose testing method")
        print("1. Test for data from console")
        print("2. Test for amount of random data")
        print("3. Automatic test for computational complexity")
        test_type = get_input_from_range(1, 3)

        return test_type

    @staticmethod
    def get_algorithm_type():
        print("Choose algorithm for testing")
        print("1. Brutal algorithm")
        print("2. First algorithm")
        print("3. Both algorithms")
        algorithm_type = get_input_from_range(1, 3)

        return algorithm_type

    @staticmethod
    def print_result(result):
        print(f"Result for {result.algorithm_type}")
        print(f"Algorithm was computing: {result.time}")
        print(f"Items amount: {result.items}")
        print(f"Minimal boxes amount: {result.boxes}\n")

    @staticmethod
    def print_complexity_results( items, time, q):
        print(f"{items} {time} {q}")
