import json

from utils.cipher_identifier import CipherIdentifier

from utils.solvers.caesar_solver import CaesarSolver
from utils.solvers.affine_solver import AffineSolver
from utils.solvers.simple_substitution_solver import SimpleSubSolver
from utils.solvers.columnar_transposition_solver import ColumnarTranspositionSolver as ColTransSolver
from utils.solvers.vigenere_solver import VigenereSolver
from utils.solvers.railfence_solver import RailfenceSolver
from utils.solvers.transposition_solver import TranspositionSolver

from utils.stat_measurer import StatMeasurer
from utils.ngrams_scorer import NgramScorer, NgramFiles
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
        # Setup the solver
        transposition_solver = ColTransSolver()
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
    elif (type == "uniform"):
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
    #solver = TranspositionSolver()
    #print(solver.create_grid(("LESIE DKRRO SICER RNDEE ACITE VSSEE EICEV SHSRT RGSEI HLEIV OIETE BANND EOIGO IAECD EASUT FAMDE YAUHF HIWMU SASEH TTTTA IMETM CEAGN NBTEG OEDRO ADLEP UUWPM FFLIE UTIYA IRBED KECTC IATOL LGTOP RIWMI THRDI EOCSF IRYDE ITFNE OHRFO EHITN NEMVS MRNUR SOHNR RISUD HMTDH BDGVC EHREE YBSEU TOTDH LEARI DTLRN TIAST DHNEA CRTHS DEAGU ERDTE TEHEI ELHFT SNEFR RCOND RSOEW DIWYF HOBNW GOMDA WIYHR ABPRB TTEGE TAENO EAPSR IPTLE CKDYO TOIYA HNHRF SDEEH PUTEO DORAS MEAOT EWDEL RWMEO NVHAE SEETS RFSOI LMMIA LBISI ILEAT AEOFE OEMMM QINHT MDOTB DEEIE AFWNT AEHSO UNHTI FAGBR HCULB UIIHI WGOEH TATKA MANIA CIUEO REAAE SXITD RRWES MHERH AOSSA EIRIL EPTEA WECII NEDHA AIHOE ASTOS RAEEA DOFHN EECSE EEIYE GENIO TSTGH UEDAA SBRLD SHIHE VIHEN NHETJ IAATG AEADD NIINT IANEW IEDLE ONRLG EHDOT NMESA AIESN EGTBG LDIRY ETODL GARNM MXALV HAEEO EYIRM TLBHK DNLEL EEHNE OHELI AOEAV TIERD EOHQT TOEYY THABH TCCDE TLLOI AGWSA IWLAO ONRIE NELUP SOTHW BCADA RMSST FSOEL PIMNO EEELI EFFRT NIEDE ESCHN DAKIN JARTH NENHN HNECN AYDFH IETRO EKOET HEHIE PPOEC EHSEH TATLA JDRET HMSOO SADFR SEPYE AHTOD EHFNC VSMGP SOOEI TLRSH DIEOL AETTS CNOWS GOTVN UESRH NNMNO IOFEN CTJSM HTIAE GRITL ETEEU EAEII NIHVT OLNIM FLADE TTATE MDRAE REEUI ATSER FWADT BRAEE AEAOW LHITG RUTCU NEULY ATNRU SNMWU EAFWA OSAEE STEOL TALEP EKNDY NLWIK SREIS MACUK EOJEL ILKNA SYOUE ASSDV UHRWO UHNHD TUEIM TELBT KRITD IEEGR CHDDT ANOEI EUNON VEKLO SEOTB RITML OKAMO RSIOO UPMNT TMFMD IONIN ENTIA TWHEH OASAK ASRGM TOARI AONTH TAPAN TNBED NETML RTFAS ORBHE OIEIY DUVRH UHTLI ADHEE EEOEN LLIYT RYEAE RTSSS AHLOD E").replace(" ", ""), "01234"))
