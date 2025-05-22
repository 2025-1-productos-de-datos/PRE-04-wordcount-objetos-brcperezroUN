import sys


class ParseArgsMixin:
    def parse_arges(self):
        if len(sys.argv) != 3:
            print("Usage: Python -m homework <input_folder> <output_folder>")
            sys.exit(1)

        self.input_folder = sys.argv[1]
        self.output_folder = sys.argv[2]
