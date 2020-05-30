# Wojciech Moczydlowski bin packing problem

from BinPacking.utils.utils import get_input_from_range
from BinPacking.algorithms.brutal_bin_packing import brutal_bin_packing
from BinPacking.algorithms.first_fit_bin_packing import first_fit_bin_packing
from BinPacking.dataController.data import DataController


class View:

    def __init__(self):
        self.dataController = DataController()

    @staticmethod
    def display_welcome_screen():
        print("This is bin packing problem\n")

    @staticmethod
    def get_items(self):
        print("Choose method of uploading dataController:")
        print("1. Get dataController from console")
        print("2. Test for amount of random dataController")
        current_input = get_input_from_range(1, 2)

        if current_input == 1:
            return self.dataController.get_items_from_console()
        if current_input == 2:
            return self.dataController.rand_items()

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