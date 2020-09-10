"""
day: 2020-09-10
url: https://leetcode-cn.com/problems/delete-columns-to-make-sorted-ii/
题目名: 删列造序II
给定由 N 个小写字母字符串组成的数组 A,其中每个字符串长度相等。
选取一个删除索引序列,对于 A 中的每个字符串,删除对应每个索引处的字符。
比如,有 A = ["abcdef", "uvwxyz"],删除索引序列 {0, 2, 3},删除后 A 为["bef", "vyz"]。
假设,我们选择了一组删除索引 D,那么在执行删除操作之后,最终得到的数组的元素是按 字典序（A[0] <= A[1] <= A[2] ... <= A[A.length - 1]）排列的
然后请你返回 D.length 的最小可能值。
示例:
    输入: ["ca","bb","ac"]
    输出: 1
思路:
    要想尽量删除少的列,那么就要从第一列开始尝试遍历,将不满足条件的列删除,直到
    某一列满足条件,就可以返回结果了.
"""
from typing import List


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        count = 0
        # 记录的是满足条件的所有列的每一个元素的的严格大于情况.
        cuts = [False] * (len(A) - 1)
        for col in zip(*A):
            # sign_1表示cuts是否全都为True
            # sign_2表示当前列是否满足条件
            sign_1 = sign_2 = True
            for i in range(len(col)-1):
                if not cuts[i]:
                    sign_1 = False
                if not cuts[i] and col[i] > col[i+1]:
                    sign_2 = False
                    break
            # 如果cuts全都是严格大于,那么就可以返回结果了.
            if sign_1:
                break
            # 如果当前列不满足条件,就需要删除,否则更新cuts
            if sign_2:
                for i in range(len(col)-1):
                    if col[i] < col[i+1]:
                        cuts[i] = True
            else:
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.minDeletionSize([
        "vvxejcrulnxamfxbkqlnpiahmbuvltqjqtwocaxapyicraeufsoppnvgjzviemxjurvmqgudlzhgupsvsxzzfgfkkrdalgnqommw",
        "lqakiuozyiuuyjfbjsfkbttmrnctgexxsizfraxfspvffrfsangdsbueyqfpkpqieqaafhbaocbzajmnidtnwqgkprixqzdfblwp",
        "majviidklyhfrixjwdhkbwoyuoldrttduhfokariaeqwgyzscjoibzbhsjtfcefzlwnskmzltizvbigduavvkvfjohjbcslgvwcy",
        "ddichavlcenxkpnbqkiewybdkmsafrnsbtnovatldrxlqcvgmeawusyflznkjbdablvvlbotyzydzbpouwbxotvbrpssoafyaran",
        "mevbayyazaqbxlnogwzzzsfrziuyrzinangdearuztvhscqdotorjdaoempuzrydtmgylzkcfcdhtuovsueuyfmjdyyqaevempxv",
        "swxumgueqqyztrcstcpsziirmqeugrndptzdfaovvvcomhljsvpoghfhcxnzetmruxrhmvvpljewvojhuztzjesommrnwhvgwrcf",
        "oouxsczlswqduchqbexhcammderstuxjludxgalvdyvozzjlrkdvciahtmoqiofieftsaioawvswqqvijnamrbbanxpgffixzvkv",
        "bcxmaudsiwrfcetjotmjbxrzxeuterckvcdcqbncdpyybqpuibptfwaaeyglghhpynyagjayiryyzugkscxlhctekocopsqfibai",
        "dmtjaomvcvtmcmyprrpkthotiouicaiigrmarcbgwpgkaxfgogskgilastwjyrkwlbqtntnxgkvfpfdypkxbrseiriqtnwqteooa",
        "xrkvkjseixbgjfbbeswzygmncfriynnjbfthucsjtbkhsiehqmchcfqzjpqajnfdxbpeaawtjukuaadunhdxtwjeyzlibxanlgtt",
        "dcbzjujzdtfrzvmectlxxnzrbrjeoajfqnmxhcvltpcltpawljpmjtdwtfarmgwbhybzljmboopukijtyxjpptgfkexhohrmpldf",
        "xeasfysgofkerpfvhufzmcssnprkpwfnbqxypcmsroeeesfcocbrkacqkuimbfoooiyczxlkmptfiocbwbjpkgihawrufyovgxsu",
        "tnnvfwbuavaifeieajrnvgwpiphxwwapweonmcdyxccirwdlqpngvckdduhuosomoekppxoksilhvmpdhpmajtpxvipeenmkkafd",
        "kjsnbzgyzozlfsxswyllbesjggiiicicnjadecgzgwddmfdrlyayuhmmuuugcnkbotxlrcedjnmlrkikxsjqqgejqkdglkazvjic",
        "syxvebchdqgxrqfdgepzkwalatgdmopigdvyhdkgkoenrjyjojrnouysjfzbzhluavvvzgigcyprbttdbdmvwunjzcmokicbmwig",
        "jobdhujosadevfjpvjblhkrtwrcgigbhadteadbkuubveqjqktmnetrqqztjkajjzgwfxtuzttdxqffwnltynwxmthzndzweyack",
        "sjlvidfovhreachpjlohhfiwhckivfnzkycmzdbljbqsgieohgcmfpugyoyiuvrrnmlbwedkkiomtahiunkxbydwhgnrpaqocvha",
        "yuuobhxdqkefwsztcrsutpqrrqdtgcivycorydzsirphcoltyffxxiwvykyvhgheuabmujfgystnxecahzcxeeqleuqnpejtlrtb",
        "odoqphvufxglfojqhdhagryhlrdlphcrvrlxmeenusjojhayyuryjbqjimpbrskniqpozpwxvnxzzawjxaidfunanyfnpkuqvgcg",
        "tnedwjomyuwgyuonaswjlvwnoytgbmawavdjaewzsgxgrvqlzyojbxtloxxqggpleawbetmnqmtqwvfvittukpegmccdvbfijvwc",
        "tmtmjvrbdkerpukrcumpctmmxzoejxmpuepkuftnmieoieesueulddkchrrnovtxoqtubxwqossmwyvgsrgqansjdqcbvftahhgn",
        "rttugtufedysqbxcshtnpsrcdgiqiqqoqdlhxgkdektndvvrrpizdysvxwcsmsvrhawowloiumbacceurroxbzugcqqwdwseiqcg",
        "nlrbahdkkzhlbjxaevpdfbxpfzklvheggwxsmgnjgnopqrmgdvhemsgaffrfyogcyfqqtzyuasmlfzhxlrpuvhypoggytwzbkdak",
        "pfsqgoawrzmtppneapcmacwsrfxfxnxgbsznygloeshnfftsnnirispfgsnnmdbwknjkslqrbzswjowsufnunazstbgggmjjaaal",
        "dbzwiiikwpxdamatqayeqtovwqbncnhuvujcdhcahpazjbuavofknubgkkezaiuvkyxbqihpszfvidrpolmtzfpdbubngeufukze",
        "hiutwttchtsxstfmonvrmfswlqhtkcelwrkxlhmkotjjazdlryuxbnerlxbegtsfyweilekuqqnuyzkljtjsajisdlficxpyodac",
        "oidzdupsecdfawqbyofdwglamhtveotbrwguzhhtafdxqugpibjlgfcykeinoyeddeuzbsuaovzvcyagbgqwpnqjurrmgucxxvzr",
        "ttfequhoomcbckhriplkrjldjjgbuosozsxhdidapwgmiztbjriycuzhtwbablrvegmntvihpxwvtohcqmrpbpdeofexcffyisbs",
        "rxdrwsuixnvxwxxvxqdamenqsmjqakulfajsxiicpaifpqykqfiqtqumjkmegszbxmrjfajxohkvbxntzjnkgqutuhgwkazdqcdo",
        "qtmawynhcbfvmkmfejmrwfforuetbotadjxhhiahwysegxklkssgmgpjyjzivlxzhybjvpoxdzcyqsdtjfcniqwrjbeveamhfrun",
        "fbujppkgzjxpkzezgsmrvbrwtarwyhtwbiyoziklmefyptiapavsnwcfilgcnobxtykhdqbabagvloxmjwpoqfhxkxtruklzliaj",
        "lvsxjycvwztduyyiiemkfnbezdirrnpwellteitnwaoctlihcxsxbnydicytcltfewazeyvbbsyztsdmyjkfmbeanovqtgojmpfi",
        "lhlpqymecsqtctvidukotjbdlpfxfvoedfgmrirqndvaehyxexnbypoeugbuuwtvvbziulwbqlbylljehaxmhvwyvbatccmglhmv",
        "jjzradoxekdczywpwepqpcafjoiffjtulxqlsikulgmevkjlypwbedxrfmjltlrqzsrzxlwmtfculzsomxrehgbkrmamrisxpwfp",
        "yspowyvusaurikqpoixlzqmiabhgkvszveuxrjxcondwnihowwtffrmcthdnksepcspmteignoxhmetkddmndtmgytqjdmepfhfi",
        "csctrlhcvsshxiipwmduhnrkiupqszquwdwxbjnouzreyjyqeljbsekdunzmhfgnjvvhojevgoynwpxvlsilcrbtisdynbjwdmov",
        "jlhaprojrzbhhtotkhdfqkspiubdnzomurdbrkkdwrstpexaligmjfmjyftuwhkqeludlutrrndsmsbylbmpdvikmombgpdpgwij",
        "bjbvltxijnsihgjurnwfgywgrebqnxuitzqvdkzootvmjhwzotqfyxepypfdvykzwidscykpmafucybkqnkvmgwqjrfzzixagdoe",
        "xtfcxgazxutdbazevijusdnkabhnkxypibfujldakzuhgzgneqwpumowqhirpqvmnmvxeeuixuoqrywjatlagqmccpylzwcogppd",
        "gykduitgbuxizbmdluoqzjspgrudcihhdfkvolpdbaodqxmdradsvbxzpqobwijvbtdaauvhxmyzogzesmxjjtuyclznvrtjvvjo",
        "nkbpmqmghhqlrhwnfgopfiubugrumefwlqqrzlwiseclgiqzkoqfljqfjqfqsvlmxdkhdfndtgvmuxpbfwdzkasverryenzfqxwi",
        "vwdhcgxazszewfahphcgaruzjmswzvrrtuqoxluibgmaziifyceelkcpgemlciewmvewcpgoqxueiyrysjrpiepkqcmnbkehdorn",
        "gnqqyxsnoacdqafifihlvgymormytbqvcklydlcrcwbeuinvecndshiaothpobikbdhxpujyqxaipkkyrxfanwxykpgayexfexzf",
        "pqbhqleuzhznwedawihmkqsibsshslbmrecvpmxbynqlbhcsaclbixbphfndiaepuqchgfxpoxvvfopjmiwevfsjtjynlpjbchve",
        "uyxrklfqbbbpdclgblgkevrqgmmvwpuxqeqhymkcnvikfpcukuznocokolqegtchtzcboebircudlmlguyceqdtfeveovxoppsex",
        "jfqhlqkrlgyitnwzcfofkmmzqduraaxydaafdmeorhmalzxdaakrlfemruoxqyaaluwodznukscrnnsxlnhocgollnfbunnkmcvs",
        "fimpptwphjomdoehcpovclnoshpufjscxcjbsmcusxjilgikoqqqjrmynxmrdlijvkwdkolpieurtyvxomdkzfsrgtrgjjxcctup",
        "nldvamkchsjbpqecawtqocstjoiuhiesvxkeomovazwheycwrrhaofsesgkiiislzefleabsqfpspdwkdxvddrrffqrcmcxijtkb",
        "euyxnjjezrloluwwngnpstoqubtlatkcotkvhncajvaeinpqnzozglctrvwvkbpygsjbtnyyyrbnkjlqkxhciuzglilyxnihjhjm",
        "aiesxbgplcbtumyxurccirxsufuleardkvjppnsljfknqqiordouqxysneqcpcymppjrsidyjwzizxljjxpbmuhtrwbxsclfdqwm",
        "rmtfualnxcjnsrsrwtxknyzoqxejeqcglwzmjnbsgrlefrgrletnucutlmfcteyvzbiglpmzviyhyqazvhulxtqqlnqlfwmcuxxy",
        "awrxgheeaoszkfddwadtohjqfayvgafqmcovlnpshydzfecfhazmhqhzyjldwljpiesdtfywijnninczrctinrvnbckazagjaaqe",
        "oiwkfjyozyhsirieidacsdzdaojdikpfdydjbnaxvelruqaouhifvvqfcjjkdmrrfrpdtxyapannqicvkwvvgalzqxgouoajfpzn",
        "lsmzdlwfbvwathgnscdgaltlqafumdukvarclogejgozolampqewjglziaveeiszgemfssiquhcuqkhjelrwkygcccbzdzyqtloo",
        "fdtxqknyrsanwjwdkcsojtsbjvkmacrsqvsirojghqgegnvliyxhqdmescoyvzvahdfhogjcyppkdwekhdhsjfejaocclmfjogzw",
        "xvbutyybaqhvetstybermemdanmsjsnfkhibkoauyphnwggncyrlicryfhsxehxrcqlnbfcyvyjopotalqevayptkzxpwunwvrba",
        "rmjjkhpgdlmfepsbvsdfwuoeiajqoelxkleapogwxmnyrqefblxiznwchridsphoyudlypcxyakmzgottlpartkgkrmmwnmzvglz",
        "egvamcvftjfdhabkkyldlbvvupwxflgmcjipgpdgfthxatoqgfvfizsiacjiymcwmsefguxhkpmpyijxekjbnfuonhkuolvfabus",
        "jcysacpeljlcnnmlaxnzjtadwphppngexewlcpnowbltcdwwxzgpqnkogfgfslqfycetghgchveecjrmrxpjghovhsgxckkxzkyc",
        "akyndnocnvrbizjplcswjyyapnpmzwuhmubqnpkzfldhzazkmkbiwlnokjsispxyzclnxkxsvfegygnqnfpqjbjeedxrlejefgqu",
        "ljpnsefnaxgntothoyoexdipzmujbaispfdjaqcbqgjsedyadgjlvokyyvnmjyvdklkrlixsdvhfedbtussgottmgmmgnfgsuzkr",
        "dfahrhmtrnmdsckcswccctmjbaxsgorcqvqjsqaguesljphonqoyjwfpbxlfcvcxptuumxdfhyrvlxjlewvwnmbvsdreswvdazeg",
        "pyhemaflwmgwdpntkiaxoankebqpsaajelyrkqxlrfnvwdaecstieumnhisyavdmjhykxdswlclikmcxjpycnttepqlxgmapfsyk",
        "bskiaplfbfopgeledgbtnhjugwnqkubdftswcqrpnpaojwipwghfmaxxvgqrbgkiamhklmpqlshbuwrahiuicimgtquezvtdieju",
        "dajfjqqeqonwyvuyostjlyksuqmgdqorptvqoqquijccopxsewwwxxktwuaiqpbenszqzmvrxvbqkmxidbqnwoxjpzelbnqwhjuh",
        "mjaqekpjoetibplniwilxiiexrljgicgmkkueqouptkvbhlzdlfbtcbdsfmzqzanszwktvoniazplvkxbdfpxsiubrgxpobdsfta",
        "zfkqgakxkjhcirvvhwrhinaybrymxdqtleqqlrhayaxqehgqihbcdidwozrgdpaezpzcvmbtgpennwrftagsbxcnrtzvriauokmi",
        "jdbxxhdirtrrruotajmvzaiwpvsbndrnywzbsrzbkkdvybketfvaltfazlvppsbbcbzjzskictpshyrztnnqnlvcxlmauujbpawc",
        "zkbbxpufdgijsziubgysvtghzgfjzylfwhnigrrertqptsoormkhajtlmuzlbukgwsnigurlzovmtihyfroiasrpqsvbiswashge",
        "nlxvrmpgsdbkplnprypkrvfvuvwlnmpmtqsrirlpahzjxawbahrkehbcbeorefhdhfmndtcshceoovmchkjuzygqyqbpvibiueju",
        "tqkckzvcawhgbwafeueqdokidutnzoblajwqlstmfaoumjfaqsqzfbzgwnwdrwjfvgulzwsughjpazwgjofslnrajoetxxpcdhvm",
        "nfkquuxgsqgtpaoqqmvzhkvehsdeoghgukmpdszszwneohxzelgnmqfqlkwxerlxnojiblbnigfawxwxidlzzhomcrbvvdhhgisc",
        "gqdeibxktuaqdheoegcidmqdkvddwhckwdjoxtsgrdnfvboqdxalekkqbvwjnfwswjmddnppqgarnhaofrweinsfybfcmgelrvkq",
        "jljgahkwfqwofzgmvhjarqrqpordhumrawqchtshdocsrzjlugnlflzhdqkizvhcheppgxzujiockxghvbhmpwqgqkhglcfjmyuh",
        "ajoyvegffjencywgixdmbkvfflvhjyvwynrwmtzkzkdncppzicvahvueygwnzhovbfxvqehxufbppwgrlsivokozbouhyojwbhwb",
        "iekpdgmeaihgkvvxobkwoapvomuobqytcywkqtcmpphaevnhvgzqxillcanxzzuszfcemdzhdrnktkfljduzxoviqpucqeejyzor",
        "cbhonhiqdjyisbnyvixhmgbhmwpakzyeqsfwcthpnecitkmzhtjqmfzimlkyqxraxotmrolyeciwysmyopzxrdlifzpbfyvgpmps",
        "bqqnpzynrwlinhydagfkpmblccjlqymmpzytetrqbrwwkcmofbytcvephmplyjuoyqluflqoexgbrstksxcezkrkfofppuyyjmrd",
        "xinequgxdwrjcanssohvbakrkaoahgdnfuprhumdyjtigkfafbhzohpgiwbiggoueqribgwnmfzsdjygdaqgpdnghejvqyerhtcn",
        "daxnbubhbvicqiotyscvprrmwrcirkatsymwsuddszdmcwobdtonvppphmyhisduwicerndyrmviugmjmsecqfjfuilitbprekpb",
        "fxkpfnwvshjhbsjrdpaarwvoyxubpzatxevbxubgdteqaovhphsohvnrwhjgrfyrlgdciqkskvalxfzeqkiokvzqfiqwzeygqklz",
        "youflzgvieowuzcljmqxwstpibfqkynsxljscuyltpppcvfbslcqocxuyztickgnyexgqyravovkykpscvzyhfdwjtdyyleejfav",
        "wkmzqnkvlxrzjnjlvnnqlpydvvyavzhaylfjjurpogexwfipzetvewqagsltqugadpsfalwyhhcxstyqpeddrszjyuqvkjmrmcfr",
        "pnmreilozjohbhgentgtrsowcmoxcfwpxazygvqeocxiapqsxzyctlebqmhwqxpnpnorksiqmlwbgzuaxxmtyelmxihnmtwqexvh",
        "mgrjsweqfamcsrcxkplgyxivnhleovcqdznyfvnfqhtpxdbutfocffgdoplvntuixroinocjkhurwywnoocqceseettdaidkfpgk",
        "kstvfondsurxhxhtuiooyrbzknrkcpcxzwdzrveikjyyaazidyuaniohwejiacnekknhkbwhkrmtwwowrgbwmncaikafkadizmtg",
        "nhgxqrasosotxncapimdjiyllndiaflwqublvvnkqkjdmckidcygyhwbjwmoutzhyllumsapjenpmkqywtitfywsleeaqcfcyazh",
        "oyzmysmwmkvphyoxzvqtjmaykkmdmtqxlfpjgvklsnvanyxvhoxzpuuxyeeubozejyxbibxdfcfzvqmtxmyxgxquaouiucehxvgn",
        "hakggvicoivhvgxoesqwjkrepbfplkwfurturwbbejtpozgxttnnkipguegbesvdhglhpfhibqhoqtxgwdgqjdfirmcukvdgswjy",
        "kfdhfecozbxxwynqntdwapxhsxnkzjcuotriuwwdgnoinqeohkmxctrcygqppdjuotwvayefbglmvggbqhsyonasdkibofxaekhk",
        "zdanrjtgzjqrmmdvpgiaayjzmonbtuqdojiwcwrfncciemecubruaxxfwuqqvuflprqqyybhllelghixpkuubmzwcpdyjglryeoz",
        "nyfwepwfcmgtkfmuwnkrsdwwwrxvgjhwkihiixrbagjjkkysyiiubtapzpascckcngqygqkaovzkjleqhguxwgexskydpupehhln",
        "yousfqsojqtyeoirmrjzfehlehpmoxyprkiduxsgxcgaddoqxstyarcavfappojjpsxxivcrdzpofitzunfjdmidumnnkcnxczcs",
        "wazcovqsnqizkwvbufknrzfiyaufckaifuclgxeljhhjfizfieopshkwmnrceegdamnfewooecnomggcsmciynypkkcqxezjyjbl",
        "yrryieqyeefiubgywiugmhlwcecyisevwawsexystbsikfjbwzgljdpldorogwyvcoqreqhloaqiogbanukrhmccbubuvzgvafqr",
        "gtnbojfqcnyhcodzzvrerqcwaogevcczrstelxssrqabvqnqglwuqgjwqgjxjvojisrhtrjogumpojtlnxbgznjftwacshuutzyq",
        "oovyqqzzxreckjykwwkhippffulmjjowauswcxutmujujibyfrxwabfjbyhjkxzlotaecsyziyytxebtinmwcwxgdvbzrbiquwag",
        "jzigqkybsssewtjmmeheiwccfweiufeqgeqrnxvyjzxhacxjccxefyjkuftkiaablvtdwivtfpkovprbripodntdlclxdntwkayv",
        "jqskcwpdcpunmncsynowjifmhdpzosehgbbdbypveqqczdptqbagrfhunclqpehwhdaujkamecpykuabvajpevysrpkiztasdtsr",
        "hgludaxhhjdagglsjudkefuoilctomlfldxxwzptbsmqcealippibzydfokzddfaxbcczgwxkkbrzbgqptwfgagvlniuqqagrcen"
    ]))
