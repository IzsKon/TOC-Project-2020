from transitions.extensions import GraphMachine
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageAction

from utils import send_text_message, send_button_message

picIRRH = 'https://i.imgur.com/cxJVCWG.png'
picWolf = 'https://i.imgur.com/1Eo41qh.png'
picAlice = 'https://i.imgur.com/8oFV3WA.jpg'
picKatniss = 'https://i.imgur.com/CwF2oPx.jpg'
picMatch = 'https://i.imgur.com/ZUWrw6w.png'
picBaba = 'https://i.imgur.com/Gq9QDlX.jpg'
picSnow = 'https://i.imgur.com/mg3LC5j.jpg'
picWizard = 'https://i.imgur.com/2duWlSp.jpg'
picSelect = 'https://i.imgur.com/5IldcCf.jpg'
picPhoto = 'https://i.imgur.com/RZCxIR8.png'
picPaper = 'https://i.imgur.com/DY8XB74.png'
picFail = 'https://i.imgur.com/rqhkPMX.jpg'
picSuccess = 'https://i.imgur.com/5m45EyI.png'
picEnd = 'https://i.imgur.com/7ESxabm.jpg'
picBg = 'https://i.imgur.com/ukwX4FR.png'

class TocMachine(GraphMachine):

    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    # restart ##################################################################################################
    def is_going_to_restart(self, event):
        text = event.message.text
        return text.lower() == "restart"

    def on_enter_restart(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picBg,
                    title = 'RESTART',
                    text = '選擇開始繼續',
                    actions = [
                        MessageAction(
                            label = '開始',
                            text = '開始'
                        )
                    ]
                )
            )
        send_button_message(event.reply_token, button_message)
        self.game_over()

    

    # preview ##################################################################################################

    ## preivew 1
    def is_going_to_preview1(self, event):
        text = event.message.text
        return text.lower() == "開始" or text.lower() == '重來'

    def on_enter_preview1(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picBg,
                title = '前導: 老巫師在做研究，',
                text='不小心打翻藥水到書上有人跑了出來，將老巫師打倒在地開始亂灑藥水。其他跑出來的人也都跑走了。',
                actions=[
                    MessageAction(
                        label = '繼續',
                        text = '繼續'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## preview 2
    def is_going_to_preview2(self, event):
        text = event.message.text
        return text.lower() == "繼續"

    def on_enter_preview2(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picBg,
                title = '第二天',
                text = '有人跑進來搶走所有的東西並將老巫師打倒在地還放了把火。',
                actions = [
                    MessageAction(
                        label = '繼續',
                        text = '繼續'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## preview 3
    def is_going_to_preview3(self, event):
        text = event.message.text
        return text.lower() == "繼續"

    def on_enter_preview3(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picWizard,
                title = '老巫師:',
                text = '幫幫我……快點到圖書室找我。',
                actions = [
                    MessageAction(
                        label = '(去找老巫師)',
                        text = '(去找老巫師)'
                    ),
                    MessageAction(
                        label = '(無視)',
                        text = '(無視)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ### help
    def is_going_to_help(self, event):
        text = event.message.text
        return text.lower() == "(去找老巫師)"

    def on_enter_help(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picWizard,
                title = '老巫師: 請將他們收回書裡。',
                text = '拿著他們的書並讓他們同意回去後就行了，但現在我手上只剩這本書，其他你要自己找了。',
                actions = [
                    MessageAction(
                        label = '交給我吧',
                        text = '交給我吧'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ### helpnt
    def is_going_to_helpnt(self, event):
        text = event.message.text
        return text.lower() == "(無視)"

    def on_enter_helpnt(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picBg,
                    title = 'GAMEOVER',
                    text = ' ',
                    actions = [
                        MessageAction(
                            label = '重來',
                            text = '重來'
                        )
                    ]
                )
            )
        send_button_message(event.reply_token, button_message)
        self.game_over()



    # s1 ############################################################################################

    def is_going_to_s1(self, event):
        text = event.message.text
        return text.lower() == "交給我吧" or text.lower() == "找其他人" or text.lower() == "不要" or text.lower() == "..."

    def on_enter_s1(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '已獲得「愛麗絲夢遊仙境」',
                actions = [
                    MessageAction(
                        label = '愛麗絲',
                        text = '找愛麗絲'
                    ),
                    MessageAction(
                        label = '大野狼',
                        text = '找大野狼'
                    ),
                    MessageAction(
                        label = '賣火柴的小女孩',
                        text = '找賣火柴的小女孩'
                    ),
                    MessageAction(
                        label = '其他人',
                        text = '找其他人'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_s1p2(self, event):
        text = event.message.text
        return text.lower() == "找其他人" or text.lower() == "..." or text.lower() == "沒事" or text.lower() == "等她起床"

    def on_enter_s1p2(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '已獲得「愛麗絲夢遊仙境」',
                actions = [
                    MessageAction(
                        label = '白雪公主',
                        text = '找白雪公主'
                    ),
                    MessageAction(
                        label = '凱妮絲',
                        text = '找凱妮絲'
                    ),
                    MessageAction(
                        label = '奶奶',
                        text = '找奶奶'
                    ),
                    MessageAction(
                        label = '其他人',
                        text = '找其他人'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## alice1
    def is_going_to_alice1(self, event):
        text = event.message.text
        return text.lower() == "找愛麗絲"

    def on_enter_alice1(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picAlice,
                title = '愛麗絲',
                text = '(要問她什麼?)',
                actions = [
                    MessageAction(
                        label = '你願意回到書中嗎?',
                        text = '你願意回到書中嗎?'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_inAlice1(self, event):
        text = event.message.text
        return text.lower() == "你願意回到書中嗎?"

    def on_enter_inAlice1(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picAlice,
                title = '愛麗絲:',
                text = '我也想回去阿~~可是我找不到我的枕頭，一定是昨天跟她出去的時候弄掉了，有枕頭我就回去。',
                actions = [
                    MessageAction(
                        label = '(幫愛麗絲找枕頭)',
                        text = '(幫愛麗絲找枕頭)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## wolf1
    def is_going_to_wolf1(self, event):
        text = event.message.text
        return text.lower() == "找大野狼"

    def on_enter_wolf1(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picWolf,
                title = '大野狼:',
                text = '要不要買保險阿!',
                actions = [
                    MessageAction(
                        label = '不要...',
                        text = '不要'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## snow1
    def is_going_to_snow1(self, event):
        text = event.message.text
        return text.lower() == "找白雪公主"

    def on_enter_snow1(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSnow,
                title = '白雪公主:',
                text = '真是太瘋狂了!昨天那個瘋子突然就攻擊我們兩個。害我弄掉了一隻鞋子!希望能被王子撿到!',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## katniss1
    def is_going_to_katniss1(self, event):
        text = event.message.text
        return text.lower() == "找凱妮絲"

    def on_enter_katniss1(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picKatniss,
                title = '凱妮絲:',
                text = '我正忙打獵找食物呢!',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## match1
    def is_going_to_match1(self, event):
        text = event.message.text
        return text.lower() == "找賣火柴的小女孩"

    def on_enter_match1(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picMatch,
                title = '賣火柴的小女孩:',
                text = '我現在沒有火柴了下次再來吧。',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()
        
    ## baba1
    def is_going_to_baba1(self, event):
        text = event.message.text
        return text.lower() == "找奶奶"

    def on_enter_baba1(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picBaba,
                title = '奶奶:',
                text = '呼……呼……(睡覺中)',
                actions = [
                    MessageAction(
                        label = '(叫醒她)',
                        text = '叫醒'
                    ),
                    MessageAction(
                        label = '(等她起床再說好了)',
                        text = '等她起床'
                    ),
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## wake1
    def is_going_to_wake1(self, event):
        text = event.message.text
        return text.lower() == "叫醒"

    def on_enter_wake1(self, event):
        print("entering wake")
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picBaba,
                title = '奶奶:',
                text = '找我有什麼事嗎?',
                actions = [
                    MessageAction(
                        label = '沒事',
                        text = '沒事'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()



    # s2 ############################################################################################

    def is_going_to_s2(self, event):
        text = event.message.text
        return text.lower() == "(幫愛麗絲找枕頭)" or text.lower() == "找其他人" or text.lower() == "不要" or text.lower() == "..."

    def on_enter_s2(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '已獲得「愛麗絲夢遊仙境」',
                actions = [
                    MessageAction(
                        label = '小紅帽',
                        text = '找小紅帽'
                    ),
                    MessageAction(
                        label = '大野狼',
                        text = '找大野狼'
                    ),
                    MessageAction(
                        label = '賣火柴的小女孩',
                        text = '找賣火柴的小女孩'
                    ),
                    MessageAction(
                        label = '其他人',
                        text = '找其他人'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_s2p2(self, event):
        text = event.message.text
        return text.lower() == "找其他人" or text.lower() == "..." or text.lower() == "沒事" or text.lower() == "等她起床"

    def on_enter_s2p2(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '已獲得「愛麗絲夢遊仙境」',
                actions = [
                    MessageAction(
                        label = '白雪公主',
                        text = '找白雪公主'
                    ),
                    MessageAction(
                        label = '凱妮絲',
                        text = '找凱妮絲'
                    ),
                    MessageAction(
                        label = '奶奶',
                        text = '找奶奶'
                    ),
                    MessageAction(
                        label = '其他人',
                        text = '找其他人'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## LRRH2
    def is_going_to_LRRH2(self, event):
        text = event.message.text
        return text.lower() == "找小紅帽"

    def on_enter_LRRH2(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picIRRH,
                title = '小紅帽',
                text = '(要問她什麼?)',
                actions = [
                    MessageAction(
                        label = '愛麗絲的枕頭',
                        text = '愛麗絲的枕頭'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_inLRRH2(self, event):
        text = event.message.text
        return text.lower() == "愛麗絲的枕頭"

    def on_enter_inLRRH2(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picIRRH,
                title = '小紅帽:',
                text = '不知道~~我昨天都沒有遇到愛莉絲阿!我昨天在家聽奶奶念故事書呢!然後唸著唸著我們就一起睡著了。',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## snow2
    def is_going_to_snow2(self, event):
        text = event.message.text
        return text.lower() == "找白雪公主"

    def on_enter_snow2(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSnow,
                title = '白雪公主:',
                text = '真是太瘋狂了!昨天那個瘋子突然就攻擊我們兩個。害我弄掉了一隻鞋子!希望能被王子撿到!',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## katniss2
    def is_going_to_katniss2(self, event):
        text = event.message.text
        return text.lower() == "找凱妮絲"

    def on_enter_katniss2(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picKatniss,
                title = '凱妮絲:',
                text = '我正忙打獵找食物呢!',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## wolf2
    def is_going_to_wolf2(self, event):
        text = event.message.text
        return text.lower() == "找大野狼"

    def on_enter_wolf2(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picWolf,
                title = '大野狼:',
                text = '要不要買保險阿!',
                actions = [
                    MessageAction(
                        label = '不要...',
                        text = '不要'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## match2
    def is_going_to_match2(self, event):
        text = event.message.text
        return text.lower() == "找賣火柴的小女孩"

    def on_enter_match2(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picMatch,
                title = '賣火柴的小女孩:',
                text = '我現在沒有火柴了下次再來吧。',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()
        
    ## baba2
    def is_going_to_baba2(self, event):
        text = event.message.text
        return text.lower() == "找奶奶"

    def on_enter_baba2(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picBaba,
                title = '奶奶:',
                text = '呼……呼……(睡覺中)',
                actions = [
                    MessageAction(
                        label = '(叫醒她)',
                        text = '叫醒'
                    ),
                    MessageAction(
                        label = '(等她起床再說好了)',
                        text = '等她起床'
                    ),
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## wake2
    def is_going_to_wake2(self, event):
        text = event.message.text
        return text.lower() == "叫醒"

    def on_enter_wake2(self, event):
        print("entering wake")
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picBaba,
                title = '奶奶:',
                text = '找我有什麼事嗎?',
                actions = [
                    MessageAction(
                        label = '沒事',
                        text = '沒事'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()



    # s3 ############################################################################################

    def is_going_to_s3(self, event):
        text = event.message.text
        return text.lower() == text.lower() == "不要" or text.lower() == "找其他人" or text.lower() == "..."

    def on_enter_s3(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '已獲得「愛麗絲夢遊仙境」',
                actions = [
                    MessageAction(
                        label = '小紅帽',
                        text = '找小紅帽'
                    ),
                    MessageAction(
                        label = '大野狼',
                        text = '找大野狼'
                    ),
                    MessageAction(
                        label = '賣火柴的小女孩',
                        text = '找賣火柴的小女孩'
                    ),
                    MessageAction(
                        label = '其他人',
                        text = '找其他人'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_s3p2(self, event):
        text = event.message.text
        return text.lower() == "找其他人" or text.lower() == "..." or text.lower() == "沒事" or text.lower() == "等她起床"

    def on_enter_s3p2(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '已獲得「愛麗絲夢遊仙境」',
                actions = [
                    MessageAction(
                        label = '白雪公主',
                        text = '找白雪公主'
                    ),
                    MessageAction(
                        label = '凱妮絲',
                        text = '找凱妮絲'
                    ),
                    MessageAction(
                        label = '奶奶',
                        text = '找奶奶'
                    ),
                    MessageAction(
                        label = '其他人',
                        text = '找其他人'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## LRRH3
    def is_going_to_LRRH3(self, event):
        text = event.message.text
        return text.lower() == "找小紅帽"

    def on_enter_LRRH3(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picIRRH,
                title = '小紅帽',
                text = '(要問她什麼?)',
                actions = [
                    MessageAction(
                        label = '愛麗絲的枕頭',
                        text = '愛麗絲的枕頭'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_inLRRH3(self, event):
        text = event.message.text
        return text.lower() == "愛麗絲的枕頭"

    def on_enter_inLRRH3(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picIRRH,
                title = '小紅帽:',
                text = '不知道~~我昨天都沒有遇到愛莉絲阿!我昨天在家聽奶奶念故事書呢!然後唸著唸著我們就一起睡著了。',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## snow3
    def is_going_to_snow3(self, event):
        text = event.message.text
        return text.lower() == "找白雪公主"

    def on_enter_snow3(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSnow,
                title = '白雪公主:',
                text = '真是太瘋狂了!昨天那個瘋子突然就攻擊我們兩個。害我弄掉了一隻鞋子!希望能被王子撿到!',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## katniss3
    def is_going_to_katniss3(self, event):
        text = event.message.text
        return text.lower() == "找凱妮絲"

    def on_enter_katniss3(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picKatniss,
                title = '凱妮絲:',
                text = '我正忙打獵找食物呢!',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## wolf3
    def is_going_to_wolf3(self, event):
        text = event.message.text
        return text.lower() == "找大野狼"

    def on_enter_wolf3(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picWolf,
                title = '大野狼:',
                text = '要不要買保險阿!',
                actions = [
                    MessageAction(
                        label = '不要...',
                        text = '不要'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## match3
    def is_going_to_match3(self, event):
        text = event.message.text
        return text.lower() == "找賣火柴的小女孩"

    def on_enter_match3(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picMatch,
                title = '賣火柴的小女孩:',
                text = '我現在沒有火柴了下次再來吧。',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()
        
    ## baba3
    def is_going_to_baba3(self, event):
        text = event.message.text
        return text.lower() == "找奶奶"

    def on_enter_baba3(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picBaba,
                title = '奶奶:',
                text = '呼……呼……(睡覺中)',
                actions = [
                    MessageAction(
                        label = '(叫醒她)',
                        text = '叫醒'
                    ),
                    MessageAction(
                        label = '(等她起床再說好了)',
                        text = '等她起床'
                    ),
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## wake3
    def is_going_to_wake3(self, event):
        text = event.message.text
        return text.lower() == "叫醒"

    def on_enter_wake3(self, event):
        print("entering wake2")
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picBaba,
                title = '奶奶:',
                text = '找我有什麼事嗎?',
                actions = [
                    MessageAction(
                        label = '沒事',
                        text = '沒事'
                    ),
                    MessageAction(
                        label = '昨天念給小紅帽聽的故事書',
                        text = '故事書'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## story3
    def is_going_to_story3(self, event):
        text = event.message.text
        return text.lower() == "故事書"

    def on_enter_story3(self, event):
        print("entering bedstory")
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picBaba,
                title = '奶奶:',
                text = '是這本吧!呵呵~~不過昨天念到一半我就突然睡著了呢!',
                actions = [
                    MessageAction(
                        label = '(獲得「賣火柴的小女孩」)',
                        text = '(獲得「賣火柴的小女孩」)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    # s4 ############################################################################################

    def is_going_to_s4(self, event):
        text = event.message.text
        return text.lower() == "(獲得「賣火柴的小女孩」)" or text.lower() == "不要" or text.lower() == "..."

    def on_enter_s4(self, event):
        print("entering match")
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '獲得「賣火柴的小女孩」',
                actions = [
                    MessageAction(
                        label = '賣火柴的小女孩',
                        text = '找賣火柴的小女孩'
                    ),
                    MessageAction(
                        label = '白雪公主',
                        text = '找白雪公主'
                    ),
                    MessageAction(
                        label = '大野狼',
                        text = '找大野狼'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## match4
    def is_going_to_match4(self, event):
        text = event.message.text
        return text.lower() == "找賣火柴的小女孩"

    def on_enter_match4(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picMatch,
                title = '賣火柴的小女孩',
                text = '(要問她什麼?)',
                actions = [
                    MessageAction(
                        label = '你願意回到書中嗎?',
                        text = '你願意回到書中嗎?'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_inMatch4(self, event):
        text = event.message.text
        return text.lower() == "你願意回到書中嗎?"

    def on_enter_inMatch4(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picMatch,
                title = '賣火柴的小女孩:',
                text = '我的火柴被搶了……如果找的回來我就回去。這個給妳當線索!',
                actions = [
                    MessageAction(
                        label = '(獲得紙條)',
                        text = '(獲得紙條)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## paper4
    def is_going_to_paper4(self, event):
        text = event.message.text
        return text.lower() == "(獲得紙條)"

    def on_enter_paper4(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picPaper,
                title = '紙條:',
                text = '19:00白雪跟愛莉絲在逛街，有人突然大喊「站住!我要殺了你!」愛莉絲丟下枕頭逃跑。\n枕頭被路過的奶奶撿走。',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## snow4
    def is_going_to_snow4(self, event):
        text = event.message.text
        return text.lower() == "找白雪公主"

    def on_enter_snow4(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSnow,
                title = '白雪公主:',
                text = '真是太瘋狂了!昨天那個瘋子突然就攻擊我們兩個。害我弄掉了一隻鞋子!希望能被王子撿到!',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## wolf 4
    def is_going_to_wolf4(self, event):
        text = event.message.text
        return text.lower() == "找大野狼"

    def on_enter_wolf4(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picWolf,
                title = '大野狼:',
                text = '要不要買保險阿!',
                actions = [
                    MessageAction(
                        label = '不要...',
                        text = '不要'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()
    


    # s5 ############################################################################################

    def is_going_to_s5(self, event):
        text = event.message.text
        return text.lower() == "..." or text.lower() == "還沒"

    def on_enter_s5(self, event):
        print("entering match")
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '獲得「紙條」',
                actions = [
                    MessageAction(
                        label = '賣火柴的小女孩',
                        text = '找賣火柴的小女孩'
                    ),
                    MessageAction(
                        label = '奶奶',
                        text = '找奶奶'
                    ),
                    MessageAction(
                        label = '愛麗絲',
                        text = '找愛麗絲'
                    ),
                    MessageAction(
                        label = '凱妮絲',
                        text = '找凱妮絲'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## baba5
    def is_going_to_baba5(self, event):
        text = event.message.text
        return text.lower() == "找奶奶"

    def on_enter_baba5(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picBaba,
                title = '奶奶',
                text = '(要問她什麼?)',
                actions = [
                    MessageAction(
                        label = '愛麗絲的枕頭',
                        text = '愛麗絲的枕頭'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_inBaba5(self, event):
        text = event.message.text
        return text.lower() == "愛麗絲的枕頭"

    def on_enter_inBaba5(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picBaba,
                title = '奶奶:',
                text = '對阿十年才出門一次的我居然走在路上就被枕頭打到了。這種東西我也不要了送你吧!',
                actions = [
                    MessageAction(
                        label = '(獲得枕頭)',
                        text = '(獲得枕頭)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## alice5
    def is_going_to_alice5(self, event):
        text = event.message.text
        return text.lower() == "找愛麗絲"

    def on_enter_alice5(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picAlice,
                title = '愛麗絲:',
                text = '沒有枕頭我不回去',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## match5
    def is_going_to_match5(self, event):
        text = event.message.text
        return text.lower() == "找賣火柴的小女孩"

    def on_enter_match5(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picMatch,
                title = '賣火柴的小女孩:',
                text = '你找到我的火柴了嗎?',
                actions = [
                    MessageAction(
                        label = '還沒',
                        text = '還沒'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## katniss5
    def is_going_to_katniss5(self, event):
        text = event.message.text
        return text.lower() == "找凱妮絲"

    def on_enter_katniss5(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picKatniss,
                title = '凱妮絲:',
                text = '我正忙打獵找食物呢!',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()



    # s6 ############################################################################################

    def is_going_to_s6(self, event):
        text = event.message.text
        return text.lower() == "(獲得枕頭)" or text.lower() == "..." or text.lower() == "真是謝了" or text.lower() == "還沒"

    def on_enter_s6(self, event):
        print("entering match")
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '獲得「枕頭」',
                actions = [
                    MessageAction(
                        label = '賣火柴的小女孩',
                        text = '找賣火柴的小女孩'
                    ),
                    MessageAction(
                        label = '凱妮絲',
                        text = '找凱妮絲'
                    ),
                    MessageAction(
                        label = '愛麗絲',
                        text = '找愛麗絲'
                    ),
                    MessageAction(
                        label = '老巫師',
                        text = '找老巫師'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## alice6
    def is_going_to_alice6(self, event):
        text = event.message.text
        return text.lower() == "找愛麗絲"

    def on_enter_alice6(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picAlice,
                title = '愛麗絲: ',
                text = '謝囉~不過回去之前我想吃點東西!呵呵~',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## katniss6
    def is_going_to_katniss6(self, event):
        text = event.message.text
        return text.lower() == "找凱妮絲"

    def on_enter_katniss6(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picKatniss,
                title = '凱妮絲:',
                text = '我正忙打獵找食物呢!',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## match6
    def is_going_to_match6(self, event):
        text = event.message.text
        return text.lower() == "找賣火柴的小女孩"

    def on_enter_match6(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picMatch,
                title = '賣火柴的小女孩:',
                text = '你找到我的火柴了嗎?',
                actions = [
                    MessageAction(
                        label = '還沒',
                        text = '還沒'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## wizard6
    def is_going_to_wizard6(self, event):
        text = event.message.text
        return text.lower() == "找老巫師"

    def on_enter_wizard6(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picWizard,
                title = '老巫師:',
                text = '加油',
                actions = [
                    MessageAction(
                        label = '真是謝了',
                        text = '真是謝了'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()



    # s7 ############################################################################################

    def is_going_to_s7(self, event):
        text = event.message.text
        return text.lower() == "..." or text.lower() == "不要"

    def on_enter_s7(self, event):
        print("entering match")
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '獲得「枕頭」',
                actions = [
                    MessageAction(
                        label = '大野狼',
                        text = '找大野狼'
                    ),
                    MessageAction(
                        label = '小紅帽',
                        text = '找小紅帽'
                    ),
                    MessageAction(
                        label = '凱妮絲',
                        text = '找凱妮絲'
                    ),
                    MessageAction(
                        label = '白雪公主',
                        text = '找白雪公主'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## wolf7
    def is_going_to_wolf7(self, event):
        text = event.message.text
        return text.lower() == "找大野狼"

    def on_enter_wolf7(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picWolf,
                title = '大野狼:',
                text = '要不要買保險阿!',
                actions = [
                    MessageAction(
                        label = '不要...',
                        text = '不要'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## snow7
    def is_going_to_snow7(self, event):
        text = event.message.text
        return text.lower() == "找白雪公主"

    def on_enter_snow7(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSnow,
                title = '白雪公主',
                text = '(要問她什麼?)',
                actions = [
                    MessageAction(
                        label = '妳有食物嗎?',
                        text = '妳有食物嗎?'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_inSnow7(self, event):
        text = event.message.text
        return text.lower() == "妳有食物嗎?"

    def on_enter_inSnow7(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSnow,
                title = '白雪公主:',
                text = '我本來有蘋果的~~可是不小心被我弄掉了!',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## LRRH7
    def is_going_to_LRRH7(self, event):
        text = event.message.text
        return text.lower() == "找小紅帽"

    def on_enter_LRRH7(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picIRRH,
                title = '小紅帽',
                text = '(要問她什麼?)',
                actions = [
                    MessageAction(
                        label = '妳有食物嗎?',
                        text = '妳有食物嗎?'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_inLRRH7(self, event):
        text = event.message.text
        return text.lower() == "妳有食物嗎?"

    def on_enter_inLRRH7(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picIRRH,
                title = '小紅帽:',
                text = '我有好吃的三明治呢!送你吧',
                actions = [
                    MessageAction(
                        label = '(收下三明治)',
                        text = '(收下三明治)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ### sandwich7
    def is_going_to_sandwich7(self, event):
        text = event.message.text
        return text.lower() == "(收下三明治)"

    def on_enter_sandwich7(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '獲得「三明治」',
                actions = [
                    MessageAction(
                        label = '去找愛麗絲',
                        text = '找愛麗絲'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_inSandwich7(self, event):
        text = event.message.text
        return text.lower() == "找愛麗絲"

    def on_enter_inSandwich7(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picAlice,
                title = '愛麗絲:',
                text = '你有食物了嗎',
                actions = [
                    MessageAction(
                        label = '(給她三明治)',
                        text = '(給她三明治)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ### Alice FAIL
    def is_going_to_aliceFail(self, event):
        text = event.message.text
        return text.lower() == "(給她三明治)"

    def on_enter_aliceFail(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picFail,
                title = '愛麗絲線失敗',
                text = '三明治有毒，愛莉絲食用三明治後死亡。',
                actions = [
                    MessageAction(
                        label = '確認',
                        text = '確認'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## katniss7
    def is_going_to_katniss7(self, event):
        text = event.message.text
        return text.lower() == "找凱妮絲"

    def on_enter_katniss7(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picKatniss,
                title = '凱妮絲',
                text = '(要問她什麼?)',
                actions = [
                    MessageAction(
                        label = '妳有食物嗎?',
                        text = '妳有食物嗎?'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_inKatniss7(self, event):
        text = event.message.text
        return text.lower() == "妳有食物嗎?"

    def on_enter_inKatniss7(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picKatniss,
                title = '凱妮絲:',
                text = '我只有這個肉，還有我昨天獵到的爛蘋果',
                actions = [
                    MessageAction(
                        label = '(收下「好吃的肉」)',
                        text = '(收下「好吃的肉」)'
                    ),
                    MessageAction(
                        label = '(收下「爛蘋果」)',
                        text = '(收下「爛蘋果」)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ### apple7
    def is_going_to_apple7(self, event):
        text = event.message.text
        return text.lower() == "(收下「爛蘋果」)"

    def on_enter_apple7(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '獲得「爛蘋果」',
                actions = [
                    MessageAction(
                        label = '去找愛麗絲',
                        text = '找愛麗絲'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_inApple7(self, event):
        text = event.message.text
        return text.lower() == "找愛麗絲"

    def on_enter_inApple7(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picAlice,
                title = '愛麗絲:',
                text = '你有食物了嗎',
                actions = [
                    MessageAction(
                        label = '(給她爛蘋果)',
                        text = '(給她爛蘋果)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ### alice SUCCEESS
    def is_going_to_aliceSuc(self, event):
        text = event.message.text
        return text.lower() == "(給她爛蘋果)"

    def on_enter_aliceSuc(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picAlice,
                title = '愛麗絲線成功',
                text = '愛莉絲:謝囉~~\n簽名後回到書中',
                actions = [
                    MessageAction(
                        label = '確認',
                        text = '確認'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ### meat7
    def is_going_to_meat7(self, event):
        text = event.message.text
        return text.lower() == "(收下「好吃的肉」)"

    def on_enter_meat7(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '獲得「好吃的肉」',
                actions = [
                    MessageAction(
                        label = '愛麗絲',
                        text = '找愛麗絲'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_inMeat7(self, event):
        text = event.message.text
        return text.lower() == "找愛麗絲"

    def on_enter_inMeat7(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picAlice,
                title = '愛麗絲:',
                text = '你有食物了嗎',
                actions = [
                    MessageAction(
                        label = '(給她好吃的肉)',
                        text = '(給她好吃的肉)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    #### reject7
    def is_going_to_reject7(self, event):
        text = event.message.text
        return text.lower() == "(給她好吃的肉)"

    def on_enter_reject7(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picAlice,
                title = '愛麗絲:',
                text = '我吃素的阿你不知道嗎?',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()



    # s8 ############################################################################################

    def is_going_to_s8(self, event):
        text = event.message.text
        return text.lower() == "確認" or text.lower() == "..." or text.lower() == "還沒" 

    def on_enter_s8(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = ' ',
                actions = [
                    MessageAction(
                        label = '奶奶',
                        text = '找奶奶'
                    ),
                    MessageAction(
                        label = '老巫師',
                        text = '找老巫師'
                    ),
                    MessageAction(
                        label = '賣火柴的小女孩',
                        text = '找賣火柴的小女孩'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()
        
    ## match8
    def is_going_to_match8(self, event):
        text = event.message.text
        return text.lower() == "找賣火柴的小女孩"

    def on_enter_match8(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picMatch,
                title = '賣火柴的小女孩:',
                text = '你找到我的火柴了嗎?',
                actions = [
                    MessageAction(
                        label = '還沒',
                        text = '還沒'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## baba8
    def is_going_to_baba8(self, event):
        text = event.message.text
        return text.lower() == "找奶奶"

    def on_enter_baba8(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picBaba,
                title = '奶奶:',
                text = '好期待孫女的點心呢!',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## wizard8
    def is_going_to_wizard8(self, event):
        text = event.message.text
        return text.lower() == "找老巫師"

    def on_enter_wizard8(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picWizard,
                title = '老巫師:',
                text = '我有新線索了呢!還有這是昨天現場留下來的!',
                actions = [
                    MessageAction(
                        label = '(獲得「箭矢」)',
                        text = '(獲得「箭矢」)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()



    # s9 ############################################################################################

    def is_going_to_s9(self, event):
        text = event.message.text
        return text.lower() == "(獲得「箭矢」)" or text.lower() == "..." or text.lower() == "不要" 

    def on_enter_s9(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '獲得「箭矢」',
                actions = [
                    MessageAction(
                        label = '大野狼',
                        text = '找大野狼'
                    ),
                    MessageAction(
                        label = '凱妮絲',
                        text = '找凱妮絲'
                    ),
                    MessageAction(
                        label = '奶奶',
                        text = '找奶奶'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()
        
    ## wolf9
    def is_going_to_wolf9(self, event):
        text = event.message.text
        return text.lower() == "找大野狼"

    def on_enter_wolf9(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picWolf,
                title = '大野狼:',
                text = '要不要買保險呢!',
                actions = [
                    MessageAction(
                        label = '不要...',
                        text = '不要'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## baba9
    def is_going_to_baba9(self, event):
        text = event.message.text
        return text.lower() == "找奶奶"

    def on_enter_baba9(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picBaba,
                title = '奶奶:',
                text = '好期待孫女的點心呢!',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## katniss9
    def is_going_to_katniss9(self, event):
        text = event.message.text
        return text.lower() == "找凱妮絲"

    def on_enter_katniss9(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picKatniss,
                title = '凱妮絲',
                text = '(要問她什麼?)',
                actions = [
                    MessageAction(
                        label = '箭矢',
                        text = '箭矢'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_inKatniss9(self, event):
        text = event.message.text
        return text.lower() == "箭矢"

    def on_enter_inKatniss9(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picKatniss,
                title = '凱妮絲:',
                text = '我要殺了Snow(史諾)!',
                actions = [
                    MessageAction(
                        label = '(獲得「白雪公主」)',
                        text = '(獲得「白雪公主」)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()



    # s10 ############################################################################################

    def is_going_to_s10(self, event):
        text = event.message.text
        return text.lower() == "(獲得「白雪公主」)" or text.lower() == "..." or text.lower() == "不要" or text.lower() == "還沒"

    def on_enter_s10(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '獲得「白雪公主」',
                actions = [
                    MessageAction(
                        label = '大野狼',
                        text = '找大野狼'
                    ),
                    MessageAction(
                        label = '奶奶',
                        text = '找奶奶'
                    ),
                    MessageAction(
                        label = '白雪公主',
                        text = '找白雪公主'
                    ),
                    MessageAction(
                        label = '賣火柴的小女孩',
                        text = '找賣火柴的小女孩'
                    )

                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()
        
    ## wolf10
    def is_going_to_wolf10(self, event):
        text = event.message.text
        return text.lower() == "找大野狼"

    def on_enter_wolf10(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picWolf,
                title = '大野狼:',
                text = '要不要買保險呢!',
                actions = [
                    MessageAction(
                        label = '不要...',
                        text = '不要'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## baba10
    def is_going_to_baba10(self, event):
        text = event.message.text
        return text.lower() == "找奶奶"

    def on_enter_baba10(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picBaba,
                title = '奶奶:',
                text = '好期待孫女的點心呢!',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## match10
    def is_going_to_match10(self, event):
        text = event.message.text
        return text.lower() == "找賣火柴的小女孩"

    def on_enter_match10(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picMatch,
                title = '賣火柴的小女孩:',
                text = '你找到我的火柴了嗎?',
                actions = [
                    MessageAction(
                        label = '還沒',
                        text = '還沒'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## snow10
    def is_going_to_snow10(self, event):
        text = event.message.text
        return text.lower() == "找白雪公主"

    def on_enter_snow10(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSnow,
                title = '白雪公主',
                text = '(要問她什麼?)',
                actions = [
                    MessageAction(
                        label = '妳願意回到書中嗎?',
                        text = '妳願意回到書中嗎?'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_inSnow10(self, event):
        text = event.message.text
        return text.lower() == "妳願意回到書中嗎?"

    def on_enter_inSnow10(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSnow,
                title = '白雪公主:如果解開誤會我就回去。',
                text = '你去找證據啦!對了我昨晚看到小紅帽在撕牆上的通緝單喔!那應該能用，記得拿給凱妮絲看喔!',
                actions = [
                    MessageAction(
                        label = '(尋找通緝單)',
                        text = '(尋找通緝單)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()



    # s11 ############################################################################################

    def is_going_to_s11(self, event):
        text = event.message.text
        return text.lower() == "(尋找通緝單)" or text.lower() == "..." or text.lower() == "還沒"

    def on_enter_s11(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '獲得「白雪公主」',
                actions = [
                    MessageAction(
                        label = '凱妮絲',
                        text = '找凱妮絲'
                    ),
                    MessageAction(
                        label = '奶奶',
                        text = '找奶奶'
                    ),
                    MessageAction(
                        label = '小紅帽',
                        text = '找小紅帽'
                    ),
                    MessageAction(
                        label = '賣火柴的小女孩',
                        text = '找賣火柴的小女孩'
                    )

                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()
        
    ## katniss11
    def is_going_to_katniss11(self, event):
        text = event.message.text
        return text.lower() == "找凱妮絲"

    def on_enter_katniss11(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picKatniss,
                title = '凱妮絲:',
                text = '我恨你……史諾!',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## baba11
    def is_going_to_baba11(self, event):
        text = event.message.text
        return text.lower() == "找奶奶"

    def on_enter_baba11(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picBaba,
                title = '奶奶:',
                text = '好期待孫女的點心呢!',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## match11
    def is_going_to_match11(self, event):
        text = event.message.text
        return text.lower() == "找賣火柴的小女孩"

    def on_enter_match11(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picMatch,
                title = '賣火柴的小女孩:',
                text = '你找到我的火柴了嗎?',
                actions = [
                    MessageAction(
                        label = '還沒',
                        text = '還沒'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## LRRH11
    def is_going_to_LRRH11(self, event):
        text = event.message.text
        return text.lower() == "找小紅帽"

    def on_enter_LRRH11(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picIRRH,
                title = '小紅帽',
                text = '(要問她什麼?)',
                actions = [
                    MessageAction(
                        label = '通緝單',
                        text = '通緝單'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_inLRRH11(self, event):
        text = event.message.text
        return text.lower() == "通緝單"

    def on_enter_inLRRH11(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picIRRH,
                title = '小紅帽:',
                text = '有阿!給你吧',
                actions = [
                    MessageAction(
                        label = '(獲得「通緝單」)',
                        text = '(獲得「通緝單」)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()



    # s12 ############################################################################################

    def is_going_to_s12(self, event):
        text = event.message.text
        return text.lower() == "(獲得「通緝單」)" or text.lower() == "..." or text.lower() == "還沒"

    def on_enter_s12(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '獲得「通緝單」',
                actions = [
                    MessageAction(
                        label = '凱妮絲',
                        text = '找凱妮絲'
                    ),
                    MessageAction(
                        label = '奶奶',
                        text = '找奶奶'
                    ),
                    MessageAction(
                        label = '小紅帽',
                        text = '找小紅帽'
                    ),
                    MessageAction(
                        label = '賣火柴的小女孩',
                        text = '找賣火柴的小女孩'
                    )

                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()
        
    ## baba12
    def is_going_to_baba12(self, event):
        text = event.message.text
        return text.lower() == "找奶奶"

    def on_enter_baba12(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picBaba,
                title = '奶奶:',
                text = '好期待孫女的點心呢!',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## match12
    def is_going_to_match12(self, event):
        text = event.message.text
        return text.lower() == "找賣火柴的小女孩"

    def on_enter_match12(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picMatch,
                title = '賣火柴的小女孩:',
                text = '你找到我的火柴了嗎?',
                actions = [
                    MessageAction(
                        label = '還沒',
                        text = '還沒'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## LRRH12
    def is_going_to_LRRH12(self, event):
        text = event.message.text
        return text.lower() == "找小紅帽"

    def on_enter_LRRH12(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picIRRH,
                title = '找小紅帽',
                text = '(要問她什麼?)',
                actions = [
                    MessageAction(
                        label = '通緝單很可疑',
                        text = '通緝單很可疑'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_inLRRH12(self, event):
        text = event.message.text
        return text.lower() == "通緝單很可疑"

    def on_enter_inLRRH12(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picIRRH,
                title = '小紅帽:',
                text = '啊!不小心拿錯了，哈哈!',
                actions = [
                    MessageAction(
                        label = '(獲得「通緝單」)',
                        text = '(獲得「通緝單」)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## katniss12
    def is_going_to_katniss12(self, event):
        text = event.message.text
        return text.lower() == "找凱妮絲"

    def on_enter_katniss12(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picKatniss,
                title = '凱妮絲',
                text = '(要問她什麼?)',
                actions = [
                    MessageAction(
                        label = '通緝單',
                        text = '通緝單'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_inKatniss12(self, event):
        text = event.message.text
        return text.lower() == "通緝單"

    def on_enter_inKatniss12(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picKatniss,
                title = '凱妮絲:',
                text = '那妳幫我拿這個蘋果給白雪說我誤會她了!',
                actions = [
                    MessageAction(
                        label = '(獲得「蘋果」)',
                        text = '(獲得「蘋果」)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ### poison apple
    def is_going_to_apple12(self, event):
        text = event.message.text
        return text.lower() == "(獲得「蘋果」)"

    def on_enter_apple12(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '獲得「蘋果」',
                actions = [
                    MessageAction(
                        label = '白雪公主',
                        text = '找白雪公主'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ### snow FAIL
    def is_going_to_snowFail(self, event):
        text = event.message.text
        return text.lower() == "找白雪公主"

    def on_enter_snowFail(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picFail,
                title = '白雪公主線失敗',
                text = '蘋果是有毒的',
                actions = [
                    MessageAction(
                        label = '確認',
                        text = '確認'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()



    # s13 ############################################################################################

    def is_going_to_s13(self, event):
        text = event.message.text
        return text.lower() == "(獲得「通緝單」)" or text.lower() == "..." or text.lower() == "還沒"

    def on_enter_s13(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '獲得「通緝單」',
                actions = [
                    MessageAction(
                        label = '凱妮絲',
                        text = '找凱妮絲'
                    ),
                    MessageAction(
                        label = '奶奶',
                        text = '找奶奶'
                    ),
                    MessageAction(
                        label = '小紅帽',
                        text = '找小紅帽'
                    ),
                    MessageAction(
                        label = '賣火柴的小女孩',
                        text = '找賣火柴的小女孩'
                    )

                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()
        
    ## baba13
    def is_going_to_baba13(self, event):
        text = event.message.text
        return text.lower() == "找奶奶"

    def on_enter_baba13(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picBaba,
                title = '奶奶:',
                text = '好期待孫女的點心呢!',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## match13
    def is_going_to_match13(self, event):
        text = event.message.text
        return text.lower() == "找賣火柴的小女孩"

    def on_enter_match13(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picMatch,
                title = '賣火柴的小女孩:',
                text = '你找到我的火柴了嗎?',
                actions = [
                    MessageAction(
                        label = '還沒',
                        text = '還沒'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## LRRH13
    def is_going_to_LRRH13(self, event):
        text = event.message.text
        return text.lower() == "找小紅帽"

    def on_enter_LRRH13(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picIRRH,
                title = '小紅帽:',
                text = '這次真的沒問題了啦',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## katniss13
    def is_going_to_katniss13(self, event):
        text = event.message.text
        return text.lower() == "找凱妮絲"

    def on_enter_katniss13(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picKatniss,
                title = '凱妮絲',
                text = '(要問她什麼?)',
                actions = [
                    MessageAction(
                        label = '通緝單',
                        text = '通緝單'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_inKatniss13(self, event):
        text = event.message.text
        return text.lower() == "通緝單"

    def on_enter_inKatniss13(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picKatniss,
                title = '凱妮絲:',
                text = '謝謝啦~原來是我誤會了，拿這個蘋果給白雪幫我道歉吧!',
                actions = [
                    MessageAction(
                        label = '(獲得「蘋果」)',
                        text = '(獲得「蘋果」)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ### apple
    def is_going_to_apple13(self, event):
        text = event.message.text
        return text.lower() == "(獲得「蘋果」)"

    def on_enter_apple13(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '獲得「蘋果」',
                actions = [
                    MessageAction(
                        label = '白雪公主',
                        text = '找白雪公主'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ### snow SUCCESS
    def is_going_to_snowSuc(self, event):
        text = event.message.text
        return text.lower() == "找白雪公主"

    def on_enter_snowSuc(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSuccess,
                title = '白雪公主線成功',
                text = '簽名回書中，白雪篇完成',
                actions = [
                    MessageAction(
                        label = '確認',
                        text = '確認'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    

    # s14 ############################################################################################

    def is_going_to_s14(self, event):
        text = event.message.text
        return text.lower() == "確認" or text.lower() == "..." or text.lower() == "還沒"

    def on_enter_s14(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = ' ',
                actions = [
                    MessageAction(
                        label = '賣火柴的小女孩',
                        text = '找賣火柴的小女孩'
                    ),
                    MessageAction(
                        label = '奶奶',
                        text = '找奶奶'
                    ),
                    MessageAction(
                        label = '老巫師',
                        text = '找老巫師'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## baba14
    def is_going_to_baba14(self, event):
        text = event.message.text
        return text.lower() == "找奶奶"

    def on_enter_baba14(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picBaba,
                title = '奶奶:',
                text = '好期待孫女的點心呢!',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## match14
    def is_going_to_match14(self, event):
        text = event.message.text
        return text.lower() == "找賣火柴的小女孩"

    def on_enter_match14(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picMatch,
                title = '賣火柴的小女孩:',
                text = '你找到我的火柴了嗎?',
                actions = [
                    MessageAction(
                        label = '還沒',
                        text = '還沒'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## wizard14
    def is_going_to_wizard14(self, event):
        text = event.message.text
        return text.lower() == "找老巫師"

    def on_enter_wizard14(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picWizard,
                title = '老巫師:',
                text = '這是我剛剛找到的，給你吧',
                actions = [
                    MessageAction(
                        label = '(獲得「飢餓遊戲」)',
                        text = '(獲得「飢餓遊戲」)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()



    # s15 ############################################################################################

    def is_going_to_s15(self, event):
        text = event.message.text
        return text.lower() == "(獲得「飢餓遊戲」)" or text.lower() == "..." or text.lower() == "還沒"

    def on_enter_s15(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '獲得「飢餓遊戲」',
                actions = [
                    MessageAction(
                        label = '賣火柴的小女孩',
                        text = '找賣火柴的小女孩'
                    ),
                    MessageAction(
                        label = '奶奶',
                        text = '找奶奶'
                    ),
                    MessageAction(
                        label = '凱妮絲',
                        text = '找凱妮絲'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## baba15
    def is_going_to_baba15(self, event):
        text = event.message.text
        return text.lower() == "找奶奶"

    def on_enter_baba15(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picBaba,
                title = '奶奶:',
                text = '好期待孫女的點心呢!',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## match15
    def is_going_to_match15(self, event):
        text = event.message.text
        return text.lower() == "找賣火柴的小女孩"

    def on_enter_match15(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picMatch,
                title = '賣火柴的小女孩:',
                text = '你找到我的火柴了嗎?',
                actions = [
                    MessageAction(
                        label = '還沒',
                        text = '還沒'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## katniss15
    def is_going_to_katniss15(self, event):
        text = event.message.text
        return text.lower() == "找凱妮絲"

    def on_enter_katniss15(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picKatniss,
                title = '凱妮絲',
                text = '(要問她什麼?)',
                actions = [
                    MessageAction(
                        label = '妳願意回到書中嗎',
                        text = '妳願意回到書中嗎'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_inKatniss15(self, event):
        text = event.message.text
        return text.lower() == "妳願意回到書中嗎"

    def on_enter_inKatniss15(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picKatniss,
                title = '凱妮絲:',
                text = '我一生中都活在仇恨中，我唯一的願望就是得到來自小女孩的禮物，她們總是讓我想到小櫻。',
                actions = [
                    MessageAction(
                        label = '(找禮物)',
                        text = '(找禮物)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()



    # s16 ############################################################################################

    def is_going_to_s16(self, event):
        text = event.message.text
        return text.lower() == "(找禮物)" or text.lower() == "..." or text.lower() == "不要" or text.lower() == "還沒"

    def on_enter_s16(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = ' ',
                actions = [
                    MessageAction(
                        label = '賣火柴的小女孩',
                        text = '找賣火柴的小女孩'
                    ),
                    MessageAction(
                        label = '大野狼',
                        text = '找大野狼'
                    ),
                    MessageAction(
                        label = '小紅帽',
                        text = '找小紅帽'
                    ),
                    MessageAction(
                        label = '凱妮絲',
                        text = '找凱妮絲'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## match16
    def is_going_to_match16(self, event):
        text = event.message.text
        return text.lower() == "找賣火柴的小女孩"

    def on_enter_match16(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picMatch,
                title = '賣火柴的小女孩:',
                text = '你找到我的火柴了嗎?',
                actions = [
                    MessageAction(
                        label = '還沒',
                        text = '還沒'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## wolf16
    def is_going_to_wolf16(self, event):
        text = event.message.text
        return text.lower() == "找大野狼"

    def on_enter_wolf16(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picWolf,
                title = '大野狼:',
                text = '要不要買保險呢!',
                actions = [
                    MessageAction(
                        label = '不要...',
                        text = '不要'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## katniss16
    def is_going_to_katniss16(self, event):
        text = event.message.text
        return text.lower() == "找凱妮絲"

    def on_enter_katniss16(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picKatniss,
                title = '凱妮絲:',
                text = '我一生中都活在仇恨中，我唯一的願望就是得到來自小女孩的禮物，她們總是讓我想到小櫻。',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## LRRH16
    def is_going_to_LRRH16(self, event):
        text = event.message.text
        return text.lower() == "找小紅帽"

    def on_enter_LRRH16(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picIRRH,
                title = '小紅帽',
                text = '(要問她什麼?)',
                actions = [
                    MessageAction(
                        label = '禮物',
                        text = '禮物'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_inLRRH16(self, event):
        text = event.message.text
        return text.lower() == "禮物"

    def on_enter_inLRRH16(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picIRRH,
                title = '小紅帽:',
                text = '有阿我有禮物要給凱妮絲姊姊呢!有兩種喔',
                actions = [
                    MessageAction(
                        label = '(花錢買禮物)',
                        text = '(花錢買禮物)'
                    ),
                    MessageAction(
                        label = '(拿免費的禮物)',
                        text = '(拿免費的禮物)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ### bomb16
    def is_going_to_bomb16(self, event):
        text = event.message.text
        return text.lower() == "(花錢買禮物)"

    def on_enter_bomb16(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '獲得「禮物」',
                actions = [
                    MessageAction(
                        label = '凱妮絲',
                        text = '找凱妮絲'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_inBomb16(self, event):
        text = event.message.text
        return text.lower() == "找凱妮絲"

    def on_enter_inBomb16(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picKatniss,
                title = '凱妮絲',
                text = '(要問她什麼?)',
                actions = [
                    MessageAction(
                        label = '禮物',
                        text = '禮物'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ### katniss FAIL
    def is_going_to_katnissFail(self, event):
        text = event.message.text
        return text.lower() == "禮物"

    def on_enter_katnissFail(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picFail,
                title = '凱妮絲線失敗',
                text = '禮物是炸彈，凱妮絲被炸死',
                actions = [
                    MessageAction(
                        label = '確認',
                        text = '確認'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.game_over()

    ### gift16
    def is_going_to_gift16(self, event):
        text = event.message.text
        return text.lower() == "(拿免費的禮物)"

    def on_enter_gift16(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '獲得「禮物」',
                actions = [
                    MessageAction(
                        label = '凱妮絲',
                        text = '找凱妮絲'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_inGift16(self, event):
        text = event.message.text
        return text.lower() == "找凱妮絲"

    def on_enter_inGift16(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picKatniss,
                title = '凱妮絲',
                text = '(要問她什麼?)',
                actions = [
                    MessageAction(
                        label = '禮物',
                        text = '禮物'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ### pic16
    def is_going_to_pic16(self, event):
        text = event.message.text
        return text.lower() == "禮物"

    def on_enter_pic16(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picKatniss,
                title = '凱妮絲:',
                text = '謝謝你囉!這是給你的禮物',
                actions = [
                    MessageAction(
                        label = '(獲得「照片」)',
                        text = '(獲得「照片」)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_inPic16(self, event):
        text = event.message.text
        return text.lower() == "(獲得「照片」)"

    def on_enter_inPic16(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picPhoto,
                title = '照片:',
                text = '(小紅帽搶走小女孩的火柴)',
                actions = [
                    MessageAction(
                        label = '繼續',
                        text = '繼續'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ### katniss SUCCESS
    def is_going_to_katnissSuc(self, event):
        text = event.message.text
        return text.lower() == "繼續"

    def on_enter_katnissSuc(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSuccess,
                title = '凱妮絲線成功',
                text = '簽名回到書中，凱妮絲篇成功',
                actions = [
                    MessageAction(
                        label = '確認',
                        text = '確認'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    

    # s17 ############################################################################################

    def is_going_to_s17(self, event):
        text = event.message.text
        return text.lower() == "確認" or text.lower() == "..." or text.lower() == "不要" or text.lower() == "還沒"

    def on_enter_s17(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '獲得「照片」',
                actions = [
                    MessageAction(
                        label = '賣火柴的小女孩',
                        text = '找賣火柴的小女孩'
                    ),
                    MessageAction(
                        label = '大野狼',
                        text = '找大野狼'
                    ),
                    MessageAction(
                        label = '小紅帽',
                        text = '找小紅帽'
                    ),
                    MessageAction(
                        label = '奶奶',
                        text = '找奶奶'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## match17
    def is_going_to_match17(self, event):
        text = event.message.text
        return text.lower() == "找賣火柴的小女孩"

    def on_enter_match17(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picMatch,
                title = '賣火柴的小女孩:',
                text = '你找到我的火柴了嗎?',
                actions = [
                    MessageAction(
                        label = '還沒',
                        text = '還沒'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## wolf17
    def is_going_to_wolf17(self, event):
        text = event.message.text
        return text.lower() == "找大野狼"

    def on_enter_wolf17(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picWolf,
                title = '大野狼:',
                text = '要不要買保險呢!',
                actions = [
                    MessageAction(
                        label = '不要...',
                        text = '不要'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## baba17
    def is_going_to_baba17(self, event):
        text = event.message.text
        return text.lower() == "找奶奶"

    def on_enter_baba17(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picBaba,
                title = '奶奶:',
                text = '好期待孫女的點心呢!',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## LRRH17
    def is_going_to_LRRH17(self, event):
        text = event.message.text
        return text.lower() == "找小紅帽"

    def on_enter_LRRH17(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picIRRH,
                title = '小紅帽',
                text = '(要問她什麼?)',
                actions = [
                    MessageAction(
                        label = '火柴',
                        text = '火柴'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_inLRRH17(self, event):
        text = event.message.text
        return text.lower() == "火柴"

    def on_enter_inLRRH17(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picIRRH,
                title = '小紅帽:',
                text = '是唷!火柴在我手上，裝在這個信封裡',
                actions = [
                    MessageAction(
                        label = '(獲得「信封」)',
                        text = '(獲得「信封」)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()



    # s18 ############################################################################################

    def is_going_to_s18(self, event):
        text = event.message.text
        return text.lower() == "(獲得「信封」)" or text.lower() == "..." or text.lower() == "不要"

    def on_enter_s18(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '獲得「信封袋」',
                actions = [
                    MessageAction(
                        label = '賣火柴的小女孩',
                        text = '找賣火柴的小女孩'
                    ),
                    MessageAction(
                        label = '大野狼',
                        text = '找大野狼'
                    ),
                    MessageAction(
                        label = '小紅帽',
                        text = '找小紅帽'
                    ),
                    MessageAction(
                        label = '奶奶',
                        text = '找奶奶'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## match18
    def is_going_to_match18(self, event):
        text = event.message.text
        return text.lower() == "找賣火柴的小女孩"

    def on_enter_match18(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picMatch,
                title = '賣火柴的小女孩:',
                text = '你找到我的火柴了嗎?',
                actions = [
                    MessageAction(
                        label = '(把信封給她)',
                        text = '(把信封給她)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## match FAIL
    def is_going_to_matchFail(self, event):
        text = event.message.text
        return text.lower() == "(把信封給她)"

    def on_enter_matchFail(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picFail,
                title = '賣火柴的小女孩線失敗',
                text = '信封中是炸藥，賣火柴的小女孩死亡',
                actions = [
                    MessageAction(
                        label = '確認',
                        text = '確認'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.game_over()

    ## wolf18
    def is_going_to_wolf18(self, event):
        text = event.message.text
        return text.lower() == "找大野狼"

    def on_enter_wolf18(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picWolf,
                title = '大野狼:',
                text = '要不要買保險呢!',
                actions = [
                    MessageAction(
                        label = '不要...',
                        text = '不要'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## baba18
    def is_going_to_baba18(self, event):
        text = event.message.text
        return text.lower() == "找奶奶"

    def on_enter_baba18(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picBaba,
                title = '奶奶:',
                text = '好期待孫女的點心呢!',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## LRRH18
    def is_going_to_LRRH18(self, event):
        text = event.message.text
        return text.lower() == "找小紅帽"

    def on_enter_LRRH18(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picIRRH,
                title = '小紅帽',
                text = '(要問她什麼?)',
                actions = [
                    MessageAction(
                        label = '信封裡面裝的是炸藥',
                        text = '信封裡面裝的是炸藥'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_inLRRH18(self, event):
        text = event.message.text
        return text.lower() == "信封裡面裝的是炸藥"

    def on_enter_inLRRH18(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picIRRH,
                title = '小紅帽:',
                text = '哎呀~~我真是冒失呢!這個才對!',
                actions = [
                    MessageAction(
                        label = '(獲得「信封」)',
                        text = '(獲得「信封」)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()



    # s19 ############################################################################################

    def is_going_to_s19(self, event):
        text = event.message.text
        return text.lower() == "(獲得「信封」)" or text.lower() == "..." or text.lower() == "不要"

    def on_enter_s19(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '獲得「信封袋」',
                actions = [
                    MessageAction(
                        label = '賣火柴的小女孩',
                        text = '找賣火柴的小女孩'
                    ),
                    MessageAction(
                        label = '大野狼',
                        text = '找大野狼'
                    ),
                    MessageAction(
                        label = '小紅帽',
                        text = '找小紅帽'
                    ),
                    MessageAction(
                        label = '奶奶',
                        text = '找奶奶'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## match18
    def is_going_to_match19(self, event):
        text = event.message.text
        return text.lower() == "找賣火柴的小女孩"

    def on_enter_match19(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picMatch,
                title = '賣火柴的小女孩:',
                text = '你找到我的火柴了嗎?',
                actions = [
                    MessageAction(
                        label = '(把信封給她)',
                        text = '(把信封給她)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_book19(self, event):
        text = event.message.text
        return text.lower() == "(把信封給她)"

    def on_enter_book19(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picMatch,
                title = '賣火柴的小女孩:',
                text = '謝囉!這是給你的禮物!',
                actions = [
                    MessageAction(
                        label = '(獲得「小紅帽」)',
                        text = '(獲得「小紅帽」)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ### match SUCCESS
    def is_going_to_matchSuc(self, event):
        text = event.message.text
        return text.lower() == "(獲得「小紅帽」)"

    def on_enter_matchSuc(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSuccess,
                title = '賣火柴的小女孩線成功',
                text = '賣火柴的小女孩簽名回到書中，任務成功。',
                actions = [
                    MessageAction(
                        label = '確認',
                        text = '確認'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## wolf19
    def is_going_to_wolf19(self, event):
        text = event.message.text
        return text.lower() == "找大野狼"

    def on_enter_wolf19(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picWolf,
                title = '大野狼:',
                text = '要不要買保險呢!',
                actions = [
                    MessageAction(
                        label = '不要...',
                        text = '不要'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## baba19
    def is_going_to_baba19(self, event):
        text = event.message.text
        return text.lower() == "找奶奶"

    def on_enter_baba19(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picBaba,
                title = '奶奶:',
                text = '好期待孫女的點心呢!',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## LRRH19
    def is_going_to_LRRH19(self, event):
        text = event.message.text
        return text.lower() == "找小紅帽"

    def on_enter_LRRH19(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picIRRH,
                title = '小紅帽:',
                text = '這次沒搞錯了啦!',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()



    # s20 ############################################################################################

    def is_going_to_s20(self, event):
        text = event.message.text
        return text.lower() == "確認" or text.lower() == "..." or text.lower() == "沒錢"

    def on_enter_s20(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '獲得「小紅帽」',
                actions = [
                    MessageAction(
                        label = '大野狼',
                        text = '找大野狼'
                    ),
                    MessageAction(
                        label = '小紅帽',
                        text = '找小紅帽'
                    ),
                    MessageAction(
                        label = '奶奶',
                        text = '找奶奶'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## wolf20
    def is_going_to_wolf20(self, event):
        text = event.message.text
        return text.lower() == '找大野狼'

    def on_enter_wolf20(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picWolf,
                title = '大野狼',
                text = '(要問牠什麼?)',
                actions = [
                    MessageAction(
                        label = '你願意回到書中嗎?',
                        text = '你願意回到書中嗎?'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_inWolf20(self, event):
        text = event.message.text
        return text.lower() == '你願意回到書中嗎?'

    def on_enter_inWolf20(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picWolf,
                title = '大野狼:',
                text = '我賣了一個晚上的保險!我昨天好不容易賣給一個老女人!你要買嗎?如果你肯買我就回去',
                actions = [
                    MessageAction(
                        label = '沒錢...',
                        text = '沒錢'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## baba20
    def is_going_to_baba20(self, event):
        text = event.message.text
        return text.lower() == "找奶奶"

    def on_enter_baba20(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picBaba,
                title = '奶奶',
                text = '(要問她什麼?)',
                actions = [
                    MessageAction(
                        label = '妳願意回到書中嗎?',
                        text = '妳願意回到書中嗎?'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_inBaba20(self, event):
        text = event.message.text
        return text.lower() == "妳願意回到書中嗎?"

    def on_enter_inBaba20(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picBaba,
                title = '奶奶:我都等不到我孫女要送給我的點心呢!',
                text = '我好期待呀!有蛋糕跟禮物!和我最期待的酒，能喝到酒我就回去。',
                actions = [
                    MessageAction(
                        label = '...',
                        text = '...'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## LRRH20
    def is_going_to_LRRH20(self, event):
        text = event.message.text
        return text.lower() == "找小紅帽"

    def on_enter_LRRH20(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picIRRH,
                title = '小紅帽',
                text = '(要問她什麼?)',
                actions = [
                    MessageAction(
                        label = '妳願意回到書中嗎?',
                        text = '妳願意回到書中嗎?'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_inLRRH20(self, event):
        text = event.message.text
        return text.lower() == "妳願意回到書中嗎?"

    def on_enter_inLRRH20(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picIRRH,
                title = '小紅帽:',
                text = '嘻嘻~我還有好多事沒完成呢!幫我把酒送去給我奶奶吧!可是我有兩瓶你要哪一瓶呢?',
                actions = [
                    MessageAction(
                        label = '有毒的酒',
                        text = '有毒的酒'
                    ),
                    MessageAction(
                        label = '沒毒的酒',
                        text = '沒毒的酒'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ### poison20
    def is_going_to_poison20(self, event):
        text = event.message.text
        return text.lower() == "沒毒的酒"

    def on_enter_poison20(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '獲得「沒毒的酒」',
                actions = [
                    MessageAction(
                        label = '奶奶',
                        text = '找奶奶'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_inPoison20(self, event):
        text = event.message.text
        return text.lower() == "找奶奶"

    def on_enter_inPoison20(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picBaba,
                title = '奶奶:我都等不到我孫女要送給我的點心呢!',
                text = '我好期待呀!有蛋糕跟禮物!和我最期待的酒，能喝到酒我就回去。',
                actions = [
                    MessageAction(
                        label = '(給她酒)',
                        text = '(給她酒)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ### baba FAIL
    def is_going_to_babaFail(self, event):
        text = event.message.text
        return text.lower() == "(給她酒)"

    def on_enter_babaFail(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picFail,
                title = '奶奶線失敗',
                text = '酒是有毒的，奶奶死亡',
                actions = [
                    MessageAction(
                        label = '確認',
                        text = '確認'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.game_over()

    ### sake20
    def is_going_to_sake20(self, event):
        text = event.message.text
        return text.lower() == "有毒的酒"

    def on_enter_sake20(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '獲得「有毒的酒」',
                actions = [
                    MessageAction(
                        label = '奶奶',
                        text = '找奶奶'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_inSake20(self, event):
        text = event.message.text
        return text.lower() == "找奶奶"

    def on_enter_inSake20(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picBaba,
                title = '奶奶:我都等不到我孫女要送給我的點心呢!',
                text = '我好期待呀!有蛋糕跟禮物!和我最期待的酒，能喝到酒我就回去。',
                actions = [
                    MessageAction(
                        label = '(給她酒)',
                        text = '(給她酒)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    def is_going_to_money20(self, event):
        text = event.message.text
        return text.lower() == "(給她酒)"

    def on_enter_money20(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picBaba,
                title = '奶奶:',
                text = '謝謝妳啊~~這是給你的錢和保單(上面寫著受益人小紅帽)',
                actions = [
                    MessageAction(
                        label = '(獲得「錢」「保單」)',
                        text = '(獲得「錢」「保單」)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ### baba SUCCESS
    def is_going_to_babaSuc(self, event):
        text = event.message.text
        return text.lower() == "(獲得「錢」「保單」)"

    def on_enter_babaSuc(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSuccess,
                title = '奶奶線成功',
                text = ' ',
                actions = [
                    MessageAction(
                        label = '確認',
                        text = '確認'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()



    # s21 ############################################################################################

    def is_going_to_s21(self, event):
        text = event.message.text
        return text.lower() == "確認"

    def on_enter_s21(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '獲得「錢」「保單」',
                actions = [
                    MessageAction(
                        label = '大野狼',
                        text = '找大野狼'
                    ),
                    MessageAction(
                        label = '小紅帽',
                        text = '找小紅帽'
                    ),
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## wolf21
    def is_going_to_wolf21(self, event):
        text = event.message.text
        return text.lower() == '找大野狼'

    def on_enter_wolf21(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picWolf,
                title = '大野狼:',
                text = '我賣了一個晚上的保險!我昨天好不容易賣給一個老女人!你要買嗎?如果你肯買我就回去',
                actions = [
                    MessageAction(
                        label = '買',
                        text = '買'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ### wolf SUCCESS 21
    def is_going_to_wolfSuc21(self, event):
        text = event.message.text
        return text.lower() == '買'

    def on_enter_wolfSuc21(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSuccess,
                title = '大野狼線成功',
                text = '大野狼:謝謝你啦~~我可以放心的回去了。',
                actions = [
                    MessageAction(
                        label = '確認',
                        text = '確認'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## LRRH21
    def is_going_to_LRRH21(self, event):
        text = event.message.text
        return text.lower() == '找小紅帽'

    def on_enter_LRRH21(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picIRRH,
                title = '小紅帽:',
                text = '我要我的保單~~只要那個老太婆去死我就有錢拿了!',
                actions = [
                    MessageAction(
                        label = '(給她保單)',
                        text = '(給她保單)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ### LRRH SUCCESS 21
    def is_going_to_LRRHSuc21(self, event):
        text = event.message.text
        return text.lower() == '(給她保單)'

    def on_enter_LRRHSuc21(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSuccess,
                title = '小紅帽成功',
                text = '小紅帽:切!沒成功害死老太婆真不甘心!',
                actions = [
                    MessageAction(
                        label = '確認',
                        text = '確認'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()



    # s22 ############################################################################################

    def is_going_to_s22(self, event):
        text = event.message.text
        return text.lower() == "確認"

    def on_enter_s22(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '獲得「保單」',
                actions = [
                    MessageAction(
                        label = '小紅帽',
                        text = '找小紅帽'
                    ),
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## LRRH22
    def is_going_to_LRRH22(self, event):
        text = event.message.text
        return text.lower() == '找小紅帽'

    def on_enter_LRRH22(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picIRRH,
                title = '小紅帽:',
                text = '我要我的保單~~只要那個老太婆去死我就有錢拿了!',
                actions = [
                    MessageAction(
                        label = '(給她保單)',
                        text = '(給她保單)'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ### LRRH SUCCESS 22
    def is_going_to_LRRHSuc22(self, event):
        text = event.message.text
        return text.lower() == '(給她保單)'

    def on_enter_LRRHSuc22(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSuccess,
                title = '小紅帽成功',
                text = '小紅帽:切!沒成功害死老太婆真不甘心!',
                actions = [
                    MessageAction(
                        label = '確認',
                        text = '確認'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()



    # s23 ############################################################################################

    def is_going_to_s23(self, event):
        text = event.message.text
        return text.lower() == "確認"

    def on_enter_s23(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSelect,
                title = '找誰說話呢?',
                text = '獲得「錢」',
                actions = [
                    MessageAction(
                        label = '大野狼',
                        text = '找大野狼'
                    ),
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ## wolf23
    def is_going_to_wolf23(self, event):
        text = event.message.text
        return text.lower() == '找大野狼'

    def on_enter_wolf23(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picWolf,
                title = '大野狼:',
                text = '我賣了一個晚上的保險!我昨天好不容易賣給一個老女人!你要買嗎?如果你肯買我就回去',
                actions = [
                    MessageAction(
                        label = '買',
                        text = '買'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()

    ### wolf SUCCESS 23
    def is_going_to_wolfSuc23(self, event):
        text = event.message.text
        return text.lower() == '買'

    def on_enter_wolfSuc23(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picSuccess,
                title = '大野狼線成功',
                text = '大野狼:謝謝你啦~~我可以放心的回去了。',
                actions = [
                    MessageAction(
                        label = '確認',
                        text = '確認'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.advance()



    # END ############################################################################################
    
    def is_going_to_end(self, event):
        text = event.message.text
        return text.lower() == '確認'

    def on_enter_end(self, event):
        button_message = TemplateSendMessage(
            alt_text = 'Button',
            template = ButtonsTemplate(
                thumbnail_image_url = picEnd,
                title = '感謝遊玩',
                text = '製作: 陳彥勳\n劇本: 天宇',
                actions = [
                    MessageAction(
                        label = '重新開始',
                        text = '重新開始'
                    )
                ]
            )
        )
        send_button_message(event.reply_token, button_message)
        self.game_over()
