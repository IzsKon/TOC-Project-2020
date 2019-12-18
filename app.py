import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageAction

from fsm import TocMachine
from utils import send_text_message, send_button_message

load_dotenv()

def makeMachine():
    return TocMachine(
        states = [
            "user", "restart",
            "preview1", "preview2", "preview3",
            "help", "helpnt", 
            "s1", "s1p2", "alice1", "inAlice1", "wolf1", "match1", "snow1", "katniss1", "baba1", "wake1",
            "s2", "s2p2", "LRRH2", "inLRRH2", "wolf2", "match2", "snow2", "katniss2", "baba2", "wake2",
            "s3", "s3p2", "LRRH3", "inLRRH3", "wolf3", "match3", "snow3", "katniss3", "baba3", "wake3", "story3",
            "s4", "match4", "inMatch4", "paper4", "wolf4", "snow4", 
            "s5", "baba5", "inBaba5", "alice5", "match5", "katniss5",
            "s6", "alice6", "match6", "katniss6", "wizard6",
            "s7", "wolf7", "snow7", "inSnow7", "LRRH7", "inLRRH7", "sandwich7", "inSandwich7", "aliceFail",
            "katniss7", "inKatniss7", "apple7", "inApple7", "aliceSuc", "meat7", "inMeat7", "reject7",
            "s8", "wizard8", "match8", "baba8",
            "s9", "katniss9", "inKatniss9", "wolf9", "baba9",
            "s10", "wolf10", "match10", "baba10", "snow10", "inSnow10",
            "s11", "katniss11", "LRRH11", "inLRRH11", "baba11", "match11",
            "s12", "snow12", "katniss12", "inKatniss12", "apple12", "snowFail", "LRRH12", "inLRRH12", "baba12", "match12",
            "s13", "snow13", "katniss13", "inKatniss13", "apple13", "snowSuc", "LRRH13", "baba13", "match13",
            "s14", "wizard14", "baba14", "match14",
            "s15", "katniss15", "inKatniss15", "baba15", "match15",
            "s16", "katniss16", "wolf16", "match16", "LRRH16", "inLRRH16",
            "bomb16", "inBomb16", "katnissFail", "gift16", "inGift16", "pic16", "inPic16", "katnissSuc",
            "s17", "wolf17", "match17", "baba17", "LRRH17", "inLRRH17",
            "s18", "wolf18", "baba18", "LRRH18", "inLRRH18", "match18", "matchFail",
            "s19", "wolf19", "baba19", "LRRH19", "match19", "book19", "matchSuc",
            "s20", "wolf20", "inWolf20", "baba20", "inBaba20", "LRRH20", "inLRRH20", "poison20", "inPoison20", "babaFail",
            "sake20", "inSake20", "money20", "babaSuc",
            "s21", "wolf21", "wolfSuc21", "LRRH21", "LRRHSuc21",
            "s22", "LRRH22", "LRRHSuc22",
            "s23", "wolf23", "wolfSuc23",
            "end"
        ],
        transitions = [

            # restart ###############################################################################################
            {
                "trigger": "advance",
                "source": 
                [
                    "preview1", "preview2", "preview3",
                    "help", "helpnt", 
                    "s1", "s1p2", "alice1", "inAlice1", "wolf1", "match1", "snow1", "katniss1", "baba1", "wake1",
                    "s2", "s2p2", "LRRH2", "inLRRH2", "wolf2", "match2", "snow2", "katniss2", "baba2", "wake2",
                    "s3", "s3p2", "LRRH3", "inLRRH3", "wolf3", "match3", "snow3", "katniss3", "baba3", "wake3", "story3",
                    "s4", "match4", "inMatch4", "paper4", "wolf4", "snow4", 
                    "s5", "baba5", "inBaba5", "alice5", "match5", "katniss5",
                    "s6", "alice6", "match6", "katniss6", "wizard6",
                    "s7", "wolf7", "snow7", "inSnow7", "LRRH7", "inLRRH7", "sandwich7", "inSandwich7", "aliceFail",
                    "katniss7", "inKatniss7", "apple7", "inApple7", "aliceSuc", "meat7", "inMeat7", "reject7",
                    "s8", "wizard8", "match8", "baba8",
                    "s9", "katniss9", "inKatniss9", "wolf9", "baba9",
                    "s10", "wolf10", "match10", "baba10", "snow10", "inSnow10",
                    "s11", "katniss11", "LRRH11", "inLRRH11", "baba11", "match11",
                    "s12", "snow12", "katniss12", "inKatniss12", "apple12", "snowFail", "LRRH12", "inLRRH12", "baba12", "match12",
                    "s13", "snow13", "katniss13", "inKatniss13", "apple13", "snowSuc", "LRRH13", "baba13", "match13",
                    "s14", "wizard14", "baba14", "match14",
                    "s15", "katniss15", "inKatniss15", "baba15", "match15",
                    "s16", "katniss16", "wolf16", "match16", "LRRH16", "inLRRH16",
                    "bomb16", "inBomb16", "katnissFail", "gift16", "inGift16", "pic16", "inPic16", "katnissSuc",
                    "s17", "wolf17", "match17", "baba17", "LRRH17", "inLRRH17",
                    "s18", "wolf18", "baba18", "LRRH18", "inLRRH18", "match18", "matchFail",
                    "s19", "wolf19", "baba19", "LRRH19", "match19", "book19", "matchSuc",
                    "s20", "wolf20", "inWolf20", "baba20", "inBaba20", "LRRH20", "inLRRH20", "poison20", "inPoison20", "babaFail",
                    "sake20", "inSake20", "money20", "babaSuc",
                    "s21", "wolf21", "wolfSuc21", "LRRH21", "LRRHSuc21",
                    "s22", "LRRH22", "LRRHSuc22",
                    "s23", "wolf23", "wolfSuc23",
                    "end"
                ],
                "dest": "restart",
                "conditions": "is_going_to_restart"
            },



            # preview ###############################################################################################

            {"trigger": "advance", "source": "user"    , "dest": "preview1", "conditions": "is_going_to_preview1" },
            {"trigger": "advance", "source": "preview1", "dest": "preview2", "conditions": "is_going_to_preview2" },
            {"trigger": "advance", "source": "preview2", "dest": "preview3", "conditions": "is_going_to_preview3" },

            ## start game
            {"trigger": "advance", "source": "preview3", "dest": "help", "conditions": "is_going_to_help"  },
            {"trigger": "advance", "source": "help"    , "dest": "s1"  , "conditions": "is_going_to_s1"    },

            ## game over
            {"trigger": "advance", "source": "preview3", "dest": "helpnt", "conditions": "is_going_to_helpnt"},


            
            # s1 ############################################################################################

            ## s1p2
            {"trigger": "advance", "source": "s1"  , "dest": "s1p2", "conditions": "is_going_to_s1p2"},
            {"trigger": "advance", "source": "s1p2", "dest": "s1"  , "conditions": "is_going_to_s1"  },

            ## alice1
            {"trigger": "advance", "source": "s1"      , "dest": "alice1"  , "conditions": "is_going_to_alice1"  },
            {"trigger": "advance", "source": "alice1"  , "dest": "inAlice1", "conditions": "is_going_to_inAlice1"},
            {"trigger": "advance", "source": "inAlice1", "dest": "s2"      , "conditions": "is_going_to_s2"      },

            ## wolf1
            {"trigger": "advance", "source": "s1", "dest": "wolf1", "conditions": "is_going_to_wolf1"},

            ## match1
            {"trigger": "advance", "source": "s1", "dest": "match1", "conditions": "is_going_to_match1"},

            ## snow1
            {"trigger": "advance", "source": "s1p2", "dest": "snow1"  , "conditions": "is_going_to_snow1"},

            ## katniss1
            {"trigger": "advance", "source": "s1p2", "dest": "katniss1", "conditions": "is_going_to_katniss1"},

            ## baba1
            {"trigger": "advance", "source": "s1p2" , "dest": "baba1", "conditions": "is_going_to_baba1"},
            ### wake1
            {"trigger": "advance", "source": "baba1", "dest": "wake1", "conditions": "is_going_to_wake1"},
            ### sleep1
            {"trigger": "advance", "source": "baba1", "dest": "s1p2" , "conditions": "is_going_to_s1p2" },

            ## back to s1
            {
                "trigger": "advance",
                "source": ["wolf1", "match1"],
                "dest": "s1",
                "conditions": "is_going_to_s1"
            },

            ## back to s1p2
            {
                "trigger": "advance",
                "source": ["wake1", "snow1", "katniss1"],
                "dest": "s1p2",
                "conditions": "is_going_to_s1p2"
            },



            # s2 ############################################################################################

            ## s2p2
            {"trigger": "advance", "source": "s2"  , "dest": "s2p2", "conditions": "is_going_to_s2p2"},
            {"trigger": "advance", "source": "s2p2", "dest": "s2"  , "conditions": "is_going_to_s2"  },

            ## LRRH2
            {"trigger": "advance", "source": "s2"     , "dest": "LRRH2"  ,  "conditions": "is_going_to_LRRH2"  },
            {"trigger": "advance", "source": "LRRH2"  , "dest": "inLRRH2",  "conditions": "is_going_to_inLRRH2"},
            {"trigger": "advance", "source": "inLRRH2", "dest": "s3"      , "conditions": "is_going_to_s3"    },

            ## wolf2
            {"trigger": "advance", "source": "s2", "dest": "wolf2", "conditions": "is_going_to_wolf2"},

            ## match2
            {"trigger": "advance", "source": "s2", "dest": "match2", "conditions": "is_going_to_match2"},

            ## snow2
            {"trigger": "advance", "source": "s2p2", "dest": "snow2"  , "conditions": "is_going_to_snow2"},

            ## katniss2
            {"trigger": "advance", "source": "s2p2", "dest": "katniss2", "conditions": "is_going_to_katniss2"},

            ## baba2
            {"trigger": "advance", "source": "s2p2" , "dest": "baba2", "conditions": "is_going_to_baba2"},
            ### wake2
            {"trigger": "advance", "source": "baba2", "dest": "wake2", "conditions": "is_going_to_wake2"},
            ### sleep2
            {"trigger": "advance", "source": "baba2", "dest": "s2p2" , "conditions": "is_going_to_s2p2" },

            ## back to s2
            {
                "trigger": "advance",
                "source": ["wolf2", "match2"],
                "dest": "s2",
                "conditions": "is_going_to_s2"
            },

            ## back to s2p2
            {
                "trigger": "advance",
                "source": ["wake2", "snow2", "katniss2"],
                "dest": "s2p2",
                "conditions": "is_going_to_s2p2"
            },



            # s3 ############################################################################################
            
            ## s3p2
            {"trigger": "advance", "source": "s3"  , "dest": "s3p2", "conditions": "is_going_to_s3p2"},
            {"trigger": "advance", "source": "s3p2", "dest": "s3"  , "conditions": "is_going_to_s3"  },

            ## LRRH3
            {"trigger": "advance", "source": "s3"     , "dest": "LRRH3"  , "conditions": "is_going_to_LRRH3"  },
            {"trigger": "advance", "source": "LRRH3"  , "dest": "inLRRH3", "conditions": "is_going_to_inLRRH3"},
            {"trigger": "advance", "source": "inLRRH3", "dest": "s3"     , "conditions": "is_going_to_s3"     },

            ## wolf3
            {"trigger": "advance", "source": "s3", "dest": "wolf3", "conditions": "is_going_to_wolf3"},

            ## match3
            {"trigger": "advance", "source": "s3", "dest": "match3", "conditions": "is_going_to_match3"},

            ## snow3
            {"trigger": "advance", "source": "s3p2", "dest": "snow3"  , "conditions": "is_going_to_snow3"},

            ## katniss3
            {"trigger": "advance", "source": "s3p2", "dest": "katniss3", "conditions": "is_going_to_katniss3"},

            ## baba3
            {"trigger": "advance", "source": "s3p2"  , "dest": "baba3", "conditions": "is_going_to_baba3"},
            ### wake3
            {"trigger": "advance", "source": "baba3" , "dest": "wake3" , "conditions": "is_going_to_wake3" },
            {"trigger": "advance", "source": "wake3" , "dest": "story3", "conditions": "is_going_to_story3"},
            {"trigger": "advance", "source": "story3", "dest": "s4"    , "conditions": "is_going_to_s4"    },
            ### sleep3
            {"trigger": "advance", "source": "baba3", "dest": "s3p2", "conditions": "is_going_to_s3p2"},

            ## back to s3
            {
                "trigger": "advance",
                "source": ["wolf3", "match3"],
                "dest": "s3",
                "conditions": "is_going_to_s3"
            },

            ## back to s3p2
            {
                "trigger": "advance",
                "source": ["wake3", "snow3", "katniss3"],
                "dest": "s3p2",
                "conditions": "is_going_to_s3p2"
            },



            # s4 ############################################################################################
            
            ## match4
            {"trigger": "advance", "source": "s4"      , "dest": "match4"  , "conditions": "is_going_to_match4"  },
            {"trigger": "advance", "source": "match4"  , "dest": "inMatch4", "conditions": "is_going_to_inMatch4"},
            {"trigger": "advance", "source": "inMatch4", "dest": "paper4"  , "conditions": "is_going_to_paper4"  },
            {"trigger": "advance", "source": "paper4"  , "dest": "s5"      , "conditions": "is_going_to_s5"      },
            
            ## wolf4
            {"trigger": "advance", "source": "s4", "dest": "wolf4", "conditions": "is_going_to_wolf4"},

            ## snow4
            {"trigger": "advance", "source": "s4", "dest": "snow4"  , "conditions": "is_going_to_snow4"},

            ## back to s4
            {
                "trigger": "advance",
                "source": ["wolf4", "snow4"],
                "dest": "s4",
                "conditions": "is_going_to_s4"
            },



            # s5 ############################################################################################

            ## baba5
            {"trigger": "advance", "source": "s5"     , "dest": "baba5"  , "conditions": "is_going_to_baba5"  },
            {"trigger": "advance", "source": "baba5"  , "dest": "inBaba5", "conditions": "is_going_to_inBaba5"},
            {"trigger": "advance", "source": "inBaba5", "dest": "s6"     , "conditions": "is_going_to_s6"     },

            ## alice5
            {"trigger": "advance", "source": "s5", "dest": "alice5", "conditions": "is_going_to_alice5"},

            ## match5
            {"trigger": "advance", "source": "s5", "dest": "match5", "conditions": "is_going_to_match5"},

            ## katniss5
            {"trigger": "advance", "source": "s5", "dest": "katniss5", "conditions": "is_going_to_katniss5"},

            ## back to s5
            {
                "trigger": "advance",
                "source": ["alice5", "match5", "katniss5"],
                "dest": "s5",
                "conditions": "is_going_to_s5"
            },



            # s6 ############################################################################################

            ## alice6
            {"trigger": "advance", "source": "s6"    , "dest": "alice6", "conditions": "is_going_to_alice6"},
            {"trigger": "advance", "source": "alice6", "dest": "s7"    , "conditions": "is_going_to_s7"    },

            ## match6
            {"trigger": "advance", "source": "s6", "dest": "match6", "conditions": "is_going_to_match6"},

            ## wizard6
            {"trigger": "advance", "source": "s6", "dest": "wizard6", "conditions": "is_going_to_wizard6"},

            ## katniss6
            {"trigger": "advance", "source": "s6", "dest": "katniss6", "conditions": "is_going_to_katniss6"},

            ## back to s6
            {
                "trigger": "advance",
                "source": ["match6", "wizard6", "katniss6"],
                "dest": "s6",
                "conditions": "is_going_to_s6"
            },



            # s7 ############################################################################################

            ## katniss7
            {"trigger": "advance", "source": "s7"        , "dest": "katniss7"  , "conditions": "is_going_to_katniss7"  },
            {"trigger": "advance", "source": "katniss7"  , "dest": "inKatniss7", "conditions": "is_going_to_inKatniss7"},
            ### rotten apple7
            {"trigger": "advance", "source": "inKatniss7", "dest": "apple7"  , "conditions": "is_going_to_apple7"  },
            {"trigger": "advance", "source": "apple7"    , "dest": "inApple7", "conditions": "is_going_to_inApple7"},
            {"trigger": "advance", "source": "inApple7"  , "dest": "aliceSuc", "conditions": "is_going_to_aliceSuc"},
            {"trigger": "advance", "source": "aliceSuc"  , "dest": "s8"      , "conditions": "is_going_to_s8"      },
            ### meat7
            {"trigger": "advance", "source": "inKatniss7", "dest": "meat7"  , "conditions": "is_going_to_meat7"  },
            {"trigger": "advance", "source": "meat7"     , "dest": "inMeat7", "conditions": "is_going_to_inMeat7"},
            {"trigger": "advance", "source": "inMeat7"   , "dest": "reject7", "conditions": "is_going_to_reject7"},
            {"trigger": "advance", "source": "reject7"   , "dest": "s7"     , "conditions": "is_going_to_s7"     },

            ## snow7
            {"trigger": "advance", "source": "s7"   , "dest": "snow7"  , "conditions": "is_going_to_snow7"  },
            {"trigger": "advance", "source": "snow7", "dest": "inSnow7", "conditions": "is_going_to_inSnow7"},

            ## LRRH7
            {"trigger": "advance", "source": "s7"     , "dest": "LRRH7"  , "conditions": "is_going_to_LRRH7"  },
            {"trigger": "advance", "source": "LRRH7"  , "dest": "inLRRH7", "conditions": "is_going_to_inLRRH7"},
            ### sandwich7
            {"trigger": "advance", "source": "inLRRH7"    , "dest": "sandwich7"  , "conditions": "is_going_to_sandwich7"  },
            {"trigger": "advance", "source": "sandwich7"  , "dest": "inSandwich7", "conditions": "is_going_to_inSandwich7"},
            {"trigger": "advance", "source": "inSandwich7", "dest": "aliceFail"  , "conditions": "is_going_to_aliceFail"  },
            {"trigger": "advance", "source": "aliceFail"  , "dest": "s8"         , "conditions": "is_going_to_s8"         },

            ## wolf7
            {"trigger": "advance", "source": "s7", "dest": "wolf7", "conditions": "is_going_to_wolf7"},

            ## back to s7
            {
                "trigger": "advance",
                "source": ["wolf7", "inSnow7"],
                "dest": "s7",
                "conditions": "is_going_to_s7"
            },



            # s8 ############################################################################################
            
            ## wizard8
            {"trigger": "advance", "source": "s8"     , "dest": "wizard8", "conditions": "is_going_to_wizard8"},
            {"trigger": "advance", "source": "wizard8", "dest": "s9"     , "conditions": "is_going_to_s9"     },

            ## match8
            {"trigger": "advance", "source": "s8", "dest": "match8", "conditions": "is_going_to_match8"},

            ## baba8
            {"trigger": "advance", "source": "s8", "dest": "baba8", "conditions": "is_going_to_baba8"},

            ## back to s8
            {
                "trigger": "advance",
                "source": ["match8", "baba8"],
                "dest": "s8",
                "conditions": "is_going_to_s8"
            },



            # s9 ############################################################################################

            ## katniss9
            {"trigger": "advance", "source": "s9"        , "dest": "katniss9"  , "conditions": "is_going_to_katniss9"  },
            {"trigger": "advance", "source": "katniss9"  , "dest": "inKatniss9", "conditions": "is_going_to_inKatniss9"},
            {"trigger": "advance", "source": "inKatniss9", "dest": "s10"       , "conditions": "is_going_to_s10"       },

            ## wolf9
            {"trigger": "advance", "source": "s9", "dest": "wolf9", "conditions": "is_going_to_wolf9"},

            ## baba9
            {"trigger": "advance", "source": "s9", "dest": "baba9", "conditions": "is_going_to_baba9"},

            ## back to s9
            {
                "trigger": "advance",
                "source": ["wolf9", "baba9"],
                "dest": "s9",
                "conditions": "is_going_to_s9"
            },



            # s10 ############################################################################################

            ## wolf10
            {"trigger": "advance", "source": "s10", "dest": "wolf10", "conditions": "is_going_to_wolf10"},

            ## match10
            {"trigger": "advance", "source": "s10", "dest": "match10", "conditions": "is_going_to_match10"},

            ## baba10
            {"trigger": "advance", "source": "s10", "dest": "baba10", "conditions": "is_going_to_baba10"},

            ## snow10
            {"trigger": "advance", "source": "s10"     , "dest": "snow10"  , "conditions": "is_going_to_snow10"  },
            {"trigger": "advance", "source": "snow10"  , "dest": "inSnow10", "conditions": "is_going_to_inSnow10"},
            {"trigger": "advance", "source": "inSnow10", "dest": "s11"     , "conditions": "is_going_to_s11"     },

            ## back to s10
            {
                "trigger": "advance",
                "source": ["match10", "baba10", "wolf10"],
                "dest": "s10",
                "conditions": "is_going_to_s10"
            },



            # s11 ############################################################################################

            ## katniss11
            {"trigger": "advance", "source": "s11", "dest": "katniss11", "conditions": "is_going_to_katniss11"},

            ## LRRH11
            {"trigger": "advance", "source": "s11"     , "dest": "LRRH11"  , "conditions": "is_going_to_LRRH11"  },
            {"trigger": "advance", "source": "LRRH11"  , "dest": "inLRRH11", "conditions": "is_going_to_inLRRH11"},
            {"trigger": "advance", "source": "inLRRH11", "dest": "s12"     , "conditions": "is_going_to_s12"     },

            ## baba11
            {"trigger": "advance", "source": "s11", "dest": "baba11", "conditions": "is_going_to_baba11"},

            ## match11
            {"trigger": "advance", "source": "s11", "dest": "match11", "conditions": "is_going_to_match11"},

            ## back to s11
            {
                "trigger": "advance",
                "source": ["match11", "baba11", "katniss11"],
                "dest": "s11",
                "conditions": "is_going_to_s11"
            },



            # s12 ############################################################################################

            ## katniss12
            {"trigger": "advance", "source": "s12"        , "dest": "katniss12"  , "conditions": "is_going_to_katniss12"  },
            {"trigger": "advance", "source": "katniss12"  , "dest": "inKatniss12", "conditions": "is_going_to_inKatniss12"},
            {"trigger": "advance", "source": "inKatniss12", "dest": "apple12"    , "conditions": "is_going_to_apple12"    },
            {"trigger": "advance", "source": "apple12"    , "dest": "snowFail"   , "conditions": "is_going_to_snowFail"   },
            {"trigger": "advance", "source": "snowFail"   , "dest": "s14"        , "conditions": "is_going_to_s14"        },

            ## LRRH12
            {"trigger": "advance", "source": "s12"     , "dest": "LRRH12"  , "conditions": "is_going_to_LRRH12"  },
            {"trigger": "advance", "source": "LRRH12"  , "dest": "inLRRH12", "conditions": "is_going_to_inLRRH12"},
            {"trigger": "advance", "source": "inLRRH12", "dest": "s13"     , "conditions": "is_going_to_s12"     },

            ## baba12
            {"trigger": "advance", "source": "s12", "dest": "baba12", "conditions": "is_going_to_baba12"},

            ## match12
            {"trigger": "advance", "source": "s12", "dest": "match12", "conditions": "is_going_to_match12"},

            ## back to s12
            {
                "trigger": "advance",
                "source": ["match12", "baba12"],
                "dest": "s12",
                "conditions": "is_going_to_s12"
            },



            # s13 ############################################################################################

            ## katniss13
            {"trigger": "advance", "source": "s13"        , "dest": "katniss13"  , "conditions": "is_going_to_katniss13"  },
            {"trigger": "advance", "source": "katniss13"  , "dest": "inKatniss13", "conditions": "is_going_to_inKatniss13"},
            {"trigger": "advance", "source": "inKatniss13", "dest": "apple13"    , "conditions": "is_going_to_apple13"    },
            {"trigger": "advance", "source": "apple13"    , "dest": "snowSuc"    , "conditions": "is_going_to_snowSuc"    },
            {"trigger": "advance", "source": "snowSuc"    , "dest": "s14"        , "conditions": "is_going_to_s14"        },

            ## LRRH13
            {"trigger": "advance", "source": "s13", "dest": "LRRH13", "conditions": "is_going_to_LRRH13"},

            ## baba13
            {"trigger": "advance", "source": "s13", "dest": "baba13", "conditions": "is_going_to_baba13"},

            ## match13
            {"trigger": "advance", "source": "s13", "dest": "match13", "conditions": "is_going_to_match13"},

            ## back to s13
            {
                "trigger": "advance",
                "source": ["match13", "baba13", "LRRH13"],
                "dest": "s13",
                "conditions": "is_going_to_s13"
            },



            # s14 ############################################################################################

            ## wizard14
            {"trigger": "advance", "source": "s14"     , "dest": "wizard14", "conditions": "is_going_to_wizard14"},
            {"trigger": "advance", "source": "wizard14", "dest": "s15"     , "conditions": "is_going_to_s15"     },

            ## baba14
            {"trigger": "advance", "source": "s14", "dest": "baba14", "conditions": "is_going_to_baba14"},

            ## match14
            {"trigger": "advance", "source": "s14", "dest": "match14", "conditions": "is_going_to_match14"},

            ## back to s14
            {
                "trigger": "advance",
                "source": ["match14", "baba14"],
                "dest": "s14",
                "conditions": "is_going_to_s14"
            },



            # s15 ############################################################################################

            ## katniss15
            {"trigger": "advance", "source": "s15"        , "dest": "katniss15"  , "conditions": "is_going_to_katniss15"  },
            {"trigger": "advance", "source": "katniss15"  , "dest": "inKatniss15", "conditions": "is_going_to_inKatniss15"},
            {"trigger": "advance", "source": "inKatniss15", "dest": "s16"        , "conditions": "is_going_to_s16"        },

            ## baba15
            {"trigger": "advance", "source": "s15", "dest": "baba15", "conditions": "is_going_to_baba15"},

            ## match15
            {"trigger": "advance", "source": "s15", "dest": "match15", "conditions": "is_going_to_match15"},

            ## back to s15
            {
                "trigger": "advance",
                "source": ["match15", "baba15"],
                "dest": "s15",
                "conditions": "is_going_to_s15"
            },



            # s16 ############################################################################################

            ## katniss16
            {"trigger": "advance", "source": "s16", "dest": "katniss16", "conditions": "is_going_to_katniss16"},
            
            ## wolf16
            {"trigger": "advance", "source": "s16", "dest": "wolf16", "conditions": "is_going_to_wolf16"},

            ## match16
            {"trigger": "advance", "source": "s16", "dest": "match16", "conditions": "is_going_to_match16"},

            ## LRRH16
            {"trigger": "advance", "source": "s16"     , "dest": "LRRH16"  , "conditions": "is_going_to_LRRH16"  },
            {"trigger": "advance", "source": "LRRH16"  , "dest": "inLRRH16", "conditions": "is_going_to_inLRRH16"},

            ### bomb16
            {"trigger": "advance", "source": "inLRRH16"   , "dest": "bomb16"     , "conditions": "is_going_to_bomb16"     },
            {"trigger": "advance", "source": "bomb16"     , "dest": "inBomb16"   , "conditions": "is_going_to_inBomb16"   },
            {"trigger": "advance", "source": "inBomb16"   , "dest": "katnissFail", "conditions": "is_going_to_katnissFail"},
            {"trigger": "advance", "source": "katnissFail", "dest": "s17"        , "conditions": "is_going_to_s17"        },

            ### gift16
            {"trigger": "advance", "source": "inLRRH16"  , "dest": "gift16"    , "conditions": "is_going_to_gift16"    },
            {"trigger": "advance", "source": "gift16"    , "dest": "inGift16"  , "conditions": "is_going_to_inGift16"  },
            {"trigger": "advance", "source": "inGift16"  , "dest": "pic16"     , "conditions": "is_going_to_pic16"     },
            {"trigger": "advance", "source": "pic16"     , "dest": "inPic16"   , "conditions": "is_going_to_inPic16"   },
            {"trigger": "advance", "source": "inPic16"   , "dest": "katnissSuc", "conditions": "is_going_to_katnissSuc"},
            {"trigger": "advance", "source": "katnissSuc", "dest": "s17"       , "conditions": "is_going_to_s17"       },

            ## back to s16
            {
                "trigger": "advance",
                "source": ["match16", "wolf16", "katniss16"],
                "dest": "s16",
                "conditions": "is_going_to_s16"
            },

            

            # s17 ############################################################################################

            ## wolf17
            {"trigger": "advance", "source": "s17", "dest": "wolf17", "conditions": "is_going_to_wolf17"},

            ## match17
            {"trigger": "advance", "source": "s17", "dest": "match17", "conditions": "is_going_to_match17"},

            ## baba17
            {"trigger": "advance", "source": "s17", "dest": "baba17", "conditions": "is_going_to_baba17"},

            ## LRRH17
            {"trigger": "advance", "source": "s17"     , "dest": "LRRH17"  , "conditions": "is_going_to_LRRH17"  },
            {"trigger": "advance", "source": "LRRH17"  , "dest": "inLRRH17", "conditions": "is_going_to_inLRRH17"},
            {"trigger": "advance", "source": "inLRRH17", "dest": "s18"     , "conditions": "is_going_to_s18"     },

            ## back to s17
            {
                "trigger": "advance",
                "source": ["match17", "wolf17", "baba17"],
                "dest": "s17",
                "conditions": "is_going_to_s17"
            },



            # s18 ############################################################################################

            ## wolf18
            {"trigger": "advance", "source": "s18", "dest": "wolf18", "conditions": "is_going_to_wolf18"},

            ## baba18
            {"trigger": "advance", "source": "s18", "dest": "baba18", "conditions": "is_going_to_baba18"},

            ## LRRH18
            {"trigger": "advance", "source": "s18"     , "dest": "LRRH18"  , "conditions": "is_going_to_LRRH18"  },
            {"trigger": "advance", "source": "LRRH18"  , "dest": "inLRRH18", "conditions": "is_going_to_inLRRH18"},
            {"trigger": "advance", "source": "inLRRH18", "dest": "s19"     , "conditions": "is_going_to_s19"     },

            ## match18
            {"trigger": "advance", "source": "s18"    , "dest": "match18"  , "conditions": "is_going_to_match18"  },
            {"trigger": "advance", "source": "match18", "dest": "matchFail", "conditions": "is_going_to_matchFail"},

            ## back to s18
            {
                "trigger": "advance",
                "source": ["wolf18", "baba18"],
                "dest": "s18",
                "conditions": "is_going_to_s18"
            },



            # s19 ############################################################################################

            ## wolf19
            {"trigger": "advance", "source": "s19", "dest": "wolf19", "conditions": "is_going_to_wolf19"},

            ## baba19
            {"trigger": "advance", "source": "s19", "dest": "baba19", "conditions": "is_going_to_baba19"},

            ## LRRH19
            {"trigger": "advance", "source": "s19", "dest": "LRRH19", "conditions": "is_going_to_LRRH19"},

            ## match19
            {"trigger": "advance", "source": "s19"      , "dest": "match19" , "conditions": "is_going_to_match19" },
            {"trigger": "advance", "source": "match19"  , "dest": "book19"  , "conditions": "is_going_to_book19"  },
            {"trigger": "advance", "source": "book19"   , "dest": "matchSuc", "conditions": "is_going_to_matchSuc"},
            {"trigger": "advance", "source": "matchSuc" , "dest": "s20"     , "conditions": "is_going_to_s20"     },

            ## back to s19
            {
                "trigger": "advance",
                "source": ["baba19", "wolf19", "LRRH19"],
                "dest": "s19",
                "conditions": "is_going_to_s19"
            },



            # s20 ############################################################################################

            ## wolf20
            {"trigger": "advance", "source": "s20"   , "dest": "wolf20"  , "conditions": "is_going_to_wolf20"  },
            {"trigger": "advance", "source": "wolf20", "dest": "inWolf20", "conditions": "is_going_to_inWolf20"},

            ## baba20
            {"trigger": "advance", "source": "s20"   , "dest": "baba20"  , "conditions": "is_going_to_baba20"  },
            {"trigger": "advance", "source": "baba20", "dest": "inBaba20", "conditions": "is_going_to_inBaba20"},

            ## LRRH20
            {"trigger": "advance", "source": "s20"   , "dest": "LRRH20"  , "conditions": "is_going_to_LRRH20"  },
            {"trigger": "advance", "source": "LRRH20", "dest": "inLRRH20", "conditions": "is_going_to_inLRRH20"},
            ### poison20
            {"trigger": "advance", "source": "inLRRH20"  , "dest": "poison20"  , "conditions": "is_going_to_poison20"  },
            {"trigger": "advance", "source": "poison20"  , "dest": "inPoison20", "conditions": "is_going_to_inPoison20"},
            {"trigger": "advance", "source": "inPoison20", "dest": "babaFail"  , "conditions": "is_going_to_babaFail"  },
            ### sake20
            {"trigger": "advance", "source": "inLRRH20", "dest": "sake20"  , "conditions": "is_going_to_sake20" },
            {"trigger": "advance", "source": "sake20"  , "dest": "inSake20", "conditions": "is_going_to_inSake20" },
            {"trigger": "advance", "source": "inSake20", "dest": "money20" , "conditions": "is_going_to_money20"},
            {"trigger": "advance", "source": "money20" , "dest": "babaSuc" , "conditions": "is_going_to_babaSuc"},
            {"trigger": "advance", "source": "babaSuc" , "dest": "s21"     , "conditions": "is_going_to_s21"    },

            ## back to s20
            {
                "trigger": "advance",
                "source": ["inBaba20", "inWolf20"],
                "dest": "s20",
                "conditions": "is_going_to_s20"
            },



            # s21 ############################################################################################
            ## wolf21
            {"trigger": "advance", "source": "s21"      , "dest": "wolf21"   , "conditions": "is_going_to_wolf21"   },
            {"trigger": "advance", "source": "wolf21"   , "dest": "wolfSuc21", "conditions": "is_going_to_wolfSuc21"},
            {"trigger": "advance", "source": "wolfSuc21", "dest": "s22"      , "conditions": "is_going_to_s22"      },

            ## LRRH21
            {"trigger": "advance", "source": "s21"      , "dest": "LRRH21"   , "conditions": "is_going_to_LRRH21"   },
            {"trigger": "advance", "source": "LRRH21"   , "dest": "LRRHSuc21", "conditions": "is_going_to_LRRHSuc21"},
            {"trigger": "advance", "source": "LRRHSuc21", "dest": "s23"      , "conditions": "is_going_to_s23"      },



            # s22 ############################################################################################
            ## LRRH22
            {"trigger": "advance", "source": "s22"      , "dest": "LRRH22"   , "conditions": "is_going_to_LRRH22"   },
            {"trigger": "advance", "source": "LRRH22"   , "dest": "LRRHSuc22", "conditions": "is_going_to_LRRHSuc22"},



            # s23 ############################################################################################
            ## wolf23
            {"trigger": "advance", "source": "s23"      , "dest": "wolf23"   , "conditions": "is_going_to_wolf23"   },
            {"trigger": "advance", "source": "wolf23"   , "dest": "wolfSuc23", "conditions": "is_going_to_wolfSuc23"},



            # end ############################################################################################
            {"trigger": "advance", "source": ["wolfSuc23", "LRRHSuc22"], "dest": "end", "conditions": "is_going_to_end"},



            # game over ############################################################################################
            {
                "trigger": "game_over",
                "source": ["helpnt", "katnissFail", "matchFail", "babaFail", "end", "restart"],
                "dest": "user"
            }
        ],
        initial = "user",
        auto_transitions = False,
        show_conditions = True,
    )

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"

userMachines = dict()

@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        user_id = event.source.user_id
        if (user_id not in userMachines):
            userMachines[user_id] = makeMachine()
        userMachine = userMachines[user_id]
        print(f"\nFSM STATE: {userMachine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = userMachine.advance(event)
        if response == False:
            if userMachine.state == 'user':
                button_message = TemplateSendMessage(
                    alt_text = 'Button',
                    template = ButtonsTemplate(
                        thumbnail_image_url = 'https://i.imgur.com/ukwX4FR.png',
                        title = 'RPG',
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
                
    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    makeMachine().get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
