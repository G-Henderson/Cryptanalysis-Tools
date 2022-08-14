from msilib import sequence
from utils.TextUtils import TextUtils
from utils.FitnessTest import FitnessTest
from ..cipher_solver import CipherSolver

class VigenereSolver(CipherSolver):

    """
    Class for decrypting ciphertexts encrypted using the Vigenere cipher
    """

    def __init__(self) -> None:
        super().__init__()

    def with_key(self, message: str, key) -> str:
        return super().with_key(message, key)

    def with_keylen(self, message: str, keylen: int) -> str:
        return super().with_keylen(message, keylen)

    def brute_force(self, message: str) -> str:
        self.get_period(message)
        return super().brute_force(message)

    def get_period(self, message: str) -> int:
        # Find the I.C's of key lengths between 2 and 15
        for a in range(2,16):
            sequences = []
            for b in range(a):
                current = ""
                more_letters = True
                index = b
                while more_letters:
                    try:
                        current += message[index]
                        index += a
                    except:
                        more_letters = False

                sequences.append(current)

            total = 0
            for b in range(len(sequences)):
                total += self.mFitTester.get_ic(sequences[b])

            average = total / len(sequences)
            print(str(a)+":  "+str(average))


        return 0