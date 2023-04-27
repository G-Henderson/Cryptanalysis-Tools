import json
import sys

from utils.cipher_identifier import CipherIdentifier

from utils.solvers.caesar_solver import CaesarSolver
from utils.solvers.affine_solver import AffineSolver
from utils.solvers.simple_substitution_solver import SimpleSubSolver
from utils.solvers.columnar_transposition_solver import ColumnarTranspositionSolver as ColTransSolver
from utils.solvers.vigenere_solver import VigenereSolver
from utils.solvers.railfence_solver import RailfenceSolver
from utils.solvers.transposition_solver import TranspositionSolver
from utils.solvers.morse_translator import MorseTranslator

from utils.test import Test
from utils.frequency_graph import FrequencyGraph
from utils.TextUtils import TextUtils
from utils.ngrams_scorer import NgramScorer
from utils.stat_measurer import StatMeasurer

class MenuOption:

    def __init__(self, option_name: str, keys: str, option_function) -> None:
        self.option_name = option_name
        self.keys = keys
        self.option_function = option_function

    def getOption_name(self) -> str:
        return self.option_name
    
    def getKeys(self) -> list:
        return self.keys
    
    def getOption_function(self):
        return self.option_function
    
    def __str__(self) -> str:
        return self.option_name
    
class Menu:

    def __init__(self, menu_name: str, menu_options: list=[]) -> None:
        self.menu_name = menu_name # Set menu name
        self.menu_options = menu_options # Setup list to contain menu options

    def add_menu_option(self, option: MenuOption) -> None:
        self.menu_options.append(option)

    def getMenu_name(self) -> str:
        return self.menu_name
    
    def getMenu_options(self) -> list:
        return self.menu_options
    
    def display(self) -> None:
        print(f"\n{self.menu_name}")
        print("Options:", end=" ")
        for count, option in enumerate(self.menu_options):
            print(f"{count+1}. {option.getOption_name()} ({option.getKeys()[0]})", end=" ")

def create_menu():
    # Create list of menu options
    options = [MenuOption('Enter new ciphertext', ['new', 'n'], "enter_message"),
                MenuOption('Load ciphertext', ['load', 'l'], "load_message"),
                MenuOption('Get Help', ['help', 'h', '?'], "get_help"),
                MenuOption('Run tests', ['test', 't'], "run_tests"),
                MenuOption('Exit', ['exit', 'x', 'e'], "sys.exit")
        ]

    # Create menu object
    main_menu = Menu("Main Menu", options)
    ciphertext = ""
    plaintext = ""

    while True:
        # Display the main menu
        main_menu.display()
        # Get the user's command
        command = get_user_input()
        my_option = None
        # Search for their command
        for option in main_menu.getMenu_options():
            if (command in option.getKeys()):
                my_option = option
                break

        else:
            # Command wasn't found
            print("\nPlease enter a valid command!! Type 'h' for help...")
        
        # Run the command
        if (my_option != None):
            # Sort input for function
            args = ""
            if (my_option.getOption_name() == "Auto Decrypt"):
                extra = ciphertext
                args = "extra"

            elif (my_option.getOption_name() == "Manual Decrypt"):
                extra = ciphertext
                args = "extra"

            elif (my_option.getOption_name() == "Enter new ciphertext"):
                extra = main_menu
                args = "extra"

            elif (my_option.getOption_name() == "Frequency graph"):
                extra = ciphertext
                args = "extra"

            # Run function
            output = eval(f"{my_option.getOption_function()}({args})")

            # Deal with output from function
            if (my_option.getOption_name() == "Load ciphertext") or (my_option.getOption_name() == "Enter new ciphertext"):
                main_menu = output[0]
                ciphertext = output[1]

            elif (my_option.getOption_name() == "Auto Decrypt"):
                plaintext = output
                # Print the decrypted message
                print(f"\nHere is your decrypted message: {plaintext}.")

            elif (my_option.getOption_name() == "Manual Decrypt"):
                plaintext = output
                # Print the decrypted message
                print(f"\nHere is your decrypted message: {plaintext}.")

def get_user_input(msg: str="Enter command:") -> str:
    """
    Function to get user input
    """

    # Get user input and store as string
    command = input(f"\n\n{msg} ")
    # Return string
    return command.lower()

def enter_message(menu: Menu) -> list:
    """
    Function to get the user to input their message
    """

    # Get user input
    message = input("Enter your message: ")    

    # Add new option to menu
    menu.add_menu_option(MenuOption('Auto Decrypt', ['auto', 'a'], "auto_solve"))
    menu.add_menu_option(MenuOption('Manual Decrypt', ['man', 'manual', 'm'], "manual_solve"))
    menu.add_menu_option(MenuOption('Frequency graph', ['graph', 'g'], "create_graph"))
    menu.add_menu_option(MenuOption('Save', ['save', 's'], "save_to_file"))

    # Return menu and message
    return [menu, message]

def get_help() -> None:
    """
    Function to print help for program
    """

    HELP_FILE = "data/help.txt"
    help_contents = []

    # Read the help information from the file
    with open(HELP_FILE, "r") as my_file:
        help_contents = my_file.readlines()

    # Print the contents of the file, line by line
    for line in help_contents:
        print(line.replace("\n", ""))
    
    # Return
    return

def create_graph(message: str) -> None:
    """
    Display a frequency graph
    """

    new_graph = FrequencyGraph(message)
    new_graph.show()

    # Return
    return

def manual_solve(message: str) -> str:
    """
    Function to manually decipher an enciphered message
    """

    # Create list of menu options
    options = [MenuOption('Caesar', ['caesar', 'c'], "CaesarSolver().solve"),
                MenuOption('Affine', ['affine', 'a'], "AffineSolver().solve"),
                MenuOption('Simple substitution', ['simple sub', 's'], "SimpleSubSolver().solve"),
                MenuOption('Rail Fence', ['rail', 'r'], "RailfenceSolver().solve"),
                MenuOption('Transposition', ['trans', 't'], "TranspositionSolver().solve"),
                MenuOption('Columnar Transposition', ['col', 'ct'], "ColTransSolver().solve"),
                MenuOption('Vigenere', ['vigenere', 'v'], "VigenereSolver().solve"),
                MenuOption('Morse Code', ['morse', 'm'], "MorseTranslator().decode"),
                MenuOption('Get Help', ['help', 'h', '?'], "get_help")
        ]

    # Create sub menu for manual decryption
    manual_menu = Menu("Manual Decryption", options)
    manual_menu.display()

    my_option = None
    while my_option == None:
        # Get user input
        command = get_user_input()

        # Search for their command
        for option in manual_menu.getMenu_options():
            if (command in option.getKeys()):
                if (option.getOption_name() == "Get Help"):
                    eval(f"{option.getOption_function()}()")
                else:
                    my_option = option
                    break

        else:
            # Command wasn't found
            print("\nPlease enter a valid command!! Type 'h' for help...")

    # Return the decrypted message
    return eval(f"{my_option.getOption_function()}(message)")
    

def auto_solve(message: str) -> str:
    """
    Function to automatically decipher an enciphered message
    """

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

    # Return the decrypted message
    return decrypt

def identify(message: str) -> tuple:
    """
    Function to identify the type of cipher used to encrypt a message
    """

    # Identify the type of cipher
    cipher_identifier = CipherIdentifier()
    cipher_type = cipher_identifier.identify(message)

    # Output a message
    if (cipher_type == "morse"):
        print(f"\nDecoding morse and trying again...")
        morse_translator = MorseTranslator()
        identify(morse_translator.decode(message))
    elif ("un" not in cipher_type):
        print(f"\nI identified your cipher to be a {cipher_type} cipher. I will now try to decrypt it...")
    elif (cipher_type == "uniform"):
        print(f"\nI found that your cipher had uniform distribution. I will try and solve it using the Vigenere solver...")
    else:
        print("\nI was unable to determine the type of cipher used...")

    # Output the identifier and type of cipher
    return cipher_identifier, cipher_type


def run_tests():
    # Run automated tests
    test_num = 1

    # Test using previous challenges
    my_file = open('data/tests.json')
    data = json.load(my_file)

    for challenge in data["test_ciphers"]:
        print(challenge)
        print(f"\n{test_num}. Trying {challenge['name']}")

        decrypt_a = auto_solve(challenge["ctext_a"])
        decrypt_b = auto_solve(challenge["ctext_b"])

        print(f"\nPart A decrypt: {decrypt_a}")
        print(f"Official Part A decrypt: {challenge['answer_a']}")

        print(f"\nPart B decrypt: {decrypt_b}")
        print(f"Official Part B decrypt: {challenge['answer_b']}")

        test_num += 1

    text_utils = TextUtils()
    # 1. Test the space removal
    test = Test(f"\n{test_num}. Testing space remover...")
    test.setTest(lambda: text_utils.remove_spaces("HELLO WORLD!!"), "HELLOWORLD!!")
    test.run()
    test_num += 1

    # 2. Test the punctuation remover
    test = Test(f"\n{test_num}. Testing punctuation remover...")
    test.setTest(lambda: text_utils.remove_punctuation("HELLO WORLD!!"), "HELLO WORLD")
    test.run()
    test_num += 1

    # 3. Test the only letters function
    test = Test(f"\n{test_num}. Testing only letters...")
    test.setTest(lambda: text_utils.only_letters("HELLO WORLD!!"), "HELLOWORLD")
    test.run()
    test_num += 1

    # 4. Test quadgram scorer
    ngram_scorer = NgramScorer()
    test = Test(f"\n{test_num}. Testing quadgram scorer...")
    test.setTest(lambda: ngram_scorer.ngram_score("HELLOWORLD"), -28.42865649982033)
    test.run()
    test_num += 1

    stat_helper = StatMeasurer()
    # 5. Test chi-squared statistic calculator
    test = Test(f"\n{test_num}. Testing chi calculator...")
    test.setTest(lambda: stat_helper.chi_squared("Programming in python is fun"), 27.907733765597285)
    test.run()
    test_num += 1

    # 6. Test I.C statistic calculator
    test = Test(f"\n{test_num}. Testing I.C calculator...")
    test.setTest(lambda: stat_helper.get_ic("Programming in python is fun"), 0.050724637681159424)
    test.run()
    test_num += 1

    caesar_solver = CaesarSolver()
    # 7. Test the caesar solver with shift
    test = Test(f"\n{test_num}. Testing caesar with shift...")
    test.setTest(lambda: caesar_solver.solve("Qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald.", key=3), "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG")
    test.run()
    test_num += 1

    # 8. Test the caesar solver without the shift
    test = Test(f"\n{test_num}. Testing caesar without shift...")
    test.setTest(lambda: caesar_solver.solve("Qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald."), "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG")
    test.run()
    test_num += 1

    affine_solver = AffineSolver()
    # 9. Test the affine solver with the keys
    test = Test(f"\n{test_num}. Testing affine with keys...")
    test.setTest(lambda: affine_solver.solve("Gwn xjzhf earpo qrs cjlud rmna gwn ibyv krt.", key=(3,1)), "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG")
    test.run()
    test_num += 1

    # 10. Test the affine solver without the keys
    test = Test(f"\n{test_num}. Testing affine without keys...")
    test.setTest(lambda: affine_solver.solve("Gwn xjzhf earpo qrs cjlud rmna gwn ibyv krt."), "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG")
    test.run()
    test_num += 1

    simple_sub_solver = SimpleSubSolver()
    # 11. Test the simple substitution solver with the key
    test = Test(f"\n{test_num}. Testing simple substitution with key...")
    test.setTest(lambda: simple_sub_solver.solve("R NZMZTVW GL GIZXV QZWV/QLWRV GL Z HFRGV ZG Z SRTS-XOZHH SLGVO WLDMGLDM. GSV HLIG LU KOZXV LMOB Z YZMP XLFOW ZUULIW, ZMW R XLFOWM'G HGZB GSVIV NBHVOU, VEVM RU R DZH LM VCKVMHVH. R GSRMP RG DLFOW SZEV YVVM GVNKGRMT UZGV ZMBDZB. RU R XZM URMW QLWRV, R ZN HFIV HSV XZM URMW NV. HLNVGSRMT RM SVI OVGGVI GVOOH NV HSV ZOIVZWB SZH. RM ZMB XZHV, R WVXRWVW GL PVVK Z OLMT GZRO LM SVI, RU LMOB GL ZELRW HKLLPRMT ZMBLMV VOHV DSL NRTSG YV ULOOLDRMT SVI. R ZN ULXFHRMT LM RMGVIXVKGRMT SVI XLNNH DRGS OBMM UIZMP. GSVB ZIV HGROO FHRMT UZRIOB ORTSG VMXIBKGRLM, ZMW RG RH VZHRVI GL TVG ZXXVHH GL NH UIZMP’H LUURXV GSZM RG DLFOW YV GL RMUROGIZGV QLWRV’H ILLN ZG GSV SLGVO. GSLHV KOZXVH GZPV GSV HVXFIRGB LU GSVRI XORVMGH VEVM NLIV HVIRLFHOB GSZM GSV YZMPH. GSV ZGGZXSVW OVGGVI HSLDH GSZG QLWRV RH TVGGRMT NLIV XZFGRLFH, YFG RG ZOHL HVVNH GL YV ZM RMERGZGRLM GL TVG RMELOEVW. R ZN MLG HFIV DSVIV GL TL UILN SVIV. ZH QLWRV HZBH RM GSV OVGGVI, GSV MFNYVIH RM GSV HRTM-RM YLLP HFTTVHG HLNVGSRMT LWW, YFG FMORPV QLWRV R DLM’G SZEV ZXXVHH GL GSV EZFOG GL XSVXP RG. RH HSV SRMGRMT GSZG DV HSLFOW GVZN FK, LI DZIMRMT NV GSZG HSV PMLDH R ZN SVIV ZMW HSLFOW PVVK ZDZB? (RU BLF ZIV MLG HFIV DSZG R ZN GZOPRMT ZYLFG, GZPV Z EVIB XZIVUFO OLLP ZG BLFI WVXIBKG LU SVI OVGGVI. BLF HSLFOW URMW Z SRWWVM NVHHZTV.) YB GSV DZB, GSVIV RH HLNVGSRMT MZTTRMT ZG NV GSZG R XZM’G JFRGV KOZXV. GSVIV RH Z MZNV RM GSV HRTM-RM YLLP GSZG, RM NB SVZW ZG OVZHG, RH XLMMVXGVW RM HLNV DZB GL GSV MZNV LU GSV YZMP, ZMW R XZM’G IVNVNYVI DSZG GSZG XLMMVXGRLM RH. NZBYV RG RH MLG RNKLIGZMG, YFG R DLM’G HOVVK KILKVIOB FMGRO R XZM URTFIV RG LFG. LMXV BLF SZEV XIZXPVW QLWRV’H OVGGVI, SVZW LEVI GL GSV XZHV UROVH ZMW GZPV Z OLLP ZG GSV HRTMZGFIVH. NZBYV BLF XZM URTFIV RG LFG ULI NV. SZIIB", key="ZYXWVUTSRQPONMLKJIHGFEDCBA"), "IMANAGEDTOTRACEJADEJODIETOASUITEATAHIGHCLASSHOTELDOWNTOWNTHESORTOFPLACEONLYABANKCOULDAFFORDANDICOULDNTSTAYTHEREMYSELFEVENIFIWASONEXPENSESITHINKITWOULDHAVEBEENTEMPTINGFATEANYWAYIFICANFINDJODIEIAMSURESHECANFINDMESOMETHINGINHERLETTERTELLSMESHEALREADYHASINANYCASEIDECIDEDTOKEEPALONGTAILONHERIFONLYTOAVOIDSPOOKINGANYONEELSEWHOMIGHTBEFOLLOWINGHERIAMFOCUSINGONINTERCEPTINGHERCOMMSWITHLYNNFRANKTHEYARESTILLUSINGFAIRLYLIGHTENCRYPTIONANDITISEASIERTOGETACCESSTOMSFRANKSOFFICETHANITWOULDBETOINFILTRATEJODIESROOMATTHEHOTELTHOSEPLACESTAKETHESECURITYOFTHEIRCLIENTSEVENMORESERIOUSLYTHANTHEBANKSTHEATTACHEDLETTERSHOWSTHATJODIEISGETTINGMORECAUTIOUSBUTITALSOSEEMSTOBEANINVITATIONTOGETINVOLVEDIAMNOTSUREWHERETOGOFROMHEREASJODIESAYSINTHELETTERTHENUMBERSINTHESIGNINBOOKSUGGESTSOMETHINGODDBUTUNLIKEJODIEIWONTHAVEACCESSTOTHEVAULTTOCHECKITISSHEHINTINGTHATWESHOULDTEAMUPORWARNINGMETHATSHEKNOWSIAMHEREANDSHOULDKEEPAWAYIFYOUARENOTSUREWHATIAMTALKINGABOUTTAKEAVERYCAREFULLOOKATYOURDECRYPTOFHERLETTERYOUSHOULDFINDAHIDDENMESSAGEBYTHEWAYTHEREISSOMETHINGNAGGINGATMETHATICANTQUITEPLACETHEREISANAMEINTHESIGNINBOOKTHATINMYHEADATLEASTISCONNECTEDINSOMEWAYTOTHENAMEOFTHEBANKANDICANTREMEMBERWHATTHATCONNECTIONISMAYBEITISNOTIMPORTANTBUTIWONTSLEEPPROPERLYUNTILICANFIGUREITOUTONCEYOUHAVECRACKEDJODIESLETTERHEADOVERTOTHECASEFILESANDTAKEALOOKATTHESIGNATURESMAYBEYOUCANFIGUREITOUTFORMEHARRY")
    test.run()
    test_num += 1

    # 12. Test the simple substitution solver without the key
    test = Test(f"\n{test_num}. Testing simple substitution without key...")
    test.setTest(lambda: simple_sub_solver.solve("R NZMZTVW GL GIZXV QZWV/QLWRV GL Z HFRGV ZG Z SRTS-XOZHH SLGVO WLDMGLDM. GSV HLIG LU KOZXV LMOB Z YZMP XLFOW ZUULIW, ZMW R XLFOWM'G HGZB GSVIV NBHVOU, VEVM RU R DZH LM VCKVMHVH. R GSRMP RG DLFOW SZEV YVVM GVNKGRMT UZGV ZMBDZB. RU R XZM URMW QLWRV, R ZN HFIV HSV XZM URMW NV. HLNVGSRMT RM SVI OVGGVI GVOOH NV HSV ZOIVZWB SZH. RM ZMB XZHV, R WVXRWVW GL PVVK Z OLMT GZRO LM SVI, RU LMOB GL ZELRW HKLLPRMT ZMBLMV VOHV DSL NRTSG YV ULOOLDRMT SVI. R ZN ULXFHRMT LM RMGVIXVKGRMT SVI XLNNH DRGS OBMM UIZMP. GSVB ZIV HGROO FHRMT UZRIOB ORTSG VMXIBKGRLM, ZMW RG RH VZHRVI GL TVG ZXXVHH GL NH UIZMP’H LUURXV GSZM RG DLFOW YV GL RMUROGIZGV QLWRV’H ILLN ZG GSV SLGVO. GSLHV KOZXVH GZPV GSV HVXFIRGB LU GSVRI XORVMGH VEVM NLIV HVIRLFHOB GSZM GSV YZMPH. GSV ZGGZXSVW OVGGVI HSLDH GSZG QLWRV RH TVGGRMT NLIV XZFGRLFH, YFG RG ZOHL HVVNH GL YV ZM RMERGZGRLM GL TVG RMELOEVW. R ZN MLG HFIV DSVIV GL TL UILN SVIV. ZH QLWRV HZBH RM GSV OVGGVI, GSV MFNYVIH RM GSV HRTM-RM YLLP HFTTVHG HLNVGSRMT LWW, YFG FMORPV QLWRV R DLM’G SZEV ZXXVHH GL GSV EZFOG GL XSVXP RG. RH HSV SRMGRMT GSZG DV HSLFOW GVZN FK, LI DZIMRMT NV GSZG HSV PMLDH R ZN SVIV ZMW HSLFOW PVVK ZDZB? (RU BLF ZIV MLG HFIV DSZG R ZN GZOPRMT ZYLFG, GZPV Z EVIB XZIVUFO OLLP ZG BLFI WVXIBKG LU SVI OVGGVI. BLF HSLFOW URMW Z SRWWVM NVHHZTV.) YB GSV DZB, GSVIV RH HLNVGSRMT MZTTRMT ZG NV GSZG R XZM’G JFRGV KOZXV. GSVIV RH Z MZNV RM GSV HRTM-RM YLLP GSZG, RM NB SVZW ZG OVZHG, RH XLMMVXGVW RM HLNV DZB GL GSV MZNV LU GSV YZMP, ZMW R XZM’G IVNVNYVI DSZG GSZG XLMMVXGRLM RH. NZBYV RG RH MLG RNKLIGZMG, YFG R DLM’G HOVVK KILKVIOB FMGRO R XZM URTFIV RG LFG. LMXV BLF SZEV XIZXPVW QLWRV’H OVGGVI, SVZW LEVI GL GSV XZHV UROVH ZMW GZPV Z OLLP ZG GSV HRTMZGFIVH. NZBYV BLF XZM URTFIV RG LFG ULI NV. SZIIB"), "IMANAGEDTOTRACEJADEJODIETOASUITEATAHIGHCLASSHOTELDOWNTOWNTHESORTOFPLACEONLYABANKCOULDAFFORDANDICOULDNTSTAYTHEREMYSELFEVENIFIWASONEXPENSESITHINKITWOULDHAVEBEENTEMPTINGFATEANYWAYIFICANFINDJODIEIAMSURESHECANFINDMESOMETHINGINHERLETTERTELLSMESHEALREADYHASINANYCASEIDECIDEDTOKEEPALONGTAILONHERIFONLYTOAVOIDSPOOKINGANYONEELSEWHOMIGHTBEFOLLOWINGHERIAMFOCUSINGONINTERCEPTINGHERCOMMSWITHLYNNFRANKTHEYARESTILLUSINGFAIRLYLIGHTENCRYPTIONANDITISEASIERTOGETACCESSTOMSFRANKSOFFICETHANITWOULDBETOINFILTRATEJODIESROOMATTHEHOTELTHOSEPLACESTAKETHESECURITYOFTHEIRCLIENTSEVENMORESERIOUSLYTHANTHEBANKSTHEATTACHEDLETTERSHOWSTHATJODIEISGETTINGMORECAUTIOUSBUTITALSOSEEMSTOBEANINVITATIONTOGETINVOLVEDIAMNOTSUREWHERETOGOFROMHEREASJODIESAYSINTHELETTERTHENUMBERSINTHESIGNINBOOKSUGGESTSOMETHINGODDBUTUNLIKEJODIEIWONTHAVEACCESSTOTHEVAULTTOCHECKITISSHEHINTINGTHATWESHOULDTEAMUPORWARNINGMETHATSHEKNOWSIAMHEREANDSHOULDKEEPAWAYIFYOUARENOTSUREWHATIAMTALKINGABOUTTAKEAVERYCAREFULLOOKATYOURDECRYPTOFHERLETTERYOUSHOULDFINDAHIDDENMESSAGEBYTHEWAYTHEREISSOMETHINGNAGGINGATMETHATICANTQUITEPLACETHEREISANAMEINTHESIGNINBOOKTHATINMYHEADATLEASTISCONNECTEDINSOMEWAYTOTHENAMEOFTHEBANKANDICANTREMEMBERWHATTHATCONNECTIONISMAYBEITISNOTIMPORTANTBUTIWONTSLEEPPROPERLYUNTILICANFIGUREITOUTONCEYOUHAVECRACKEDJODIESLETTERHEADOVERTOTHECASEFILESANDTAKEALOOKATTHESIGNATURESMAYBEYOUCANFIGUREITOUTFORMEHARRY")
    test.run()
    test_num += 1

    col_trans_solver = ColTransSolver()
    # 13. Test the permutations generator
    test = Test(f"\n{test_num}. Testing permutations generator...")
    test.setTest(lambda: col_trans_solver.get_permutations(list("ABC")), [['A', 'B', 'C'], ['A', 'C', 'B'], ['B', 'A', 'C'], ['B', 'C', 'A'], ['C', 'A', 'B'], ['C', 'B', 'A']])
    test.run()
    test_num += 1

    # 14. Test the columnar transposition solver with the key
    test = Test(f"\n{test_num}. Testing columnar transposition with key...")
    test.setTest(lambda: col_trans_solver.solve("ATAIUALTNHOEBUOINTYVWXSKLBMFYINERAMTNTLHAIACOLIRYIKYSIFIIUNCGMHRETIRHYASRATAFAUOTOOHLPTEIHIVEUAAEHTWJSNCUTEBVOTVNETOAENTERENUSIBIITCOUHIITSTOIHKAAUPFERIKOECLTEOEOLANGEEONIECICEMENHYTIENAEFNCMWAEIEORUTPLLITCACDTATAEAOETAUGOMYMDCJOEGSDWOLLKAAUTRLIONHWANIEYNOMHIONRRMLHNIEEGNOAPGEHTLHFNTTRWNKRLFLNIISGESSETBFTEAOOCECORTMRYHSTLSHITOTUSSNAOVISEOEOYERMNGOEEOUJWVSETKHITUMAMSWESKAUTHTGTEEOUYEEHIDSYYITAAATPHANGOIAAOEMOMENTBTOIAIMNWEPNARTOCDSRVHFNATGEENEFAIEAETTISLOSPNNDDOSEENSETTHETTAAJASFSIEESAYAEDENOFOSNNWHLGMINPESYNALGYETDAOCMKCIDNAIMHHAKEYINNELTKTDRTDEMUBLMATTNDTHGHJAHEUIIOGMGTEIAEHTCSTAOAWGTOHDDWOOWMNTVROORHTSFIEBAEENGHNETSIIOTEECTOTAHANMACTMTIAILOUCUUYEEEEOTEAEAIRBARTHNOJDSTCOWTTCAOFDDYMEIEENUEEGNFIIUCDEIEESESCETAAELOONLMEWRCORNOTFHSSIGRNIETSRFHOTLJRTEESHRTLEROHBHCTOTIIEOISONIELMREREIIEHEHISTHDLDNATACTHGEDPNTEIEOEIRUTLBKYUADTLYUDEAHHSIGMIUARAHITMATNIWHOAIERHNNBNOBNPRIFINHAOEERCLTOHAMOITRRGRDEIHAETEFOALRCTHSEAPIIDEPAWCDIENEHHTLEDNSIKOLITDIOEGONASIEHMLAYINLTPNETCONINLIRDOETLASTEEESSNNAEESOGGASAEEINIEOWOMSSTTNSSBGONUKEHCTLESNHHERNANMNLAYNEAIUAALYCFTUDHMEWRMGNTATEIESBAHLSCSYNTKAEHTCSITTTSRYIGOEVKITDOSSKKSUYCUUEATEOAAHHONRAYCFNLAEFFNSIOVTNAIFDSENMGLTERAYDDPTHNVOAEOBOEOGEICINTEUAICOTIESFOTWEIESTTSETUFCSOITETAEHAETRITOTITGOAURFRDSLTBTNKSTDNOOESVOIENWLUREHSRHEYASAAAARFKRPRRONDSTTSHGTTQLENTNKNDSNDETEBDRETNOYSPTOEETNEOURJLHEEIDLTNSYFIOR", key="GERMAN"), "IMANAGEDTOTRACEJADEJODIETOASUITEATAHIGHCLASSHOTELDOWNTOWNTHESORTOFPLACEONLYABANKCOULDAFFORDANDICOULDNTSTAYTHEREMYSELFEVENIFIWASONEXPENSESITHINKITWOULDHAVEBEENTEMPTINGFATEANYWAYIFICANFINDJODIEIAMSURESHECANFINDMESOMETHINGINHERLETTERTELLSMESHEALREADYHASINANYCASEIDECIDEDTOKEEPALONGTAILONHERIFONLYTOAVOIDSPOOKINGANYONEELSEWHOMIGHTBEFOLLOWINGHERIAMFOCUSINGONINTERCEPTINGHERCOMMSWITHLYNNFRANKTHEYARESTILLUSINGFAIRLYLIGHTENCRYPTIONANDITISEASIERTOGETACCESSTOMSFRANKSOFFICETHANITWOULDBETOINFILTRATEJODIESROOMATTHEHOTELTHOSEPLACESTAKETHESECURITYOFTHEIRCLIENTSEVENMORESERIOUSLYTHANTHEBANKSTHEATTACHEDLETTERSHOWSTHATJODIEISGETTINGMORECAUTIOUSBUTITALSOSEEMSTOBEANINVITATIONTOGETINVOLVEDIAMNOTSUREWHERETOGOFROMHEREASJODIESAYSINTHELETTERTHENUMBERSINTHESIGNINBOOKSUGGESTSOMETHINGODDBUTUNLIKEJODIEIWONTHAVEACCESSTOTHEVAULTTOCHECKITISSHEHINTINGTHATWESHOULDTEAMUPORWARNINGMETHATSHEKNOWSIAMHEREANDSHOULDKEEPAWAYIFYOUARENOTSUREWHATIAMTALKINGABOUTTAKEAVERYCAREFULLOOKATYOURDECRYPTOFHERLETTERYOUSHOULDFINDAHIDDENMESSAGEBYTHEWAYTHEREISSOMETHINGNAGGINGATMETHATICANTQUITEPLACETHEREISANAMEINTHESIGNINBOOKTHATINMYHEADATLEASTISCONNECTEDINSOMEWAYTOTHENAMEOFTHEBANKANDICANTREMEMBERWHATTHATCONNECTIONISMAYBEITISNOTIMPORTANTBUTIWONTSLEEPPROPERLYUNTILICANFIGUREITOUTONCEYOUHAVECRACKEDJODIESLETTERHEADOVERTOTHECASEFILESANDTAKEALOOKATTHESIGNATURESMAYBEYOUCANFIGUREITOUTFORMEHARRY")
    test.run()
    test_num += 1

    # 15. Test the columnar transposition solver with the key length
    test = Test(f"\n{test_num}. Testing columnar transposition with key length...")
    test.setTest(lambda: col_trans_solver.solve("ATAIUALTNHOEBUOINTYVWXSKLBMFYINERAMTNTLHAIACOLIRYIKYSIFIIUNCGMHRETIRHYASRATAFAUOTOOHLPTEIHIVEUAAEHTWJSNCUTEBVOTVNETOAENTERENUSIBIITCOUHIITSTOIHKAAUPFERIKOECLTEOEOLANGEEONIECICEMENHYTIENAEFNCMWAEIEORUTPLLITCACDTATAEAOETAUGOMYMDCJOEGSDWOLLKAAUTRLIONHWANIEYNOMHIONRRMLHNIEEGNOAPGEHTLHFNTTRWNKRLFLNIISGESSETBFTEAOOCECORTMRYHSTLSHITOTUSSNAOVISEOEOYERMNGOEEOUJWVSETKHITUMAMSWESKAUTHTGTEEOUYEEHIDSYYITAAATPHANGOIAAOEMOMENTBTOIAIMNWEPNARTOCDSRVHFNATGEENEFAIEAETTISLOSPNNDDOSEENSETTHETTAAJASFSIEESAYAEDENOFOSNNWHLGMINPESYNALGYETDAOCMKCIDNAIMHHAKEYINNELTKTDRTDEMUBLMATTNDTHGHJAHEUIIOGMGTEIAEHTCSTAOAWGTOHDDWOOWMNTVROORHTSFIEBAEENGHNETSIIOTEECTOTAHANMACTMTIAILOUCUUYEEEEOTEAEAIRBARTHNOJDSTCOWTTCAOFDDYMEIEENUEEGNFIIUCDEIEESESCETAAELOONLMEWRCORNOTFHSSIGRNIETSRFHOTLJRTEESHRTLEROHBHCTOTIIEOISONIELMREREIIEHEHISTHDLDNATACTHGEDPNTEIEOEIRUTLBKYUADTLYUDEAHHSIGMIUARAHITMATNIWHOAIERHNNBNOBNPRIFINHAOEERCLTOHAMOITRRGRDEIHAETEFOALRCTHSEAPIIDEPAWCDIENEHHTLEDNSIKOLITDIOEGONASIEHMLAYINLTPNETCONINLIRDOETLASTEEESSNNAEESOGGASAEEINIEOWOMSSTTNSSBGONUKEHCTLESNHHERNANMNLAYNEAIUAALYCFTUDHMEWRMGNTATEIESBAHLSCSYNTKAEHTCSITTTSRYIGOEVKITDOSSKKSUYCUUEATEOAAHHONRAYCFNLAEFFNSIOVTNAIFDSENMGLTERAYDDPTHNVOAEOBOEOGEICINTEUAICOTIESFOTWEIESTTSETUFCSOITETAEHAETRITOTITGOAURFRDSLTBTNKSTDNOOESVOIENWLUREHSRHEYASAAAARFKRPRRONDSTTSHGTTQLENTNKNDSNDETEBDRETNOYSPTOEETNEOURJLHEEIDLTNSYFIOR", keylen=6), "IMANAGEDTOTRACEJADEJODIETOASUITEATAHIGHCLASSHOTELDOWNTOWNTHESORTOFPLACEONLYABANKCOULDAFFORDANDICOULDNTSTAYTHEREMYSELFEVENIFIWASONEXPENSESITHINKITWOULDHAVEBEENTEMPTINGFATEANYWAYIFICANFINDJODIEIAMSURESHECANFINDMESOMETHINGINHERLETTERTELLSMESHEALREADYHASINANYCASEIDECIDEDTOKEEPALONGTAILONHERIFONLYTOAVOIDSPOOKINGANYONEELSEWHOMIGHTBEFOLLOWINGHERIAMFOCUSINGONINTERCEPTINGHERCOMMSWITHLYNNFRANKTHEYARESTILLUSINGFAIRLYLIGHTENCRYPTIONANDITISEASIERTOGETACCESSTOMSFRANKSOFFICETHANITWOULDBETOINFILTRATEJODIESROOMATTHEHOTELTHOSEPLACESTAKETHESECURITYOFTHEIRCLIENTSEVENMORESERIOUSLYTHANTHEBANKSTHEATTACHEDLETTERSHOWSTHATJODIEISGETTINGMORECAUTIOUSBUTITALSOSEEMSTOBEANINVITATIONTOGETINVOLVEDIAMNOTSUREWHERETOGOFROMHEREASJODIESAYSINTHELETTERTHENUMBERSINTHESIGNINBOOKSUGGESTSOMETHINGODDBUTUNLIKEJODIEIWONTHAVEACCESSTOTHEVAULTTOCHECKITISSHEHINTINGTHATWESHOULDTEAMUPORWARNINGMETHATSHEKNOWSIAMHEREANDSHOULDKEEPAWAYIFYOUARENOTSUREWHATIAMTALKINGABOUTTAKEAVERYCAREFULLOOKATYOURDECRYPTOFHERLETTERYOUSHOULDFINDAHIDDENMESSAGEBYTHEWAYTHEREISSOMETHINGNAGGINGATMETHATICANTQUITEPLACETHEREISANAMEINTHESIGNINBOOKTHATINMYHEADATLEASTISCONNECTEDINSOMEWAYTOTHENAMEOFTHEBANKANDICANTREMEMBERWHATTHATCONNECTIONISMAYBEITISNOTIMPORTANTBUTIWONTSLEEPPROPERLYUNTILICANFIGUREITOUTONCEYOUHAVECRACKEDJODIESLETTERHEADOVERTOTHECASEFILESANDTAKEALOOKATTHESIGNATURESMAYBEYOUCANFIGUREITOUTFORMEHARRY")
    test.run()
    test_num += 1

    # 16. Test the columnar transposition solver using brute force
    test = Test(f"\n{test_num}. Testing columnar transposition without key...")
    test.setTest(lambda: col_trans_solver.solve("ATAIUALTNHOEBUOINTYVWXSKLBMFYINERAMTNTLHAIACOLIRYIKYSIFIIUNCGMHRETIRHYASRATAFAUOTOOHLPTEIHIVEUAAEHTWJSNCUTEBVOTVNETOAENTERENUSIBIITCOUHIITSTOIHKAAUPFERIKOECLTEOEOLANGEEONIECICEMENHYTIENAEFNCMWAEIEORUTPLLITCACDTATAEAOETAUGOMYMDCJOEGSDWOLLKAAUTRLIONHWANIEYNOMHIONRRMLHNIEEGNOAPGEHTLHFNTTRWNKRLFLNIISGESSETBFTEAOOCECORTMRYHSTLSHITOTUSSNAOVISEOEOYERMNGOEEOUJWVSETKHITUMAMSWESKAUTHTGTEEOUYEEHIDSYYITAAATPHANGOIAAOEMOMENTBTOIAIMNWEPNARTOCDSRVHFNATGEENEFAIEAETTISLOSPNNDDOSEENSETTHETTAAJASFSIEESAYAEDENOFOSNNWHLGMINPESYNALGYETDAOCMKCIDNAIMHHAKEYINNELTKTDRTDEMUBLMATTNDTHGHJAHEUIIOGMGTEIAEHTCSTAOAWGTOHDDWOOWMNTVROORHTSFIEBAEENGHNETSIIOTEECTOTAHANMACTMTIAILOUCUUYEEEEOTEAEAIRBARTHNOJDSTCOWTTCAOFDDYMEIEENUEEGNFIIUCDEIEESESCETAAELOONLMEWRCORNOTFHSSIGRNIETSRFHOTLJRTEESHRTLEROHBHCTOTIIEOISONIELMREREIIEHEHISTHDLDNATACTHGEDPNTEIEOEIRUTLBKYUADTLYUDEAHHSIGMIUARAHITMATNIWHOAIERHNNBNOBNPRIFINHAOEERCLTOHAMOITRRGRDEIHAETEFOALRCTHSEAPIIDEPAWCDIENEHHTLEDNSIKOLITDIOEGONASIEHMLAYINLTPNETCONINLIRDOETLASTEEESSNNAEESOGGASAEEINIEOWOMSSTTNSSBGONUKEHCTLESNHHERNANMNLAYNEAIUAALYCFTUDHMEWRMGNTATEIESBAHLSCSYNTKAEHTCSITTTSRYIGOEVKITDOSSKKSUYCUUEATEOAAHHONRAYCFNLAEFFNSIOVTNAIFDSENMGLTERAYDDPTHNVOAEOBOEOGEICINTEUAICOTIESFOTWEIESTTSETUFCSOITETAEHAETRITOTITGOAURFRDSLTBTNKSTDNOOESVOIENWLUREHSRHEYASAAAARFKRPRRONDSTTSHGTTQLENTNKNDSNDETEBDRETNOYSPTOEETNEOURJLHEEIDLTNSYFIOR"), "IMANAGEDTOTRACEJADEJODIETOASUITEATAHIGHCLASSHOTELDOWNTOWNTHESORTOFPLACEONLYABANKCOULDAFFORDANDICOULDNTSTAYTHEREMYSELFEVENIFIWASONEXPENSESITHINKITWOULDHAVEBEENTEMPTINGFATEANYWAYIFICANFINDJODIEIAMSURESHECANFINDMESOMETHINGINHERLETTERTELLSMESHEALREADYHASINANYCASEIDECIDEDTOKEEPALONGTAILONHERIFONLYTOAVOIDSPOOKINGANYONEELSEWHOMIGHTBEFOLLOWINGHERIAMFOCUSINGONINTERCEPTINGHERCOMMSWITHLYNNFRANKTHEYARESTILLUSINGFAIRLYLIGHTENCRYPTIONANDITISEASIERTOGETACCESSTOMSFRANKSOFFICETHANITWOULDBETOINFILTRATEJODIESROOMATTHEHOTELTHOSEPLACESTAKETHESECURITYOFTHEIRCLIENTSEVENMORESERIOUSLYTHANTHEBANKSTHEATTACHEDLETTERSHOWSTHATJODIEISGETTINGMORECAUTIOUSBUTITALSOSEEMSTOBEANINVITATIONTOGETINVOLVEDIAMNOTSUREWHERETOGOFROMHEREASJODIESAYSINTHELETTERTHENUMBERSINTHESIGNINBOOKSUGGESTSOMETHINGODDBUTUNLIKEJODIEIWONTHAVEACCESSTOTHEVAULTTOCHECKITISSHEHINTINGTHATWESHOULDTEAMUPORWARNINGMETHATSHEKNOWSIAMHEREANDSHOULDKEEPAWAYIFYOUARENOTSUREWHATIAMTALKINGABOUTTAKEAVERYCAREFULLOOKATYOURDECRYPTOFHERLETTERYOUSHOULDFINDAHIDDENMESSAGEBYTHEWAYTHEREISSOMETHINGNAGGINGATMETHATICANTQUITEPLACETHEREISANAMEINTHESIGNINBOOKTHATINMYHEADATLEASTISCONNECTEDINSOMEWAYTOTHENAMEOFTHEBANKANDICANTREMEMBERWHATTHATCONNECTIONISMAYBEITISNOTIMPORTANTBUTIWONTSLEEPPROPERLYUNTILICANFIGUREITOUTONCEYOUHAVECRACKEDJODIESLETTERHEADOVERTOTHECASEFILESANDTAKEALOOKATTHESIGNATURESMAYBEYOUCANFIGUREITOUTFORMEHARRY")
    test.run()
    test_num += 1

    trans_solver = TranspositionSolver()
    # 17. Test the basic transposition solver with the key
    test = Test(f"\n{test_num}. Testing basic transposition with key...")
    test.setTest(lambda: trans_solver.solve("TyrraHpmalehethgilevagsrxobaemcartotmllaTkpsegdaisenohnalangllofIdihdewohtronmuotsaeluCfotorepepihehtnIyawhgdesolcwodmihatsujnsawehsniniojSIehtgiSytximidnaxtaidemsiwyleahIdehweWtndaehereofgnidihsaWranotgngebIdnegotnafdabatgnileeituobactahTtlatsyridesiledaotnaenupessenisutehsafodenrtotnofroeGehnwotegnaekiPlaerIdhwdesiweheredaehsaheWgnirpaevaImelboodtsujwonktnostahwohrotrubgibweenewtnifotduqtuodIylkcidekcabdnaffoehttuciecartiesacnggirttnadereamotuaelacitahehtrseccasolaotsteromtlonhceahtygoaodewnnacIdnrusebtttahtenohpehecarteednusibatcetsmaIelahterumesihtreyolpnlliwsahebtofotyppoemdniatsihnIdnaliiatrecnodylnttnawtdnepsoniemitmesabayrttneeotgninialpxflesymmehtotellacIhtffodlpmalerethgirofebscyehteerdluowesilaawehohikrowsIrofgnnosawtgnihtegniksaofmehtovafarnehwruguohtIsihtthorasawcenitucremmonoclaibtcartsitituehtonaritnerdotyleehtgartotnimelohehsItahthotmeegudevasymroflaIfleevahosotannAoknihtcsawIfedifnouocItnllofdlllaTwowegdamtuohtivocsiddnayrepohdahowehdeaeldluhotemdItubrektndidehtwonwIohwnebdluoiagaputiWtsnerehthecruosliwehsaevahlbaliaviwtielahebllvaotdrteddionoitceyatsybawagnilatelyfybenoiwollotmihgnfoehtopIecifhotnalipuelonilrAntInotgdluohsysubebhguoneevigotevocemoynaCrmniojuWerehetdeeneaekamoalpweneidoJn", key="FEDCBA"), "HARRYTHELAMPLIGHTERSGAVEMEABOXTOTRACKTALLMADGESPHONESIGNALANDIFOLLOWEDHIMNORTHEASTOUTOFCULPEPERONTHEHIGHWAYICLOSEDHIMDOWNJUSTASHEWASJOININGTHEISIXTYSIXANDIMMEDIATELYWISHEDIHADNTWEWEREHEADINGFORWASHINGTONANDIBEGANTOGETABADFEELINGABOUTITTHATCRYSTALLISEDINTOADEEPUNEASINESSASHETURNEDOFFONTOTHEGEORGETOWNPIKEANDIREALISEDWHEREHEWASHEADINGWEHAVEAPROBLEMIJUSTDONTKNOWWHATSORTORHOWBIGBUTWENEEDTOFINDOUTQUICKLYIBACKEDOFFANDCUTTHETRACEINCASEITTRIGGEREDANAUTOMATICALERTHEHASACCESSTOALOTMORETECHNOLOGYTHANWEDOANDICANTBESURETHATTHEPHONETRACEISUNDETECTABLEIAMSURETHATHISEMPLOYERSWILLNOTBEHAPPYTOFINDMEONHISTAILANDICERTAINLYDONTWANTTOSPENDTIMEINABASEMENTTRYINGTOEXPLAINMYSELFTOTHEMICALLEDOFFTHELAMPLIGHTERSBEFORETHEYCOULDREALISEWHOHEWASWORKINGFORITWASONETHINGASKINGTHEMFORAFAVOURWHENITHOUGHTTHISWASAROUTINECOMMERCIALCONTRACTBUTITISANOTHERENTIRELYTODRAGTHEMINTOTHEHOLETHATISEEMTOHAVEDUGFORMYSELFIALSOHAVEANNATOTHINKOFIWASCONFIDENTICOULDFOLLOWTALLMADGEWITHOUTDISCOVERYANDHADHOPEDHEWOULDLEADMETOHERBUTIDIDNTKNOWTHENWHOIWOULDBEUPAGAINSTWITHTHERESOURCESHEWILLHAVEAVAILABLEITWILLBEHARDTOAVOIDDETECTIONBYSTAYINGAWAYLETALONEBYFOLLOWINGHIMTOTHEOFFICEIPLANTOHOLEUPINARLINGTONITSHOULDBEBUSYENOUGHTOGIVEMECOVERCANYOUJOINMEHEREWENEEDTOMAKEANEWPLANJODIE")
    test.run()
    test_num += 1

    # 18. Test the basic transposition solver with the key length
    test = Test(f"\n{test_num}. Testing basic transposition with key length...")
    test.setTest(lambda: trans_solver.solve("TyrraHpmalehethgilevagsrxobaemcartotmllaTkpsegdaisenohnalangllofIdihdewohtronmuotsaeluCfotorepepihehtnIyawhgdesolcwodmihatsujnsawehsniniojSIehtgiSytximidnaxtaidemsiwyleahIdehweWtndaehereofgnidihsaWranotgngebIdnegotnafdabatgnileeituobactahTtlatsyridesiledaotnaenupessenisutehsafodenrtotnofroeGehnwotegnaekiPlaerIdhwdesiweheredaehsaheWgnirpaevaImelboodtsujwonktnostahwohrotrubgibweenewtnifotduqtuodIylkcidekcabdnaffoehttuciecartiesacnggirttnadereamotuaelacitahehtrseccasolaotsteromtlonhceahtygoaodewnnacIdnrusebtttahtenohpehecarteednusibatcetsmaIelahterumesihtreyolpnlliwsahebtofotyppoemdniatsihnIdnaliiatrecnodylnttnawtdnepsoniemitmesabayrttneeotgninialpxflesymmehtotellacIhtffodlpmalerethgirofebscyehteerdluowesilaawehohikrowsIrofgnnosawtgnihtegniksaofmehtovafarnehwruguohtIsihtthorasawcenitucremmonoclaibtcartsitituehtonaritnerdotyleehtgartotnimelohehsItahthotmeegudevasymroflaIfleevahosotannAoknihtcsawIfedifnouocItnllofdlllaTwowegdamtuohtivocsiddnayrepohdahowehdeaeldluhotemdItubrektndidehtwonwIohwnebdluoiagaputiWtsnerehthecruosliwehsaevahlbaliaviwtielahebllvaotdrteddionoitceyatsybawagnilatelyfybenoiwollotmihgnfoehtopIecifhotnalipuelonilrAntInotgdluohsysubebhguoneevigotevocemoynaCrmniojuWerehetdeeneaekamoalpweneidoJn", keylen=6), "HARRYTHELAMPLIGHTERSGAVEMEABOXTOTRACKTALLMADGESPHONESIGNALANDIFOLLOWEDHIMNORTHEASTOUTOFCULPEPERONTHEHIGHWAYICLOSEDHIMDOWNJUSTASHEWASJOININGTHEISIXTYSIXANDIMMEDIATELYWISHEDIHADNTWEWEREHEADINGFORWASHINGTONANDIBEGANTOGETABADFEELINGABOUTITTHATCRYSTALLISEDINTOADEEPUNEASINESSASHETURNEDOFFONTOTHEGEORGETOWNPIKEANDIREALISEDWHEREHEWASHEADINGWEHAVEAPROBLEMIJUSTDONTKNOWWHATSORTORHOWBIGBUTWENEEDTOFINDOUTQUICKLYIBACKEDOFFANDCUTTHETRACEINCASEITTRIGGEREDANAUTOMATICALERTHEHASACCESSTOALOTMORETECHNOLOGYTHANWEDOANDICANTBESURETHATTHEPHONETRACEISUNDETECTABLEIAMSURETHATHISEMPLOYERSWILLNOTBEHAPPYTOFINDMEONHISTAILANDICERTAINLYDONTWANTTOSPENDTIMEINABASEMENTTRYINGTOEXPLAINMYSELFTOTHEMICALLEDOFFTHELAMPLIGHTERSBEFORETHEYCOULDREALISEWHOHEWASWORKINGFORITWASONETHINGASKINGTHEMFORAFAVOURWHENITHOUGHTTHISWASAROUTINECOMMERCIALCONTRACTBUTITISANOTHERENTIRELYTODRAGTHEMINTOTHEHOLETHATISEEMTOHAVEDUGFORMYSELFIALSOHAVEANNATOTHINKOFIWASCONFIDENTICOULDFOLLOWTALLMADGEWITHOUTDISCOVERYANDHADHOPEDHEWOULDLEADMETOHERBUTIDIDNTKNOWTHENWHOIWOULDBEUPAGAINSTWITHTHERESOURCESHEWILLHAVEAVAILABLEITWILLBEHARDTOAVOIDDETECTIONBYSTAYINGAWAYLETALONEBYFOLLOWINGHIMTOTHEOFFICEIPLANTOHOLEUPINARLINGTONITSHOULDBEBUSYENOUGHTOGIVEMECOVERCANYOUJOINMEHEREWENEEDTOMAKEANEWPLANJODIE")
    test.run()
    test_num += 1

    # 19. Test the basic transposition solver using brute force
    test = Test(f"\n{test_num}. Testing basic transposition without key...")
    test.setTest(lambda: trans_solver.solve("TyrraHpmalehethgilevagsrxobaemcartotmllaTkpsegdaisenohnalangllofIdihdewohtronmuotsaeluCfotorepepihehtnIyawhgdesolcwodmihatsujnsawehsniniojSIehtgiSytximidnaxtaidemsiwyleahIdehweWtndaehereofgnidihsaWranotgngebIdnegotnafdabatgnileeituobactahTtlatsyridesiledaotnaenupessenisutehsafodenrtotnofroeGehnwotegnaekiPlaerIdhwdesiweheredaehsaheWgnirpaevaImelboodtsujwonktnostahwohrotrubgibweenewtnifotduqtuodIylkcidekcabdnaffoehttuciecartiesacnggirttnadereamotuaelacitahehtrseccasolaotsteromtlonhceahtygoaodewnnacIdnrusebtttahtenohpehecarteednusibatcetsmaIelahterumesihtreyolpnlliwsahebtofotyppoemdniatsihnIdnaliiatrecnodylnttnawtdnepsoniemitmesabayrttneeotgninialpxflesymmehtotellacIhtffodlpmalerethgirofebscyehteerdluowesilaawehohikrowsIrofgnnosawtgnihtegniksaofmehtovafarnehwruguohtIsihtthorasawcenitucremmonoclaibtcartsitituehtonaritnerdotyleehtgartotnimelohehsItahthotmeegudevasymroflaIfleevahosotannAoknihtcsawIfedifnouocItnllofdlllaTwowegdamtuohtivocsiddnayrepohdahowehdeaeldluhotemdItubrektndidehtwonwIohwnebdluoiagaputiWtsnerehthecruosliwehsaevahlbaliaviwtielahebllvaotdrteddionoitceyatsybawagnilatelyfybenoiwollotmihgnfoehtopIecifhotnalipuelonilrAntInotgdluohsysubebhguoneevigotevocemoynaCrmniojuWerehetdeeneaekamoalpweneidoJn"), "HARRYTHELAMPLIGHTERSGAVEMEABOXTOTRACKTALLMADGESPHONESIGNALANDIFOLLOWEDHIMNORTHEASTOUTOFCULPEPERONTHEHIGHWAYICLOSEDHIMDOWNJUSTASHEWASJOININGTHEISIXTYSIXANDIMMEDIATELYWISHEDIHADNTWEWEREHEADINGFORWASHINGTONANDIBEGANTOGETABADFEELINGABOUTITTHATCRYSTALLISEDINTOADEEPUNEASINESSASHETURNEDOFFONTOTHEGEORGETOWNPIKEANDIREALISEDWHEREHEWASHEADINGWEHAVEAPROBLEMIJUSTDONTKNOWWHATSORTORHOWBIGBUTWENEEDTOFINDOUTQUICKLYIBACKEDOFFANDCUTTHETRACEINCASEITTRIGGEREDANAUTOMATICALERTHEHASACCESSTOALOTMORETECHNOLOGYTHANWEDOANDICANTBESURETHATTHEPHONETRACEISUNDETECTABLEIAMSURETHATHISEMPLOYERSWILLNOTBEHAPPYTOFINDMEONHISTAILANDICERTAINLYDONTWANTTOSPENDTIMEINABASEMENTTRYINGTOEXPLAINMYSELFTOTHEMICALLEDOFFTHELAMPLIGHTERSBEFORETHEYCOULDREALISEWHOHEWASWORKINGFORITWASONETHINGASKINGTHEMFORAFAVOURWHENITHOUGHTTHISWASAROUTINECOMMERCIALCONTRACTBUTITISANOTHERENTIRELYTODRAGTHEMINTOTHEHOLETHATISEEMTOHAVEDUGFORMYSELFIALSOHAVEANNATOTHINKOFIWASCONFIDENTICOULDFOLLOWTALLMADGEWITHOUTDISCOVERYANDHADHOPEDHEWOULDLEADMETOHERBUTIDIDNTKNOWTHENWHOIWOULDBEUPAGAINSTWITHTHERESOURCESHEWILLHAVEAVAILABLEITWILLBEHARDTOAVOIDDETECTIONBYSTAYINGAWAYLETALONEBYFOLLOWINGHIMTOTHEOFFICEIPLANTOHOLEUPINARLINGTONITSHOULDBEBUSYENOUGHTOGIVEMECOVERCANYOUJOINMEHEREWENEEDTOMAKEANEWPLANJODIE")
    test.run()
    test_num += 1

    railfence_solver = RailfenceSolver()
    # 20. Test the railfence solver with known number of rails
    test = Test(f"\n{test_num}. Testing Rail Fence with known number of rails...")
    test.setTest(lambda: railfence_solver.solve("HGCETAATTOLIXORUALDSBOUAINILTLEASSWSUWITLGBEALEPCUOABTHVUDAMEONYHLOJRSAYOAYGBSHEHBEEROYAITAOLYLFFTIOEOFEERUOSOEYORELASIWOAEEHEGNSINTTASNTAEDMACTTDCOLTERITTUNIYNAWEDITDNTEAIEAGHHCMIDGIHREVAIMUILDOHCTANPANTONHDESNFIURDBECGCAESHINNTEHORSEGTLLHTECYAICMHHDGHMHAESREIWDNEENTUNCIMEATUTAEFNOUEHSEILNREEPIIIMEGEANHNOTIRTWEROEYYRLGRNNSOEWORTHTNPAEHLSFHMIDELEEWGHOEEEEDEERRSOINWOOIRDTWBIEEGIRVEAEOEDDIBINDDWRFCDRDNTMTTEFSIHCTTMIAEUWWDAELORMGLHONHINUOEEOIAAOOUHDATLEEKELHAYFLHTTIDWCICEPDLTWAADGPFSHTNRNMASANINFBWSNAEHSNLDISLIAINEWLAONNXDNAEFIARDTATNITINETSHAIIRTEOMEDNLOYFGMEIMWOJINABEOLVOOEUODEHFLMOROGTCEELCAPIIHVLFTENGLERUSTNODNAESUHTLICIOYETEHNHRNLFSDODAAAEOOVEHLDESYWOUATEATTTOACASTDSHTEIOETOIAGHNGVOTENIETAHPTTETTOORPAQTMOAREYOAEHWHUMIHAWEDTAETAHIGDETIEAXWGITTIRHUUATNTMPNBMGATGMRELIWAKPADLTTOTRKMPSIENTNHDOWICTSTEPPTAIISEHOEHSFIHNUVROOSTOSCNLHSRITIENBWCDISBNLAWNCLWNTCLTOOTDOEAANTHHMEGAOUEIEHHDGALOKNCEEOOHAIAPOOTEYOHKHNWBIHEMOGAIARRCWEHSAEEEENLAACSHYENELMRSHNTTANOATDLEBIUUKDVTTFAHEATSOKMKYFLCUPEBTMLAKAIIONVIUYHLABYHLOEOEOHOSTAWCIRIITIFEARERTTIELIWSTDIEHTREUBLFGDNAJMTETJGDRRLGPJNBORSEHSOOTDENTWURMATDENOLLONBENNEXAUONIOYLENUOADTATTWNSDOHGIAOAENOIVWWEILIEYEAAOSOIINFSATWSDCEHHHTILPNFTFRSRGHNTSOHIIWLWBSWLBTNGTOTKEALEFOATACOTOUP", key=28), "HARRYTHELAMPLIGHTERSGAVEMEABOXTOTRACKTALLMADGESPHONESIGNALANDIFOLLOWEDHIMNORTHEASTOUTOFCULPEPERONTHEHIGHWAYICLOSEDHIMDOWNJUSTASHEWASJOININGTHEISIXTYSIXANDIMMEDIATELYWISHEDIHADNTWEWEREHEADINGFORWASHINGTONANDIBEGANTOGETABADFEELINGABOUTITTHATCRYSTALLISEDINTOADEEPUNEASINESSASHETURNEDOFFONTOTHEGEORGETOWNPIKEANDIREALISEDWHEREHEWASHEADINGWEHAVEAPROBLEMIJUSTDONTKNOWWHATSORTORHOWBIGBUTWENEEDTOFINDOUTQUICKLYIBACKEDOFFANDCUTTHETRACEINCASEITTRIGGEREDANAUTOMATICALERTHEHASACCESSTOALOTMORETECHNOLOGYTHANWEDOANDICANTBESURETHATTHEPHONETRACEISUNDETECTABLEIAMSURETHATHISEMPLOYERSWILLNOTBEHAPPYTOFINDMEONHISTAILANDICERTAINLYDONTWANTTOSPENDTIMEINABASEMENTTRYINGTOEXPLAINMYSELFTOTHEMICALLEDOFFTHELAMPLIGHTERSBEFORETHEYCOULDREALISEWHOHEWASWORKINGFORITWASONETHINGASKINGTHEMFORAFAVOURWHENITHOUGHTTHISWASAROUTINECOMMERCIALCONTRACTBUTITISANOTHERENTIRELYTODRAGTHEMINTOTHEHOLETHATISEEMTOHAVEDUGFORMYSELFIALSOHAVEANNATOTHINKOFIWASCONFIDENTICOULDFOLLOWTALLMADGEWITHOUTDISCOVERYANDHADHOPEDHEWOULDLEADMETOHERBUTIDIDNTKNOWTHENWHOIWOULDBEUPAGAINSTWITHTHERESOURCESHEWILLHAVEAVAILABLEITWILLBEHARDTOAVOIDDETECTIONBYSTAYINGAWAYLETALONEBYFOLLOWINGHIMTOTHEOFFICEIPLANTOHOLEUPINARLINGTONITSHOULDBEBUSYENOUGHTOGIVEMECOVERCANYOUJOINMEHEREWENEEDTOMAKEANEWPLANJODIE")
    test.run()
    test_num += 1

    # 21. Test the railfence solver with unknown number of rails
    test = Test(f"\n{test_num}. Testing Rail Fence with unknown number of rails...")
    test.setTest(lambda: railfence_solver.solve("HGCETAATTOLIXORUALDSBOUAINILTLEASSWSUWITLGBEALEPCUOABTHVUDAMEONYHLOJRSAYOAYGBSHEHBEEROYAITAOLYLFFTIOEOFEERUOSOEYORELASIWOAEEHEGNSINTTASNTAEDMACTTDCOLTERITTUNIYNAWEDITDNTEAIEAGHHCMIDGIHREVAIMUILDOHCTANPANTONHDESNFIURDBECGCAESHINNTEHORSEGTLLHTECYAICMHHDGHMHAESREIWDNEENTUNCIMEATUTAEFNOUEHSEILNREEPIIIMEGEANHNOTIRTWEROEYYRLGRNNSOEWORTHTNPAEHLSFHMIDELEEWGHOEEEEDEERRSOINWOOIRDTWBIEEGIRVEAEOEDDIBINDDWRFCDRDNTMTTEFSIHCTTMIAEUWWDAELORMGLHONHINUOEEOIAAOOUHDATLEEKELHAYFLHTTIDWCICEPDLTWAADGPFSHTNRNMASANINFBWSNAEHSNLDISLIAINEWLAONNXDNAEFIARDTATNITINETSHAIIRTEOMEDNLOYFGMEIMWOJINABEOLVOOEUODEHFLMOROGTCEELCAPIIHVLFTENGLERUSTNODNAESUHTLICIOYETEHNHRNLFSDODAAAEOOVEHLDESYWOUATEATTTOACASTDSHTEIOETOIAGHNGVOTENIETAHPTTETTOORPAQTMOAREYOAEHWHUMIHAWEDTAETAHIGDETIEAXWGITTIRHUUATNTMPNBMGATGMRELIWAKPADLTTOTRKMPSIENTNHDOWICTSTEPPTAIISEHOEHSFIHNUVROOSTOSCNLHSRITIENBWCDISBNLAWNCLWNTCLTOOTDOEAANTHHMEGAOUEIEHHDGALOKNCEEOOHAIAPOOTEYOHKHNWBIHEMOGAIARRCWEHSAEEEENLAACSHYENELMRSHNTTANOATDLEBIUUKDVTTFAHEATSOKMKYFLCUPEBTMLAKAIIONVIUYHLABYHLOEOEOHOSTAWCIRIITIFEARERTTIELIWSTDIEHTREUBLFGDNAJMTETJGDRRLGPJNBORSEHSOOTDENTWURMATDENOLLONBENNEXAUONIOYLENUOADTATTWNSDOHGIAOAENOIVWWEILIEYEAAOSOIINFSATWSDCEHHHTILPNFTFRSRGHNTSOHIIWLWBSWLBTNGTOTKEALEFOATACOTOUP"), "HARRYTHELAMPLIGHTERSGAVEMEABOXTOTRACKTALLMADGESPHONESIGNALANDIFOLLOWEDHIMNORTHEASTOUTOFCULPEPERONTHEHIGHWAYICLOSEDHIMDOWNJUSTASHEWASJOININGTHEISIXTYSIXANDIMMEDIATELYWISHEDIHADNTWEWEREHEADINGFORWASHINGTONANDIBEGANTOGETABADFEELINGABOUTITTHATCRYSTALLISEDINTOADEEPUNEASINESSASHETURNEDOFFONTOTHEGEORGETOWNPIKEANDIREALISEDWHEREHEWASHEADINGWEHAVEAPROBLEMIJUSTDONTKNOWWHATSORTORHOWBIGBUTWENEEDTOFINDOUTQUICKLYIBACKEDOFFANDCUTTHETRACEINCASEITTRIGGEREDANAUTOMATICALERTHEHASACCESSTOALOTMORETECHNOLOGYTHANWEDOANDICANTBESURETHATTHEPHONETRACEISUNDETECTABLEIAMSURETHATHISEMPLOYERSWILLNOTBEHAPPYTOFINDMEONHISTAILANDICERTAINLYDONTWANTTOSPENDTIMEINABASEMENTTRYINGTOEXPLAINMYSELFTOTHEMICALLEDOFFTHELAMPLIGHTERSBEFORETHEYCOULDREALISEWHOHEWASWORKINGFORITWASONETHINGASKINGTHEMFORAFAVOURWHENITHOUGHTTHISWASAROUTINECOMMERCIALCONTRACTBUTITISANOTHERENTIRELYTODRAGTHEMINTOTHEHOLETHATISEEMTOHAVEDUGFORMYSELFIALSOHAVEANNATOTHINKOFIWASCONFIDENTICOULDFOLLOWTALLMADGEWITHOUTDISCOVERYANDHADHOPEDHEWOULDLEADMETOHERBUTIDIDNTKNOWTHENWHOIWOULDBEUPAGAINSTWITHTHERESOURCESHEWILLHAVEAVAILABLEITWILLBEHARDTOAVOIDDETECTIONBYSTAYINGAWAYLETALONEBYFOLLOWINGHIMTOTHEOFFICEIPLANTOHOLEUPINARLINGTONITSHOULDBEBUSYENOUGHTOGIVEMECOVERCANYOUJOINMEHEREWENEEDTOMAKEANEWPLANJODIE")
    test.run()
    test_num += 1

    vigenere_solver = VigenereSolver()
    # 22. Test the permutations with cycles generator
    test = Test(f"\n{test_num}. Testing permutations with cycles generator...")
    test.setTest(lambda: vigenere_solver.get_permutations(list("ABCDE"), 3), [['A', 'B', 'C'], ['A', 'B', 'D'], ['A', 'B', 'E'], ['A', 'C', 'B'], ['A', 'C', 'D'], ['A', 'C', 'E'], ['A', 'D', 'B'], ['A', 'D', 'C'], ['A', 'D', 'E'], ['A', 'E', 'B'], ['A', 'E', 'C'], ['A', 'E', 'D'], ['B', 'A', 'C'], ['B', 'A', 'D'], ['B', 'A', 'E'], ['B', 'C', 'A'], ['B', 'C', 'D'], ['B', 'C', 'E'], ['B', 'D', 'A'], ['B', 'D', 'C'], ['B', 'D', 'E'], ['B', 'E', 'A'], ['B', 'E', 'C'], ['B', 'E', 'D'], ['C', 'A', 'B'], ['C', 'A', 'D'], ['C', 'A', 'E'], ['C', 'B', 'A'], ['C', 'B', 'D'], ['C', 'B', 'E'], ['C', 'D', 'A'], ['C', 'D', 'B'], ['C', 'D', 'E'], ['C', 'E', 'A'], ['C', 'E', 'B'], ['C', 'E', 'D'], ['D', 'A', 'B'], ['D', 'A', 'C'], ['D', 'A', 'E'], ['D', 'B', 'A'], ['D', 'B', 'C'], ['D', 'B', 'E'], ['D', 'C', 'A'], ['D', 'C', 'B'], ['D', 'C', 'E'], ['D', 'E', 'A'], ['D', 'E', 'B'], ['D', 'E', 'C'], ['E', 'A', 'B'], ['E', 'A', 'C'], ['E', 'A', 'D'], ['E', 'B', 'A'], ['E', 'B', 'C'], ['E', 'B', 'D'], ['E', 'C', 'A'], ['E', 'C', 'B'], ['E', 'C', 'D'], ['E', 'D', 'A'], ['E', 'D', 'B'], ['E', 'D', 'C']])
    test.run()
    test_num += 1

    # 23. Test the vigenere solver with a known key
    test = Test(f"\n{test_num}. Testing vigenere with key...")
    test.setTest(lambda: vigenere_solver.solve("Neidy, Gni cmmcrmxttrxw xmvr si r nok zs kdapq Xrxlzghxq’s cnseq svmrrx aaj M walyuavp hvs rfdtukejf ohz sw Ouyvigqr bt xyq hvmlnmy. V ipfeeq nmd pojt nlet ny lv iaf pszziam xyq I Fobkk-Svd eep izsiuuagkpp iifniu U hnjr’k. Ie jkvv tenjmes fbx Arehvtkkan, nth Z netgr ka grz e smd skicunt gffgt vz. Xymt pxcjfayrmjqd vtxf m drkt lzenymeqsf gw yq thxrvp osl sefo gni Xqoemikawa Vmbq aaj M iqayowvp wukvv te jgw yqaqorx. Ie ugzv m peufcqm, V pyjf dbt’x bzoj clrf sbxx fd hbc fzs, bhz av zerj xf riaj slf qhogbxy. V hetweq ujw mnq iyk fhr zvroe vt gree vz xiugtkvvp aa gykamnzmt mlrxx – yq hny etoefy xf m lbz qfde gkgyzoyukp fhnt av po, nth Z oaa’z fv euek xymt gni gtoak ximcr ow lzdrzitfaori. Z mm favv fhnz lze ezvpfkeey azxl aux sq hnvtp fo soru ye bt lze tnop, rzd V iiifavtpp poa’z arzt gu wgqnq zmdq ia g freezkrk frlorx fo rdtcmia scjqls zs ktez. O grxlrj swr tuk prypyokyfeey fvroek xyqy puycp rrgpzee jns yq wny afdkvtk war. Vz are oak xyunt gwbunt zlvy fbx e wmvbav, ntea O xyautnx ktif cej m rbaxzze puqdqrpoec ooazvrot, oax zf if grffhrx iefiekpp fo qxex fhrs mefo gni yalr zlrf I fkid fo ugzv put lsi yyfkpw. U ayys ymvr Grem tb zlzzk bl. M nms purwudrtx Z oohrh walyua Kmlyseuse joxyaug jmjooikvp mnq neu tockh yq wbapu xenj qv fo ukv, sgt V jmuz’t xtsn fhrt aya I juycp br at rsavtwk. Iign xyq rrysldcry lv iiyr lrhe nbezxaori zf wvrp sq hnxh ka aiumu pegkgkuoa hc jfalorx mwne, pvf ayurv ny supcawvtk yum gu xyq oslmtq. I cree fo uupv gp vt Eixiamxfz. Ig ylfglq hi sgsl krfggu zs xuvr si tavrx. Grz yba nfun zk lvde? Jk rvqd gu qrwe n tin blnt. Nfpir", key="GERMAN"), "HARRYTHELAMPLIGHTERSGAVEMEABOXTOTRACKTALLMADGESPHONESIGNALANDIFOLLOWEDHIMNORTHEASTOUTOFCULPEPERONTHEHIGHWAYICLOSEDHIMDOWNJUSTASHEWASJOININGTHEISIXTYSIXANDIMMEDIATELYWISHEDIHADNTWEWEREHEADINGFORWASHINGTONANDIBEGANTOGETABADFEELINGABOUTITTHATCRYSTALLISEDINTOADEEPUNEASINESSASHETURNEDOFFONTOTHEGEORGETOWNPIKEANDIREALISEDWHEREHEWASHEADINGWEHAVEAPROBLEMIJUSTDONTKNOWWHATSORTORHOWBIGBUTWENEEDTOFINDOUTQUICKLYIBACKEDOFFANDCUTTHETRACEINCASEITTRIGGEREDANAUTOMATICALERTHEHASACCESSTOALOTMORETECHNOLOGYTHANWEDOANDICANTBESURETHATTHEPHONETRACEISUNDETECTABLEIAMSURETHATHISEMPLOYERSWILLNOTBEHAPPYTOFINDMEONHISTAILANDICERTAINLYDONTWANTTOSPENDTIMEINABASEMENTTRYINGTOEXPLAINMYSELFTOTHEMICALLEDOFFTHELAMPLIGHTERSBEFORETHEYCOULDREALISEWHOHEWASWORKINGFORITWASONETHINGASKINGTHEMFORAFAVOURWHENITHOUGHTTHISWASAROUTINECOMMERCIALCONTRACTBUTITISANOTHERENTIRELYTODRAGTHEMINTOTHEHOLETHATISEEMTOHAVEDUGFORMYSELFIALSOHAVEANNATOTHINKOFIWASCONFIDENTICOULDFOLLOWTALLMADGEWITHOUTDISCOVERYANDHADHOPEDHEWOULDLEADMETOHERBUTIDIDNTKNOWTHENWHOIWOULDBEUPAGAINSTWITHTHERESOURCESHEWILLHAVEAVAILABLEITWILLBEHARDTOAVOIDDETECTIONBYSTAYINGAWAYLETALONEBYFOLLOWINGHIMTOTHEOFFICEIPLANTOHOLEUPINARLINGTONITSHOULDBEBUSYENOUGHTOGIVEMECOVERCANYOUJOINMEHEREWENEEDTOMAKEANEWPLANJODIE")
    test.run()
    test_num += 1

    # 24. Test the vigenere solver with a known key length
    test = Test(f"\n{test_num}. Testing vigenere with key length...")
    test.setTest(lambda: vigenere_solver.solve("Neidy, Gni cmmcrmxttrxw xmvr si r nok zs kdapq Xrxlzghxq’s cnseq svmrrx aaj M walyuavp hvs rfdtukejf ohz sw Ouyvigqr bt xyq hvmlnmy. V ipfeeq nmd pojt nlet ny lv iaf pszziam xyq I Fobkk-Svd eep izsiuuagkpp iifniu U hnjr’k. Ie jkvv tenjmes fbx Arehvtkkan, nth Z netgr ka grz e smd skicunt gffgt vz. Xymt pxcjfayrmjqd vtxf m drkt lzenymeqsf gw yq thxrvp osl sefo gni Xqoemikawa Vmbq aaj M iqayowvp wukvv te jgw yqaqorx. Ie ugzv m peufcqm, V pyjf dbt’x bzoj clrf sbxx fd hbc fzs, bhz av zerj xf riaj slf qhogbxy. V hetweq ujw mnq iyk fhr zvroe vt gree vz xiugtkvvp aa gykamnzmt mlrxx – yq hny etoefy xf m lbz qfde gkgyzoyukp fhnt av po, nth Z oaa’z fv euek xymt gni gtoak ximcr ow lzdrzitfaori. Z mm favv fhnz lze ezvpfkeey azxl aux sq hnvtp fo soru ye bt lze tnop, rzd V iiifavtpp poa’z arzt gu wgqnq zmdq ia g freezkrk frlorx fo rdtcmia scjqls zs ktez. O grxlrj swr tuk prypyokyfeey fvroek xyqy puycp rrgpzee jns yq wny afdkvtk war. Vz are oak xyunt gwbunt zlvy fbx e wmvbav, ntea O xyautnx ktif cej m rbaxzze puqdqrpoec ooazvrot, oax zf if grffhrx iefiekpp fo qxex fhrs mefo gni yalr zlrf I fkid fo ugzv put lsi yyfkpw. U ayys ymvr Grem tb zlzzk bl. M nms purwudrtx Z oohrh walyua Kmlyseuse joxyaug jmjooikvp mnq neu tockh yq wbapu xenj qv fo ukv, sgt V jmuz’t xtsn fhrt aya I juycp br at rsavtwk. Iign xyq rrysldcry lv iiyr lrhe nbezxaori zf wvrp sq hnxh ka aiumu pegkgkuoa hc jfalorx mwne, pvf ayurv ny supcawvtk yum gu xyq oslmtq. I cree fo uupv gp vt Eixiamxfz. Ig ylfglq hi sgsl krfggu zs xuvr si tavrx. Grz yba nfun zk lvde? Jk rvqd gu qrwe n tin blnt. Nfpir", keylen=6), "HARRYTHELAMPLIGHTERSGAVEMEABOXTOTRACKTALLMADGESPHONESIGNALANDIFOLLOWEDHIMNORTHEASTOUTOFCULPEPERONTHEHIGHWAYICLOSEDHIMDOWNJUSTASHEWASJOININGTHEISIXTYSIXANDIMMEDIATELYWISHEDIHADNTWEWEREHEADINGFORWASHINGTONANDIBEGANTOGETABADFEELINGABOUTITTHATCRYSTALLISEDINTOADEEPUNEASINESSASHETURNEDOFFONTOTHEGEORGETOWNPIKEANDIREALISEDWHEREHEWASHEADINGWEHAVEAPROBLEMIJUSTDONTKNOWWHATSORTORHOWBIGBUTWENEEDTOFINDOUTQUICKLYIBACKEDOFFANDCUTTHETRACEINCASEITTRIGGEREDANAUTOMATICALERTHEHASACCESSTOALOTMORETECHNOLOGYTHANWEDOANDICANTBESURETHATTHEPHONETRACEISUNDETECTABLEIAMSURETHATHISEMPLOYERSWILLNOTBEHAPPYTOFINDMEONHISTAILANDICERTAINLYDONTWANTTOSPENDTIMEINABASEMENTTRYINGTOEXPLAINMYSELFTOTHEMICALLEDOFFTHELAMPLIGHTERSBEFORETHEYCOULDREALISEWHOHEWASWORKINGFORITWASONETHINGASKINGTHEMFORAFAVOURWHENITHOUGHTTHISWASAROUTINECOMMERCIALCONTRACTBUTITISANOTHERENTIRELYTODRAGTHEMINTOTHEHOLETHATISEEMTOHAVEDUGFORMYSELFIALSOHAVEANNATOTHINKOFIWASCONFIDENTICOULDFOLLOWTALLMADGEWITHOUTDISCOVERYANDHADHOPEDHEWOULDLEADMETOHERBUTIDIDNTKNOWTHENWHOIWOULDBEUPAGAINSTWITHTHERESOURCESHEWILLHAVEAVAILABLEITWILLBEHARDTOAVOIDDETECTIONBYSTAYINGAWAYLETALONEBYFOLLOWINGHIMTOTHEOFFICEIPLANTOHOLEUPINARLINGTONITSHOULDBEBUSYENOUGHTOGIVEMECOVERCANYOUJOINMEHEREWENEEDTOMAKEANEWPLANJODIE")
    test.run()
    test_num += 1

    # 25. Test the vigenere solver with an unknown key
    test = Test(f"\n{test_num}. Testing vigenere without key...")
    test.setTest(lambda: vigenere_solver.solve("Neidy, Gni cmmcrmxttrxw xmvr si r nok zs kdapq Xrxlzghxq’s cnseq svmrrx aaj M walyuavp hvs rfdtukejf ohz sw Ouyvigqr bt xyq hvmlnmy. V ipfeeq nmd pojt nlet ny lv iaf pszziam xyq I Fobkk-Svd eep izsiuuagkpp iifniu U hnjr’k. Ie jkvv tenjmes fbx Arehvtkkan, nth Z netgr ka grz e smd skicunt gffgt vz. Xymt pxcjfayrmjqd vtxf m drkt lzenymeqsf gw yq thxrvp osl sefo gni Xqoemikawa Vmbq aaj M iqayowvp wukvv te jgw yqaqorx. Ie ugzv m peufcqm, V pyjf dbt’x bzoj clrf sbxx fd hbc fzs, bhz av zerj xf riaj slf qhogbxy. V hetweq ujw mnq iyk fhr zvroe vt gree vz xiugtkvvp aa gykamnzmt mlrxx – yq hny etoefy xf m lbz qfde gkgyzoyukp fhnt av po, nth Z oaa’z fv euek xymt gni gtoak ximcr ow lzdrzitfaori. Z mm favv fhnz lze ezvpfkeey azxl aux sq hnvtp fo soru ye bt lze tnop, rzd V iiifavtpp poa’z arzt gu wgqnq zmdq ia g freezkrk frlorx fo rdtcmia scjqls zs ktez. O grxlrj swr tuk prypyokyfeey fvroek xyqy puycp rrgpzee jns yq wny afdkvtk war. Vz are oak xyunt gwbunt zlvy fbx e wmvbav, ntea O xyautnx ktif cej m rbaxzze puqdqrpoec ooazvrot, oax zf if grffhrx iefiekpp fo qxex fhrs mefo gni yalr zlrf I fkid fo ugzv put lsi yyfkpw. U ayys ymvr Grem tb zlzzk bl. M nms purwudrtx Z oohrh walyua Kmlyseuse joxyaug jmjooikvp mnq neu tockh yq wbapu xenj qv fo ukv, sgt V jmuz’t xtsn fhrt aya I juycp br at rsavtwk. Iign xyq rrysldcry lv iiyr lrhe nbezxaori zf wvrp sq hnxh ka aiumu pegkgkuoa hc jfalorx mwne, pvf ayurv ny supcawvtk yum gu xyq oslmtq. I cree fo uupv gp vt Eixiamxfz. Ig ylfglq hi sgsl krfggu zs xuvr si tavrx. Grz yba nfun zk lvde? Jk rvqd gu qrwe n tin blnt. Nfpir", key="GERMAN"), "HARRYTHELAMPLIGHTERSGAVEMEABOXTOTRACKTALLMADGESPHONESIGNALANDIFOLLOWEDHIMNORTHEASTOUTOFCULPEPERONTHEHIGHWAYICLOSEDHIMDOWNJUSTASHEWASJOININGTHEISIXTYSIXANDIMMEDIATELYWISHEDIHADNTWEWEREHEADINGFORWASHINGTONANDIBEGANTOGETABADFEELINGABOUTITTHATCRYSTALLISEDINTOADEEPUNEASINESSASHETURNEDOFFONTOTHEGEORGETOWNPIKEANDIREALISEDWHEREHEWASHEADINGWEHAVEAPROBLEMIJUSTDONTKNOWWHATSORTORHOWBIGBUTWENEEDTOFINDOUTQUICKLYIBACKEDOFFANDCUTTHETRACEINCASEITTRIGGEREDANAUTOMATICALERTHEHASACCESSTOALOTMORETECHNOLOGYTHANWEDOANDICANTBESURETHATTHEPHONETRACEISUNDETECTABLEIAMSURETHATHISEMPLOYERSWILLNOTBEHAPPYTOFINDMEONHISTAILANDICERTAINLYDONTWANTTOSPENDTIMEINABASEMENTTRYINGTOEXPLAINMYSELFTOTHEMICALLEDOFFTHELAMPLIGHTERSBEFORETHEYCOULDREALISEWHOHEWASWORKINGFORITWASONETHINGASKINGTHEMFORAFAVOURWHENITHOUGHTTHISWASAROUTINECOMMERCIALCONTRACTBUTITISANOTHERENTIRELYTODRAGTHEMINTOTHEHOLETHATISEEMTOHAVEDUGFORMYSELFIALSOHAVEANNATOTHINKOFIWASCONFIDENTICOULDFOLLOWTALLMADGEWITHOUTDISCOVERYANDHADHOPEDHEWOULDLEADMETOHERBUTIDIDNTKNOWTHENWHOIWOULDBEUPAGAINSTWITHTHERESOURCESHEWILLHAVEAVAILABLEITWILLBEHARDTOAVOIDDETECTIONBYSTAYINGAWAYLETALONEBYFOLLOWINGHIMTOTHEOFFICEIPLANTOHOLEUPINARLINGTONITSHOULDBEBUSYENOUGHTOGIVEMECOVERCANYOUJOINMEHEREWENEEDTOMAKEANEWPLANJODIE")
    test.run()
    test_num += 1

    morse_decoder = MorseTranslator()
    # 26. Test the morse decoder
    test = Test(f"\n{test_num}. Testing morse translator...")
    test.setTest(lambda: morse_decoder.decode(".... . .-.. .-.. ---"), "HELLO")
    test.run()
    test_num += 1

    # 27. Test the morse decoder with spaces
    test = Test(f"\n{test_num}. Testing morse translator with spaces...")
    test.setTest(lambda: morse_decoder.decode(".... . .-.. .-.. --- / .-- --- .-. .-.. -.."), "HELLO WORLD")
    test.run()
    test_num += 1

    # 28. Test the morse decoder with numbers
    test = Test(f"\n{test_num}. Testing morse translator with numbers...")
    test.setTest(lambda: morse_decoder.decode(".... . .-.. .-.. --- / .-- --- .-. .-.. -.. / .---- ..--- ...--"), "HELLO WORLD 123")
    test.run()
    test_num += 1

    # 29. Test the morse decoder with punctation
    test = Test(f"\n{test_num}. Testing morse translator with punctuation...")
    test.setTest(lambda: morse_decoder.decode(".... . .-.. .-.. --- / .-- --- .-. .-.. -.. / .---- ..--- ...-- / -.-.-- -.-.--"), "HELLO WORLD 123")
    test.run()
    test_num += 1

    # 30. Test the morse decoder with other special character in the string
    test = Test(f"\n{test_num}. Testing morse translator with extra characters...")
    test.setTest(lambda: morse_decoder.decode("g .... . .-.. .-.. --- / .-- --- .-. .-.. -.. #"), "HELLO WORLD")
    test.run()
    test_num += 1

    cipher_identifier = CipherIdentifier()
    # 31. Test the cipher identifier with morse code
    test = Test(f"\n{test_num}. Testing the cipher identifier with morse code...")
    test.setTest(lambda: cipher_identifier.identify(".... . .-.. .-.. --- / .-- --- .-. .-.. -.."), "morse")
    test.run()
    test_num += 1

    # 32. Test the cipher identifier with a substitution cipher
    test = Test(f"\n{test_num}. Testing the cipher identifier with substitution...")
    test.setTest(lambda: cipher_identifier.identify("K EWJWAQL NO NDWGQ PWLQ/POLKQ NO W ISKNQ WN W FKAF-GZWII FONQZ LOCJNOCJ. NFQ IODN OV TZWGQ OJZM W BWJU GOSZL WVVODL, WJL K GOSZLJ’N INWM NFQDQ EMIQZV, QXQJ KV K CWI OJ QHTQJIQI. K NFKJU KN COSZL FWXQ BQQJ NQETNKJA VWNQ WJMCWM. KV K GWJ VKJL POLKQ, K WE ISDQ IFQ GWJ VKJL EQ. IOEQNFKJA KJ FQD ZQNNQD NQZZI EQ IFQ WZDQWLM FWI. KJ WJM GWIQ, K LQGKLQL NO UQQT W ZOJA NWKZ OJ FQD, KV OJZM NO WXOKL ITOOUKJA WJMOJQ QZIQ CFO EKAFN BQ VOZZOCKJA FQD. K WE VOGSIKJA OJ KJNQDGQTNKJA FQD GOEEI CKNF ZMJJ VDWJU. NFQM WDQ INKZZ SIKJA VWKDZM ZKAFN QJGDMTNKOJ, WJL KN KI QWIKQD NO AQN WGGQII NO EI VDWJU’I OVVKGQ NFWJ KN COSZL BQ NO KJVKZNDWNQ POLKQ’I DOOE WN NFQ FONQZ. NFOIQ TZWGQI NWUQ NFQ IQGSDKNM OV NFQKD GZKQJNI QXQJ EODQ IQDKOSIZM NFWJ NFQ BWJUI. NFQ WNNWGFQL ZQNNQD IFOCI NFWN POLKQ KI AQNNKJA EODQ GWSNKOSI, BSN KN WZIO IQQEI NO BQ WJ KJXKNWNKOJ NO AQN KJXOZXQL. K WE JON ISDQ CFQDQ NO AO VDOE FQDQ. WI POLKQ IWMI KJ NFQ ZQNNQD, NFQ JSEBQDI KJ NFQ IKAJ-KJ BOOU ISAAQIN IOEQNFKJA OLL, BSN SJZKUQ POLKQ K COJ’N FWXQ WGGQII NO NFQ XWSZN NO GFQGU KN. KI IFQ FKJNKJA NFWN CQ IFOSZL NQWE ST, OD CWDJKJA EQ NFWN IFQ UJOCI K WE FQDQ WJL IFOSZL UQQT WCWM? (KV MOS WDQ JON ISDQ CFWN K WE NWZUKJA WBOSN, NWUQ W XQDM GWDQVSZ ZOOU WN MOSD LQGDMTN OV FQD ZQNNQD. MOS IFOSZL VKJL W FKLLQJ EQIIWAQ.) BM NFQ CWM, NFQDQ KI IOEQNFKJA JWAAKJA WN EQ NFWN K GWJ’N YSKNQ TZWGQ. NFQDQ KI W JWEQ KJ NFQ IKAJ-KJ BOOU NFWN, KJ EM FQWL WN ZQWIN, KI GOJJQGNQL KJ IOEQ CWM NO NFQ JWEQ OV NFQ BWJU, WJL K GWJ’N DQEQEBQD CFWN NFWN GOJJQGNKOJ KI. EWMBQ KN KI JON KETODNWJN, BSN K COJ’N IZQQT TDOTQDZM SJNKZ K GWJ VKASDQ KN OSN. OJGQ MOS FWXQ GDWGUQL POLKQ’I ZQNNQD, FQWL OXQD NO NFQ GWIQ VKZQI WJL NWUQ W ZOOU WN NFQ IKAJWNSDQI. EWMBQ MOS GWJ VKASDQ KN OSN VOD EQ. FWDDM"), "substitution")
    test.run()
    test_num += 1

    # 33. Test the cipher identifier with a transposition cipher
    test = Test(f"\n{test_num}. Testing the cipher identifier with transposition...")
    test.setTest(lambda: cipher_identifier.identify("ATAIUALTNHOEBUOINTYVWXSKLBMFYINERAMTNTLHAIACOLIRYIKYSIFIIUNCGMHRETIRHYASRATAFAUOTOOHLPTEIHIVEUAAEHTWJSNCUTEBVOTVNETOAENTERENUSIBIITCOUHIITSTOIHKAAUPFERIKOECLTEOEOLANGEEONIECICEMENHYTIENAEFNCMWAEIEORUTPLLITCACDTATAEAOETAUGOMYMDCJOEGSDWOLLKAAUTRLIONHWANIEYNOMHIONRRMLHNIEEGNOAPGEHTLHFNTTRWNKRLFLNIISGESSETBFTEAOOCECORTMRYHSTLSHITOTUSSNAOVISEOEOYERMNGOEEOUJWVSETKHITUMAMSWESKAUTHTGTEEOUYEEHIDSYYITAAATPHANGOIAAOEMOMENTBTOIAIMNWEPNARTOCDSRVHFNATGEENEFAIEAETTISLOSPNNDDOSEENSETTHETTAAJASFSIEESAYAEDENOFOSNNWHLGMINPESYNALGYETDAOCMKCIDNAIMHHAKEYINNELTKTDRTDEMUBLMATTNDTHGHJAHEUIIOGMGTEIAEHTCSTAOAWGTOHDDWOOWMNTVROORHTSFIEBAEENGHNETSIIOTEECTOTAHANMACTMTIAILOUCUUYEEEEOTEAEAIRBARTHNOJDSTCOWTTCAOFDDYMEIEENUEEGNFIIUCDEIEESESCETAAELOONLMEWRCORNOTFHSSIGRNIETSRFHOTLJRTEESHRTLEROHBHCTOTIIEOISONIELMREREIIEHEHISTHDLDNATACTHGEDPNTEIEOEIRUTLBKYUADTLYUDEAHHSIGMIUARAHITMATNIWHOAIERHNNBNOBNPRIFINHAOEERCLTOHAMOITRRGRDEIHAETEFOALRCTHSEAPIIDEPAWCDIENEHHTLEDNSIKOLITDIOEGONASIEHMLAYINLTPNETCONINLIRDOETLASTEEESSNNAEESOGGASAEEINIEOWOMSSTTNSSBGONUKEHCTLESNHHERNANMNLAYNEAIUAALYCFTUDHMEWRMGNTATEIESBAHLSCSYNTKAEHTCSITTTSRYIGOEVKITDOSSKKSUYCUUEATEOAAHHONRAYCFNLAEFFNSIOVTNAIFDSENMGLTERAYDDPTHNVOAEOBOEOGEICINTEUAICOTIESFOTWEIESTTSETUFCSOITETAEHAETRITOTITGOAURFRDSLTBTNKSTDNOOESVOIENWLUREHSRHEYASAAAARFKRPRRONDSTTSHGTTQLENTNKNDSNDETEBDRETNOYSPTOEETNEOURJLHEEIDLTNSYFIOR"), "transposition")
    test.run()
    test_num += 1

    # 34. Test the cipher identifier with a vigenere cipher
    test = Test(f"\n{test_num}. Testing the cipher identifier with uniform distribution...")
    test.setTest(lambda: cipher_identifier.identify("NOGXI AVBUI WVJXS NLBFE CSKMH XLGTI RKCPX FHBAA EAMIR TVDRI VZFAT RUBEX RYRQH KVBAQ POMYI NVPWF VUHMQ ZURMP CTYPK VDYEX FZYKX YLJQE JAYZY EBQGE CUYYI RUBMR ZURQV ELREI RYATP ZUIQH ZARAE JWWRV FTRTI NHPAJ ZUBQT VUBQR TLRTI FYGSM EHJIE JSCMH VYMRX YLAGP GLPDM ENUTM TOBUH EAQQI DSGWI RJMUR TPBQR TLYZH RUMFL VYHGK FMAAJ WLCSE MLKQX ZTCFS VENXS ILRTI CPLWX YLMDM XPLMP TBJBI IYGZK NHQEI KBNNC NHQTM ENRAR RUBFE CSKMH XLRAW GFMZX YLZDM KPQTA RZFUR XAMZL RKQGK XLQFI UAFQR RTCMR UAYWI EPRRV FTAGP GLNQV TVSZX PCGDK ZUGMQ FZRAJ KOCUV RJRUZ ZAGQW NLPQJ FJSEW VKYDS LUBZI NFMDO TPRKA ZAFFL VHEQR KZYZH JWGQW ILADY ZACPJ IVKXS ENGEP RUBMR UJMZR VJRUG LARTI PDMDO VKDAV RIMGX WPTQC VHPEV VWMDX ZUEAR KOCNV ZAGEL KYMAT DVTQQ VUREY JPLSG FKCEE EKQBC TYYRX KVQFE PBLPI KLAFI UHQRE IHQUG FBJPW VLRTI ILUMW EVPQG FYBAJ KOCDM ENMBI IHRUR XPLAV RYMGR UJSXT VWCDA YPATQ RKCEI EZCZS FUCQZ VYATS FZCEE TVBQR RTCOS EUCOX VKUUX YAFQS GLPMX ZVLNY KAFMX CLDFQ VDMZH VYGZK NOWAY IUCIQ IAYXP DHBSI NHQAT VYYFM ENFQV VHLPA YHRFL VFUQV VBNFS FUYIL ZTGEI RYATI UHLZE JTGFL KHJXQ RKEQE EKRTI ILQGP KDYEE JBPBV ZZCNY KZKUX YPQMG FTKAR EHKQE EKGIE JUREY ILGFQ VHLFE EFRTM ENRTI SHLWZ RBJFA RZAXI RYJKM DWMDX RURNY KZGZG VAFQF FECEH ZKLFG FURMM EHLKX YPLSS KOCDX YHLZY DICDW ZAKGW KICFL VJYEI KOYFX YLLGQ SLPEX YLKEI CCCEL RCCMQ VHLUR XPUMW FURAQ PAFUV UQSSS WJMRJ VLZQJ FYCUJ FBLPX YLAGP GLPOS ULZAS BVLXM ELYZH KOGZK JZRMV KLBFS DHIQW VUQQM UBEAY KAFQP ZZRAJ SVVQW RUBZY DICDW KOYFN FKGQL RKEUZ VUKQE EKQFE IACPX FWSFM KAMSI KOCDF LASZJ FYRGR RACXC ABQFE JPZQK RUKKT YVLQV RUEMR UDFQR ZWGOO VKGFY GPFMH ILAQM MLBMR RBBUS DLQEE XLDDS DQMPM VPRIE JPLYS IZCOS ULYZH VUADC GACPM WZFQA RZRMO ZUEFL RAKGG YJYDI KOCZM BUCIA VTSEX SLGZF ZNRDS LIJQ"), "uniform")
    test.run()
    test_num += 1

    # 35. Test frequency graph for uniform distribution
    new_graph = FrequencyGraph("NOGXI AVBUI WVJXS NLBFE CSKMH XLGTI RKCPX FHBAA EAMIR TVDRI VZFAT RUBEX RYRQH KVBAQ POMYI NVPWF VUHMQ ZURMP CTYPK VDYEX FZYKX YLJQE JAYZY EBQGE CUYYI RUBMR ZURQV ELREI RYATP ZUIQH ZARAE JWWRV FTRTI NHPAJ ZUBQT VUBQR TLRTI FYGSM EHJIE JSCMH VYMRX YLAGP GLPDM ENUTM TOBUH EAQQI DSGWI RJMUR TPBQR TLYZH RUMFL VYHGK FMAAJ WLCSE MLKQX ZTCFS VENXS ILRTI CPLWX YLMDM XPLMP TBJBI IYGZK NHQEI KBNNC NHQTM ENRAR RUBFE CSKMH XLRAW GFMZX YLZDM KPQTA RZFUR XAMZL RKQGK XLQFI UAFQR RTCMR UAYWI EPRRV FTAGP GLNQV TVSZX PCGDK ZUGMQ FZRAJ KOCUV RJRUZ ZAGQW NLPQJ FJSEW VKYDS LUBZI NFMDO TPRKA ZAFFL VHEQR KZYZH JWGQW ILADY ZACPJ IVKXS ENGEP RUBMR UJMZR VJRUG LARTI PDMDO VKDAV RIMGX WPTQC VHPEV VWMDX ZUEAR KOCNV ZAGEL KYMAT DVTQQ VUREY JPLSG FKCEE EKQBC TYYRX KVQFE PBLPI KLAFI UHQRE IHQUG FBJPW VLRTI ILUMW EVPQG FYBAJ KOCDM ENMBI IHRUR XPLAV RYMGR UJSXT VWCDA YPATQ RKCEI EZCZS FUCQZ VYATS FZCEE TVBQR RTCOS EUCOX VKUUX YAFQS GLPMX ZVLNY KAFMX CLDFQ VDMZH VYGZK NOWAY IUCIQ IAYXP DHBSI NHQAT VYYFM ENFQV VHLPA YHRFL VFUQV VBNFS FUYIL ZTGEI RYATI UHLZE JTGFL KHJXQ RKEQE EKRTI ILQGP KDYEE JBPBV ZZCNY KZKUX YPQMG FTKAR EHKQE EKGIE JUREY ILGFQ VHLFE EFRTM ENRTI SHLWZ RBJFA RZAXI RYJKM DWMDX RURNY KZGZG VAFQF FECEH ZKLFG FURMM EHLKX YPLSS KOCDX YHLZY DICDW ZAKGW KICFL VJYEI KOYFX YLLGQ SLPEX YLKEI CCCEL RCCMQ VHLUR XPUMW FURAQ PAFUV UQSSS WJMRJ VLZQJ FYCUJ FBLPX YLAGP GLPOS ULZAS BVLXM ELYZH KOGZK JZRMV KLBFS DHIQW VUQQM UBEAY KAFQP ZZRAJ SVVQW RUBZY DICDW KOYFN FKGQL RKEUZ VUKQE EKQFE IACPX FWSFM KAMSI KOCDF LASZJ FYRGR RACXC ABQFE JPZQK RUKKT YVLQV RUEMR UDFQR ZWGOO VKGFY GPFMH ILAQM MLBMR RBBUS DLQEE XLDDS DQMPM VPRIE JPLYS IZCOS ULYZH VUADC GACPM WZFQA RZRMO ZUEFL RAKGG YJYDI KOCZM BUCIA VTSEX SLGZF ZNRDS LIJQ")
    new_graph.show()
    test_num += 1

    # 36. Test frequency graph for caesar cipher
    new_graph = FrequencyGraph("J XBT IPQJOH J XPVME GJOE ZPV IFSF. XJUIPVU UIF PGGJDJBM TVQQPSU PG CPTT JU JT HPJOH UP CF IBSE UP USBDL KPEJF EPXO BOE J BN HPJOH UP OFFE ZPVS IFMQ. J TUPMF UIF BUUBDIFE OPUF (OPU TVSF UIFSF JT B CFUUFS XBZ UP QVU UIBU HJWFO UIBU UIJT PQFSBUJPO JT TUSJDUMZ PGG UIF CPPLT) GSPN MZOO GSBOL'T PGGJDF, BOE J UIJOL JU JT GSPN KPEJF. UIF XPSE OFJHICPVSIPPE TVHHFTUT JU XBT XSJUUFO CZ B OBUJWF FOHMJTI TQFBLFS SBUIFS UIBO BO BNFSJDBO, BOE JU JT TJHOFE PGG DJGSBS BHBJO. J DBMMFE UIBU BO BMJCJ CFGPSF, CVU NBZCF OPN EF HVFSSF JT NPSF BQQSPQSJBUF. J OFFE UJNF UP EFDJQIFS UIF SFQMZ, CVU FWFO UIF QBQFS JU JT XSJUUFO PO JT B DMVF. JU JT UIF TPSU ZPV GJOE JO UIF GBODZ IPUFMT, TP J XJMM TUBSU MPPLJOH UIFSF. UIFZ BSF OPU SFBMMZ KPEJF'T TUZMF, CVU JG TIF JT GSFFMBODJOH GPS CBOLT, TIF XJMM XBOU UP HJWF UIF SJHIU JNQSFTTJPO. XIJDI HJWFT NF BO JEFB. J UIJOL J XJMM UBLF B NVDI DMPTFS MPPL BU UIBU MFUUFS.")
    new_graph.show()
    test_num += 1

    # 37. Test frequency graph for transposition
    new_graph = FrequencyGraph("ATAIUALTNHOEBUOINTYVWXSKLBMFYINERAMTNTLHAIACOLIRYIKYSIFIIUNCGMHRETIRHYASRATAFAUOTOOHLPTEIHIVEUAAEHTWJSNCUTEBVOTVNETOAENTERENUSIBIITCOUHIITSTOIHKAAUPFERIKOECLTEOEOLANGEEONIECICEMENHYTIENAEFNCMWAEIEORUTPLLITCACDTATAEAOETAUGOMYMDCJOEGSDWOLLKAAUTRLIONHWANIEYNOMHIONRRMLHNIEEGNOAPGEHTLHFNTTRWNKRLFLNIISGESSETBFTEAOOCECORTMRYHSTLSHITOTUSSNAOVISEOEOYERMNGOEEOUJWVSETKHITUMAMSWESKAUTHTGTEEOUYEEHIDSYYITAAATPHANGOIAAOEMOMENTBTOIAIMNWEPNARTOCDSRVHFNATGEENEFAIEAETTISLOSPNNDDOSEENSETTHETTAAJASFSIEESAYAEDENOFOSNNWHLGMINPESYNALGYETDAOCMKCIDNAIMHHAKEYINNELTKTDRTDEMUBLMATTNDTHGHJAHEUIIOGMGTEIAEHTCSTAOAWGTOHDDWOOWMNTVROORHTSFIEBAEENGHNETSIIOTEECTOTAHANMACTMTIAILOUCUUYEEEEOTEAEAIRBARTHNOJDSTCOWTTCAOFDDYMEIEENUEEGNFIIUCDEIEESESCETAAELOONLMEWRCORNOTFHSSIGRNIETSRFHOTLJRTEESHRTLEROHBHCTOTIIEOISONIELMREREIIEHEHISTHDLDNATACTHGEDPNTEIEOEIRUTLBKYUADTLYUDEAHHSIGMIUARAHITMATNIWHOAIERHNNBNOBNPRIFINHAOEERCLTOHAMOITRRGRDEIHAETEFOALRCTHSEAPIIDEPAWCDIENEHHTLEDNSIKOLITDIOEGONASIEHMLAYINLTPNETCONINLIRDOETLASTEEESSNNAEESOGGASAEEINIEOWOMSSTTNSSBGONUKEHCTLESNHHERNANMNLAYNEAIUAALYCFTUDHMEWRMGNTATEIESBAHLSCSYNTKAEHTCSITTTSRYIGOEVKITDOSSKKSUYCUUEATEOAAHHONRAYCFNLAEFFNSIOVTNAIFDSENMGLTERAYDDPTHNVOAEOBOEOGEICINTEUAICOTIESFOTWEIESTTSETUFCSOITETAEHAETRITOTITGOAURFRDSLTBTNKSTDNOOESVOIENWLUREHSRHEYASAAAARFKRPRRONDSTTSHGTTQLENTNKNDSNDETEBDRETNOYSPTOEETNEOURJLHEEIDLTNSYFIOR")
    new_graph.show()
    test_num += 1

    # Test unknown cipher encoded with morse code
    test = Test(f"\n{test_num}. Test an unknown cipher encoded with morse code...")
    test.setTest(lambda: auto_solve("... .- . -..- .--- -..- ..-. .--. .-.. -. ... .- .--. --. .-. .... --. -.- -.-. .-- . .-.. ...- .-. ... .--. . --.. --.. -..- --. ..- . ...- -.-- -. -.- --. --. .-- .--. -.- .-.. -.. - -.- -.. - ..-. --.. -. .-. -.-- - -.- .-.. .-.. .-.. -. - --- -- -.. --.. .-.. -.-- ..- .... .. -... ... .. --.. - --.. ...- .-. ... . -. -.-- . ... ... . --- ... .. ..-. .--. -. .--. .--. .-. -..- --.. .-. .-. ... . ..- --- .-. .-.. ..- .-.. -.-- ...- .. .-- ... --.- .--. -.. ..- --- -..- .... -- .... -. .-- .- -.. -..- -.-- -.. .... .-. -.-. .-.. .-- .... --.. .. .- --- -.-- -.- .-. ... . ...- -.-- - -... .-. .--- ... ...- -.. .-.. .-. -... - -- --.. -.- --- -- -.-- . . -.-- . .... -- --.- ... . --.- --- ... . -... -.-- - .--- -.- .... .. .--. .--. .... .-. --. --- -- .-.. .-. ..-. -... -..- .... . --.- ... .. .- -- . ... .-.. .-.. -. --.- --- -- .. . .-.. -. --. ..- .-. .. .-. .-.. -... -. .--- --.- .. -.-. .-- .. .- -- .-.. ..-. -- ..-. - ...- --.. . .-.. -.-- . -.-. . . -.. -..- -.-- .-- .-.. ...- -.-- .--. .... --. -.-- - -... --. --- .. -.-. .- ..- .- -.- .-.. .-- --. -.-- . ..-. -.-- .-.. .-- ..-. .--. - .... -..- -.-- .. -... --.. ..-. ... ..- -.-- -..- -- . .... .-. -- .--. ... .--. .-. . --. ..- .... .-. -. - -.- .-. --. -.-- .... --. -.-. . -. .-. - .-- -.-. --- .-- ..- -.- -.-. .. ..-. .--. .-- -. -.-- ... .. -.-- --- .. .- -- .... .. ..-. .-.. ...- .-. --. .- ...- -- -- .-.. .-. ... - -. ... -.. - --.- ..- -.-- -..- .. -.-- --- .--- -.-. ... . .-. -.. --- . --.. --.. ...- ..-. --.. .-- --- --- .-. ..-. ... . .-- .-. - .--. .. -... . --- ... --- -.-- .... -- ..-. - -.. .- - --. .. .-- -.-- ...- .... .-.. --. .. .--. -.. -... .-.. --.- . .-.. --- -.-. .... --.. . .-.. -.-. . .-. -. .. .--. -- .-.. -. .- ..-. -.- - -..- .-. -.-. .. - -- .--. ...- -.-. --- .- .- --. ..-. -..- -- -..- .- --. --- -. . .--- .--. .-. --. -. .--. .-.. -.-- -.. .- .--. .. .--. .-- --.- . --- -. .-. --.. -..- -.- --.. .-. .-. --.. .--. --. ..-. -.-- --- -.-- ..- .-. -.-. .-. ... .- .- -.-. .--. .... -- .-.. -. --.- --- -. . .-.. . -... .-. -.-- ..-. ...- -.-. . .... -. --.. . .-.. -.-. .- .... -... - .--. -..- .--. .-.. -.-. .-. --- -.. -.-- .-.. --- . --. -.- -. -..- -.-- -- .-.. .-. --- .-.. --.- --.- ..-. .-. .-. --.. ... . .-. ... .. ..-. -.- -..- - .--- --.. -.-- .-. -..- -.. .- --. .-- .-.. .- ..- . ..-. -.-. ... .- -.-. ...- .--- -..- -- --.- .. .- .--- -..- .. -- -.-- .... ...- -.-- . . --. .-- .- .- .--- - --. -.-. -.-. - -. --- -.-- .--. .-- --- --- .- --.. .... . .-.. . - -... -.-- .- .. .-.. --- - ...- ... .--. -- .-.. .-.. -... -. -.-- .--. --.- -.-. -.-- - --. -..- .--- -- .-.. .-. - -... -.- .. - .--- .-.. .. .- ... .--- .-- -.-. .-- ..-. --. ..- . .-.. -.-. -..- .. .--. --. .-- .--. -.-. --- --- ... .-.. . .-.. -.-. .-- .- --.. ...- .-- -- . ... - .-. -..- -.. ..-. -.-. --.- --- . -.- . .-.. -.-. .--- -.-. -... .- .-- .... .--. .--. .- -.-- --- -.. .. ..- ... --- ..- -.- .... . --.- .... --- . --.- - .-. . --.- --- . --- . .- -.-- -.. --- .- -.- . .-.. --. -.-- --. -. -.-- ...- -- .-.. .-. - ..- -.- -..- .--- -- -.-. .- ... --. --. ... ... -.-. .-- ..- -.- -.-- -- .-. ... --- .... -- ... -..- .-. ... .. ..-. -.-. .-.. .-- -.-- -.-. --- .... --.. - .-. -.-. -. --- --.. ... .--. ...- .- - .- -.-- .. --.. .-. .-. -.-. .- .--. --.. -- -.-- .-. - - ...- -.-- .-.. .-. -- . .... .-. -..- .--. .-. .-. - .-. .-. .-. .--- -..- -- --- .-. -. -- . .-.. -.-. -..- .. .- --.. --.. -..- ..-. .--. .... -... .-. .--. -..- ..-. .-.. - ...- -.-- .--. .. -.- . --- ..- --. --. .. -... ..-. --. ... ..- -.-. --.- .-- -.. . -.-- .-.. - . .--- -.. --- ..- --. --. .. -.-- -.-- -. -. --.. --.. -..- ..-. - -. -..- ..- --.- -- ..- .-.. ... .--. ..- -.-- .--- --. --- . .- --.. - --. -- ..-. .-.. --.- .-.. --.. .--. .--- --.. .-- --. --. .-- .--. -.- .-.. -.. - -.- .... -- .-. ... --- .... --.. --- -- --.- -. --- .. -.- -.-. -.-. -.-- -.-- -.. ..- --. --- .-.. -- .- . --.- -. .--. .- -- ..-. .-.. --.- .-. .--. . -... -..- . --. ..- ... .. .--. -- ..- --. --- --- -- -... -.-- - -..- - --.. .- .-. ... . .- -.-. ... ... --. .... --- .... .-. --- ..-. -.-. ..-. .--. -. -- .-.. -- .-.. -.. - .--- --- . .-.. .-. ... . . -.- -.. ... ... -.-. -.-. .-. -.-- ... .. ..- - .-.. -.-- -. .-.. --.. -.-. .-.. ...- -. --- .-- . --.. .-- . ...- --.. .... -- .--- .-- -... .-. -. .-.. ...- -... . --- -. -... --.. -- -... --- . --. -.- -. -..- --. --.. -. --- . -.. -..- -.-- .--- .. .- -- .-.. .- -.-- .--- .-.. .-. --.. .-.. .--. -- -.-- . --- . --.- ... .--- .-- --- .--- --- -.-- -.- ..-. - -- --. ..- . .-.. -.-. --.. ..-. ... --- -. .. --. .- .-.. -. - . ... ..-. --.. .-.. .-. .- .- -- .-.. .-.. .-. -.-- --- -.-- -.- .-. --.. -. ...- --.. -.. .-.. -- ..-. .-.. --.- .... .--. ..-. ... -.. -.-- .-. - --.. -.-- . ... - -... -- - --.. -.-. -..- . .--. ..- --. .. .--. -. .- .- . --.. -.-- .... --.. .. .- ... .--. .-.. -.-. -.-. . .--- -.- -.-- .. -.-. --- - -... ... .-.. --- -.-. .-.. -. .-. -.-. .- .--. -.-- -.-- .--- -... .--- - .."), "")
    test.run()
    test_num += 1

    # Test using previous challenges
    with open("data/tests.json", "r") as my_file:
        data = json.load(my_file)

    for challenge in data["test_ciphers"]:
        print(challenge)
        print(f"\n{test_num}. Trying {challenge['name']}")

        decrypt_a = auto_solve(challenge["ctext_a"])
        decrypt_b = auto_solve(challenge["ctext_b"])

        print(f"\nPart A decrypt: {decrypt_a}")
        print(f"Official Part A decrypt: {challenge['answer_a']}")

        print(f"\nPart B decrypt: {decrypt_b}")
        print(f"Official Part B decrypt: {challenge['answer_b']}")

        test_num += 1

    # Test the load cipher from file function
    test_num += 1

    # Test saving the cipher to the file
    test_num += 1

    # Test the help command
    test_num += 1

    # Test the exit command
    test_num += 1


def main():
    # Run the tests
    create_menu()

    # Run the main program
    #start()

if __name__ == "__main__":
    main()