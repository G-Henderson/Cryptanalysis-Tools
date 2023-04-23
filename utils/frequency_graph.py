import matplotlib.pyplot as plt
import numpy as np
from utils.TextUtils import TextUtils

class FrequencyGraph:

    def __init__(self, message: str) -> None:
        self.text_utils = TextUtils()

        self.ENGLISH_MEANS = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]
        self.ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        self.message = self.text_utils.only_letters(message).upper()

    def show(self) -> None:
        letter_frequencies = [0 for i in range(26)]

        for char in self.message:
            index = self.ALPHABET.index(char)
            letter_frequencies[index] += 1

        ciphertext_means = [((letter_frequencies[i])/len(self.message)) for i in range(26)]

        ind = np.arange(26)
        width = 0.35
        plt.bar(ind, ciphertext_means, width, label='Cipher Text')
        plt.bar(ind + width, self.ENGLISH_MEANS, width, label='English')

        plt.ylabel('Frequencies')
        plt.title('Frequency Analysis')

        plt.xticks(ind + width / 2, (char for char in self.ALPHABET))
        plt.legend(loc='best')
        plt.show()