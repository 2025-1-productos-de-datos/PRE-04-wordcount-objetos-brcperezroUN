class CountWordsMixin:
    def count_words(self):
        counter = {}
        for word in self.words:
            counter[word] = counter.get(word, 0) + 1
        self.counter = counter
