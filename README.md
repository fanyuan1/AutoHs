# AutoHS
目前还在开发过程中，可能有很多Bug……

欢迎任何批评建议~

原来的脚本是通过计算机视觉手段（分析图片哈希相似度等）来分析局势的，但现在这个方案已经被放弃了（非常不靠谱）。可以在`cv`分支中看到cv相关的代码。

### 如何运行

0. 安装`Python3`。

1. 安装所需依赖:
```
pip install -r requirements.txt
```

2. 在`constants/constants`里有一些参数可以设置，其中有两项必须修改：
   - 名为`YOUR_NAME`的变量需要改成你的炉石用户名，形如`为所欲为、异灵术#54321`。如果不在文件里修改，每次启动脚本时系统都会提示你手动输入用户名。
   - 名为`HEARTHSTONE_POWER_LOG_PATH`的变量必须修改成你的电脑上的炉石传说日志`Power.log`的路径，`Power.log`在炉石安装路径下的`Logs/`文件夹中。

> `Power.log`中记录了对战过程中每一个**对象**(**Entity**)的每一项**属性**(**tag**)的变化。 这个**对象**包括玩家、英雄、英雄技能、卡牌(无论在牌库里、手牌中、战场上还是坟地里)等。
> 
> `Power.log`会在进入炉石后第一次对战开始时创建，在退出炉石后会被重命名为`Power_bk.log`，在再一次进入炉石时被删除。
> 
> 如果你在`Logs/`目录下没有找到`Power.log`（指对战开始后），那稍微有一些麻烦。你需要到`C:\Users\YOURUSER\AppData\Local\Blizzard\Hearthstone`目录下新建一个叫`log.config`的文件（如果已经有就不用新建了），然后把下面这段代码放进去（如果已经有`[Power]`相关则更改相关设置）:
> ```
> [Power]
> LogLevel=1
> FilePrinting=True
> ConsolePrinting=False
> ScreenPrinting=False
> Verbose=True
> ```
> 
> 关于炉石log的更多信息可以查看这个
> [Reddit帖子](https://www.reddit.com/r/hearthstone/comments/268fkk/simple_hearthstone_logging_see_your_complete_play/) 。

3. 可以先跑一跑`demo/`下的一些文件。

4. 若要启动脚本，将当前目录切换到`AutoHS/`下（重要），运行`python main.py`即可。注意以下几点：
   - **显示分辨率**（在桌面右击的显示设置里调整）以及**炉石分辨率**为**1920 * 1080**。
   - 项目大小缩放比例为**100%**（同样在显示设置里调整）。
   - 炉石**全屏**且语言为**简体中文**、**繁体中文**或**英文**。
   - 炉石放在**最前台**。 
   - 你可以把战网客户端最小化到任务栏，或是放在炉石应用下面，但请不要关闭战网客户端。有时炉石会意外关闭，这时程序会试图重新打开炉石。
   

### 我目前用的挂机卡组 
#### 经典模式－动物园的亲爹
- 2x (1) 精灵弓箭手
- 2x (1) 银色侍从
- 2x (2) 战利品贮藏者
- 2x (2) 末日预言者
- 1x (2) 血法师萨尔诺斯
- 2x (2) 雷铸战斧
- 2x (3) 大地之环先知
- 1x (3) 妖术
- 2x (3) 精神控制技师
- 2x (3) 苦痛侍僧
- 1x (3) 血骑士
- 2x (3) 闪电风暴
- 1x (4) 冰风雪人
- 2x (4) 森金持盾卫士
- 2x (5) 土元素
- 2x (5) 狂奔科多兽
- 2x (6) 烈日行者


神秘代码:
```
AAEDAfWfAwSwlgTnlgS1oQSWowQNr5YEs5YE+qAEsaEEsqEEvqEE0KEE1aEEiKIEi6IEjqIExaME0qMEAA==
```

在广大动物园脚本的鼎力支持下，已于2021年8月14日上传说。上传说时排名6785，上传说前29场对战战绩为20-9。

没必要特意去合卡，所有卡牌都可以替换成任意**非战吼随从**，或是`card/classic_card.py`中已经写过逻辑的卡牌。比如卡组中血法师萨尔诺斯这张牌据我观察毫无作用，只是鉴于第一次上传说的纪念意义予以保留。


### 如果想加入新的卡牌
对于所有的**非战吼随从**，如果没有具体实现它，脚本会根据它的费用猜测它的价值（费用越高越厉害）。而脚本不会使用未识别的战吼随从、法术、武器。如果想要让脚本识别并合理运用一张卡牌，你需要干两件事：
1. 在`card/classic_card.py`中写下它的使用规则，比如使用它的期望值、使用它时鼠标要点哪里等。
2. 在`card/id2card.py`中加入一个它的**id**与其卡牌实现类的键值对。

> 关于**id**，在炉石中每一个**Entity**都有其对应的**id**，比如各种各样的吉安娜有各种各样的**id**：
> - HERO_08 吉安娜·普罗德摩尔
> - HERO_08c 火法师吉安娜
> - HERO_08f 学生吉安娜
> - HERO_08g 奥术师吉安娜
> - HERO_08h 学徒吉安娜
> - HERO_08i 大法师吉安娜
> - HERO_08j 库尔提拉斯的吉安娜
> - HERO_08k 灵风吉安娜
> 
> 英雄技能各有**id**，一个同样的技能会有好多**id**，并随着皮肤的切换改变**id**：
> - HERO_07bp 生命分流
> - HERO_07dbp 生命分流
> - HERO_07ebp 生命分流
> - VAN_HERO_07bp 生命分流
> - CS2_056_H1 生命分流
> - CS2_056_H2 生命分流
> - CS2_056_H3 生命分流
> - HERO_07bp2 灵魂分流（生命分流的升级技能）
> 
> 卡牌，连带着它的衍生牌、增益效果、抉择选项，各有各的**id**：
> - SW_091 恶魔之种
> - SW_091t 建立连接
> - SW_091t3 完成仪式
> - SW_091t4 枯萎化身塔姆辛
> - SW_091t5 枯萎化身
> 
> 如果想获取卡牌的**id**，可以直接运行`json_op.py`，它会在脚本根目录下生成一个名为`id-name.txt`的文件，包含了炉石中每一个对象的**id**与中文名的对应关系。

### 文件说明
- `demo/catch_screen_demo.py`: 运行此文件会获取炉石传说进程的整个截屏(无论是在前台还是后台)，并画上一些坐标基准线，方便判断想实现的操作的坐标值。
- `demo/game_state_snapshot_demo.py`: 在控制台显示目前的炉石战局情况，包括显示手牌情况，英雄情况，随从情况等； 还会在`demo/`目录下创建一个名为`game_state_sanpshot.txt`的文件，记录log分析情况。 需要在`Power.log`存在，即进入对战模式后调用。
- `demo/get_window_name.py`: 显示当前所有窗口的名称和编号，可以用来看炉石传说叫什么名字……
- `demo/mouse_control_demo.py`: 一个样例程序，展示了如何控制鼠标。
- `click.py`: 包含了与鼠标控制相关的代码。
- `FSM_action.py`: 包含了脚本在炉石运行中的不同状态（比如选英雄界面、对战时、对扎结束后）应该采取什么行为以及何时进入下一站状态的代码。
- `lop_op.py`: 包含了与读取`Power.log`相关的代码，比如针对不同日志行的正则表达式。
- `json_op.py`: 包含了从网络上下载炉石数据JSON文件，并将其初步处理的代码。直接运行可以生成`id-name.txt`，一个包含了炉石所有对象**id**与中文名对应关系的文件。  
- `log_state.py`: 读取`log.py`提取的日志信息，并把他们转化成字典的列表的形式。每一个字典是一个 **Entity**，**Entity** 由不同的 **tag** 及其对应值构成。
- `strategy.py`: 读取`log_state.py`提取的信息，并从中提取出手牌信息，战场信息，墓地信息等，再根据这些具体信息思考行动策略。
- `card/`: 用于存放针对某些特殊卡牌的具体逻辑。



[comment]: <> (### 关于控制鼠标)

[comment]: <> (原本想通过发送信号的方式在让炉石在后台也能接收到鼠标点击)

[comment]: <> (但是发现炉石应该是所谓的接受直接输入的进程，信号模拟它不会接收……)

[comment]: <> (所以只能使用很low的鼠标点击了)

[comment]: <> (也许能直接模拟网络发包？)


[comment]: <> (### 关于网络连接的观察)

[comment]: <> (一打开炉石就会建立两个TCP连接，这两个所有的数据都是加密的。像分解卡牌， 只有退出了某个卡牌的分解界面（就是可以撤销的界面）才会发包确认分解结果。)

[comment]: <> (实验下来感觉只有其中一条连接在真的交换数据。)

[comment]: <> (点击匹配会新建一个连接，这个连接是加密的。在匹配完成后连接就销毁。)

[comment]: <> (进入对战会又新建一个连接，这个是纯TCP没有加密，不过我仍然无法解析数据交换的格式……。)

[comment]: <> (任何一个操作都会触发数据传输（比如空中乱晃鼠标……），而如果什么都不做炉石也会每个5秒跟服务器互相ping一下，应该是在确认是否掉线)