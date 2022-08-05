import json

from utils.FitnessTest import FitnessTest

from utils.solvers.caesar_solver import CaesarSolver
from utils.solvers.affine_solver import AffineSolver

def loadCipherText():
    file_path = "cipher-texts/2021.json"
    my_file = open(file_path)
    my_obj = json.load(my_file)
    my_file.close()

    ctext = my_obj["challenges"][0]["ctext"]

    return ctext

def main():

    ### Run the tests ###
    print("Running Tests...")

    ft = FitnessTest()

    # Test the chi-squared statistic function
    print("\nTesting the Chi-squared statistic function...")
    if (ft.chi_squared("Defend the east wall of the castle") == 18.528310082299488):
        print("Passed")
    else:
        print("Failed")

    # Test the ngram fitness score function
    print("\nTesting the ngram fitness score function...")
    if (ft.ngram_score("HELLOWORLD") == -28.42865649982033):
        print("Passed")
    else:
        print("Failed")

    # Test the caesar solver with known shift
    mCaesarSolver = CaesarSolver()
    print("\nTesting the caesar solver with known shift...")
    if (mCaesarSolver.solve("dbcbka qeb bxpq txii lc qeb zxpqib", 3) == "DEFENDTHEEASTWALLOFTHECASTLE"):
        print("Passed")
    else:
        print("Failed")

    # Test the caesar solver with unknown shift
    print("\nTesting the caesar solver with unknown shift...")
    if (mCaesarSolver.solve("abcbka qeb bxpq txii lc qeb zxpqib") == "DEFENDTHEEASTWALLOFTHECASTLE"):
        print("Passed")
    else:
        print("Failed")

    # Test the affine solver with known key
    mAffineSolver = AffineSolver()
    print("\nTesting the affine solver with known key...")
    if (mAffineSolver.solve("knqnok gwn nbdg pbii rq gwn hbdgin", 3, 1) == "DEFENDTHEEASTWALLOFTHECASTLE"):
        print("Passed")
    else:
        print("Failed")

    # Test the affine solver with unknown key
    print("\nTesting the affine solver with unknown key...")
    if (mAffineSolver.solve("knqnok gwn nbdg pbii rq gwn hbdgin") == "DEFENDTHEEASTWALLOFTHECASTLE"):
        print("Passed")
    else:
        print("Failed")

    ### End of tests ###
    print("")

    ### Start the main program ###

if __name__ == "__main__":
    main()