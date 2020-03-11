# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   trulyMostPopular.py
@Contact :   9824373@qq.com
@Desc    :
            每年，政府都会公布一万个最常见的婴儿名字和它们出现的频率，也就是同名婴儿的数量。有些名字有多种拼法，例如，John 和 Jon 本质上是相同的名字，但被当成了两个名字公布出来。给定两个列表，一个是名字及对应的频率，另一个是本质相同的名字对。设计一个算法打印出每个真实名字的实际频率。注意，如果 John 和 Jon 是相同的，并且 Jon 和 Johnny 相同，则 John 与 Johnny 也相同，即它们有传递和对称性。

            在结果列表中，选择字典序最小的名字作为真实名字。

            示例：

            输入：names = ["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"], synonyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"]
            输出：["John(27)","Chris(36)"]
            提示：

            names.length <= 100000


            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/baby-names-lcci

@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-10     zhan        1.0         None
'''
from typing import List

class Solution:
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        # flag = [eval(namePair) for namePair in synonyms]

        myMap = {}
        eleLst = []
        for namePair in synonyms:
            n1, n2 = namePair[1:-1].split(',')
            if n1 in myMap and n2 not in myMap:
                myMap[n1].add(n2)
                myMap[n2] = myMap[n1]
            elif n2 in myMap and n1 not in myMap:
                myMap[n2].add(n1)
                myMap[n1] = myMap[n2]
            elif n2 not in myMap and n1 not in myMap:
                myMap[n1] = {n1,n2}
                myMap[n2] = myMap[n1]
                eleLst.append(myMap[n1])
            else:# 都在字典中，合并val集合,
                # 判断是否需要合并
                if myMap[n1] != myMap[n2]:
                    eleLst.remove(myMap[n1])
                    eleLst.remove(myMap[n2])
                    newSet = myMap[n2].union(myMap[n1])
                    for item in newSet:
                        myMap[item] = newSet

                    eleLst.append(newSet)


        list2key = {}
        for item in eleLst:
            curKey = ",".join(item)
            list2key[curKey] = 9*'z'
            for ele in item:
                list2key[curKey] = min(list2key[curKey],ele)

        ansdict = {}
        for name in names:
            nms = name.split('(')
            iCount = int(nms[1][:-1])
            nm = nms[0]
            if nm in myMap:
                curkey = ",".join(myMap[nm])
                shortName = list2key[curkey]
            else:
                shortName = nm

            ansdict.setdefault(shortName,0)
            ansdict[shortName] += iCount

        ans = []
        for name, count in ansdict.items():
            ans.append(name+'(' + str(count) + ')')

        return ans


if __name__ == '__main__':
    names = ["John(15)", "Jon(12)", "Chris(13)", "Kris(4)", "Christopher(19)"]
    synonyms = ["(Jon,John)",
                "(John,Johnny)",
                "(Chris,Kris)",
                "(Chris,Christopher)"
                ]

    names = ["Fcclu(70)", "Ommjh(63)", "Dnsay(60)", "Qbmk(45)", "Unsb(26)", "Gauuk(75)", "Wzyyim(34)", "Bnea(55)", "Kri(71)",
             "Qnaakk(76)", "Gnplfi(68)", "Hfp(97)", "Qoi(70)", "Ijveol(46)", "Iidh(64)", "Qiy(26)", "Mcnef(59)", "Hvueqc(91)",
             "Obcbxb(54)", "Dhe(79)", "Jfq(26)", "Uwjsu(41)", "Wfmspz(39)", "Ebov(96)", "Ofl(72)", "Uvkdpn(71)", "Avcp(41)",
             "Msyr(9)", "Pgfpma(95)", "Vbp(89)", "Koaak(53)", "Qyqifg(85)", "Dwayf(97)", "Oltadg(95)", "Mwwvj(70)", "Uxf(74)",
             "Qvjp(6)", "Grqrg(81)", "Naf(3)", "Xjjol(62)", "Ibink(32)", "Qxabri(41)", "Ucqh(51)", "Mtz(72)", "Aeax(82)",
             "Kxutz(5)", "Qweye(15)", "Ard(82)", "Chycnm(4)", "Hcvcgc(97)", "Knpuq(61)", "Yeekgc(11)", "Ntfr(70)", "Lucf(62)",
             "Uhsg(23)", "Csh(39)", "Txixz(87)", "Kgabb(80)", "Weusps(79)", "Nuq(61)", "Drzsnw(87)", "Xxmsn(98)", "Onnev(77)",
             "Owh(64)", "Fpaf(46)", "Hvia(6)", "Kufa(95)", "Chhmx(66)", "Avmzs(39)", "Okwuq(96)", "Hrschk(30)", "Ffwni(67)",
             "Wpagta(25)", "Npilye(14)", "Axwtno(57)", "Qxkjt(31)", "Dwifi(51)", "Kasgmw(95)", "Vgxj(11)", "Nsgbth(26)",
             "Nzaz(51)", "Owk(87)", "Yjc(94)", "Hljt(21)", "Jvqg(47)", "Alrksy(69)", "Tlv(95)", "Acohsf(86)", "Qejo(60)",
             "Gbclj(20)", "Nekuam(17)", "Meutux(64)", "Tuvzkd(85)", "Fvkhz(98)", "Rngl(12)", "Gbkq(77)", "Uzgx(65)", "Ghc(15)",
             "Qsc(48)", "Siv(47)"]
    synonyms = ["(Gnplfi,Qxabri)", "(Uzgx,Siv)", "(Bnea,Lucf)", "(Qnaakk,Msyr)", "(Grqrg,Gbclj)", "(Uhsg,Qejo)", "(Csh,Wpagta)",
                 "(Xjjol,Lucf)", "(Qoi,Obcbxb)", "(Npilye,Vgxj)", "(Aeax,Ghc)", "(Txixz,Ffwni)", "(Qweye,Qsc)", "(Kri,Tuvzkd)",
                 "(Ommjh,Vbp)", "(Pgfpma,Xxmsn)", "(Uhsg,Csh)", "(Qvjp,Kxutz)", "(Qxkjt,Tlv)", "(Wfmspz,Owk)", "(Dwayf,Chycnm)",
                 "(Iidh,Qvjp)", "(Dnsay,Rngl)", "(Qweye,Tlv)", "(Wzyyim,Kxutz)", "(Hvueqc,Qejo)", "(Tlv,Ghc)", "(Hvia,Fvkhz)",
                 "(Msyr,Owk)", "(Hrschk,Hljt)", "(Owh,Gbclj)", "(Dwifi,Uzgx)", "(Iidh,Fpaf)", "(Iidh,Meutux)", "(Txixz,Ghc)",
                 "(Gbclj,Qsc)", "(Kgabb,Tuvzkd)", "(Uwjsu,Grqrg)", "(Vbp,Dwayf)", "(Xxmsn,Chhmx)", "(Uxf,Uzgx)"]

    ans = Solution().trulyMostPopular(names,synonyms)
    print(ans)



# "Ommjh(152)","Bnea(179)","Kgabb(236)","Msyr(85)","Hvueqc(174)","Gbclj(206)","Owk(126)","Chhmx(259)","Koaak(53)","Qyqifg(85)","Chycnm(101)","Oltadg(95)","Mwwvj(70)","Dwifi(237)","Naf(3)","Ibink(32)","Ucqh(51)","Mtz(72)","Aeax(97)","Qsc(63)","Ard(82)","Hcvcgc(97)","Knpuq(61)","Yeekgc(11)","Ntfr(70)","Csh(64)","Ffwni(154)","Weusps(79)","Nuq(61)","Drzsnw(87)","Onnev(77)","Fvkhz(104)","Kufa(95)","Avmzs(39)","Okwuq(96)","Hljt(51)","Npilye(25)","Axwtno(57)","Qxkjt(126)","Kasgmw(95)","Nsgbth(26)","Nzaz(51)","Yjc(94)","Jvqg(47)","Alrksy(69)","Acohsf(86)","Nekuam(17)","Gbkq(77)"]

# ,"Chycnm(253)","Koaak(53)","Qyqifg(85)","Oltadg(95)","Mwwvj(70)","Naf(3)","Ibink(32)","Ucqh(51)","Mtz(72)","Ard(82)","Hcvcgc(97)","Knpuq(61)","Yeekgc(11)","Ntfr(70)","Bnea(179)","Weusps(79)","Nuq(61)","Drzsnw(87)","Chhmx(259)","Onnev(77)","Kufa(95)","Avmzs(39)","Okwuq(96)","Hljt(51)","Npilye(25)","Axwtno(57)","Kasgmw(95)","Nsgbth(26)","Nzaz(51)","Msyr(211)","Yjc(94)","Jvqg(47)","Alrksy(69)","Aeax(646)","Acohsf(86)","Csh(238)","Nekuam(17)","Kgabb(236)","Fvkhz(104)","Gbkq(77)","Dwifi(237)"]





