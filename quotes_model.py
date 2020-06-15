import json
import random

class QuotesModel:

    markov_chain = {
        'START': [],
        'END': []
    }
    verbose = False

    def __init__(self, verbose=False):
        self.verbose = verbose

    def load_quotes(self, path):
        if self.verbose:
            print('Loading the quotes')
        quotes = []
        with open(path, 'r') as f:
            quotes = json.load(f)
        return quotes

    def load_model(self, path):
        if self.verbose:
            print('Loading the model')
        with open(path, 'r') as f:
            self.markov_chain = json.load(f)
    
    def train(self, quotes, output_path):
        if self.verbose:
            print('Training the model')
        for quote in quotes:
            tokens = quote.lower().split()
            for i, word in enumerate(tokens):
                if i == len(tokens) - 1:
                    self.markov_chain['END'].append(word)
                else:
                    if i == 0:
                        self.markov_chain['START'].append(word)
                    if not word in self.markov_chain:
                        self.markov_chain[word] = []
                    self.markov_chain[word].append(tokens[i + 1])
        with open(output_path, 'w') as f:
            if self.verbose:
                print('Writing model.json')
            json.dump(self.markov_chain, f)
    
    def generate(self, min_len=5):
        if self.verbose:
            print('Generating quote')
        generated = []
        while True:
            if not generated:
                words = self.markov_chain['START']
            elif generated[-1] in self.markov_chain['END'] and len(generated) >= min_len:
                break
            else:
                words = self.markov_chain[generated[-1]]
            generated.append(random.choice(words))
        quote = ' '.join(generated)
        return quote
