#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for HIGH_RISK

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

import json
import os

DEBUG_HIGH_RISK = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"fin_noun":["除息","S&P500","S&P 500","聯準會","多頭","美股","個股","金控","毛利","季線","類股","航運","後市","生技股","內資","年增率","指數","賣點","成交量","營收","行情","加權指數","物價指數","空點","三大法人","下影線","台股","電子權值","暴利稅","金融類股","主力股","毛利率","費半","空頭","未平倉口數",""],"fin_verb":["利空","出盡","落底","升息","墊高","上沖下洗","可望","除息","轉弱","落短底","多殺多","軋空","上看","跌停","逼出","下滑"],"capital_name":["台積電","中鋼","元晶","聚和","長榮航","中油","美琪瑪","兆豐產險","艾克森美孚"],"general_noun":["製造商","原料","壽險業","行情","製鞋類股","上膛","俄烏戰爭","半導體","前景","中期","期貨","選擇權","基礎建設","半導體產業","電動車","評審團","供應鏈"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_HIGH_RISK:
        print("[HIGH_RISK] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[一度]大跌":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[今天]開低走[低]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[低檔]佈局":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[供需]失衡":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[信心]潰散":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[全][數]走跌":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[全面]走弱下":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[全面]走跌":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[前][十][大]賣超":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[加權指數][終場]重挫[389][點]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[原先]估計的衰退":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[台幣]貶值":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[台股]開低走[低]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[同樣]創下":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[報復性]消費":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[外資][今日]大減":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[外資]回頭加碼":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[多單]未平倉口數來到":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[多方]支撐":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[大]跌逾[半根]停板":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[大幅度]回測整理":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[大陸]復甦的[時刻]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[央行][將]召開[理監事][會議]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[富邦][下]挫":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[將]通膨[責任]甩鍋給[聯準會]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[將]通膨甩鍋":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[市場態度][保守]觀望":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[底部]反彈[格局]確立":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[庫存]高達":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[彰銀]下跌超過":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[成外資]提款機":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[才][會]缺貨":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[拜登]痛批[艾克森美孚]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[毛利率]站回":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[消費者][物價指數]高於預期":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[無情]大砍":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[營收]開始轉好":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[物價]上升":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[狂]飆創高":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[疫情]衝擊":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[盤勢][偏弱]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[盤勢]壓回":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[盤勢]震盪提供[更好]的佈局[機會]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[直接]回測":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[短線]探底":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[空方]狙擊":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[終場]下跌":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[經濟對策]來解決":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[繼續]重挫":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[美股]出現賣壓":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[聯準會][也][即將]在[周四]公布[最新][利率決策]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[聯準會][貨幣][政策]存在不[確定性]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[聯準會][鷹派]緊縮":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[聯發科]重挫[4.6%]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[股價][也]下跌":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[股價][相對]有撐":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[股價]已經開始反應":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[股價]整理":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[自營商]終止[連續]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[觸底]反彈":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[費半]更重挫":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[資本]支出":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[跌幅][也]超過[半根]停板":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[都][會]缺貨":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[金融類股]賣壓[同樣][沉重]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[雙雙][年]衰退":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "[驚人]的通膨成為[年底][期中]選舉":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "上任來[不斷]印鈔及推出刺激[方案]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "下修[台灣][今年][經濟][成長率]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "下挫超過":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "不當的[財政]擴張":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "不要[隨便]進場接[刀子]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "不願[積極]配合[原油]增產":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "且若回補":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "佈局跑車":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "低接[筆電族群]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "供給跟不[上][需求]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "公布的[美國][五月]通膨[數據]不如預期":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "具備[一定]的上漲[空間]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "出現[趨緩疑慮]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "出現供大於求":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "創下[近][十年][新低]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "加上[台幣]走貶":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "加上[我]央行[理監事][會議]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "加上[油價]位處[高檔]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "包括[長期][寬鬆][貨幣][政策]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "反彈[架構]恐遭破壞":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "反彈結束":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "反映解封題材":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "受[大陸]影響":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "受[美股]大跌影響":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "受[美股]影響陷入震盪":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "受到[聯準會][政策]不[確定性]影響":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "各被賣逾":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "合計提款逾":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "合計賣超":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "同步大跌":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "同步跳水":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "吸引[買盤]進駐":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "呈現震盪走勢":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "噴出[才][後]悔":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "回歸空頭[走勢]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "回測[萬六]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "回測[萬六]支撐":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "因應[外資]賣壓":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "多留意":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "大砍[聯電]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "威脅課徵[暴利稅]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "守住[前][次]低點":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "守住[萬六][關卡]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "封城[政策]解除":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "導致市場對聯準會加速升息的預期":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "小跌作收":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "尚未反映的[股票]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "就任[後]與[沙烏地阿拉伯][關係]惡化":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "已經反應":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "已高達":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "帶來影響":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "干擾[部分]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "引爆[報復性][需求]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "影響[大盤]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "從[全球]通膨來看":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "恐怕[美國]通膨":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "恐怕反彈[即將]結束":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "恐持續回測[前]波低點":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "成長停頓":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "扭轉第[一季]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "把握最後買[點]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "投信調節[對象]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "投信賣超":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "拉抬[績效]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "拖累[台股]回跌":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "持續佈局":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "持續加速升息和縮表":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "持續攀升":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "持續鎖定投信[籌碼][穩定]的[主力股]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "掌握[主力股]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "推估[國內]升息[機率]高":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "推升[美國]通膨":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "推測[六月]開始[業績]就[會]有[明顯]的[起色]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "提[前]反映":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "提款[台股]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "摜破月線回測[萬六]支撐":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "擔心升息[三碼]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "擴大到衰退":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "攤開[外資][今天]調節的[標的]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "收[黑]拖累":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "收盤[下]挫":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "收盤下跌":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "攻上漲停":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "是[近][三個月]來[單日][最大]賣超":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "最低下探":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "止跌反彈":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "淪為[外資]調節[目標]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "準備向[航運][公司]開刀":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "準備復甦":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "為[一個月]來[單日]最大跌[點]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "爆發[俄烏戰爭]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "牽動著[全球][電子][產品]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "獲利影響":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "獲得緩衝[時間]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "用[政治]來處理":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "留意[雙鴻]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "發動[戰爭]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "監管[航運][公司]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "研判[季線][上方]賣壓仍[大]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "確定升息[二碼]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "維持區間震盪格局":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "緊盯[聯準會][升息]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "衝擊[拜登][總統]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "衝擊本周台股":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "衰退的[可能]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "觀察[台股]是否[能]拉出長[下影線]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "觀察[成交量][能]變化":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "觀察[美股]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "觀察到[營收][好]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "解封帶來的[需求]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "解封的[刺激]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "調漲報價":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "調節[電子權值]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "賣壓[都][相當][沉重]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "賣壓同步湧現":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "賣超[張數]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "賣超[金額]高達[480.28]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "超額[總需求]造成[經濟][過熱]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "跌幅[一度]擴大":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "跌幅[也都]超過":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "跌幅持續擴大":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "跌幅超過":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "跌破[萬六]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "跟著跳水":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "跟隨[美股]下跌":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "跳空跌破[月線]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "較[去年][同期]大增":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "轉為賣超":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "通膨[壓力][超]乎市場預期":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "通膨[壓力]壓抑[美股]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "通膨[疑慮]重擊[美股]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "通膨上升":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "通膨仍有[變數]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "通膨保值[債券]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "通膨元[兇]是[普丁]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "通膨居高不下":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "通膨惡化":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "通膨是[經濟]的[麻煩]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "通膨是否[能夠][慢慢]獲得紓解":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "通膨更加惡化":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "通膨未見降溫":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "通膨舒緩的期待破滅":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "通膨降溫[時程]不如[市場]預期":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "造成[今天][台股]的大跌":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "進場佈局":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "進場低接[台積電]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "進場低接買超":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "達到分散[風險]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "遭遇[黑色][星期一]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "避免[跌幅]擴大":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "配合[前面][堤維西]說到的[台幣]貶值":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "配合[台幣]貶值":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "重回[軌道]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "鎖定遭[外資]調節":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "開始有遞延[訂單]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "陷入[五][窮][六][絕]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "陷入修正":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "需求大增":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "震盪下修":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "面臨[萬六]保衛[戰]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "面臨高通膨[利空]籠罩":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "預期在[國內外][兩][大][重要][會議]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "預期第[三季]台股仍[將]呈現區間震盪":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "預期釋出的[升息][態度][將]牽動[全球][股市]":
        resultDICT["risk_value"].append(22.5946)

    if utterance == "高於預期":
        resultDICT["risk_value"].append(22.5946)

    return resultDICT