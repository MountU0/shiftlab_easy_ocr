from evaluate import load
from collections import Counter
import math

def cosine_similarity(str1:str, str2:str) -> float:
    """Text Similarity has to determine
    how the two text documents close
    to each other in terms of their context or meaning
    """
    def text_to_vector(text):
        words = text.split()
        return Counter(words)
    
    vector1 = text_to_vector(str1)
    vector2 = text_to_vector(str2)

    dot_product = sum(vector1[word] * vector2[word] for word in vector1 if word in vector2)
    magnitude1 = math.sqrt(sum(vector1[word] ** 2 for word in vector1))
    magnitude2 = math.sqrt(sum(vector2[word] ** 2 for word in vector2))

    if magnitude1 == 0 or magnitude2 == 0:
        return 0
    else:
        return dot_product / (magnitude1 * magnitude2)


def cer(y_true:str, y_pred:str) -> float:
    """Character error rate (CER) is a common metric 
    of the performance of an automatic
    speech recognition system.
    """
    cer_metric = load("cer")
    cer_score = cer_metric.compute(predictions=[y_pred], references=[y_true])
    return cer_score
