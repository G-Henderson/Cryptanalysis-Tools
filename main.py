import json

from utils.cipher_identifier import CipherIdentifier

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
    cipher_identifier = CipherIdentifier()
    cipher_identifier.identify("Defend the east wall of the castle")
    cipher_identifier.identify("My dear M, thank you for letting me know about T's offer to join with us in the Great Matter. While I still have many ideas for how to prosecute our plan, my days are growing short, as are yours, and we will need to find others of a similar mind who have the wit and imagination to carry it forward. Our ability to influence matters directly will continue to depend on the power of the devices we can fashion, and it will be clear to you that this will require new ways of thinking about the world as well as new technologies to manipulate it. T, together with L and the young E will, I hope, bring a new perspective, and help to keep our little conspiracy alive for another generation. Our adventures so far have, of necessity, been limited in scope, though our acquisition of Babbage's plans and the suppression of his Analytic Engine must count as a highlight. If we are to succeed on the grand scale that we both think is necessary, then it is time for us to formalise our arrangements and to establish a headquarters for our operations. I have given this some thought and have an idea that I hope will please you. We should build a lighthouse in London! I can immediately see your objection. London has no rocky shores, and so no need of one, but your experiments with lanterns give us the ideal excuse to build one as a place to test them. The opportunities this will afford are many: The delivery of large crates of equipment will go unnoticed, considered as part of the natural business of the place; its location on a busy wharf would disguise the necessary comings and goings of our co-conspirators; the waterway will provide us with ready transportation both inland via the canals and to the docks at Tilbury for our international ventures. Not least, the extraordinary power needed for our devices will be mistaken for the energy required to run your public experiments. I have little expertise in the design or engineering of such structures, but I imagine that they require substantial footings. The development of these will provide the cover we need to construct our secret headquarters under the more public face of the lighthouse itself and its ancillary buildings. It may be that I have missed something important in my considerations, in which case please do point that out, but if we are to pass on our discoveries, ambitions and plans to the next generation we will need to give them a more permanent home, so I hope we can agree together on the best way to proceed. Yours, CH")
    cipher_identifier.identify("Harry, I am bored, and I am really not sure why I have been exiled to the archaeologists. Did I do something to upset someone? I am really, really hoping that our overlords will find something a bit more relevant for me to tackle soon. The group here is great, but it feels like there is a diminishing return on breaking WWII ciphers seventy-six years on, and even the Cold War Fialka intercept pile doesn't seem to be giving much back. If you don't have anything for me to work on, then maybe you could send over some newbies for me to train up? We received a stack of material from London a couple of weeks ago that might make a good exercise for them, and while the first few texts are relatively simple, it would be a good exercise for young analysts to try to work out what they are telling us. I have attached the first item from the batch so you can see what I mean. I would very dearly like to know what \"the great matter\" refers to, and I suspect you will want to know too. The recruits don't need to know much to break this one; if they have done our induction training on basic ciphers, they should be fine. My colleagues here have nicknamed this file The Lighthouse Conspiracy, because of where the papers were found. That makes it sound a lot more impressive than it first looks, but you never know where something like this might lead. I have set up a secure online system so the trainees can get access to case files and send me their attempts at deciphering. If you point them there, then I will check how they are getting on. Maybe they could look at the BOSS codebreaking guide as well if they need to brush up their skills. All the best, Jodie")
    cipher_identifier.identify("GZQQX, H ZL ANQDC, ZMC H ZL QDZKKX MNS RTQD VGX H GZUD ADDM DWHKDC SN SGD ZQBGZDNKNFHRSR. CHC H CN RNLDSGHMF SN TORDS RNLDNMD? H ZL QDZKKX, QDZKKX GNOHMF SGZS NTQ NUDQKNQCR VHKK EHMC RNLDSGHMF Z AHS LNQD QDKDUZMS ENQ LD SN SZBJKD RNNM. SGD FQNTO GDQD HR FQDZS, ATS HS EDDKR KHJD SGDQD HR Z CHLHMHRGHMF QDSTQM NM AQDZJHMF VVHH BHOGDQR RDUDMSX-RHW XDZQR NM, ZMC DUDM SGD BNKC VZQ EHZKJZ HMSDQBDOS OHKD CNDRM'S RDDL SN AD FHUHMF LTBG AZBJ. HE XNT CNM'S GZUD ZMXSGHMF ENQ LD SN VNQJ NM, SGDM LZXAD XNT BNTKC RDMC NUDQ RNLD MDVAHDR ENQ LD SN SQZHM TO? VD QDBDHUDC Z RSZBJ NE LZSDQHZK EQNL KNMCNM Z BNTOKD NE VDDJR ZFN SGZS LHFGS LZJD Z FNNC DWDQBHRD ENQ SGDL, ZMC VGHKD SGD EHQRS EDV SDWSR ZQD QDKZSHUDKX RHLOKD, HS VNTKC AD Z FNNC DWDQBHRD ENQ XNTMF ZMZKXRSR SN SQX SN VNQJ NTS VGZS SGDX ZQD SDKKHMF TR. H GZUD ZSSZBGDC SGD EHQRS HSDL EQNL SGD AZSBG RN XNT BZM RDD VGZS H LDZM. H VNTKC UDQX CDZQKX KHJD SN JMNV VGZS \"SGD FQDZS LZSSDQ\" QDEDQR SN, ZMC H RTRODBS XNT VHKK VZMS SN JMNV SNN. SGD QDBQTHSR CNM'S MDDC SN JMNV LTBG SN AQDZJ SGHR NMD; HE SGDX GZUD CNMD NTQ HMCTBSHNM SQZHMHMF NM AZRHB BHOGDQR, SGDX RGNTKC AD EHMD. LX BNKKDZFTDR GDQD GZUD MHBJMZLDC SGHR EHKD SGD KHFGSGNTRD BNMROHQZBX, ADBZTRD NE VGDQD SGD OZODQR VDQD ENTMC. SGZS LZJDR HS RNTMC Z KNS LNQD HLOQDRRHUD SGZM HS EHQRS KNNJR, ATS XNT MDUDQ JMNV VGDQD RNLDSGHMF KHJD SGHR LHFGS KDZC. H GZUD RDS TO Z RDBTQD NMKHMD RXRSDL RN SGD SQZHMDDR BZM FDS ZBBDRR SN BZRD EHKDR ZMC RDMC LD SGDHQ ZSSDLOSR ZS CDBHOGDQHMF. HE XNT ONHMS SGDL SGDQD, SGDM H VHKK BGDBJ GNV SGDX ZQD FDSSHMF NM. LZXAD SGDX BNTKC KNNJ ZS SGD ANRR BNCDAQDZJHMF FTHCD ZR VDKK HE SGDX MDDC SN AQTRG TO SGDHQ RJHKKR. ZKK SGD ADRS, INCHD")
    cipher_identifier.identify("PB GHDU P, WKDQN BRX IRU OHWWLQJ PH NQRZ DERXW W'V RIIHU WR MRLQ ZLWK XV LQ WKH JUHDW PDWWHU. ZKLOH L VWLOO KDYH PDQB LGHDV IRU KRZ WR SURVHFXWH RXU SODQ, PB GDBV DUH JURZLQJ VKRUW, DV DUH BRXUV, DQG ZH ZLOO QHHG WR ILQG RWKHUV RI D VLPLODU PLQG ZKR KDYH WKH ZLW DQG LPDJLQDWLRQ WR FDUUB LW IRUZDUG. RXU DELOLWB WR LQIOXHQFH PDWWHUV GLUHFWOB ZLOO FRQWLQXH WR GHSHQG RQ WKH SRZHU RI WKH GHYLFHV ZH FDQ IDVKLRQ, DQG LW ZLOO EH FOHDU WR BRX WKDW WKLV ZLOO UHTXLUH QHZ ZDBV RI WKLQNLQJ DERXW WKH ZRUOG DV ZHOO DV QHZ WHFKQRORJLHV WR PDQLSXODWH LW. W, WRJHWKHU ZLWK O DQG WKH BRXQJ H ZLOO, L KRSH, EULQJ D QHZ SHUVSHFWLYH, DQG KHOS WR NHHS RXU OLWWOH FRQVSLUDFB DOLYH IRU DQRWKHU JHQHUDWLRQ. RXU DGYHQWXUHV VR IDU KDYH, RI QHFHVVLWB, EHHQ OLPLWHG LQ VFRSH, WKRXJK RXU DFTXLVLWLRQ RI EDEEDJH'V SODQV DQG WKH VXSSUHVVLRQ RI KLV DQDOBWLF HQJLQH PXVW FRXQW DV D KLJKOLJKW. LI ZH DUH WR VXFFHHG RQ WKH JUDQG VFDOH WKDW ZH ERWK WKLQN LV QHFHVVDUB, WKHQ LW LV WLPH IRU XV WR IRUPDOLVH RXU DUUDQJHPHQWV DQG WR HVWDEOLVK D KHDGTXDUWHUV IRU RXU RSHUDWLRQV. L KDYH JLYHQ WKLV VRPH WKRXJKW DQG KDYH DQ LGHD WKDW L KRSH ZLOO SOHDVH BRX. ZH VKRXOG EXLOG D OLJKWKRXVH LQ ORQGRQ! L FDQ LPPHGLDWHOB VHH BRXU REMHFWLRQ. ORQGRQ KDV QR URFNB VKRUHV, DQG VR QR QHHG RI RQH, EXW BRXU HASHULPHQWV ZLWK ODQWHUQV JLYH XV WKH LGHDO HAFXVH WR EXLOG RQH DV D SODFH WR WHVW WKHP. WKH RSSRUWXQLWLHV WKLV ZLOO DIIRUG DUH PDQB: WKH GHOLYHUB RI ODUJH FUDWHV RI HTXLSPHQW ZLOO JR XQQRWLFHG, FRQVLGHUHG DV SDUW RI WKH QDWXUDO EXVLQHVV RI WKH SODFH; LWV ORFDWLRQ RQ D EXVB ZKDUI ZRXOG GLVJXLVH WKH QHFHVVDUB FRPLQJV DQG JRLQJV RI RXU FR-FRQVSLUDWRUV; WKH ZDWHUZDB ZLOO SURYLGH XV ZLWK UHDGB WUDQVSRUWDWLRQ ERWK LQODQG YLD WKH FDQDOV DQG WR WKH GRFNV DW WLOEXUB IRU RXU LQWHUQDWLRQDO YHQWXUHV. QRW OHDVW, WKH HAWUDRUGLQDUB SRZHU QHHGHG IRU RXU GHYLFHV ZLOO EH PLVWDNHQ IRU WKH HQHUJB UHTXLUHG WR UXQ BRXU SXEOLF HASHULPHQWV. L KDYH OLWWOH HASHUWLVH LQ WKH GHVLJQ RU HQJLQHHULQJ RI VXFK VWUXFWXUHV, EXW L LPDJLQH WKDW WKHB UHTXLUH VXEVWDQWLDO IRRWLQJV. WKH GHYHORSPHQW RI WKHVH ZLOO SURYLGH WKH FRYHU ZH QHHG WR FRQVWUXFW RXU VHFUHW KHDGTXDUWHUV XQGHU WKH PRUH SXEOLF IDFH RI WKH OLJKWKRXVH LWVHOI DQG LWV DQFLOODUB EXLOGLQJV. LW PDB EH WKDW L KDYH PLVVHG VRPHWKLQJ LPSRUWDQW LQ PB FRQVLGHUDWLRQV, LQ ZKLFK FDVH SOHDVH GR SRLQW WKDW RXW, EXW LI ZH DUH WR SDVV RQ RXU GLVFRYHULHV, DPELWLRQV DQG SODQV WR WKH QHAW JHQHUDWLRQ ZH ZLOO QHHG WR JLYH WKHP D PRUH SHUPDQHQW KRPH, VR L KRSH ZH FDQ DJUHH WRJHWKHU RQ WKH EHVW ZDB WR SURFHHG. BRXUV, FK")
    cipher_identifier.identify("HRAODDMAYTRHHEEXEOECEOSDISEITPTMNAELELONHOORRWLNOTNBMELAFMOCEOHRPRSEBIESKHEAMIIRUORKGIIESEYXAONVTCDRAATCTLONETEVGCAIOOHEYIFMORNEAEUUSDEONBSRTRNWEIDTKMEARLDAUEWKGHMHAAOXCERENHEERFTTRETESPIODAOXCERUALTOYWKTAHATLGIVTCDERIMOHAHYCSWTEIUVYAYKOOHTGAAEERODUEYWLNOOOHEUSNETNMHBAHOIHHENUNCORNGBIIETYODFECLGSRANKMTSLHITUCSRYCSFETPEWEUTTKIODOOIRSEATRLKUOEROHEMHGKHMHEIVEPERNNYEOEAECGAETAFENEMHRTPAEPRGYPNHTRHILHKWEREIOAEEODOTESOBANUEWLTYEOUUHRISLESOERIBENAELOUWIVEELTHRALISDOMHGUEOOIRLRLHITTREOSLISEIATREVTRTALOTGUEIRTTFLITRSINHGTNBANWCHSVTIESAENELAIKNRPIDSSMBINUBKYDTVNHGRTOOHMBOODNVSEWEOETIPREESCFTIFMNNOLFEATTGMEOERSOHAWLHITWXARAVYMEWLEOERSOOGASTRORUHTYELNSAAAEHITERTBCOUNEAMNODRELITNWTEEMTRETNSPTULATNTTRRTONDKWCOETSETYVOOIUITINNSCHSEHLENYLAEEHECADIITLHOENICEUOHEEPSRODAASSNLMEPSVHIITOBYNENWROTNITSGLDASUSUOISTSHRNSNTCSCELASDTITMSDIENFUITMETNICCOHAGTGMBHCLOAHOCEEIGDSLFEETRHTIKLLHEJIAYMRAIRLNSEYABNIDTAHOGTIDOTNOSSEEMAYAYPGAUVLDIFDMHGIORENOETKSNEOHEGAUTELEEIDISNERNEIWIPRENSYRNDEHOWFLIEEPEETEOGIMHCFUNAATNOEWKTNYYCLEORMEIFMOAUECVAAOARLOOOCPOESOAITKGDEIFTMDITFSEESELILILTUBGDEIFYNNYSTTOOWTEREIUHETHTFSTFMETSOAEHIAWLEDRLEKWAHRTTRFSAISCOIWTKWOECIDTEOOUTRKINFEADERDTNAIOACPRHSUBIMOEUHEVINEHFEEGHSOPABAEWRHAREFNHMETUATRMEITNFSOSTUVKWESEILEIITAHETACELESMTTIEAECSOSISDNEEAETTCHIIOOTEHEEWLEHTYETNNYTYULKTBSDRKGIAEIHNDBSPESLATBTD")
    

def tests():

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