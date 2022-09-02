#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki 3.0 Template For Python3

    [URL] https://api.droidtown.co/Loki/BulkAPI/

    Request:
        {
            "username": "your_username",
            "input_list": ["your_input_1", "your_input_2"],
            "loki_key": "your_loki_key",
            "filter_list": ["intent_filter_list"] # optional
        }

    Response:
        {
            "status": True,
            "msg": "Success!",
            "version": "v223",
            "word_count_balance": 2000,
            "result_list": [
                {
                    "status": True,
                    "msg": "Success!",
                    "results": [
                        {
                            "intent": "intentName",
                            "pattern": "matchPattern",
                            "utterance": "matchUtterance",
                            "argument": ["arg1", "arg2", ... "argN"]
                        },
                        ...
                    ]
                },
                {
                    "status": False,
                    "msg": "No Match Intent!"
                }
            ]
        }
"""

from requests import post
from requests import codes
import math
import re
import json
try:
    from intent import Loki_HIGH_RISK
    from intent import Loki_LOW_RISK
except:
    from .intent import Loki_HIGH_RISK
    from .intent import Loki_LOW_RISK


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
accountDICT = json.load(open("account.info", encoding = "utf-8"))
USERNAME = accountDICT["username"]
LOKI_KEY = accountDICT["loki_key"]
# 意圖過濾器說明
# INTENT_FILTER = []        => 比對全部的意圖 (預設)
# INTENT_FILTER = [intentN] => 僅比對 INTENT_FILTER 內的意圖
INTENT_FILTER = []
INPUT_LIMIT = 20

class LokiResult():
    status = False
    message = ""
    version = ""
    balance = -1
    lokiResultLIST = []

    def __init__(self, inputLIST, filterLIST):
        self.status = False
        self.message = ""
        self.version = ""
        self.balance = -1
        self.lokiResultLIST = []
        # filterLIST 空的就採用預設的 INTENT_FILTER
        if filterLIST == []:
            filterLIST = INTENT_FILTER

        try:
            result = post(LOKI_URL, json={
                "username": USERNAME,
                "input_list": inputLIST,
                "loki_key": LOKI_KEY,
                "filter_list": filterLIST
            })

            if result.status_code == codes.ok:
                result = result.json()
                self.status = result["status"]
                self.message = result["msg"]
                if result["status"]:
                    self.version = result["version"]
                    self.balance = result["word_count_balance"]
                    self.lokiResultLIST = result["result_list"]
            else:
                self.message = "{} Connection failed.".format(result.status_code)
        except Exception as e:
            self.message = str(e)

    def getStatus(self):
        return self.status

    def getMessage(self):
        return self.message

    def getVersion(self):
        return self.version

    def getBalance(self):
        return self.balance

    def getLokiStatus(self, index):
        rst = False
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["status"]
        return rst

    def getLokiMessage(self, index):
        rst = ""
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["msg"]
        return rst

    def getLokiLen(self, index):
        rst = 0
        if index < len(self.lokiResultLIST):
            if self.lokiResultLIST[index]["status"]:
                rst = len(self.lokiResultLIST[index]["results"])
        return rst

    def getLokiResult(self, index, resultIndex):
        lokiResultDICT = None
        if resultIndex < self.getLokiLen(index):
            lokiResultDICT = self.lokiResultLIST[index]["results"][resultIndex]
        return lokiResultDICT

    def getIntent(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["intent"]
        return rst

    def getPattern(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["pattern"]
        return rst

    def getUtterance(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["utterance"]
        return rst

    def getArgs(self, index, resultIndex):
        rst = []
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["argument"]
        return rst

def runLoki(inputLIST, filterLIST=[]):
    # 將 intent 會使用到的 key 預先設爲空列表
    resultDICT = {
       "risk_value": []
    }
    lokiRst = LokiResult(inputLIST, filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # HIGH_RISK
                if lokiRst.getIntent(index, resultIndex) == "HIGH_RISK":
                    resultDICT = Loki_HIGH_RISK.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # LOW_RISK
                if lokiRst.getIntent(index, resultIndex) == "LOW_RISK":
                    resultDICT = Loki_LOW_RISK.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

def execLoki(content, filterLIST=[], splitLIST=[]):
    """
    input
        content       STR / STR[]    要執行 loki 分析的內容 (可以是字串或字串列表)
        filterLIST    STR[]          指定要比對的意圖 (空列表代表不指定)
        splitLIST     STR[]          指定要斷句的符號 (空列表代表不指定)
                                     * 如果一句 content 內包含同一意圖的多個 utterance，請使用 splitLIST 切割 content

    output
        resultDICT    DICT           合併 runLoki() 的結果，請先設定 runLoki() 的 resultDICT 初始值

    e.g.
        splitLIST = ["！", "，", "。", "？", "!", ",", "
", "；", "　", ";"]
        resultDICT = execLoki("今天天氣如何？後天氣象如何？")                      # output => ["今天天氣"]
        resultDICT = execLoki("今天天氣如何？後天氣象如何？", splitLIST=splitLIST) # output => ["今天天氣", "後天氣象"]
        resultDICT = execLoki(["今天天氣如何？", "後天氣象如何？"])                # output => ["今天天氣", "後天氣象"]
    """
    contentLIST = []
    if type(content) == str:
        contentLIST = [content]
    if type(content) == list:
        contentLIST = content

    resultDICT = {}
    if contentLIST:
        if splitLIST:
            # 依 splitLIST 做分句切割
            splitPAT = re.compile("[{}]".format("".join(splitLIST)))
            inputLIST = []
            for c in contentLIST:
                tmpLIST = splitPAT.split(c)
                inputLIST.extend(tmpLIST)
            # 去除空字串
            while "" in inputLIST:
                inputLIST.remove("")
        else:
            # 不做分句切割處理
            inputLIST = contentLIST

        # 依 INPUT_LIMIT 限制批次處理
        for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
            lokiResultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)
            if "msg" in lokiResultDICT:
                return lokiResultDICT

            # 將 lokiResultDICT 結果儲存至 resultDICT
            for k in lokiResultDICT:
                if k not in resultDICT:
                    resultDICT[k] = []
                resultDICT[k].extend(lokiResultDICT[k])

    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)

    if "msg" in resultDICT:
        print(resultDICT["msg"])

def testIntent():
    # HIGH_RISK
    print("[TEST] HIGH_RISK")
    inputLIST = ['多留意','已高達','一度大跌','下挫超過','且若回補','佈局跑車','低檔佈局','供需失衡','信心潰散','全數走跌','全面走跌','反彈結束','台幣貶值','各被賣逾','合計賣超','同樣創下','同步大跌','同步跳水','回測萬六','多方支撐','大砍聯電','富邦下挫','小跌作收','已經反應','帶來影響','干擾部分','庫存高達','影響大盤','成長停頓','才會缺貨','投信賣超','拉抬績效','持續佈局','持續攀升','提前反映','提款台股','收盤下挫','收盤下跌','收黑拖累','攻上漲停','最低下探','止跌反彈','準備復甦','無情大砍','物價上升','狂飆創高','獲利影響','留意雙鴻','疫情衝擊','發動戰爭','盤勢偏弱','盤勢壓回','直接回測','短線探底','空方狙擊','終場下跌','繼續重挫','股價整理','觀察美股','觸底反彈','調漲報價','資本支出','賣超張數','跌幅超過','跌破萬六','跟著跳水','轉為賣超','通膨上升','通膨惡化','進場佈局','都會缺貨','重回軌道','陷入修正','需求大增','震盪下修','高於預期','全面走弱下','前十大賣超','受大陸影響','合計提款逾','噴出才後悔','報復性消費','將通膨甩鍋','扭轉第一季','掌握主力股','擴大到衰退','毛利率站回','股價也下跌','衰退的可能','解封的刺激','費半更重挫','雙雙年衰退','今天開低走低','低接筆電族群','出現供大於求','出現趨緩疑慮','加上台幣走貶','反映解封題材','台股開低走低','吸引買盤進駐','呈現震盪走勢','回歸空頭走勢','回測萬六支撐','因應外資賣壓','外資今日大減','外資回頭加碼','守住前次低點','守住萬六關卡','封城政策解除','彰銀下跌超過','恐怕美國通膨','成外資提款機','把握最後買點','投信調節對象','拖累台股回跌','推升美國通膨','擔心升息三碼','營收開始轉好','爆發俄烏戰爭','獲得緩衝時間','用政治來處理','監管航運公司','確定升息二碼','美股出現賣壓','股價相對有撐','衝擊拜登總統','衝擊本周台股','觀察到營收好','調節電子權值','賣壓同步湧現','跌幅一度擴大','跌幅也都超過','跌幅持續擴大','跟隨美股下跌','跳空跌破月線','通膨仍有變數','通膨保值債券','通膨居高不下','通膨更加惡化','通膨未見降溫','進場低接買超','達到分散風險','避免跌幅擴大','配合台幣貶值','陷入五窮六絕','聯發科重挫4.6%','不當的財政擴張','供給跟不上需求','創下近十年新低','原先估計的衰退','受美股大跌影響','大幅度回測整理','大跌逾半根停板','大陸復甦的時刻','威脅課徵暴利稅','尚未反映的股票','引爆報復性需求','從全球通膨來看','經濟對策來解決','緊盯聯準會升息','聯準會鷹派緊縮','自營商終止連續','解封帶來的需求','賣壓都相當沉重','較去年同期大增','通膨元兇是普丁','進場低接台積電','遭遇黑色星期一','鎖定遭外資調節','開始有遞延訂單','面臨萬六保衛戰','加上油價位處高檔','反彈架構恐遭破壞','市場態度保守觀望','底部反彈格局確立','恐怕反彈即將結束','淪為外資調節目標','維持區間震盪格局','股價已經開始反應','觀察成交量能變化','賣超金額高達480.28','通膨壓力壓抑美股','通膨是經濟的麻煩','通膨疑慮重擊美股','不要隨便進場接刀子','具備一定的上漲空間','受美股影響陷入震盪','多單未平倉口數來到','恐持續回測前波低點','拜登痛批艾克森美孚','持續加速升息和縮表','推估國內升息機率高','準備向航運公司開刀','牽動著全球電子產品','跌幅也超過半根停板','通膨舒緩的期待破滅','造成今天台股的大跌','面臨高通膨利空籠罩','不願積極配合原油增產','加上我央行理監事會議','加權指數終場重挫389點','包括長期寬鬆貨幣政策','央行將召開理監事會議','摜破月線回測萬六支撐','研判季線上方賣壓仍大','通膨壓力超乎市場預期','金融類股賣壓同樣沉重','下修台灣今年經濟成長率','將通膨責任甩鍋給聯準會','攤開外資今天調節的標的','消費者物價指數高於預期','為一個月來單日最大跌點','超額總需求造成經濟過熱','是近三個月來單日最大賣超','通膨是否能夠慢慢獲得紓解','通膨降溫時程不如市場預期','預期在國內外兩大重要會議','受到聯準會政策不確定性影響','盤勢震盪提供更好的佈局機會','聯準會貨幣政策存在不確定性','觀察台股是否能拉出長下影線','驚人的通膨成為年底期中選舉','上任來不斷印鈔及推出刺激方案','就任後與沙烏地阿拉伯關係惡化','持續鎖定投信籌碼穩定的主力股','配合前面堤維西說到的台幣貶值','公布的美國五月通膨數據不如預期','導致市場對聯準會加速升息的預期','預期第三季台股仍將呈現區間震盪','推測六月開始業績就會有明顯的起色','預期釋出的升息態度將牽動全球股市','聯準會也即將在周四公布最新利率決策']
    testLoki(inputLIST, ['HIGH_RISK'])
    print("")

    # LOW_RISK
    print("[TEST] LOW_RISK")
    inputLIST = ['仍成長','共獲利','又大漲','將斥資','搶反彈','要獲利','一飛沖天','並未缺席','但觀察前','作帳行情','值得關注','再度回測','出現大漲','分批佈局','創新推出','努力獲利','受到影響','可以關注','可望回溫','合作布局','增加績效','多方掌控','多方支撐','展望後市','展望未來','才會缺貨','投入營運','持續佈局','持續實踐','持續成長','持續拓展','持續擴產','持續看好','操作首選','擴充需求','擴大獲利','改寫新高','更新速度','有助旗下','正式突破','洞察先機','浮現價值','營運船隊','獲利之後','獲利了結','獲得緩衝','產能吃緊','留意雙鴻','盤勢震盪','短線大漲','穩定成長','站上季線','站穩季線','經濟復甦','股價整理','航線營運','觀察元晶','貨量略減','輕鬆賺到','進入大量','邁向解封','還要漲價','都會缺貨','重大傷害','重新操作','長期關注','開始修正','開始轉好','關注合晶','需求提升','需求暢旺','仍維持暢旺','反映半導體','受惠半導體','可以多留意','在聚和大賺','增購金額為','增購金額達','增購額各達','將竣工交付','展望第三季','從獲利來看','成長爆發年','成長的來源','持續與政府','東南亞布局','營收與獲利','獲利有保障','第一季大賺','第一季獲利','維持正成長','製造業受惠','長榮航獲利','需求的擴張','佈局跑車來襲','保持成長態勢','元晶一樣大賺','具國際競爭力','創下近期新高','加速基礎建設','增添銷售表現','多方不想強攻','帶動金屬加工','拉回都是買點','持續影響全球','推升整體產能','推進越南布局','擴張趨勢明確','滿意度年成長','營收逐月遞增','營運概況調查','獲利就會很好','獲利還是看好','獲利雙飛創高','確保穩定供電','站穩今天高點','等待季線走平','等待打底完成','維持審慎樂觀','群聚效應浮現','股價直接回測','能拉出下影線','變成市場焦點','跟著美股下跌','透過積極調配','進入傳統淡季','重啟兩岸對話','開始投入長榮','面臨季線反壓','受惠半導體廠商','受惠半導體產業','受景氣波動影響','可望維持正成長','增添強勁新動能','外資開始撿便宜','大幅度回測整理','對股價就有保障','拉抬績效的行情','擴大產業生態圈','擴建廠房及產線','更好的佈局機會','月電價恐再調漲','極擴增資本支出','營收獲利大爆發','看好半導體產業','股價大幅度回測','設備增購為大宗','較去年同期成長','通過資本支出案','電動車銷量成長','不利經濟因素影響','亦受到評審團認可','偏多思考偏多操作','加速遞延訂單出貨','受到中國停工影響','強化長期競爭優勢','持續積極擴充產能','新唐浮現投資價值','新唐短線大賺將近','有利後續市場開拓','未來營運策略佈局','獲利都還是會很好','等待美國物價指數','透過上下游供應鏈','配合長期營運規劃','量縮震盪找佈局點','不要等到噴出才後悔','可望延續我國製造業','持續提升市場滲透率','決議通過取得不動產','浮現更高的投資價值','觀察正極材料美琪瑪','低檔佈局就是簡單獲利','停工問題衝擊股價下跌','受到中國疫情封控影響','因去年同期比較基期高','提高船體整體推進效率','擔憂通膨衝擊消費力道','擴大展示電子紙應用布局','增購金額均維持雙位數年增','透過電價平穩基金緩解中油','設計需求持續強勁的情況之下','帶動第二季及上半年營收同創歷史新高','高通膨問題與全球景氣趨向保守等因素影響']
    testLoki(inputLIST, ['LOW_RISK'])
    print("")


if __name__ == "__main__":
    # 測試所有意圖
    #testIntent()

    # 測試其它句子
    filterLIST = []
    splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"]
    #resultDICT = execLoki("今天天氣如何？後天氣象如何？", filterLIST)            # output => ["今天天氣"]
    #resultDICT = execLoki("今天天氣如何？後天氣象如何？", filterLIST, splitLIST) # output => ["今天天氣", "後天氣象"]
    #resultDICT = execLoki(["今天天氣如何？", "後天氣象如何？"], filterLIST)      # output => ["今天天氣", "後天氣象"]
    #inputLIST = ["油價修正"]
    #inputLIST  = ['台股盤後美股昨日震盪收漲費半反彈']
    inputLIST  = ["股價整理", "觸底反彈"]
    
    #print("Result ==> {}".format(resultDICT))
    #resultDICT = execLoki(inputLIST, filterLIST)
    
    testLIST = []
    for sentence in inputLIST:
        resultDICT = execLoki(sentence, filterLIST)
        testLIST.append(resultDICT["risk_value"]) 
    print(testLIST)