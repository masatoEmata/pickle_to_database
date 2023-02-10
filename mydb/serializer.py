import pickle
import bz2


def binarize(obj):
    return pickle.dumps(obj, pickle.HIGHEST_PROTOCOL)

def debinarize(binary):
    return bz2.decompress(binary)

def serialize(obj):
    return bz2.compress(binarize(obj), 3)

def deserialize(binary):
    return pickle.loads(debinarize(binary))

print(binarize([1,2,3,{'a': [1.2, 2.2]}]))
