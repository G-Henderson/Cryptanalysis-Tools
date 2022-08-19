from utils.TextUtils import TextUtils
from utils.ngrams_scorer import NgramScorer, NgramFiles
from utils.stat_measurer import StatMeasurer

class CipherIdentifier:

    def __init__(self) -> None:
        self.message = ""

        # Setup text utils instance
        self.TU = TextUtils()

        # Setup cipher variables
        self.SUBSTITUTION = 1
        self.TRANSPOSITION = 2

        # Setup monogram fitness scorer
        self.monogram_scorer = NgramScorer(NgramFiles.MONOGRAM_FILE)

        # Setup stats calculator
        self.stat_measurer = StatMeasurer()

    def setMessage(self, message: str) -> None:
        self.message = message

    def identify(self, message: str=None):
        # Look at number of characters
        
        # Work out if it is transposition
        if (self.is_transposition(message)):
            return self.TRANSPOSITION

        

    def is_transposition(self, message) -> int:
        # Get rid of any characters that aren't letters
        message = self.TU.only_letters(message)
        # Make all letters uppercase
        message = message.upper()

        # Use monograms to score it
        ngram_score = self.monogram_scorer.ngram_score(message) / len(message)

        # Calculate the chi-squared statistic
        chi_score = self.stat_measurer.chi_squared(message) / len(message)
        
        # Check if it is below the threshold
        if (chi_score < 1):
            # Then it is likely to be a transposition
            return True

        elif (ngram_score > -1.29):
            # Then it is likely to be a transposition
            return True

        else:
            # Otherwise it's probably something else
            return False