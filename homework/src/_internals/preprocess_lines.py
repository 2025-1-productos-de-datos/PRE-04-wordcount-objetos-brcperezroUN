class PreprocessLinesMixin:
    def preprocess_lines(self):
        all_lines = [line.lower().strip() for line in self.lines]
        self.preprocessed_lines = all_lines
