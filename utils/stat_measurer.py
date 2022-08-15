from utils.TextUtils import TextUtils as TU
import math

class StatMeasurer:

    def __init__(self) -> None:
        self.my_textutils = TU()

    def chi_squared(self, message: str) -> float:
        """
        An algorithm to calculate chi-squared statistics
        (Against English distribution)
        """

        # set the letters to lower case
        message = message.lower()
        # Remove the spaces and punctuation
        message = self.my_textutils.only_letters(message)
        counts = [0 for i in range(26)]
        expected = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]

        total_count = len(message)
        for char in message:
            counts[ord(char) - 97] += 1

        # Calculate chi-squared statistic against English distribution
        sum = 0.0
        for i in range(26):
            sum = sum + math.pow((counts[i] - total_count * expected[i]), 2) / (total_count * expected[i])

        # Return the statistic
        return sum

    def get_ic(self, message: str) -> float:
        """
        A function to determine the index of coincidence of a ciphertext
        """

        # Set the message to lowercase
        message = message.lower()

        # Remove any characters not in the alphabet
        message = self.my_textutils.only_letters(message)

        # Create an empty list to hold the amount of times each letter appears
        frequencies = [0 for i in range(26)]

        # Create a variable to contain the length of the message
        msg_len = len(message)

        # Iterate through the message, to calculate the frequencies
        for char in message:
            frequencies[ord(char) - 97] += 1

        total = 0
        for i in range(26):
            total = total + frequencies[i] * (frequencies[i] - 1)

        # Calculate the index of coincidence (ic)
        ic = total / (msg_len * (msg_len-1))

        # Return the ic
        return ic