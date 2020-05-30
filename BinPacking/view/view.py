from BinPacking.utils.utils import get_input_from_range


class View:
    @staticmethod
    def display_welcome_screen():
        print("This is bin packing problem\n")

    @staticmethod
    def  get_items_from_console():
        print("Enter number of items: ")
        number_of_items = int(input())

        items = []
        for i in range(number_of_items):
            print(f"Enter {i} item: ")
            item = float(input())

            while item <= 0 or item >= 1:
                print(f"Invalid value.Enter {i} item again: ")
                item = float(input())

            items.append(item)

        return items

    @staticmethod
    def get_items(self):
        print("Choose method of uploading data:")
        print("1. Get data from console")
        current_input = get_input_from_range(1,1)

        if current_input == 1:
            return self.get_items_from_console()
