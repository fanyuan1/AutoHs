from card.basic_card import Coin
from card.standard_card import *
from card.classic_card import *
from card.hero_power_card import *

ID2CARD_DICT = {
    # 特殊项-幸运币
    "COIN": Coin,

    # 英雄技能
    "TOTEMIC_CALL": TotemicCall,
    "LESSER_HEAL": LesserHeal,
    "BALLISTA_SHOT": BallistaShot,
    "DEMON_CLAWS" : DemonClaws,
    "FIRE_BLAST" : Fireblast,
    "GHOUL_CHARGE" : GhoulCharge, 

    # 标准模式-牧师
    "YOP_032": ArmorVendor,  # 护甲商贩
    "CORE_CS1_130": HolySmite,  # 神圣惩击
    "CS1_130": HolySmite,  # 神圣惩击
    "SCH_250": WaveOfApathy,  # 倦怠光波
    "BT_715": BonechewerBrawler,  # 噬骨殴斗者
    "CORE_EX1_622": ShadowWordDeath,  # 暗言术：灭
    "EX1_622": ShadowWordDeath,  # 暗言术：灭
    "BT_257": Apotheosis,  # 神圣化身
    "BAR_026": DeathsHeadCultist,  # 亡首教徒
    "BAR_311": DevouringPlague,  # 噬灵疫病
    "BT_730": OverconfidentOrc,  # 狂傲的兽人
    "CORE_CS1_112": HolyNova,  # 神圣新星
    "CS1_112": HolyNova,  # 神圣新星
    "YOP_006": Hysteria,  # 狂乱
    "CORE_EX1_197": ShadowWordRuin,  # 暗言术：毁
    "EX1_197": ShadowWordRuin,  # 暗言术：毁
    "WC_014": AgainstAllOdds,  # 除奇致胜
    "BT_720": RuststeedRaider,  # 锈骑劫匪
    "CS3_024": TaelanFordring,  # 泰兰·弗丁
    "EX1_110": CairneBloodhoof,  # 凯恩·血蹄
    "CORE_EX1_110": CairneBloodhoof,  # 凯恩·血蹄
    "WC_030": MutanusTheDevourer,  # 吞噬者穆坦努斯
    "BT_198": SoulMirror,  # 灵魂之镜
    "DMF_053": BloodOfGhuun,  # 戈霍恩之血
    "CS2_234" : ShadowWordPain,
    "CS2_004" : PowerWordShield,
    #newest expansion
    "RLK_707" : GraveStrength,
    "RLK_039" : PlaguedGrain,
    "RLK_118" : TombGuardians,
    "RLK_048" : MagicShell,

    #astalor bloodsworn (minionpointoppo)
    "RLK_222" : Astalor,
    "RLK_222t1" : Astalor1,
    "RLK_222t2" : Astalor2,

    #bone flinger (minionpointoppo)
    "RLK_123" : BoneFlinger,
    #plague strike (spellpointoppo)
    "RLK_018" : PlagueStrike,
    #vrykul necrolyte (minionpointmine)
    "RLK_867" : VrykulNecrolyte,
    #dark transformation (spellpointmine)
    "RLK_057" : DarkTransformation,
    #priest of the deceased (needs infused)
    "REV_956" : PriestDeceased,
    "REV_956t" : PriestDeceasedt,
    "SCH_283" : ManaFeederHP,
    "RLK_753" : BoneDigger,
    "RLK_061" : BattlefieldNecromancer,

    # 经典模式
    "VAN_CS2_042": FireElemental,
    "VAN_EX1_562": Onyxia,
    "VAN_EX1_248": FeralSpirit,
    "VAN_EX1_246": Hex,
    "VAN_EX1_238": LightingBolt,
    "VAN_EX1_085": MindControlTech,
    "VAN_EX1_284": AzureDrake,
    "VAN_EX1_259": LightningStorm,
    "VAN_CS2_189": ElvenArcher,
    "VAN_CS2_117": EarthenRingFarseer,
    "VAN_EX1_097": Abomination,
    "VAN_NEW1_021": DoomSayer,
    "VAN_NEW1_041": StampedingKodo,
    "VAN_EX1_590": BloodKnight,
    "VAN_EX1_247": StormforgedAxe,
    "VAN_CS1_112": HolyNovaClassic,
    "VAN_HERO_09bp" : LesserHeal,
    "VAN_CS1_130" : HolySmiteClassic,
    "VAN_CS2_234" : ShadowWordPain,
    "VAN_EX1_622" : ShadowWordDeath,
    "VAN_CS2_004" : PowerWordShield,
    "EX1_014t" : PowerWordShield,
    "EX1_014te" : PowerWordShield,

}
