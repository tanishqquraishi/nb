from collections import defaultdict
import math
import corpus

class SpamFilter:
    def __init__(self):
        self.word_counts = defaultdict(int)
        self.category_counts = defaultdict(int)
        self.total_words = 0
        self.total_documents = 0

# takes in a string of text and a category ("spam" or "ham") and updates the internal word and category counts.
    def train(self, text, category):
        words = text.split()
        for word in words:
            self.word_counts[word] += 1
            self.total_words += 1
        self.category_counts[category] += 1
        self.total_documents += 1

#takes in a string of text and returns the predicted category 
    def classify(self, text):
        words = text.split()

        log_prob_spam = 0
        log_prob_ham = 0
        for word in words:
            log_prob_spam += math.log((self.word_counts[word] + 1) / (self.total_words + self.total_documents))
            log_prob_ham += math.log((self.word_counts[word] + 1) / (self.total_words + self.total_documents))

        log_prob_spam += math.log(self.category_counts["spam"] / self.total_documents)
        log_prob_ham += math.log(self.category_counts["ham"] / self.total_documents)

        if log_prob_spam > log_prob_ham:
            return "spam"
        else:
            return "ham"
