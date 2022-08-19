import json

from utils.solvers.caesar_solver import CaesarSolver
from utils.solvers.affine_solver import AffineSolver
from utils.solvers.simple_substitution_solver import SimpleSubSolver
from utils.solvers.columnar_transposition_solver import ColumnarTranspositionSolver as ColTransSolver
from utils.solvers.vigenere_solver import VigenereSolver

from utils.stat_measurer import StatMeasurer
from utils.ngrams_scorer import NgramScorer, NgramFiles

def loadCipherText():
    file_path = "cipher-texts/2021.json"
    my_file = open(file_path)
    my_obj = json.load(my_file)
    my_file.close()

    ctext = my_obj["challenges"][0]["ctext"]

    return ctext

def get_message() -> str:
    message = input("Please enter your ciphertext: ")

    return message
    

def main():

    ### Run the tests ###
    print("Running Tests...")

    # Test the chi-squared statistic function
    mStatMeasurer = StatMeasurer()
    print("\nTesting the Chi-squared statistic function...")
    if (mStatMeasurer.chi_squared("Defend the east wall of the castle") == 18.528310082299488):
        print("Passed")
    else:
        print("Failed")

    # Test the ngram fitness score function
    mNgramScorer = NgramScorer(NgramFiles.QUADGRAM_FILE)
    print("\nTesting the ngram fitness score function...")
    if (mNgramScorer.ngram_score("HELLOWORLD") == -28.42865649982033):
        print("Passed")
    else:
        print("Failed")

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