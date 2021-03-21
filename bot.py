# -*- coding: utf-8 -*-
#無名LINEBOT檔 賴426426wmsszw 改檔將會錯誤 請小心使用
from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,timeit,atexit
from gtts import gTTS
from googletrans import Translator
botStart = time.time()
cl=LINE("tesutorei631@gmail.com","asd123123")
cl.log("Auth Token : " + str(cl.authToken))
profile = cl.getProfile()
status = str(profile.statusMessage)
lock = _name = " 邪月LINE BOT\n\n     \n\n 機器製作者Line ID:kaixuan666 \n\n邪月機器\n\n👿👿👿👿👿\n\n❤️❤️❤️\n\n🧡���\邪月機器\n👿👿👿👿👿���\n\n❤️❤️❤️\n\n🧡������邪月機器\n\nMade in Taiwan\n\nmake from 邪月\n\n👿👿👿👿👿���\n\n  "
if lock not in status:
    profile.statusMessage = lock + status
    cl.updateProfile(profile)
else:
    pass
oepoll = OEPoll(cl)
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
lineSettings = cl.getSettings()
clProfile = cl.getProfile()
clMID = cl.profile.mid
myProfile["displayName"] = clProfile.displayName
myProfile["statusMessage"] = clProfile.statusMessage
myProfile["pictureStatus"] = clProfile.pictureStatus
admin=['u8d9993b49b5c199a8657f2fd2b02902a','u403f1261e06558bfaad641843302a66b','u9c0b65006e756c237622c54ad2d7f48f',clMID]
msg_dict = {}
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
}
setTime = {}
setTime = wait2['setTime']
bl = [""]
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def restartBot():
    print ("[ 訊息 ] 機器重啟")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False    
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def logError(text):
    cl.log("[ 錯誤 ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def updateProfilePicture(self, path, type='p'):
        files = {'file': open(path, 'rb')}
        params = {'oid': self.profile.mid,'type': 'image'}
        if text.lower() == 'vp':
            params.update({'ver': '2.0', 'cat': 'vp.mp4'})
        data = {'params': self.genOBSParams(params)}
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/p/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Update profile picture failure.')
        return True
def updateProfileVideoPicture(self, path):
        try:
            from ffmpy import FFmpeg
            files = {'file': open(path, 'rb')}
            data = {'params': self.genOBSParams({'oid': self.profile.mid,'ver': '2.0','type': 'video','cat': 'vp.mp4'})}
            r_vp = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/vp/upload.nhn', data=data, files=files)
            if r_vp.status_code != 201:
                raise Exception('Update profile video picture failure.')
            path_p = self.genTempFile('path')
            ff = FFmpeg(inputs={'%s' % path: None}, outputs={'%s' % path_p: ['-ss', '00:00:2', '-vframes', '1']})
            ff.run()
            self.updateProfilePicture(path_p, 'vp')
        except:
            raise Exception('You should install FFmpeg and ffmpy from pypi')
def  helpmessage():
    helpMessage = """❤️指令表-Instruction list❤️
🏹邪月半垢機器指令表，作者:邪月👻
👻👻👻👻👻蘿莉我的👻👻👻👻👻
🦄「H」 所有指令🧡
🏹「Rebot 」重新啟動🧡
🐽「Save」 儲存设定🧡
🐷「Runtime」 運作时间🧡
😋「Sp」 速度🧡
😪「Speed 」速度🧡
🤔「Set 」設定🧡
😁「About 」關於本帳🧡
🥰「bye」機器退出群组🧡
❤️設定-setting❤️
🧡「Add On/Off」自动加入🧡
🧡「Join On/Off」 自动加入群组🧡
🧡「Leave On/Off 」自动离开副本🧡
🧡「Read On/Off」 自动已读🧡
🧡「Mention On/Off」 标注回覆🧡
🧡「Reread On/Off」 查询收回🧡
🧡「Qr On/Off」 群组网址保护🧡
🧡「QrProtect On/Off」 網址保護🧡
🧡「Groupprotect On/Off」 踢人保護🧡
🧡「Invprotect On/Off」 邀請保護🧡
🧡「Ptt On/Off」 自动进退🧡
🧡「Sj On/Off」 进群通知🧡
🧡「Sl On/Off」 退群通知🧡
🧡「Tl On/Off」 文章🧡
🧡「Contact」 On/Off 🧡
❤資訊-Information❤️
🧡「Me」 我的连结🧡
🧡「MyMid」 我的Mid🧡
🧡「MyName」 我的名字🧡
🧡「MyBio」 我的个签🧡
🧡「MyPicture」 我的头贴🧡
🧡「MyCover」 我的封面🧡
🧡「Contact @」 标注取得连结🧡
🧡「Mid @」标注查看Mid🧡
🧡「Name @」 标注查看名字🧡
🧡「Bio @」查看个签🧡
🧡「Picture @」查看头贴🧡
🧡「Cover @」查看封面🧡
❤黑單-Black list️❤️
🧡「Ban @」 加入黑单🧡
🧡「Unban @」 取消黑单🧡
🧡「Banlist」 查看黑单🧡
🧡「Clear Ban」 清空所有黑单🧡
🧡「Killbanall」 针对全部群踢出黑单🧡
❤️群组-Group❤️
🧡「Gowner」創群者🧡
🧡「Gb」 查看群组成員🧡
🧡「Qurl/Curl」 群组网址開關🧡
🧡「Ginfo」 查看群组狀態🧡
🧡「Tagall」 標注所有成員🧡
🧡「Gn 文字」 更改群名🧡
🧡「Vk @」 標注踢出並清除資料🧡
🧡「Tk @」 多踢🧡
🧡「Mk @」單踢🧡
🧡「Zk」踢出0字元🧡
🧡「Kick」 翻群🧡
🧡「Inv (mid）」 透過mid邀请🧡
🧡「Inv @」 標注多邀🧡
🧡「Cancel」 取消所有邀请🧡
🧡「Ri @」 來回機票🧡
❤️其他-other❤️
🧡「Sr/Dr」 已讀設置 開關🧡
🧡「Lr」查看已讀🧡
🧡「op@」 權限加入🧡
🧡「deop@」 取消權限🧡
🧡「Say 數字」 重覆發話🧡
🧡「Tag @」 次數🧡
🧡「call:數字」 群組通話邀请🧡
🧡「rall:數字」 副本群通邀请🧡
"""
    return helpMessage
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            contact = cl.getContact(op.param1)
            print ("[ 5 ] 通知添加好友 名字: " + contact.displayName)
            if settings["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                cl.sendMessage(op.param1, "感謝您加我為好友".format(str(contact.displayName)))
        if op.type == 11:
            group = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            if settings["qrprotect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    gs = cl.getGroup(op.param1)
                    gs.preventJoinByTicket = True
                    cl.updateGroup(gs)
                    invsend = 0
                    cl.sendMessage(op.param1,cl.getContact(op.param2).displayName + "網址保護中...不要動群組網址！")
                    cl.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 13:
            contact1 = cl.getContact(op.param2)
            contact2 = cl.getContact(op.param3)
            group = cl.getGroup(op.param1)
            if settings["inviteprotect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1,[op.param3])
                    time.sleep(0.15)
                    cl.kickoutFromGroup(op.param1,[op.param3])
                    time.sleep(0.15)
                    cl.kickoutFromGroup(op.param1,[op.param2])
            if clMID in op.param3:
                if settings["autoJoin"] == True:
                    try:
                        arrData = ""
                        text = "%s "%('[嗷嗚，邪月入群囉]')
                        arr = []
                        mention = "@x "
                        slen = str(len(text))
                        elen = str(len(text) + len(mention) - 1)
                        arrData = {'S':slen, 'E':elen, 'M':op.param2}
                        arr.append(arrData)
                        text += mention + "招待使用\n半垢運行中..."
                        cl.acceptGroupInvitation(op.param1)
                        cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        cl.sendMessage(op.param1, "我的作者：")
                        cl.sendContact(op.param1, "u403f1261e06558bfaad641843302a66b")
                    except Exception as error:
                        print(error)
            if clMID in op.param3:
                if settings["autoPtt"] == True:
                    cl.acceptGroupInvitation(op.param1)
                    cl.sendMessage(op.param1, "自動並退運行中...")
                    cl.leaveGroup(op.param1)
        if op.type == 15:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            if settings["seeLeave"] == True:
                try:
                    arrData = ""
                    text = "%s "%('[警告]')
                    arr = []
                    mention = "@x "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + "退出出去了   {} ！".format(str(group.name))
                    cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                except Exception as error:
                    print(error)
        if op.type == 17:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            if settings["seeJoin"] == True:
                try:
                    arrData = ""
                    text = "%s "%('♥️歡迎新人♥️')
                    arr = []
                    mention = "@x "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + "加入 {} ！".format(str(group.name))
                    cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                except Exception as error:
                    print(error)
        if op.type == 19:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            contact2 = cl.getContact(op.param3)
            print ("[19]有人把人踢出群組 群組名稱: " + str(group.name) + "\n" + op.param1 +"\n踢人者: " + contact1.displayName + "\nMid:" + contact1.mid + "\n被踢者: " + contact2.displayName + "\nMid:" + contact2.mid )
            if settings["protect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    if settings["kickContact"] == True:
                        try:
                            arrData = ""
                            text = "%s " %('[警告]')
                            arr = []
                            mention1 = "@arasi "
                            slen = str(len(text))
                            elen = str(len(text) + len(mention1) - 1)
                            arrData = {'S':slen, 'E':elen, 'M':op.param2}
                            arr.append(arrData)
                            text += mention1 + '踢了 '
                            mention2 = "@kick "
                            sslen = str(len(text))
                            eelen = str(len(text) + len(mention2) - 1)
                            arrdata = {'S':sslen, 'E':eelen, 'M':op.param3}
                            arr.append(arrdata)
                            text += mention2
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            settings["blacklist"][op.param2] = True
                            time.sleep(0.1)
                            cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        except Exception as error:
                            print(error)
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        settings["blacklist"][op.param2] = True
                        time.sleep(0.1)
            else:
                if settings["kickContact"] == True:
                    try:
                        arrData = ""
                        text = "%s " %('[警告]')
                        arr = []
                        mention1 = "@arasi "
                        slen = str(len(text))
                        elen = str(len(text) + len(mention1) - 1)
                        arrData = {'S':slen, 'E':elen, 'M':op.param2}
                        arr.append(arrData)
                        text += mention1 + '踢了 '
                        mention2 = "@kick "
                        sslen = str(len(text))
                        eelen = str(len(text) + len(mention2) - 1)
                        arrdata = {'S':sslen, 'E':eelen, 'M':op.param3}
                        arr.append(arrdata)
                        text += mention2
                        cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                    except Exception as error:
                        print(error)
                        if op.param2 in ban["admin"] or op.param2 in ban["bots"] or op.param2 in ban["owners"]:
                            pass
                        if op.param1 in settings["protect"]:
                            ban["blacklist"][op.param2] = True
                            cl.kickoutFromGroup(op.param1,[op.param2])
                        if op.param3 in ban["owners"]:
                            cl.inviteIntoGroup(op.param1,[op.param3])
        if op.type == 22:
            print ("[ 22 ] 通知離開副本")
            if settings["autoLeave"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 1:
            print ("[1]更新配置文件")
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 7:
               if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    path = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/ANDROID/sticker.png;compress=true".format(stk_id)
                    ret_ = "[ 貼圖資料 ]"
                    ret_ += "\n貼圖ID : {}".format(stk_id)
                    ret_ += "\n貼圖包ID : {}".format(pkg_id)
                    ret_ += "\n貼圖網址 : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n貼圖圖片網址：https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/ANDROID/sticker.png;compress=true".format(stk_id)
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
            if msg.contentType == 13:
                if settings["contact"] == True:
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendMessage(msg.to,"[名稱]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[個簽]:\n" + contact.statusMessage + "\n[頭貼網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendMessage(msg.to,"[名稱]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[個簽]:\n" + contact.statusMessage + "\n[頭貼網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu))
            elif msg.contentType == 16:
                if settings["timeline"] == True:
                    if msg.contentMetadata["serviceType"] == 'MH':
                        msg.contentType = 0
                        f_mid = msg.contentMetadata["postEndUrl"].split("userMid=")
                        s_mid = f_mid[1].split("&")
                        mid = s_mid[0]
                        if 'stickerId' not in msg.contentMetadata:
                            if 'mediaOid' in msg.contentMetadata:
                                if 'mediaCount' not in msg.contentMetadata:
                                    list_ = msg.contentMetadata['mediaOid'].split("oid=")
                                    object = list_[1]
                                    try:
                                        arrData = ""
                                        text = "%s\n%s\n"%("---[分享文章預覽]---","[文章作成者]:")
                                        arr = []
                                        mention = "@sheng "
                                        slen = str(len(text))
                                        elen = str(len(text) + len(mention) - 1)
                                        arrData = {'S':slen, 'E':elen, 'M':mid}
                                        arr.append(arrData)
                                        text += mention + "\n[文字預覽]:\n" + msg.contentMetadata["text"] + "\n(僅顯示100字)" + "\n[媒體資訊]:\nhttp://profile.line-cdn.net/r/myhome/h/" + object + "\n數量 : 1" + "\n[文章網址]:\n" + msg.contentMetadata["postEndUrl"]
                                        cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                                    except Exception as error:
                                        print(error)
                                else:
                                    list_ = msg.contentMetadata['mediaOid'].split("oid=")
                                    object = list_[1]
                                    num = int(msg.contentMetadata["mediaCount"])
                                    numb = num + 1
                                    number = str(numb)
                                    try:
                                        arrData = ""
                                        text = "%s\n%s\n"%("---[分享文章預覽]---","[文章作成者]:")
                                        arr = []
                                        mention = "@sheng "
                                        slen = str(len(text))
                                        elen = str(len(text) + len(mention) - 1)
                                        arrData = {'S':slen, 'E':elen, 'M':mid}
                                        arr.append(arrData) 
                                        text += mention + "\n[文字預覽]:\n" + msg.contentMetadata["text"] + "\n(僅顯示100字)" + "\n[媒體資訊]:\nhttp://profile.line-cdn.net/r/myhome/h/" + object + "\n數量 : " + number + "\n[文章網址]:\n" + msg.contentMetadata["postEndUrl"]
                                        cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                                    except Exception as error:
                                        print(error)
                            else:
                                try:
                                    arrData = ""
                                    text = "%s\n%s\n"%("---[分享文章預覽]---","[文章作成者]:")
                                    arr = []
                                    mention = "@sheng "
                                    slen = str(len(text))
                                    elen = str(len(text) + len(mention) - 1)
                                    arrData = {'S':slen, 'E':elen, 'M':mid}
                                    arr.append(arrData)
                                    text += mention + "\n[文字預覽]:\n" + msg.contentMetadata["text"] + "\n(僅顯示100字)" + "\n[文章網址]:\n" + msg.contentMetadata["postEndUrl"]
                                    cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                                except Exception as error:
                                    print(error)
                        else:
                            if 'mediaOid' not in msg.contentMetadata:
                                try:
                                    arrData = ""
                                    text = "%s\n%s\n"%("---[分享文章預覽]---","[文章作成者]:")
                                    arr = []
                                    mention = "@sheng "
                                    slen = str(len(text))
                                    elen = str(len(text) + len(mention) - 1)
                                    arrData = {'S':slen, 'E':elen, 'M':mid}
                                    arr.append(arrData)
                                    text += mention + "\n[貼圖資訊]:\n" + "貼圖網址 : line://shop/detail/" + msg.contentMetadata["packageId"] + "\n貼圖ID : " + msg.contentMetadata["stickerId"] + "\n[文字預覽]:\n" + msg.contentMetadata["text"] + "\n(僅顯示100字)" + "\n[文章網址]:\n" + msg.contentMetadata["postEndUrl"]
                                    cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                                except Exception as error:
                                    print(error)
                            else:
                                list_ = msg.contentMetadata['mediaOid'].split("oid=")
                                object = list_[1]
                                try:
                                    arrData = ""
                                    text = "%s\n%s\n"%("---[分享文章預覽]---","[文章作成者]:")
                                    arr = []
                                    mention = "@sheng "
                                    slen = str(len(text))
                                    elen = str(len(text) + len(mention) - 1)
                                    arrData = {'S':slen, 'E':elen, 'M':mid}
                                    arr.append(arrData)
                                    text += mention + "\n[貼圖資訊]:\n" + "貼圖網址 : line://shop/detail/" + msg.contentMetadata["packageId"] + "\n貼圖ID : " + msg.contentMetadata["stickerId"] + "\n[文字預覽]:\n" + msg.contentMetadata["text"] + "\n(僅顯示100字)" + "\n[媒體資訊]:\nhttp://profile.line-cdn.net/r/myhome/h/" + object + "\n[文章網址]:\n" + msg.contentMetadata["postEndUrl"]
                                    cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                                except Exception as error:
                                    print(error)
                    if msg.contentMetadata["serviceType"] == 'GB':
                        if 'stickerId' not in msg.contentMetadata:
                            if 'mediaOid' in msg.contentMetadata:
                                if 'mediaCount' not in msg.contentMetadata:
                                    try:
                                        arrData = ""
                                        text = "%s\n%s\n"%("---[群組文章預覽]---","[文章作成者]:")
                                        arr = []
                                        mention = "@sheng "
                                        slen = str(len(text))
                                        elen = str(len(text) + len(mention) - 1)
                                        arrData = {'S':slen, 'E':elen, 'M':sender}
                                        arr.append(arrData)
                                        text += mention + "\n[文字預覽]:\n" + msg.contentMetadata["text"] + "\n(僅顯示100字)" + "\n[媒體資訊]:\nhttp://profile.line-cdn.net/r/myhome/h/" + msg.contentMetadata["mediaOid"] + "\n數量 : 1" + "\n[文章網址]:\n" + msg.contentMetadata["postEndUrl"]
                                        cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                                    except Exception as error:
                                        print(error)
                                else:
                                    num = int(msg.contentMetadata["mediaCount"])
                                    numb = num + 1
                                    number = str(numb)
                                    try:
                                        arrData = ""
                                        text = "%s\n%s\n"%("---[群組文章預覽]---","[文章作成者]:")
                                        arr = []
                                        mention = "@sheng "
                                        slen = str(len(text))
                                        elen = str(len(text) + len(mention) - 1)
                                        arrData = {'S':slen, 'E':elen, 'M':sender}
                                        arr.append(arrData)
                                        text += mention + "\n[文字預覽]:\n" + msg.contentMetadata["text"] + "\n(僅顯示100字)" + "\n[媒體資訊]:\nhttp://profile.line-cdn.net/r/myhome/h/" + msg.contentMetadata["mediaOid"] + "\n數量 : " + number + "\n[文章網址]:\n" + msg.contentMetadata["postEndUrl"]
                                        cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                                    except Exception as error:
                                        print(error)
                            else:
                                try:
                                    arrData = ""
                                    text = "%s\n%s\n"%("---[群組文章預覽]---","[文章作成者]:")
                                    arr = []
                                    mention = "@sheng "
                                    slen = str(len(text))
                                    elen = str(len(text) + len(mention) - 1)
                                    arrData = {'S':slen, 'E':elen, 'M':sender}
                                    arr.append(arrData)
                                    text += mention + "\n[文字預覽]:\n" + msg.contentMetadata["text"] + "\n(僅顯示100字)" + "\n[文章網址]:\n" + msg.contentMetadata["postEndUrl"]
                                    cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                                except Exception as error:
                                    print(error)
                        else:
                            if 'mediaOid' not in msg.contentMetadata:
                                try:
                                    arrData = ""
                                    text = "%s\n%s\n"%("---[群組文章預覽]---","[文章作成者]:")
                                    arr = []
                                    mention = "@sheng "
                                    slen = str(len(text))
                                    elen = str(len(text) + len(mention) - 1)
                                    arrData = {'S':slen, 'E':elen, 'M':sender}
                                    arr.append(arrData)
                                    text += mention + "\n[貼圖資訊]:\n" + "貼圖網址 : line://shop/detail/" + msg.contentMetadata["packageId"] + "\n貼圖ID : " + msg.contentMetadata["stickerId"] + "\n[文字預覽]:\n" + msg.contentMetadata["text"] + "\n(僅顯示100字)" + "\n[文章網址]:\n" + msg.contentMetadata["postEndUrl"]
                                    cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                                except Exception as error:
                                    print(error)
                            else:
                                try:
                                    arrData = ""
                                    text = "%s\n%s\n"%("---[群組文章預覽]---","[文章作成者]:")
                                    arr = []
                                    mention = "@sheng "
                                    slen = str(len(text))
                                    elen = str(len(text) + len(mention) - 1)
                                    arrData = {'S':slen, 'E':elen, 'M':sender}
                                    arr.append(arrData)
                                    text += mention + "\n[貼圖資訊]:\n" + "貼圖網址 : line://shop/detail/" + msg.contentMetadata["packageId"] + "\n貼圖ID : " + msg.contentMetadata["stickerId"] + "\n[文字預覽]:\n" + msg.contentMetadata["text"] + "\n(僅顯示100字)" + "\n[媒體資訊]:\nhttp://profile.line-cdn.net/r/myhome/h/" + msg.contentMetadata["mediaOid"] + "\n[文章網址]:\n" + msg.contentMetadata["postEndUrl"]
                                    cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                                except Exception as error:
                                    print(error)
                    if msg.contentMetadata["serviceType"] == 'AB':
                        if msg.contentMetadata["locKey"] == 'BA':
                            num = int(msg.contentMetadata["mediaCount"])
                            numb = num + 1
                            number = str(numb)
                            try:
                                arrData = ""
                                text = "%s\n%s\n"%("---[群組相簿創建]---","[相簿作成者]:")
                                arr = []
                                mention = "@sheng "
                                slen = str(len(text))
                                elen = str(len(text) + len(mention) - 1)
                                arrData = {'S':slen, 'E':elen, 'M':sender}
                                arr.append(arrData)
                                text += mention + "\n[相簿名稱]: " + msg.contentMetadata["albumName"] + "\n[新增數量]: " + number + "\n[相簿網址]:\n" + msg.contentMetadata["postEndUrl"]
                                cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                            except Exception as error:
                                print(error)
                        if msg.contentMetadata["locKey"] == 'BT':
                            num = int(msg.contentMetadata["mediaCount"])
                            numb = num + 1
                            number = str(numb)
                            try:
                                arrData = ""
                                text = "%s\n%s\n"%("---[群組相簿圖片新增]---","[新增圖片者]:")
                                arr = []
                                mention = "@sheng "
                                slen = str(len(text))
                                elen = str(len(text) + len(mention) - 1)
                                arrData = {'S':slen, 'E':elen, 'M':sender}
                                arr.append(arrData)
                                text += mention + "\n[相簿名稱]: " + msg.contentMetadata["albumName"] + "\n[新增數量]: " + number + "\n[相簿網址]:\n" + msg.contentMetadata["postEndUrl"]
                                cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                            except Exception as error:
                                print(error)
            if msg.contentType == 0:
                if text is None:
                    return
            if sender in admin:
                if text.lower() == 'h':
                    helpMessage = helpmessage()
                    cl.sendMessage(to, str(helpMessage))
                    cl.sendContact(to, "u5d0aef5aed7a7cbc05d3dfcf30f0aa9f")
                elif text.lower() == 'bot':
                    cl.sendMessage(to, "我的作者：")
                    cl.sendContact(to,"u5d0aef5aed7a7cbc05d3dfcf30f0aa9f")
                elif "Ri " in msg".text:
                    Ri0 = text.replace("Ri ","")
                    Ri1 = Ri0.rstrip()
                    Ri2 = Ri1.replace("@","")
                    Ri3 = Ri2.rstrip()
                    _name = Ri3
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                    cl.findAndAddContactsByMid(target)
                                    cl.inviteIntoGroup(to,[target])
                                except:
                                    pass
                elif text.lower() == 'save':
                    backupData()
                    cl.sendMessage(to,"儲存設定成功!")
                elif "Ri:" in msg.text:
                    midd = text.replace("Ri:","")
                    cl.kickoutFromGroup(to,[midd])
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(to,[midd])
                elif "Uk " in msg.text:
                    midd = text.replace("Uk ","")
                    cl.kickoutFromGroup(to,[midd])
                elif "Tk " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        if target in admin:
                            pass
                        else:
                            try:
                                cl.kickoutFromGroup(to,[target])
                                cl.sendMessage(to, "愛滋病發作")
                            except:
                                pass
                elif "Mk " in msg.text:
                    Mk0 = text.replace("Mk ","")
                    Mk1 = Mk0.rstrip()
                    Mk2 = Mk1.replace("@","")
                    Mk3 = Mk2.rstrip()
                    _name = Mk3
                    gs = cl.getGroup(to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif "Nk " in msg.text:
                    _name = text.replace("Nk ","")
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif "AIDSチームの責任者が侵入" in msg.text:
                    if settings["kickmeber"] == True:
                        if msg.toType == 2:
                            _name = msg.text.replace("警察來了，蘿莉姦了","")
                            gs = cl.getGroup(to)
                            cl.sendMessage(to, "蘿莉團隊翻群\n\n\n愛滋團隊團隊長：邪月。")
                            targets = []
                            for g in gs.members:
                                if _name in g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                pass
                            else:
                                for target in targets:
                                    if target in admin:
                                        pass
                                    else:
                                        try:
                                            cl.kickoutFromGroup(to, [target])
                                        except:
                                            pass
                elif "Zk" in msg.text:
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif "Vk:" in text:
                    midd = msg.text.replace("Vk:","")
                    cl.kickoutFromGroup(msg.to,[midd])
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
                    cl.cancelGroupInvitation(msg.to,[midd])
                elif "Vk " in msg.text:
                        vkick0 = msg.text.replace("Vk ","")
                        vkick1 = vkick0.rstrip()
                        vkick2 = vkick1.replace("@","")
                        vkick3 = vkick2.rstrip()
                        _name = vkick3
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for s in gs.members:
                            if _name in s.displayName:
                                targets.append(s.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    cl.kickoutFromGroup(msg.to,[target])
                                    cl.findAndAddContactsByMid(target)
                                    cl.inviteIntoGroup(msg.to,[target])
                                    cl.cancelGroupInvitation(msg.to,[target])
                                except:
                                    pass
                elif "NT " in msg.text:
                    _name = text.replace("NT ","")
                    gs = cl.getGroup(to)
                    targets = []
                    net_ = ""
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            mc = sendMessageWithMention(to,target) + "\n"
                        cl.sendMessage(to,mc)
                elif text.lower() == 'zt':
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            sendMessageWithMention(to,target)
                elif text.lower().startswith("x1: "):
                        separate = text.split(" ")
                        string = text.replace(separate[0] + " ","")
                        if len(string) <= 10000000000:
                            profile = cl.getProfile()
                            profile.displayName = string
                            cl.updateProfile(profile)
                            cl.sendMessage(to,"名稱已更改為 " + string + "")	
                elif text.lower() == 'zm':
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        mc = "0字元使用者Mid："
                        for mi_d in targets:
                            mc += "\n->" + mi_d
                        cl.sendMessage(to,mc)
                elif "Mc " in msg.text:
                    mmid = msg.text.replace("Mc ","")
                    cl.sendContact(to, mmid)
                elif "Sc " in msg.text:
                    ggid = msg.text.replace("Sc ","")
                    group = cl.getGroup(ggid)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "不明"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "關閉"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    else:
                        gQr = "開啟"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "[群組資料]"
                    ret_ += "\n顯示名稱 : {}".format(str(group.name))
                    ret_ += "\n群組ＩＤ : {}".format(group.id)
                    ret_ += "\n群組作者 : {}".format(str(gCreator))
                    ret_ += "\n成員數量 : {}".format(str(len(group.members)))
                    ret_ += "\n邀請數量 : {}".format(gPending)
                    ret_ += "\n群組網址 : {}".format(gQr)
                    ret_ += "\n群組網址 : {}".format(gTicket)
                    ret_ += "\n[完]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif msg.text in ["c","C","cancel","Cancel"]:
                  if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = (contact.mid for contact in X.invitee)
                        ginfo = cl.getGroup(msg.to)
                        sinvitee = str(len(ginfo.invitee))
                        start = time.time()
                        for cancelmod in gInviMids:
                            cl.cancelGroupInvitation(msg.to, [cancelmod])
                        elapsed_time = time.time() - start
                        cl.sendMessage(to, "已取消完成\n取消時間: %s秒" % (elapsed_time))
                        cl.sendMessage(to, "取消人數:" + sinvitee)
                    else:
                        cl.sendMessage(to, "沒有任何人在邀請中！！")
                elif text.lower() == 'gcancel':
                    gid = cl.getGroupIdsInvited()
                    start = time.time()
                    for i in gid:
                        cl.rejectGroupInvitation(i)
                    elapsed_time = time.time() - start
                    cl.sendMessage(to, "全部群組邀請已取消")
                    cl.sendMessage(to, "取消時間: %s秒" % (elapsed_time))
                elif "Gn " in msg.text:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("Gn ","")
                        cl.updateGroup(X)
                    else:
                        cl.sendMessage(msg.to,"無法使用在群組外")
                elif msg.text.startswith("Cn:"):
		                string = msg.text.replace("Cn:","")
		                profile = cl.getProfile()
		                profile.displayName = string
		                cl.updateProfile(profile)
		                cl.sendMessage(msg.to,"更換成:" + profile.displayName)
                elif text.lower().startswith('op '):
                        MENTION = eval(msg.contentMetadata['MENTION'])
                        inkey = MENTION['MENTIONEES'][0]['M']
                        admin.append(str(inkey))
                        cl.sendMessage(to, "已❤權限！")
                elif text.lower().startswith('deop '):
                        MENTION = eval(msg.contentMetadata['MENTION'])
                        inkey = MENTION['MENTIONEES'][0]['M']
                        admin.remove(str(inkey))
                        cl.sendMessage(to, "已💔權限！")
                elif text.lower().startswith('mop:'):
                        midd = msg.text.replace("mop:","")
                        admin.append(str(midd))
                        cl.sendMessage(to, "已❤權限！")
                elif text.lower().startswith('mdp:'):
                        midd = msg.text.replace("mdp:","")
                        admin.remove(str(midd))
                        cl.sendMessage(to, "已💔權限！")
                elif text.lower() == 'opmid':
                    if admin == []:
                        cl.sendMessage(to, "沒有權限者")
                    else:
                        mc = "❤清單："
                        for mi_d in admin:
                            mc += "\n-> " + mi_d
                        cl.sendMessage(to, mc)
                elif text.lower() == 'oplist':
                    if admin == []:
                        cl.sendMessage(to, "沒有權限者")
                    else:
                        mc = "女友❤清單："
                        for mi_d in admin:
                            mc += "\n◉ " + cl.getContact(mi_d).displayName
                        cl.sendMessage(to, mc)
                elif "Gc" in msg.text:
                    if msg.toType == 2:
                        key = eval(msg.contentMetadata["MENTION"])
                        u = key["MENTIONEES"][0]["M"]
                        contact = cl.getContact(u)
                        cu = cl.getProfileCoverURL(mid=u)
                        try:
                            cl.sendMessage(msg.to,"名字:\n" + contact.displayName + "\n\n系統識別碼:\n" + contact.mid + "\n\n個性簽名:\n" + contact.statusMessage + "\n\n頭貼網址 :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n封面網址 :\n" + str(cu))
                        except:
                            cl.sendMessage(msg.to,"名字:\n" + contact.displayName + "\n\n系統識別碼:\n" + contact.mid + "\n\n個性簽名:\n" + contact.statusMessage + "\n\n封面網址:\n" + str(cu))
                elif "Inv " in msg.text:
                    midd = msg.text.replace("Inv ","")
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
                elif text.lower() == 'bye':
                    cl.leaveGroup(to)
                elif "Ban" in msg.text:
                    if msg.toType == 2:
                        print ("[Ban] 成功")
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    settings["blacklist"][target] = True
                                    cl.sendMessage(to, "已加入🇨🇳")
                                except:
                                    pass
                elif "Unban" in msg.text:
                    if msg.toType == 2:
                        print ("[UnBan] 成功")
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    del settings["blacklist"][target]
                                    cl.sendMessage(to, "已解除🇹🇼")
                                except:
                                    pass
                elif "Mb:" in msg.text:
                    midd = msg.text.replace("Mb:","")
                    try:
                        settings["blacklist"][midd] = True
                        backupData()
                        cl.sendMessage(to, "已加入🇨🇳")
                    except:
                        pass
                elif "Mub:" in msg.text:
                    midd = msg.text.replace("Mub:","")
                    try:
                        del settings["blacklist"][midd]
                        backupData()
                        cl.sendMessage(to, "已解除🇹🇼")
                    except:
                        pass
                elif text.lower() == 'clear ban':
                    for mi_d in settings["blacklist"]:
                        settings["blacklist"] = {}
                    cl.sendMessage(to, "已清空中共人口")
                elif text.lower() == 'banlist':
                    if settings["blacklist"] == {}:
                        cl.sendMessage(to, "沒有中共人口")
                    else:
                        mc = "黑名單："
                        for mi_d in settings["blacklist"]:
                            mc += "\n->" + cl.getContact(mi_d).displayName
                        cl.sendMessage(to, mc)
                elif text.lower() == 'banmid':
                    if settings["blacklist"] == {}:
                        cl.sendMessage(to, "沒有🇨🇳")
                    else:
                        mc = "黑名單："
                        for mi_d in settings["blacklist"]:
                            mc += "\n->" + mi_d
                        cl.sendMessage(to, mc)
                elif text.lower() == 'kill ban':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in settings["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            print ("1")
                            cl.sendMessage(to, "沒有🇨🇳")
                            return
                        for jj in matched_list:
                            cl.kickoutFromGroup(to, [jj])
                            cl.sendMessage(to, "🇨🇳已踢除")
                elif text.lower() == 'killbanall':
                    gid = cl.getGroupIdsJoined()
                    group = cl.getGroup(to)
                    gMembMids = [contact.mid for contact in group.members]
                    ban_list = []
                    for tag in settings["blacklist"]:
                        ban_list += filter(lambda str: str == tag, gMembMids)
                    if ban_list == []:
                        cl.sendMessage(to, "沒有🇨🇳")
                    else:
                        for i in gid:
                            for jj in ban_list:
                                cl.kickoutFromGroup(i, [jj])
                            cl.sendMessage(i, "已針對所有群組清🇨🇳！")
                elif "/invitemeto:" in msg.text:
                    gid = msg.text.replace("/invitemeto:","")
                    if gid == "":
                        cl.sendMessage(to, "請輸入群組ID")
                    else:
                        try:
                            cl.findAndAddContactsByMid(msg._from)
                            cl.inviteIntoGroup(gid,[msg._from])
                        except:
                            cl.sendMessage(to, "我不在那個群組裡")
                elif text.lower().startswith('call:'):
                    if msg.toType == 2:
                        number = msg.text.replace("call:","")
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        num = int(number)
                        for var in range(0,num):
                            cl.inviteIntoGroupCall(to,gMembMids,1)
                        cl.sendMessage(to, "邀请完毕 共邀请{}次".format(number))
                elif text.lower().startswith('rall:'):
                    if msg.toType == 1:
                        number = msg.text.replace("rall:","")
                        room = cl.getRoom(to)
                        rMembMids = [contact.mid for contact in room.contacts]
                        num = int(number)
                        for var in range(0,num):
                            cl.inviteIntoGroupCall(to,rMembMids,1)
                        cl.sendMessage(to, "邀请完毕 共邀请了{}次".format(number))
                elif text.lower().startswith('tag '):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    list_ = msg.text.split(" ")
                    number = list_[2]
                    num = int(number)
                    for var in range(0,num):
                        sendMessageWithMention(to, inkey)
                    cl.sendMessage(to, "".format(number))
                elif text.lower().startswith('say '):
                    list_ = msg.text.split(" ")
                    text = list_[1]
                    number = list_[2]
                    num = int(number)
                    for var in range(0,num):
                        cl.sendMessage(to, text)
                    cl.sendMessage(to, "".format(number))
                elif text.lower().startswith('post:'):
                    list_ = msg.text.split(":")
                    post = list_[1]
                    number = list_[2]
                    num = int(number)
                    for var in range(0,num):
                        cl.sendPostToTalk(to,post)
                    cl.sendMessage(to, "分享完畢 共分享了{}次".format(number))
                elif text.lower().startswith('talk:'):
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        text = msg.text.replace("talk:","")
                        for mem in group.members:
                            path = "http://dl.profile.line-cdn.net/" + str(mem.pictureStatus)
                            cl.sendMessage(to, text, {'MSG_SENDER_NAME': str(mem.displayName),'MSG_SENDER_ICON': str(path)})
                elif text.lower().startswith('prank '):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    sep = msg.text.split(" ")
                    text = sep[2]
                    contact = cl.getContact(inkey)
                    path = "http://dl.profile.line-cdn.net/" + str(contact.pictureStatus)
                    cl.sendMessage(to, text, {'MSG_SENDER_NAME': str(contact.displayName),'MSG_SENDER_ICON': str(path)})
                elif text.lower().startswith('send-tw '):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-tw'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(to,"hasil.mp3")
                elif text.lower().startswith('send-en '):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(to,"hasil.mp3")
                elif text.lower().startswith('send-jp '):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ja'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(to,"hasil.mp3")
                elif text.lower().startswith('send-id '):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'id'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(to,"hasil.mp3")
                elif text.lower().startswith('tr-tw '):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-tw')
                    A = hasil.text
                    cl.sendMessage(to, A)
                elif text.lower().startswith('tr-en '):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='en')
                    A = hasil.text
                    cl.sendMessage(to, A)
                elif text.lower().startswith('tr-jp '):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ja')
                    A = hasil.text
                    cl.sendMessage(to, A)
                elif text.lower().startswith('tr-id '):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='id')
                    A = hasil.text
                    cl.sendMessage(to, A)
                elif "/ti/g/" in msg.text.lower():
                    if settings["autoJoinTicket"] == True:
                        link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                        links = link_re.findall(text)
                        n_links = []
                        for l in links:
                            if l not in n_links:
                                n_links.append(l)
                        for ticket_id in n_links:
                            group = cl.findGroupByTicket(ticket_id)
                            cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                            cl.sendMessage(group.id, "網址自動入群-群名 : %s" % str(group.name))
                elif text.lower() == '阿斯':
                    cl.sendMessage(to, "醉憶醫生測試現場")
                    cl.sendMessage(to, "顏值嗎？")
                    cl.sendMessage(to, "高度嗎？")
                    cl.sendMessage(to, "可愛嗎？")
                    cl.sendMessage(to, "體貼嗎？")
                    cl.sendMessage(to, "溫柔嗎？")
                    cl.sendMessage(to, "高冷嗎？")
                    cl.sendMessage(to, "個性好嗎？")
                    cl.sendMessage(to, "好聊嗎？")
                    cl.sendMessage(to, "胸圍大嗎？")
                    cl.sendMessage(to, "拜金嗎？")
                    cl.sendMessage(to, "迷人嗎？")
                    cl.sendMessage(to, "好看嗎？")
                    cl.sendMessage(to, "處女嗎？")
                    cl.sendMessage(to, "愛我嗎？")
                    cl.sendMessage(to, "很色嗎？")
                    cl.sendMessage(to, "很騷嗎？")
                    cl.sendMessage(to, "很會搖嗎？")
                    cl.sendMessage(to, "身高高嗎？")
                    cl.sendMessage(to, "只愛我嗎？")
                    cl.sendMessage(to, "測試結果以上皆是！")
                elif msg.text in ["Friendlist"]:
                    anl = cl.getAllContactIds()
                    ap = ""
                    for q in anl:
                        ap += "• "+cl.getContact(q).displayName + "\n"
                    cl.sendMessage(msg.to,"「 朋友列表 」\n"+ap+"人數 : "+str(len(anl)))
                elif text.lower() == 'sp':
                    start = time.time() 
                    cl.sendMessage(to,'Test speed')
                    elapsed_time = time.time()/500 - start/500
                    cl.sendMessage(to,format(str(elapsed_time)) + "seconds")
                elif text.lower() == 'speed':
                    time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=100)
                    str1 = str(time0/100)
                    start = time.time()
                    cl.sendMessage(to,'汁妹反應速度\n' + str1 + 'seconds')
                    elapsed_time = time.time()/1 - start/1
                    cl.sendMessage(to,'指令反應\n' + format(str(elapsed_time)) + '秒')
                elif text.lower() == 'rebot':
                    cl.sendMessage(to, "重新啟動中...請稍後...")
                    time.sleep(5)
                    cl.sendMessage(to, "重新啟動完成！")
                    restartBot()
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    cl.sendMessage(to, "系統已運作 {}".format(str(runtime)))
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner ="u403f1261e06558bfaad641843302a66b"
                        creator = cl.getContact(owner)
                        contact = cl.getContact(clMID)
                        grouplist = cl.getGroupIdsJoined()
                        contactlist = cl.getAllContactIds()
                        blockedlist = cl.getBlockedContactIds()
                        ret_ = "[ 關於使用者 ]"
                        ret_ += "使用者名稱 : {}".format(contact.displayName)
                        ret_ += "群組數 : {}".format(str(len(grouplist)))
                        ret_ += "好友數 : {}".format(str(len(contactlist)))
                        ret_ += "已封鎖 : {}".format(str(len(blockedlist)))
                        ret_ += "\n[ 關於本bot ]"
                        ret_ += "\n版本 : 8.4"
                        ret_ += "\n製作者 : {}".format(creator.displayName)
                        ret_ += "[ 感謝您的使用 ]"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == 'set':
                    try:
                        ret_ = "醉憶設定表"
                        if settings["autoAdd"] == True: ret_ += "\n自動加入好友 ❤"
                        else: ret_ += "\n自動加入好友 💔"
                        if settings["autoJoin"] == True: ret_ += "\n自動加入群組 ❤"
                        else: ret_ += "\n自動加入群組 💔"
                        if settings["autoJoinTicket"] == True: ret_ += "\n網址自動入群 ❤"
                        else: ret_ += "\n網址自動入群 💔"
                        if settings["autoLeave"] == True: ret_ += "\n自動離開副本 ❤"
                        else: ret_ += "\n自動離開副本 💔"
                        if settings["autoRead"] == True: ret_ += "\n自動已讀 开.❤"
                        else: ret_ += "\n自動已讀 💔"
                        if settings["protect"] == True: ret_ += "\n群組保護開啟 ❤"
                        else: ret_ += "\n群組保護關閉 💔"
                        if settings["inviteprotect"] == True: ret_ += "\n群組邀請保護 ❤"
                        else: ret_ += "\n群組邀請保護 💔"
                        if settings["qrprotect"] == True: ret_ += "\n群組網址保護 ❤"
                        else: ret_ += "\n群組網址保護 💔"
                        if settings["contact"] == True: ret_ += "\n詳細資料 ❤"
                        else: ret_ += "\n詳細資料 💔"
                        if settings["reread"] == True: ret_ += "\n查詢收回 ❤"
                        else: ret_ += "\n查詢收回 💔"
                        if settings["detectMention"] == False: ret_ += "\n標註回覆開啟 ❤"
                        else: ret_ += "\n標註回覆 💔"
                        if settings["checkSticker"] == True: ret_ += "\n貼圖資料查詢 ❤"
                        else: ret_ += "\n貼圖資料查詢 💔"
                        if settings["kickContact"] == True: ret_ += "\n踢人標註 ❤"
                        else: ret_ += "\n踢人標註 💔"
                        if settings["autoPtt"] == True: ret_ += "\n自動進退 ❤"
                        else: ret_ += "\n自動進退 💔"
                        if settings["timeline"] == True: ret_ += "\n文章詳情 ❤"
                        else: ret_ += "\n文章詳情 💔"
                        if settings["seeJoin"] == True: ret_ += "\n入群通知 ❤"
                        else: ret_ += "\n入群通知 💔"
                        if settings["seeLeave"] == True: ret_ += "\n退群通知 ❤"
                        else: ret_ += "\n退群通知 💔"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == 'add on':
                    settings["autoAdd"] = True
                    cl.sendMessage(to, "自動加入好友已開")
                elif text.lower() == 'add off':
                    settings["autoAdd"] = False
                    cl.sendMessage(to, "自動加入好友已關")
                elif text.lower() == 'join on':
                    settings["autoJoin"] = True
                    cl.sendMessage(to, "自動加入群組已開")
                elif text.lower() == 'join off':
                    settings["autoJoin"] = False
                    cl.sendMessage(to, "自動加入群組已關")
                elif text.lower() == 'leave on':
                    settings["autoLeave"] = True
                    cl.sendMessage(to, "自動離開副本已開")
                elif text.lower() == 'leave off':
                    settings["autoLeave"] = False
                    cl.sendMessage(to, "自動離開副本已關")
                elif text.lower() == 'contact on':
                    settings["contact"] = True
                    cl.sendMessage(to, "查看好友資料詳情開")
                elif text.lower() == 'contact off':
                    settings["contact"] = False
                    cl.sendMessage(to, "查看好友資料詳情關")
                elif text.lower() == 'groupprotect on':
                    settings["protect"] = True
                    cl.sendMessage(to, "群組保護已開")
                elif text.lower() == 'groupprotect off':
                    settings["protect"] = False
                    cl.sendMessage(to, "群組保護已關")
                elif text.lower() == 'inviteprotect on':
                    settings["inviteprotect"] = True
                    cl.sendMessage(to, "群組邀請保護已開")
                elif text.lower() == 'inviteprotect off':
                    settings["inviteprotect"] = False
                    cl.sendMessage(to, "群組邀請保護已關")
                elif text.lower() == 'qr on':
                    settings["qrprotect"] = True
                    cl.sendMessage(to, "群組網址保護已開")
                elif text.lower() == 'qr off':
                    settings["qrprotect"] = False
                    cl.sendMessage(to, "群組網址保護已關")
                elif text.lower() == 'reread on':
                    settings["reread"] = True
                    cl.sendMessage(to, "查詢收回開")
                elif text.lower() == 'reread off':
                    settings["reread"] = False
                    cl.sendMessage(to, "查詢收回關")
                elif text.lower() == 'read on':
                    settings["autoRead"] = True
                    cl.sendMessage(to, "自動已讀已開")
                elif text.lower() == 'read off':
                    settings["autoRead"] = False
                    cl.sendMessage(to, "自動已讀已關")
                elif text.lower() == 'qrjoin on':
                    settings["autoJoinTicket"] = True
                    cl.sendMessage(to, "網址自動入群已開")
                elif text.lower() == 'qrjoin off':
                    settings["autoJoinTicket"] = False
                    cl.sendMessage(to, "網址自動入群已關")
                elif text.lower() == 'mention on':
                    settings["detectMention"] = True
                    cl.sendMessage(to, "標註回覆已開")
                elif text.lower() == 'mention off':
                    settings["detectMention"] = False
                    cl.sendMessage(to, "標註回覆已關")
                elif text.lower() == 'ck on':
                    settings["checkSticker"] = True
                    cl.sendMessage(to, "貼圖資料查詢已開")
                elif text.lower() == 'ck off':
                    settings["checkSticker"] = False
                    cl.sendMessage(to, "貼圖資料查詢已關")
                elif text.lower() == 'kc on':
                    settings["kickContact"] = True
                    cl.sendMessage(to, "踢人標註已開")
                elif text.lower() == 'kc off':
                    settings["kickContact"] = False
                    cl.sendMessage(to, "踢人標註已關")
                elif text.lower() == 'ptt on':
                    settings["autoPtt"] = True
                    cl.sendMessage(to, "自動進退已開")
                elif text.lower() == 'ptt off':
                    settings["autoPtt"] = False
                    cl.sendMessage(to, "自動進退已關")
                elif text.lower() == 'tl on':
                    settings["timeline"] = True
                    cl.sendMessage(to, "文章詳情已開")
                elif text.lower() == 'tl off':
                    settings["timeline"] = False
                    cl.sendMessage(to, "文章詳情已關")
                elif text.lower() == 'sj on':
                    settings["seeJoin"] = True
                    cl.sendMessage(to, "入群通知已開")
                elif text.lower() == 'sj off':
                    settings["seeJoin"] = False
                    cl.sendMessage(to, "入群通知已關")
                elif text.lower() == 'sl on':
                    settings["seeLeave"] = True
                    cl.sendMessage(to, "退群通知已開")
                elif text.lower() == 'sl off':
                    settings["seeLeave"] = False
                    cl.sendMessage(to, "退群通知已關")
                elif text.lower() == 'me':
                    sendMessageWithMention(to, sender)
                    cl.sendContact(to, sender)
                elif text.lower() == 'mymid':
                    cl.sendMessage(msg.to,"[MID]\n" +  sender)
                elif text.lower() == 'myname':
                    me = cl.getContact(sender)
                    cl.sendMessage(msg.to,"[顯示名稱]\n" + me.displayName)
                elif text.lower() == 'mybio':
                    me = cl.getContact(sender)
                    cl.sendMessage(msg.to,"[狀態消息]\n" + me.statusMessage)
                elif text.lower() == 'mypicture':
                    me = cl.getContact(sender)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'mycover':
                    me = cl.getContact(sender)
                    cover = cl.getProfileCoverURL(sender)
                    cl.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("contact "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            mi_d = contact.mid
                            cl.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "標註者系統辨識碼："
                        for ls in lists:
                            ret_ += "\n" + ls
                        cl.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("name "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            cl.sendMessage(msg.to, "[ 名稱 ]\n" + contact.displayName)
                elif msg.text.lower().startswith("bio "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            cl.sendMessage(msg.to, "[ 個簽 ]\n" + contact.statusMessage)
                elif msg.text.lower().startswith("picture "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line-cdn.net/" + cl.getContact(ls).pictureStatus
                            cl.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("mpicture "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line-cdn.net/" + cl.getContact(ls).pictureStatus
                            cl.sendVideoWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("cover "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = cl.getProfileCoverURL(ls)
                                cl.sendImageWithURL(msg.to, str(path))
                elif text.lower().startswith('un '):
                    try:
                        sep = text.split(" ")
                        try:
                            mes = int(sep[1])
                        except:
                            mes = 1
                        M = cl.getRecentMessagesV2(to)
                        midd = []
                        for ind,i in enumerate(M):
                            if ind == 0:
                                pass
                            else:
                                if i._from == clMID:
                                    midd.append(i.id)
                                    if len(midd) == mes:
                                        break
                        for i in midd:
                            cl.unsendMessage(i)
                    except Exception as e:
                        print(e)
                elif text.lower() == 'gowner':
                    group = cl.getGroup(to)
                    GS = group.creator.mid
                    cl.sendContact(to, GS)
                elif text.lower() == 'gid':
                    gid = cl.getGroup(to)
                    cl.sendMessage(to, "[群組ID : ]\n" + gid.id)
                elif text.lower() == 'gurl':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = cl.reissueGroupTicket(to)
                            cl.sendMessage(to, "[ 群組網址 ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            cl.sendMessage(to, "群組網址未開啟，請用Ourl先開啟")
                elif text.lower() == 'ourl':
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            cl.sendMessage(to, "群組網址已開啟")
                        else:
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                            cl.sendMessage(to, "成功開啟群組網址")
                elif text.lower() == 'curl':
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == True:
                            cl.sendMessage(to, "群組網址已關閉")
                        else:
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                            cl.sendMessage(to, "成功關閉群組網址")
                elif text.lower() == 'ginfo':
                    group = cl.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "不明"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "關閉"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    else:
                        gQr = "開啟"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "《群組資料》"
                    ret_ += "\n顯示名稱 : {}".format(str(group.name))
                    ret_ += "\n群組ＩＤ : {}".format(group.id)
                    ret_ += "\n群組作者 : {}".format(str(gCreator))
                    ret_ += "\n成員數量 : {}".format(str(len(group.members)))
                    ret_ += "\n邀請數量 : {}".format(gPending)
                    ret_ += "\n群組網址 : {}".format(gQr)
                    ret_ += "\n群組網址 : {}".format(gTicket)
                    ret_ += "\n[ 完 ]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif text.lower() == 'gb':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        ret_ = "[成員列表]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n{}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n[總共： {} 人]".format(str(len(group.members)))
                        cl.sendMessage(to, str(ret_))
                elif text.lower() == 'lg':
                        groups = cl.groups
                        ret_ = "[群組列表]"
                        no = 0 + 1
                        for gid in groups:
                            group = cl.getGroup(gid)
                            ret_ += "\n {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n[總共 {} 個群組]".format(str(len(groups)))
                        cl.sendMessage(to, str(ret_))
                elif text.lower() == 'tagall':
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        cl.sendMessage(to, "總共 {} 個成員".format(str(len(nama))))
                elif msg.text in ["SR","Setread"]:
                    cl.sendMessage(msg.to, "設置已讀點 ✔")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                    print ("設置已讀點")
                elif msg.text in ["DR","Delread"]:
                    cl.sendMessage(to, "刪除已讀點 ✘")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                        del wait2['setTime'][msg.to]
                    except:
                        pass
                elif msg.text in ["LR","Lookread"]:
                    if msg.to in wait2['readPoint']:
                        print ("查詢已讀")
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"
                        cl.sendMessage(msg.to, "[已讀順序]:%s\n\n[已讀的小癟三❤]:\n%s\n查詢時間:[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendMessage(msg.to, "請輸入SR設置已讀點")
        if op.type == 26:
            try:
                msg = op.message
                if settings["reread"] == True:
                    if msg.toType == 0:
                        cl.log("[%s]"%(msg._from)+msg.text)
                    else:
                        cl.log("[%s]"%(msg.to)+msg.text)
                    if msg.contentType == 0:
                        msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 65:
            try:
                at = op.param1
                msg_id = op.param2
                if settings["reread"] == True:
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"] not in bl:
                            cl.sendMessage(at,"[你三小？收回啥小，破狗:)]\n%s\n[收回不想讓別人看到的破狗內容]\n%s"%(cl.getContact(msg_dict[msg_id]["from"]).displayName,msg_dict[msg_id]["text"]))
                            print ("收回訊息")
                        del msg_dict[msg_id]
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    cl.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if msg.contentType == 0 and sender not in clMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if clMID in mention["M"]:
                                if settings["detectMention"] == True:
                                    contact = cl.getContact(sender)
                                    cl.sendMessage(to, "")
                                    sendMessageWithMention(to, contact.mid)
                                break
        if op.type == 55:
            try:
                print("[55]通知已讀訊息")
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n[★]" + Name
                        wait2['ROM'][op.param1][op.param2] = "[★]" + Name
                        print (time.time() + Name)
                else:
                    pass
            except:
                pass
    except Exception as error:
        logError(error)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
