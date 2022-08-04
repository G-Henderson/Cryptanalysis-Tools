from utils.TextUtils import TextUtils as TU
import math

class FitnessTest:

    def __init__(self) -> None:
        self.my_textutils = TU()

        self.MONOGRAM_FILE = "utils/ngrams/english_monograms.txt"
        self.BIGRAM_FILE = "utils/ngrams/english_bigrams.txt"
        self.TRIGRAM_FILE = "utils/ngrams/english_trigrams.txt"
        self.QUADGRAM_FILE = "utils/ngrams/english_quadgrams.txt"
        self.QUINTGRAM_FILE = "utils/ngrams/english_quintgrams.txt"

        # Setup ngrams (defaults to using quadgrams)
        self.setup_ngrams(self.QUADGRAM_FILE)

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

    def setup_ngrams(self, filename: str) -> None:
        """
        Procedure to load the ngrams and other variables needed to run the ngram
        fitness test.
        """

        # Create empty dict to contain the ngrams and number of times it appears
        self.ngrams = {}
        # Read the file contents
        my_file_contents = open(filename, "r").readlines()
        # Iterate through the file contents
        for line in my_file_contents:
            # Get the key and count
            content = line.split(" ")
            # Add it to the dict
            self.ngrams[content[0]] = int(content[1])

        # Get the logarithmic probabilities
        self.len_ngram = len(list(self.ngrams.keys())[0])
        # Get the total number of appearances
        self.ngram_appearances = sum(self.ngrams.values())

        # Iterate through to determine the logarithmic probabilities
        for gram in self.ngrams.keys():
            self.ngrams[gram] = math.log10(self.ngrams[gram]/self.ngram_appearances)
        
        # Calculate an ngram floor value
        self.ngram_floor_value = math.log10(0.01 / self.ngram_appearances)


    def ngram_score(self, message: str,) -> float:
        """
        An algorithm to rate the fitness of a piece of text using ngrams
        """

        # Initialise the score variable
        score = 0.0
        # Convert the ciphertext to uppercase
        message = message.upper()
        # Remove the spaces and punctuation
        message = self.my_textutils.only_letters(message)
        for x in range(len(message)-self.len_ngram+1):
            # Get the current ngram
            curr_ngram = message[x:x+self.len_ngram]
            # Check if it appears in our ngram file
            if (curr_ngram in self.ngrams):
                # Add the ngram probability
                score += self.ngrams[curr_ngram]
            else:
                # Add the floor value
                score += self.ngram_floor_value

        # Return the score
        return score