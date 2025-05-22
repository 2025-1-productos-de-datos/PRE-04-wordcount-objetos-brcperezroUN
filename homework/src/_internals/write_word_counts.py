import os


class WriteWordCountsMixin:
    def write_word_counts(self):
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        # save the results using tsv format
        output_path = os.path.join(self.output_folder, "wordcount.tsv")
        with open(output_path, "w", encoding="utf-8") as f:
            for key, value in self.counter.items():
                # write the key and value to the file
                f.write(f"{key}\t{value}\n")
