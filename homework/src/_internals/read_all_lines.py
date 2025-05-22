import os


class ReadAllLinesMixin:
    def read_all_lines(self):
        all_lines = []

        # Read all lines
        input_files_list = os.listdir(self.input_folder)
        for filename in input_files_list:
            file_path = os.path.join(self.input_folder, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                all_lines.extend(lines)
        self.lines = all_lines
