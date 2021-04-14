import operator

crypt = """VoyfmWchasfpgozsfpsgvtgljsutouhozmbvjssgkywhasbimPywhpgvhihocf,Q.Y.Fvk
zpbu.Avsucjlzgjvfvbwjzsavsswjlgcmomvibnkwgofk,VoyfmWchasf,hbrowgmfwlbrz
VsyawvbsNfouusyobkFcuKshgzlm,oszcmkvvaoysgairlbhzohOcudofagGjvcvzcm
KwaqvjfomhourKpnoyrff.HvlaopbgacffofjqcuqsybgOofym'gzhfbuussonowughScf
kJcsrstcfa,orhfydwnhfrdvcpbhlbrzhcisqvaspaavfhhz,ccsfavfvkhoskpnoyruvjsybw
uupvrmrbcdbozhvlAwuwgafmvtAhuwjobkgiixinohlozskwgofkgourAbuussg(ucbtoupqosdsvdzl).Gwuqsavsyszloglctavsmwfzhbvjss,VoyfmWchasfhbravsWvwscg
vdvlf'gZhcus,cu26Xius1997,hospvcyzvocstvibkwatsbzsdvdisofphm,wcgphwcsflj
wlkg,hbrjcatsfjwosgijqszgkvfzkkwks.Hosmoojlohafojhskokprshrishobrwlbqlogdsz
sogfciuusyfshrsygouroyscmhsuqcugwksflrqvfblfgacblgcmacksfumcbbuhrishzphs
yohbfs.
[2]HgcmTsifihfm2018,avsiccrgvhjszczkacyshoob500twzswcuqcwwszkcyzrdwrl,a
orwbnhvlahosplghzszswbnpcvyglfwlgwuvwzhcym,ourvhjsissuhfhbgsohlrwuhclwuohmsobnionsg.
[3]Avssogatcbfpvcyzqcugsjihpjssmglhflqcyrghghosthghlghzszswbnpcvygpbvpghvfm,dwhohvltwuozpbgaoztsbagsszwuufviuozmlzscsbtwzs
wcuqcwwszwbavsBbwasrZhoasgdwhowbaksuhm-mciyvcbfgvtwagflzshgs."""

message_length = len(crypt)

crypt = crypt.lower()
index = 0
key_len = 3
all_freq = {}
let_sum = 0 
while index < message_length:
    if (crypt[index].isalpha()):
        if (crypt[index]) in all_freq:
            all_freq[crypt[index]] += 1
        else:
            all_freq[crypt[index]] = 1
    index += key_len
    let_sum +=1

for l,v in all_freq.items() :
    all_freq[l] = v / let_sum

all_freq = sorted(all_freq.items(),key=operator.itemgetter(1),reverse=True)

print(all_freq)
    