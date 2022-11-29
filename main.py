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
    #main()
    solver = TranspositionSolver()
    print(solver.solve(("NNFYR LKWAN SARTO AOFLA XEERB OUATD EDIHS TPEAP RACEO NFARC OELHA GUEEL EMAHD SGOOA DETEM TPAOL OTOTO RRWIK BUTDS EASKE EHHEW TRDGQ UNEOI ONTWS REIES HEINH SSADO EFTSH ESAII GHRTL WASTN IUCHM BTITW TAUNO UEGSO RATIH OURES SPICS IUTHE NPOIC ELHOS ETDUA ARRBI PSANR DENTS EATNG TOHLE ACBHE KEEOP TGHTI SSRSA EWEBU TYTAT DIADH STOTP NDRIS VUGPA NSIHE ITNTS TIEGV IONTS AETHT EIADW OARTR ASIST ANHDG LLLEI WNDTA HTARS CEEED TMOEV EVAEH EDORF EHEHT IFWAY HAGEN TDEND THEER TERAV WAPEA BIEBA LNBHA TTWKL DHUAO SLOEW VITRD IETDO HWGHE DTRNE RSVHI LDHUA OHADE PVNTY EOLIM ETTFT OPSOO EAPLO RIFTT HUWER YEENS COICS WEUWO LFILN IUTTO ODRRO OWMTH EFRIA SAWNE HINTG YONGR WWHTH TEIAK ERSBT ITUSB MSTEO EUCHM OOCOI ANFDE NICCH ATTTE CAREM HSEDS TISAN EDHAV IENLS SEENG ALLIY TTRAO CNONI STKAY IWNST HEOWT ERITT ASODL IATFE NEDIK ELALC CIADN TTHNA ETHII TTEVE HRTEE PDEYS POTTS THENS ORELO IHENS EUNNG IITRU LDOBW IDDHE EROMF VNWTH EEIRW AASCA NDTIS ONTGH NEACB HEAIN RIDWI TGHNO ARHDA CRIFM OCENS EEVES NTIAT OGRIW ARSMS GARNO IDITN TUREW EAHOA MNBSA NCLEU RSIOG NFABO ONBUT YPDIC ELDOE RSVWI EPRRE ERINA GPSEA ORTWH EHNCL EFETW YBEAI MTOOM OAIMI TSPCB UITTO NTDTI NKTIH HWILY LENDA INFHI NTGYG UEYSM STHIA SNNAA HTBEE SNADN AIPKD ITEWP LDNUT OTHEE FBSTT RIITH AETMD HAAPH NEDET PBANA KOFIC FIOTH OLUAI TWHAG SUAUL SPRIY OLOTH TEREA KRIBI THWTN VICET HFORM CITOH DAEOV EDRNU LTACV ESIDN OCHAX NEFOR ETGIR FERHD OMEIE ULDON CUITQ ETEWH EYSME OONSO ULWDE KIDEN BPEDP AAERT THFRI MCEET IAUMB PINOG HATTH HTTTA ACEDM EESHG EMAIS TEXHP GINIA TLWAS TUIRT HOONX FOORD ICHHR WDILA LEALB GUEMA NIATD TOEGG THETL EPLIM GAERS TTHUT APTOC EOANR LLSAT CHEMT OOLEN IUBER SBOML LTAHF ENISO EANKB ORICI FAFTO GSELE RWHIT THEHP TPLEO IEYNN LFNNK SAORI CEFCF LTRLA ASDOE NCIVE GYTAS MUUOA SAHNC TERNC ITCAP NETSI UGBLS IANNL LIEGT CEHNA ELWAA YSEEN BASGP AIRBF BOOST ORKWA SJUSD TNOWI NNKHO IWSGL LIANC HOAWN GHENW TDYCA ELHDC AENLL LYEOT LOTAT USISI DHBLY UTOEI FUYRC ANUCO SSROE RRENE CFALL CSETH EOBTA VIHOE OFARS UPECS TUJOD OISET USPEI DEVOA AKETO SONBT OUTHE HBTKA NNDAE VBHAT AGAQI HREAB KNGAL NLIER UHLTA NDSWE ATASN EAITW EDORS FODTH IENMO HATPG NWEEQ PCKLI YUOTT PESPA TATDN LYRNE ADOHN NALLC EEHOR WARTH RGENI METSE OMARP FRENA TPRAN YDLLO CMAOO NSIAT EVEDR NIMET LYNIM NMYIA TDEEL EFYTL OEVHE WHEWS ARALK TISTO AGNNE ADHED ORAFQ DETSI PUTOT TAOTH EECKL ITLWA NTPSO AIBLS ESLIS OTTIN BNUEE DIWDT NAGAE MGETO TTGEO ELHAT ICOOA TADFN MTHOE RTWOE RNNDW AEKAB LEERC ROOST EFERR SCEIN TETHA ITWTT HXAEA DBHET SENNT ESTBU EJRET OHFHI RTDET HOFSO ALLCS EILEH WWOUL CDELI STTNT OTNHE ALLCS ETHOI UWWAR ARTTA TNEAI SNTOX UTOAM TICAT LAENC YRLTE DPBYH ESTYY EMSTO SELAH MTIGH LTPSW ERREB LEATE EADRI ONDCA OTDSE LEUAT THHTE NDSEE ADAHD RDALE ADROF EEYRY PCTNN THOEI ELFST MTGAA VHHET TEESU FMFAI ENCTI USEAT COGIL TOANO SFACI AILFT ERNCI TANPD ENDIA THERI VFODI EOSJL CUALC IONTS AERIR GAITU TSHAV ISGEE RENCE HERPW IHPET RIDFI OVIUT WBEEN THOAD TIMEE VCRAO CTTNO IWKWE HSAAA NOETV RLEEA HOFOT LDWIN ONLYO RWKEK NOEWW UCAON YITFO ODSAN UDROK FOOLA RDWTR EEISN OOURY DGRYP CTE").replace(" ", "")))