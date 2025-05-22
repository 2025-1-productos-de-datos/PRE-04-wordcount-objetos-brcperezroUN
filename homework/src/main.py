import argparse


class ArgumentParser:
    def __init__(self):
        self.input = None
        self.output = None

    def run(self):
        parser = argparse.ArgumentParser(description="Count words in files")

        parser.add_argument("input", type=str, help="Path to the input folder")
        parser.add_argument("output", type=str, help="Path to the output folder")

        parsed_args = parser.parse_args()

        self.input = parsed_args.input
        self.output = parsed_args.output


def main():
    argument_parser = ArgumentParser()
    argument_parser.run()
    print(argument_parser.input)
    print(argument_parser.output)
