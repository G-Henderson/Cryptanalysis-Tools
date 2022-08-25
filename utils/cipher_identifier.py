from utils.TextUtils import TextUtils
from utils.ngrams_scorer import NgramScorer, NgramFiles
from utils.stat_measurer import StatMeasurer

class CipherIdentifier:

    def __init__(self) -> None:
        self.message = ""

        # Setup text utils instance
        self.TU = TextUtils()

        # Setup cipher variables
        self.SUBSTITUTION = "substitution"
        self.TRANSPOSITION = "transposition"
        self.UNIFORM_DIST = "uniform"
        self.UNKNOWN = "unknown"

        # Setup monogram fitness scorer
        self.monogram_scorer = NgramScorer(NgramFiles.MONOGRAM_FILE)

        # Setup stats calculator
        self.stat_measurer = StatMeasurer()

    def setMessage(self, message: str) -> None:
        self.message = message

    def identify(self, message: str=None) -> str:
        # Look at number of characters
        
        # Work out if it is transposition
        if (self.is_transposition(message)):
            return self.TRANSPOSITION

        # Check if is substitution
        if (self.is_substitution(message)):
            return self.SUBSTITUTION

        # Check if uniform distribution
        if (self.is_uniform_dist(message)):
            return self.UNIFORM_DIST

        # It is likely to be something else
        return self.UNKNOWN

    def is_transposition(self, message: str) -> bool:
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

    def is_substitution(self, message: str) -> bool:
        # Get the IC of the message
        message_ic = self.stat_measurer.get_ic(message)

        # If the IC is greater than 0.06 then it is likely a substitution cipher
        if (message_ic > 0.06):
            return True

        else:
            return False

    def is_uniform_dist(self, message: str) -> bool:
        # Get the IC of the message
        message_ic = self.stat_measurer.get_ic(message)

        # If the IC is between 0.025 and 0.045, the characters are uniformly distributed
        if (0.025 < message_ic) and (message_ic < 0.045):
            return True

        else:
            return False