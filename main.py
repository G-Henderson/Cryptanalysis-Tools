import json

from utils.cipher_identifier import CipherIdentifier

from utils.solvers.caesar_solver import CaesarSolver
from utils.solvers.affine_solver import AffineSolver
from utils.solvers.simple_substitution_solver import SimpleSubSolver
from utils.solvers.columnar_transposition_solver import ColumnarTranspositionSolver as ColTransSolver
from utils.solvers.vigenere_solver import VigenereSolver

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
    tests()

    # Run the main program
    go()

def tests():
    """
    Runs all of the tests
    """

    ### Run the tests ###
    print("Running Tests...")

    # Test the chi-squared statistic function
    mStatMeasurer = StatMeasurer()
    chi_test = Test("\nTesting the Chi-squared statistic function...")
    chi_test.setTest(lambda: mStatMeasurer.chi_squared("Programming in python is fun"), 27.907733765597285)
    chi_test.print_output()

    # Test the index of coincidence calculator
    ic_test = Test("\nTesting the Index of Coincidence statistic calculator...")
    ic_test.setTest(lambda: mStatMeasurer.get_ic("Programming in python is fun"), 0.082010582010582)
    ic_test.print_output()

    # Test the ngram fitness score function
    mNgramScorer = NgramScorer(NgramFiles.QUADGRAM_FILE)
    print("\nTesting the ngram fitness score function...")
    if (mNgramScorer.ngram_score("HELLOWORLD") == -28.42865649982033):
    
    ic_test = Test("\nTesting the Index of Coincidence statistic calculator...")
    ic_test.setTest(lambda: mStatMeasurer.get_ic("Programming in python is fun"), 0.082010582010582)
    ic_test.print_output()

    # Test the caesar solver with known shift
    mCaesarSolver = CaesarSolver()
    print("\nTesting the caesar solver with known shift...")
    if (mCaesarSolver.solve("abcbka qeb bxpq txii lc qeb zxpqib", 3) == "DEFENDTHEEASTWALLOFTHECASTLE"):
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
    if (mAffineSolver.solve("knqnok gwn nbdg pbii rq gwn hbdgin", [3, 1]) == "DEFENDTHEEASTWALLOFTHECASTLE"):
        print("Passed")
    else:
        print("Failed")

    # Test the affine solver with unknown key
    print("\nTesting the affine solver with unknown key...")
    if (mAffineSolver.solve("knqnok gwn nbdg pbii rq gwn hbdgin") == "DEFENDTHEEASTWALLOFTHECASTLE"):
        print("Passed")
    else:
        print("Failed")

    # Test the simple substitution solver with known key
    mSimpSubSolver = SimpleSubSolver()
    print("\nTesting the simple substitution solver with known key...")
    if (mSimpSubSolver.solve("cjmjvc gsj jibg rill om gsj dibglj", "ifdcjmwskxzltvohynbgupreqa") == "DEFENDTHEEASTWALLOFTHECASTLE"):
        print("Passed")
    else:
        print("Failed")

    # Test the simple substitution solver with unknown key
    """
    print("\nTesting the simple substitution solver with unknown key...")
    if (mSimpSubSolver.solve("SOWFBRKAWFCZFSBSCSBQITBKOWLBFXTBKOWLSOXSOXFZWWIBICFWUQLRXINOCIJLWJFQUNWXLFBSZXFBTXAANTQIFBFSFQUFCZFSBSCSBIMWHWLNKAXBISWGSTOXLXTSWLUQLXJBUUWLWISTBKOWLSWGSTOXLXTSWLBSJBUUWLFULQRTXWFXLTBKOWLBISOXSSOWTBKOWLXAKOXZWSBFIQSFBRKANSOWXAKOXZWSFOBUSWJBSBFTQRKAWSWANECRZAWJ") == "THESIMPLESUBSTITUTIONCIPHERISACIPHERTHATHASBEENINUSEFORMANYHUNDREDSOFYEARSITBASICALLYCONSISTSOFSUBSTITUTINGEVERYPLAINTEXTCHARACTERFORADIFFERENTCIPHERTEXTCHARACTERITDIFFERSFROMCAESARCIPHERINTHATTHECIPHERALPHABETISNOTSIMPLYTHEALPHABETSHIFTEDITISCOMPLETELYJUMBLED"):
        print("Passed")
    else:
        print("Failed")
    """

    # Test the columnar transposition solver with keylen
    mColTransSolver = ColTransSolver()
    print("\nTesting the columnar transposition solver with known key length...")
    #print(mColTransSolver.solve("ACEEESCNTSSRNIAHLATUEEONEEAKPISLRERSHDFESNGHSDYETCNEVATUSECIATBNETELEBOTDTBEFAWYSTDRRISTOILCYAOIACSSTMLTLEEHEEFRESNEIREWDTAULTHEUKHNTOCTONPETNYOWOAKIPANEELDEIGTENRTEATRIUNEEAAPHEITULTUNTTANGAAHGEANAILOEONULRTEYRNATTEPSBTEEHTANAELGHOSFIDNHOHENSCNELEMOSRSHORIESHNOEISEEBLOOCILDNOTINIATSOOOWSGNHLDONCDOOYSILXENOIOTNCBEWTYTEHEIAHSETETYIFTHRTOIMIRUBNYPWLTCAYIUILHEIHMTLHINWNIARCAUNPOKONRECYPNGHDWOVRUEPONFESIHSAOBRVSDSTOTANBYODSNERLOTEYEISENUTSTCUSFOAARATEEWINKRIIENTLAOIOWETTNSWTSSODTSHVIFIHMSHWTTEFBRTLWEMRATERURENTURWAIHIBUSISANRCANATUACISHARISDOEIOSITFXETRPHSCFBLNATAYANOTHEOTMBAOEBONRCAEELKGOOTEAYNOESMENLIYIRFRDEITVDIMTHDEVTSANIHRYKODTGIFTRFEODIRSOIINHAMCDPOHLTEFITTOEFSFEIHOOPOIRWAENMXEGTRERAAOHOINYRTLTICRSOETNTAOALODLCINOPOEHURLVVRRICIICEOTALCTYHHSDFPICOOWNIAIPMSRELGSIATATENEGITAEOGEAOCSTEDOAOIISEEENEPOBUHOCOTNDTRWASTHIREEYWNOMNEEYRTHEREIBDCSSSTREMIPYSGUIDBUEREAHETITLCCTTLDWOEEEULHHLEORCCSEHNSVREMRBEREISOIUNLTSAEAOVHIIPWDOPNUDESPSTNNSAEATUNAVFARWACAONDAYBNEIVAHLCYMSEIDHRSOMEHIFURSSTVLURETTRITRUEETISLTHCLOPRIHSEIFLIENFFGSOIOAIHNDIASHEDAFGNESMXSEKBADHELAPOPAEYSADQOHMCEPTSCABTSSAGATANWMTIHRAFTLTDSOEFALHVTODCNTNPLEGMGFLINSPNKJAORNATSTTIATAHARGRRETTTAWMEEETHLIWVEBRRSWFNYTEOALRSITFESENITFNNOETOYNRAASNSAEPEVEOENWLRSLSRNGLDYTOTOYEEOWEAOLVCEETIHRWOTMELERTTINSOUGNIROSERRTWEULSFOEHEOEMUSUCPELMFNTAAUISYHLPMFDIAIRLGPWEFEHIDPOHTBAEAYOALOSDESWOSRETNTGONIEHOONTEERWOEACHFNESBNNSRERNRTEHEAHILYENKENLTDCENBVOCPOEFRCUWTUENEWEOSTEENENIATIIHSTEDEMERGAODRESAUTIWETENSSAARMEYMNEEFMHGIIOOOFMSGHMPRTIETFEIIRWAOEUDTTYTACLRPHTAEIIHHHCANSKATSOOUONFOEEHUOYWYRYDOLEEHETHSLNAIFTEEHDELTIETRETNLTERNMRCVEOETEAEIDEGNAENOOBEKAWUBOTIEFOOKTNDRIUETAROIUYLTMSWIERYUTRLTENNKITEUVETDETSLROILGRLSHAOITEELUSIUHKAESMNEASAEOOSTOYSIIDAYSHRSITASILAATOALLGONALGIASISOSDUUTASANTEUSPNPNEIPNHOEOOCWEETRHREVAPFESNAAETSCIUTEHYRRBIAMNAESWOTRF", "german"))
    #print(mColTransSolver.solve("ACEEESCNTSSRNIAHLATUEEONEEAKPISLRERSHDFESNGHSDYETCNEVATUSECIATBNETELEBOTDTBEFAWYSTDRRISTOILCYAOIACSSTMLTLEEHEEFRESNEIREWDTAULTHEUKHNTOCTONPETNYOWOAKIPANEELDEIGTENRTEATRIUNEEAAPHEITULTUNTTANGAAHGEANAILOEONULRTEYRNATTEPSBTEEHTANAELGHOSFIDNHOHENSCNELEMOSRSHORIESHNOEISEEBLOOCILDNOTINIATSOOOWSGNHLDONCDOOXYSILXENOIOTNCBEWTYTEHEIAHSETETYIFTHRTOIMIRUBNYPWLTCAYIUILHEIHMTLHINWNIARCAUNPOKONRECYPNGHDWOVRUEPONFESIHSAOBRVSDSTOTANBYODSNERLOTEYEISENUTSTCUSFOAARATEEWINKRIIENTLAOIOWETTNSWTSSODTSHVIFIHMSHWTTEFBRTLWEMRATERURENTURWAIHIBUSISANRCANATUACISHARISDOEIOSITFXETRPHSCFBLNATAYANOTHEOTMBAOEBONRCAEELKGOOTEAYNOESMENLIYIRFRDEITVDIMTHDEVTSANIHRYKODTGIFTRFEODIRSOIINHAMCDPOHLTEFITTOEFSFEIHOOPOIRWAENMXEGTRERAAOHOINYRTLTICRSOETNTAOALODLCINOPOEHURLVVRRICIICEOTALCTYHHSDFPICOOWNIAIPMSRELGSIATATENEGITAEOGEAOCSTEDOAOIISEEENEPOBUHOCOTNDTRWASTHIREEYWNOMNEEYRTHEREIBDCSSSTREMIPYSGUIDBUEREAHETITLCCTTLDWOEEEULHHLEORCCSEHNSVREMRBEREISOIUNLTSAEAOVHIIPWDOPNUDESPSTNNSAEATUNAVFARWACAONDAYBNEIVAHLCYMSEIDHRSOMEHIFURSSTVLURETTRITRUEETISLTHCLOPRIHSEIFLIENFFGSOIOAIHNDIASHEDAFGNESMXSEKBADHELAPOPAEYSADQOHMCEPTSCABTSSAGATANWMTIHRAFTLTDSOEFALHVTODCNTNPLEGMGFLINSPNKJAORNATSTTIATAHARGRRETTTAWMEEETHLIWVEBRRSWFNYTEOALRSITFESENITFNNOETOYNRAASNSAEPEVEOENWLRSLSRNGLDYTOTOYEEOWEAOLVCEETIHRWOTMELERTTINSOUGNIROSERRTWEULSFOEHEOEMUSUCPELMFNTAAUISYHLPMFDIAIRLGPWEFEHIDPOHTBAEAYOALOSDESWOSRETNTGONIEHOONTEERWOEACHFNESBNNSRERNRTEHEAHILYENKENLTDCENBVOCPOEFRCUWTUENEWEOSTEENENIATIIHSTEDEMERGAODRESAUTIWETENSSAARMEYMNEEFMHGIIOOOFMSGHMPRTIETFEIIRWAOEUXDTTYTACLRPHTAEIIHHHCANSKATSOOUONFOEEHUOYWYRYDOLEEHETHSLNAIFTEEHDELTIETRETNLTERNMRCVEOETEAEIDEGNAENOOBEKAWUBOTIEFOOKTNDRIUETAROIUYLTMSWIERYUTRLTENNKITEUVETDETSLROILGRLSHAOITEELUSIUHKAESMNEASAEOOSTOYSIIDAYSHRSITASILAATOALLGONALGIASISOSDUUTASANTEUSPNPNEIPNHOEOOCWEETRHREVAPFESNAAETSCIUTEHYRRBIAMNAESWOTRF", "german"))

    mVigenereSolver = VigenereSolver()
    print(mVigenereSolver.solve("Neidy, V ys ffdeq, yth Z mm ecgpck nbr yyiq wuw O lrhe ockr vjiycj xf fhr yxgymebjukzetf. Boh Z po fmsiktiae zs lbsrr ysdqoac? O ed denjrc, iqayje lfbiae zlrf ohp uzvdlbpjw nuly doru eozczlzzg n zox darr pkpvhaar lsi ye gm zetwlr quse. Fhr exslb hrpk mj srryz, flf ig dkice lvik xyqrr gy e uumvlowyunt pkxldn bl hvvmkvlm ANUI pgvlvds fcbiefy-fgd cvmrf mt, eep eict xyq Cbjj Ard Fvyror ungcxgvbt cgri uaefl'z wvqm gm hi xuvvlm qloh oyio. Zr ybs jse'f hntk eektugtk war zc zs narx mt, xyqn zyefv koh auycp srlj smqr fmsi eqwogkw war zc zs kdavl at? Nq rrakmmqd n qzetw os kgxvdinj lvfy Lbljse m cbsvpv af jckoj mgb rnek yitfz qrwe n eusu qxrpimjq fbp zlvy, aab clzxe gfk jzdsg dka kqxgq gvv deyyzmmqll qoqgxe, vr cslxd oc g kfad rvkvtusr duv pauae grrxyfry xf frl ru afdk bsz aymt gfkc rde gcrpzzg hq. O lrhe nrzetteq rni wurfr oxvy fems xyq bnril ja ybs iee eer unek U mryt. M nauyb biik dryxpp xixc zs bzoj unek \"fhr exirf mnrzii\" descxw ka, aab O wlepraz cfg wvjr arzt gm qrfi tbm. Zlv deppamke dbl'z rvqd gm qrfi mhan xf nrryq xyus blk; mw fhrw nemq dblk sld iabagkuoa rxezziae ur smsva imgteeq, zlvk sumapu ne sgti. Dk cbjrirsurq niiq hntk rzokaysiu fhvq lmcq Tuc Rmxttumawv Ooaqvmimcl, zkgrgsr ml ayqrr rni gmprpy avde smaru. Fhnr sebqs vr yslzd n jux darr gstiqsfgbi ktaa gz jzdsg jusbe, bhr esl zeicx oeaw jfkvv eozczlzzg ygqi ktif kokyf lryj. M ymvr qkx lb a fciyiq oajorv eyfrkq ja tuc zvrunrcy grz grr ggtqsf ru gree sgrij mnq qkru ye gfkmi mtgcstke ag bkgzbhrporx. Uf lma tfung rnid fhrpk, xyqn V uopc ohraq lfi tuce eiq grrzmes oa. Kgcsq tuce gfglq jusb mt gfk FFES pmjisdeniorx suvbk ej ieyj oj ktel lkiu fo opawy gp gfkmi ekvjrw. Rxl gfk fvet, Wmjmv"))

    ### End of tests ###
    print("")

    ### Start the main program ###
    #print(mCaesarSolver.solve(loadCipherText()))

if __name__ == "__main__":
    main()