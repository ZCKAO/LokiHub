#!/user/bin/env python
# -*- coding: utf-8 -*-

import logging
import discord
import json
import re
import requests
from datetime import datetime
from pprint import pprint
from bs4 import BeautifulSoup
from Fin_risk import runLoki

logging.basicConfig(level=logging.DEBUG)


with open("account.info", encoding="utf-8") as f: #讀取account.info
    accountDICT = json.loads(f.read())

punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
def getLokiResult(inputSTR):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    logging.debug("Loki Result => {}".format(resultDICT))
    return resultDICT

def crawler(urlSTR):
    response = requests.get(urlSTR)
    soup = BeautifulSoup(response.text, 'html.parser')
    content_get = soup.select('._2E8y')
    
    content =[]
    for i in content_get:
        content.append(i.text.strip())
    return content

def clean(content):
    s = content
    s = re.sub(r'\n','',s)
    s = re.sub(r'&lt;','',s)
    s = re.sub(r'p&gt;','',s)
    s = re.sub(r'&amp;','',s)
    s = re.sub(r'nbsp;','',s)
    s = re.sub(r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|'
        r'www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|'
        r'https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})'
      ,'',s)
    clean_textSTR = re.sub(r'(【[\u4e00-\u9fa5]】)','',s)
    return clean_textSTR

def parse(clean_textSTR):
    contentLIST = []
    content_no = re.sub(r'[^\w\s]','',clean_textSTR)
    contentLIST_tmp = content_no.split(" ")
    for i in contentLIST_tmp:
        jj = re.sub(r'[0-9]','',i)
        if jj == '':
            pass
        elif len(jj) < 2:
            pass
        else:
            contentLIST.append(jj)
    return contentLIST

def get_parse_content(url):
    text = crawler(url)
    content_clean = clean(text[0])
    content_parse = parse(content_clean)
    return content_parse

class BotClient(discord.Client):
        
    def resetMSCwith(self, messageAuthorID):
        '''
        清空與 messageAuthorID 之間的對話記錄
        '''
        templateDICT = self.templateDICT
        templateDICT["updatetime"] = datetime.now()
        return templateDICT

    async def on_ready(self):
        print('Logged on as {} with id {}'.format(self.user, self.user.id))
        # ################### Multi-Session Conversation :設定多輪對話資訊 ###################
        self.templateDICT = {"updatetime" : None,
                             "latestQuest": ""
        }
        self.mscDICT = { #userid:templateDICT
        }
        # ####################################################################################
        

    async def on_message(self, message):
        # Don't respond to bot itself. Or it would create a non-stop loop.
        # 如果訊息來自 bot 自己，就不要處理，直接回覆 None。不然會 Bot 會自問自答個不停。
        if message.author == self.user:
            return None
        elif message.content.lower().replace(" ", "") in ("bot點名"):
            await message.reply("有！")

        logging.debug("收到來自 {} 的訊息".format(message.author))
        logging.debug("訊息內容是 {}。".format(message.content))
        replySTR = "蛤？？你在說啥？？"#"我是預設的回應字串…你會看到我這串字，肯定是出了什麼錯！"
        print(self.user.mentioned_in(message))
        if self.user.mentioned_in(message):
            
            logging.debug("本 bot 被叫到了！")
            msgSTR = message.content.replace("<@{}> ".format(self.user.id), "").strip()
            logging.debug("人類說：{}".format(msgSTR))
            if msgSTR == "ping":
                await message.reply('pong')
            elif msgSTR == "ping ping":
                await message.reply('pong pong')
            elif msgSTR in ["哈囉","嗨","你好","您好","hi","hello"]:
                replySTR = ("{}！我是風險計算機器人，歡迎給我'鉅亨網'的新聞網址，我可以計算出相對風險喔！".format(msgSTR))

# ##########初次對話：這裡是 keyword trigger 的。
            #elif msgSTR.lower() in ["哈囉","嗨","你好","您好","hi","hello"]:
                ##有講過話(判斷對話時間差)
                #if message.author.id in self.mscDICT.keys():
                    #timeDIFF = datetime.now() - self.mscDICT[message.author.id]["updatetime"]
                    ##有講過話，但與上次差超過 5 分鐘(視為沒有講過話，刷新template)
                    #if timeDIFF.total_seconds() >= 300:
                        #self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                        #replySTR = "嗨嗨，我們好像見過面，但卓騰的隱私政策不允許我記得你的資料，抱歉！"
                    ##有講過話，而且還沒超過5分鐘就又跟我 hello (就繼續上次的對話)
                    #else:
                        #replySTR = self.mscDICT[message.author.id]["latestQuest"]
                ##沒有講過話(給他一個新的template)
                #else:
                    #self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                    #replySTR = msgSTR.title()
            elif msgSTR.startswith("http"):
                urlSTR = msgSTR #開始處理正式對話
                #從這裡開始接上 NLU 模型
                
                contentLIST = get_parse_content(urlSTR)
                
                risk_valueLIST_tmp = []
                filterLIST = []
                for i in range(0, len(contentLIST), 20):
                    resultDICT = runLoki(contentLIST[i:i+20], filterLIST) 
                    risk_valueLIST_tmp.append(resultDICT["risk_value"])         ##EX 回傳[[3.33], [], [], [], [], [], [], [], [], [], []]
                
                computeLIST = []
                for x in risk_valueLIST_tmp:
                    if x == []:
                        pass
                    else:
                        x_int = x[0]
                        computeLIST.append(x_int)                        
                
                replySTR = sum(computeLIST)/len(computeLIST)                
                
            else:        ##判斷如果是輸入一句話的
                resultDICT = getLokiResult(msgSTR)
                
                logging.debug("######\nLoki 處理結果如下：")
                logging.debug(resultDICT)
                if "risk_value" in resultDICT.keys() and resultDICT["risk_value"] != []:
                    responseLIST = [int(i) for i in resultDICT["risk_value"]]                
                
                    replySTR = "判斷結果為風險值為{}".format(sum(responseLIST))
                    
                responseLIST = [replySTR]    
                #if "蛤？？你在說啥？？" in responseLIST:
                    #replySTR = responseLIST[0]
            
            
# ##########非初次對話：這裡用 Loki 計算語意
         
                    
           
  
            await message.reply(replySTR)


if __name__ == "__main__":
    client = BotClient(intents=discord.Intents.default())
    client.run(accountDICT["discord_token"])