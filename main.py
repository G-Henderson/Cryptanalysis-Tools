import json

from utils.cipher_identifier import CipherIdentifier

from utils.solvers.caesar_solver import CaesarSolver
from utils.solvers.affine_solver import AffineSolver
from utils.solvers.simple_substitution_solver import SimpleSubSolver
from utils.solvers.columnar_transposition_solver import ColumnarTranspositionSolver as ColTransSolver
from utils.solvers.vigenere_solver import VigenereSolver
from utils.solvers.railfence_solver import RailfenceSolver
from utils.solvers.transposition_solver import TranspositionSolver

from utils.test import Test


def get_message() -> str:
    message = input("Please enter your ciphertext: ")

    return message


def go(message: str=None) -> str:
    if (message == None):
        message = get_message()

    # Get the type of cipher
    cipher_identifier, cipher_type = identify(message)

    # Check if it is a transposition cipher
    if (cipher_type == cipher_identifier.TRANSPOSITION):
        # Try Rail-fence
        print("\nTrying Rail-fence...")
        # Setup the solver
        railfence_solver = RailfenceSolver()
        # Try and solve it
        decrypt = railfence_solver.solve(message)
        # Print out a sample
        print(f"Decrypt sample: {decrypt[:30]}...")

        if (input("\nDoes this look right? ") == "no"):
            # Try Columnar Transposition
            print("\nTrying Columnar Transposition...")
            # Setup the solver
            col_transposition_solver = ColTransSolver()
            # Try and solve it
            decrypt = col_transposition_solver.solve(message)
            # Print out a sample
            print(f"Decrypt sample: {decrypt[:30]}...")

            if (input("\nDoes this look right? ") == "no"):
                # Try basic transposition
                print("\nTrying normal transposition...")
                # Setup the solver
                transposition_solver = TranspositionSolver()
                # Try and solve it
                decrypt = transposition_solver.solve(message)

    # Check if it is a substitution cipher
    elif (cipher_type == cipher_identifier.SUBSTITUTION):
        # Try Caesar
        print("\nTrying Caesar...")
        # Setup the solver
        caesar_solver = CaesarSolver()
        # Try and solve it
        decrypt = caesar_solver.solve(message)
        # Print out a sample
        print(f"Decrypt sample: {decrypt[:30]}...")

        if (input("\nDoes this look right? ") == "no"):
            # Try Affine
            print("\nTrying Affine...")
            # Setup the solver
            affine_solver = AffineSolver()
            # Try and solve it
            decrypt = affine_solver.solve(message)
            # Print out a sample
            print(f"Decrypt sample: {decrypt[:30]}...")

            if (input("\nDoes this look right? ") == "no"):
                # Try Simple Substitution
                print("\nTrying simple substitution...")
                # Setup the solver
                simple_sub_solver = SimpleSubSolver()
                # Try and solve it
                decrypt = simple_sub_solver.solve(message)

    # Check if it is a Vigenere cipher
    elif (cipher_type == cipher_identifier.UNIFORM_DIST):
        # Setup the solver
        vigenere_solver = VigenereSolver()
        # Try and solve it
        decrypt = vigenere_solver.solve(message)

    else:
        decrypt = "error..."

    output(decrypt)

    
def output(decrypt: str) -> None:
    # Print the decrypt
    print(f"\nHere is your decrypt: {decrypt}")


def identify(message: str) -> tuple:
    """
    Gets the type of cipher and prints a message
    """

    # Identify the type of cipher
    cipher_identifier = CipherIdentifier()
    cipher_type = cipher_identifier.identify(message)

    # Output a message
    if ("un" not in cipher_type):
        print(f"\nI identified your cipher to be a {cipher_type} cipher. I will now try to decrypt it...")
    elif (cipher_type == "uniform"):
        print(f"\nI found that your cipher had uniform distribution. I will try and solve it using the Vigenere solver...")
    else:
        print("\nI was unable to determine the type of cipher used...")

    # Output the identifier and type of cipher
    return cipher_identifier, cipher_type


def main():
    # Run the tests
    #tests()

    # Run the main program
    go()

if __name__ == "__main__":
    main()