from BinPacking.view.view import View


def main():
    view = View()

    items = view.get_items(view)

    view.pack_items(view, items)


if __name__ == "__main__":
    main()