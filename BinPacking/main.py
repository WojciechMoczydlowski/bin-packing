# Wojciech Moczydlowski bin packing problem

from BinPacking.view.view import View
from BinPacking.tests.tests import Tests

def main():
    view = View()
    tests = Tests()

    view.display_welcome_screen()

    test_type = view.get_test_type()
    algorithm_type = view.get_algorithm_type()

    tests.test_algorithms(test_type, algorithm_type)


if __name__ == "__main__":
    main()