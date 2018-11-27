import pickle

def save_tokenizer(tokenizer):
    with open('tokenizer.pickle', 'wb') as handle:
        pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

# loading
def load_tokenizer():
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
        return tokenizer
