import utils.ngrams.ngram_files as NgramFiles
from utils.TextUtils import TextUtils as TU
import math

class NgramScorer():
    
    def __init__(self, ngram_file=NgramFiles.QUADGRAM_FILE) -> None:
        # Setup ngrams (defaults to using quadgrams)
        self.setup_ngrams(ngram_file)

        # Setup the textutils instance
        self.my_textutils = TU()

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

    def ngram_score(self, message: str) -> float:
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