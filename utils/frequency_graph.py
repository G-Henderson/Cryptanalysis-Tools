import matplotlib.pyplot as plt
import numpy as np
from utils.TextUtils import TextUtils

class FrequencyGraph:

    def __init__(self, message: str) -> None:
        self.text_utils = TextUtils()

        # Define english letter frequency probabilities
        self.ENGLISH_MEANS = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]
        # Define alphabet
        self.ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        # Remove characters from message and convert to upper case
        self.message = self.text_utils.only_letters(message).upper()

    def show(self) -> None:
        letter_frequencies = [0 for i in range(26)]

        # Calculate the number of times each letter appears in the ciphertext
        for char in self.message:
            index = self.ALPHABET.index(char)
            letter_frequencies[index] += 1

        # Calculate the letter frequency probabilities of our ciphertext
        ciphertext_means = [((letter_frequencies[i]) / len(self.message)) for i in range(26)]

        ind = np.arange(26) # Set number of bar categories
        width = 0.35 # Set individual bar width

        # Create bars and labels
        plt.bar(ind, ciphertext_means, width, label='Cipher Text')
        plt.bar(ind + width, self.ENGLISH_MEANS, width, label='English')

        plt.ylabel('Frequencies') # Set y-axis title/label
        plt.title('Frequency Analysis') # Set graph title

        # Plot bars on graph
        plt.xticks(ind + width / 2, (char for char in self.ALPHABET))
        plt.legend(loc='best')
        plt.show() # Display the graph