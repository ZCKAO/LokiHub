#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for LOW_RISK

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

DEBUG_LOW_RISK = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"fin_noun":["除息","S&P500","S&P 500","聯準會","多頭","美股","個股","金控","毛利","季線","類股","航運","後市","生技股","內資","年增率","指數","賣點","成交量","營收","行情","加權指數","物價指數","空點","三大法人","下影線","台股","電子權值","暴利稅","金融類股","主力股","毛利率","費半","空頭","未平倉口數",""],"fin_verb":["利空","出盡","落底","升息","墊高","上沖下洗","可望","除息","轉弱","落短底","多殺多","軋空","上看","跌停","逼出","下滑"],"capital_name":["台積電","中鋼","元晶","聚和","長榮航","中油","美琪瑪","兆豐產險","艾克森美孚"],"general_noun":["製造商","原料","壽險業","行情","製鞋類股","上膛","俄烏戰爭","半導體","前景","中期","期貨","選擇權","基礎建設","半導體產業","電動車","評審團","供應鏈"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_LOW_RISK:
        print("[LOW_RISK] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[不利][經濟][因素]影響":
        resultDICT["risk_value"].append(6.2094)
        

    if utterance == "[亦]受到[評審團]認可":
        resultDICT["risk_value"].append(7.0792)


    if utterance == "[低檔]佈局就是[簡單]獲利":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[偏多]思考[偏多]操作":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[元晶][一樣]大賺":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[共]獲利":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[具][國際]競爭力":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "[再度]回測":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[創新]推出":
        resultDICT["risk_value"].append(7.0792)


    if utterance == "[可以]多留意":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[可以]關注":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[增購額]各達":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[外資]開始撿便宜":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[多方]不想強攻":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[大幅度]回測整理":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[將]斥資":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[將]竣工交付":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[強化][長期]競爭[優勢]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[才][會]缺貨":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[新唐][短線]大賺[將][近]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[新唐]浮現投資[價值]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[更好]的佈局[機會]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[月電價]恐再調漲":
        resultDICT["risk_value"].append(7.0792)


    if utterance == "[有利][後續][市場]開拓":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "[未來]營運[策略]佈局":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[東南亞]布局":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[極]擴增[資本]支出":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[正式]突破":
        resultDICT["risk_value"].append(7.0792)


    if utterance == "[滿意度][年]成長":
        resultDICT["risk_value"].append(7.0792)


    if utterance == "[營收]獲利[大]爆發":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[營收]與獲利":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[營收]逐月遞增":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "[盤勢]震盪":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[短線]大漲":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[穩定]成長":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "[經濟]復甦":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "[股價][大幅度]回測":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[股價][直接]回測":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[股價]整理":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[能]拉出[下影線]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[航線]營運":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[製造業]受惠":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[設備]增購為[大宗]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[貨量]略減":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "[輕鬆]賺到":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[都][會]缺貨":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[重大]傷害":
        resultDICT["risk_value"].append(7.0792)


    if utterance == "[重新]操作":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[長期]關注":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[長榮航]獲利":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[電動車][銷量]成長":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "[需求]提升":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "[需求]的擴張":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "一飛沖天":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "不要等到噴出[才][後]悔":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "並未缺席":
        resultDICT["risk_value"].append(7.0792)


    if utterance == "仍成長":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "仍維持暢[旺]":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "但觀察[前]":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "佈局跑車來襲":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "作帳[行情]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "保持成長[態勢]":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "值得關注":
        resultDICT["risk_value"].append(7.0792)


    if utterance == "停工[問題]衝擊[股價]下跌":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "出現大漲":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "分批佈局":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "創下[近期][新高]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "加速[基礎建設]":
        resultDICT["risk_value"].append(7.0792)


    if utterance == "加速遞延[訂單]出貨":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "努力獲利":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "又大漲":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "反映[半導體]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "受[景氣]波動影響":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "受到[中國]停工影響":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "受到中國疫情封控影響":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "受到影響":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "受惠[半導體]":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "受惠[半導體][廠商]":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "可望回溫":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "可望延續[我]國製造業":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "可望維持[正]成長":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "合作布局":
        resultDICT["risk_value"].append(7.0792)


    if utterance == "因[去年]同期比較基[期]高":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "在[聚和]大賺":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "增加[績效]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "增添[強勁][新動能]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "增添銷售表現":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "增購[金額][均]維持[雙位][數年]增":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "增購[金額]為":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "增購[金額]達":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "多方掌控":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "多方支撐":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "對[股價]就有保障":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "展望[後市]":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "展望[未來]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "展望第[三季]":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "帶動[金屬]加工":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "帶動第[二季]及[上][半年][營收]同創[歷史][新高]":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "從獲利來看":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "成長爆發[年]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "成長的[來源]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "投入營運":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "拉回[都]是買[點]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "拉抬[績效]的[行情]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "持續[提升市場][滲透率]":
        resultDICT["risk_value"].append(7.0792)


    if utterance == "持續[積極]擴充產[能]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "持續佈局":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "持續實踐":
        resultDICT["risk_value"].append(7.0792)


    if utterance == "持續影響[全球]":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "持續成長":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "持續拓展":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "持續擴產":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "持續看好":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "持續與[政府]":
        resultDICT["risk_value"].append(7.0792)


    if utterance == "推升整體產[能]":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "推進[越南]布局":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "提高[船體][整體]推進[效率]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "搶反彈":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "操作[首]選":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "擔憂通膨衝擊消費[力道]":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "擴充需求":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "擴大展示[電子紙]應用布局":
        resultDICT["risk_value"].append(7.0792)


    if utterance == "擴大獲利":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "擴大產業生態圈":
        resultDICT["risk_value"].append(7.0792)


    if utterance == "擴建[廠房]及[產線]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "擴張[趨勢][明確]":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "改寫[新高]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "更新[速度]":
        resultDICT["risk_value"].append(7.0792)


    if utterance == "有助[旗下]":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "決議通過取得[不動產]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "洞察[先機]":
        resultDICT["risk_value"].append(7.0792)


    if utterance == "浮現[價值]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "浮現[更高]的投資[價值]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "營運[船隊]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "營運概況調查":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "獲利[之後]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "獲利[都]還是[會][很好]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "獲利[雙]飛創高":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "獲利了結":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "獲利就[會]很好":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "獲利有保障":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "獲利還是看好":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "獲得緩衝":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "產[能]吃緊":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "留意[雙鴻]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "看好[半導體產業]":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "確保[穩定]供電":
        resultDICT["risk_value"].append(7.0792)


    if utterance == "站[上][季線]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "站穩[今天][高點]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "站穩[季線]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "第[一季]大賺":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "第[一季]獲利":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "等待[季線]走平":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "等待[美國][物價指數]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "等待打底完成":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "維持[審慎][樂觀]":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "維持[正]成長":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "群聚[效應]浮現":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "要獲利":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "觀察[元晶]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "觀察[正極][材料][美琪瑪]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "設計[需求]持續[強勁]的[情況]之[下]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "變成[市場焦點]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "跟著[美股]下跌":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "較[去年][同期]成長":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "透過[上][下]游[供應鏈]":
        resultDICT["risk_value"].append(7.0792)


    if utterance == "透過[積極]調配":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "透過[電價][平穩][基金]緩解[中油]":
        resultDICT["risk_value"].append(7.0792)


    if utterance == "通過[資本]支出[案]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "進入[傳統][淡季]":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "進入[大量]":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "邁向解封":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "還要漲價":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "配合[長期]營運規劃":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "重啟[兩岸對話]":
        resultDICT["risk_value"].append(7.0792)


    if utterance == "量縮震盪找佈局[點]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "開始修正":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "開始投入[長榮]":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "開始轉好":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "關注合晶":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "需求暢[旺]":
        resultDICT["risk_value"].append(6.2094)


    if utterance == "面臨[季線]反壓":
        resultDICT["risk_value"].append(6.3626)


    if utterance == "高通膨[問題]與[全球][景氣]趨向[保守]等[因素]影響":
        resultDICT["risk_value"].append(6.2094)
 

    return resultDICT