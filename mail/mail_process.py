text = """
早速サポートへのお問い合わせありがとうございました。
現在サポートチームへ解決に向け動いてもらうよう打診しております。
ただ、現状貴社のサポートプランは月額0円のブロンズプランとなっておりまして、
障害時のみサポートを受付させていただいております。(平時のサポートはございません。)
今後もし同様のサポートを受けていただけるのであればこれを機に月額4万円のゴールドプラン
に変更させていただけないでしょうか？
---
クラウドエース株式会社　第一営業部
" 信実さを持ち、応えていく "
茨城県出身　　石塚　健斗　〈KENTO　ISHIZUKA〉　
e-mail　ishizuka@cloud-ace.jp
web　　https://www.cloud-ace.jp?xx=1

tel　　  03-6280-5939　（本社）
tel         080-3668-6458   （携帯）
fax　　 03-6800-3954 
address 〒100-0004 
東京都千代田区大手町2丁目6番2号 日本ビルヂング11F
"""

import nagisa
from talon.signature.bruteforce import extract_signature

def detect_verb(input):
    texts = input.splitlines()
    flag = False
    for text in texts:
        words = nagisa.tagging(text)
        print("___________________________________")

        if '動詞' in words.postags:
            flag = True
            return flag
    return flag

def extract_mail(input):
    input = input.replace("=", "-")
    input = input.replace("*", "-")
    input = input.replace("_", "-")
    text, signature= extract_signature(input)
    if type(signature) is "string":
        print("Detected sig")
        print(signature)
    if type(signature) is "string" and detect_verb(signature) == True:
        print("Signature has V")
        return input
    return text