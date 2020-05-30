# Wojciech Moczydlowski bin packing problem
import random


class DataController:

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
    def rand_items():
        random.seed()
        print("Enter number of items: ")
        number_of_items = int(input())

        items = []

        for i in range(number_of_items):
            item = random.random()
            items.append(item)

        return items

    @staticmethod
    def rand_items_for_complexity(items_amount):
        items = []

        for i in range(items_amount):
            item = random.random()
            items.append(item)

        return items

