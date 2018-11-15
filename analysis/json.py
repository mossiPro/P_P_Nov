import os  # nous servir à interagir avec OS


def lunch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__))
    path_to_file = os.path.join(directory, "data", data_file)
    with open(path_to_file, 'r') as file:
        preview = file.readline()
    print("Voilà, First line of our file is: {}".format(preview))


def main():
    lunch_analysis("dataset_#Marvel_35000.json")


if __name__ == "__main__":
    main()
