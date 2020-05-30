import random

from BinPacking.utils.utils import get_input_from_range
from BinPacking.algorithms.brutal_bin_packing import brutal_bin_packing
from BinPacking.algorithms.first_fit_bin_packing import first_fit_bin_packing

class View:
    @staticmethod
    def display_welcome_screen():
        print("This is bin packing problem\n")

    @staticmethod
    def get_items_from_console():
        print("Enter number of items: ")
        number_of_items = int(input())

        items = []
        for i in range(number_of_items):
            print(f"Enter {i + 1} item: ")
            item = float(input())

            while item <= 0 or item > 1:
                print(f"Invalid value.Enter {i + 1} item again: ")
                item = float(input())

            items.append(item)

        return items

    @staticmethod
    def random_items():
        random.seed()
        print("Enter number of items: ")
        number_of_items = int(input())

        items = []

        for i in range(number_of_items):
            item = random.random()
            items.append(item)

        return items

    @staticmethod
    def get_items(self):
        print("Choose method of uploading data:")
        print("1. Get data from console")
        print("2. Test for amount of random data")
        current_input = get_input_from_range(1, 2)

        if current_input == 1:
            return self.get_items_from_console()
        if current_input == 2:
            return self.random_items()

    @staticmethod
    def print_result(result):
        print(f"Result for {result.algorithm_type}")
        print(f"Algorithm was computing: {result.time}")
        print(f"Items amount: {result.items}")
        print(f"Minimal boxes amount: {result.boxes}\n")

    @staticmethod
    def pack_items(self, items):
        print("Choose algorithm:")
        print("1. Brutal algorithm")
        print("2. First algorithm")
        print("3. Both algorithms")
        current_input = get_input_from_range(1, 3)

        if current_input == 1:
            print("1. Brutal algorithm is computing")
            self.print_result(brutal_bin_packing(items))
        if current_input == 2:
            print("1. First fit algorithm is computing")
            self.print_result(first_fit_bin_packing(items))
        if current_input == 3:
            print("1. Brutal algorithm is computing")
            self.print_result(brutal_bin_packing(items))
            print("1. First fit algorithm is computing")
            self.print_result(first_fit_bin_packing(items))