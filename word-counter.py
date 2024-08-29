import string
from collections import defaultdict

class WordCounter:
    def __init__(self):
        self.word_count = defaultdict(int)
    
    def process_text(self, text):
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = text.split()
        
        for word in words:
            self.word_count[word] += 1
    
    def get_word_counts(self):
        return dict(self.word_count)

# Get user input
user_input = input("Enter some text: ")

# Create an instance of WordCounter
counter = WordCounter()
counter.process_text(user_input)

# Get and print the word counts
word_counts = counter.get_word_counts()
print("Word counts:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
