    # -*- coding: utf-8 -*-
import json
from datetime import datetime, timedelta

def build():
    weeks = []
    start_date = datetime(2026, 3, 5)
    
    # === Mathematical Stages (41 weeks) ===
    math_stages = [
        (6, "【高数基础】三十讲课后题+1000题基础", "张宇基础三十讲课后题+1000题基础做完。\n⚠️不准当“耐听王”，不听课！整理错题并选看网课(去B站搜1000题讲解，千羽、考研数学777、没咋了等)。"),
        (4, "【线代基础】三十讲课后题+1000题基础", "张宇三十讲线代课后题+1000题基础做完。\n⚠️同样不听课！有不懂直接去B站搜播放量高的UP主讲解，很多比大机构讲得好。"),
        (3, "【概率基础】三十讲课后题+1000题基础", "张宇三十讲概率课后题+1000题基础做完。\n⚠️全科保持以练带学，只做计算不做证明。"),
        (2, "【澄箫宇大观】第一遍", "b站“澄箫宇”大观系列首刷，大概7个，两天看一个。\n⚠️每讲一个题之前必须【暂停自己先做一遍】，然后继续听！"),
        (3, "【660题速刷】一阶速刷", "660一阶题速刷。\n⚠️速刷意思是把会做的做了，但凡2分钟没思路的直接跳过，对答案订正。"),
        (7, "【第一轮真题】真题一本通（于文涛）", "最重要的习题册没有之一！\n✅ 单独整理错题本，按章节分类，务必弄懂！\n✅ 习题册只做这里的证明题，其余全丢！"),
        (2, "【澄箫宇大观】二刷", "带着前期的磨砺，二刷澄箫宇大观。\n✅ 重点串联知识点网络，寻找顿悟时刻。"),
        (3, "【二轮真题】数一真题", "每天一套数一（09-26年）。\n✅ 借套卷把真题错题本浓缩一下，整理对应的题型。"),
        (2, "【全真模拟】李林6+4", "每天一套李林6+4（10套）。练习真实考场分配节奏，别看重分数。"),
        (3, "【武忠祥选填课+错题本】", "啃两本核心错题：真题错题本、模拟卷错题本。\n✅ 配合武忠祥选填技巧课，对应错题看视频查漏补缺。"),
        (6, "【考前冲刺】近3年真题再刷", "最后阶段主要是动手算错题，不要光看！\n✅ 做近3年真题熟悉考试风格（最贴近今年真题难度）。")
    ]
    
    math_tasks = []
    for duration, title, content in math_stages:
        for _ in range(duration):
            math_tasks.append({"title": title, "content": content, "hours": "核心重点"})

    # === English Stages (41 weeks) ===
    # For English, we vary the descriptions instead of repeating exactly the same block 17 times.
    eng_tasks = []
    
    # Stage 1: Vocabulary (17 weeks)
    for w in range(17):
        if w == 0:
            content = "唯一的任务：疯狂背考研核心词（约3000个）。\n⚠️强推《不背单词》，少听或者不听课！"
        elif w == 8:
            content = "单词继续推进！最好能开始二刷。\n🚫每天读阅读和背单词，切记不精翻文章，不买手译本！"
        else:
            content = "持续使用APP刷核心词，一遍遍过，直到产生肌肉记忆。"
        eng_tasks.append({"title": "【暑假前】疯狂背单词", "content": content, "hours": "持续积累"})

    # Stage 2: Reading + Essay prep (16 weeks)
    for w in range(16):
        if w == 0:
            content = "✅ 两天一套英一真题（不写作文）。\n✅ 用《真题伴侣》标生词反复背。\n✅ 听Monkey考研作文模板课，背模板并积累主题词！"
        elif w == 8:
            content = "✅ 继续保持真题阅读手感，不写作文但要背Monkey模板并积累主题词。\n⚠️ 原单词APP不能断！"
        else:
            content = "✅ 真题阅读 + 积累Monkey作文模板单词。\n⚠️ 真题里的生词用《真题伴侣》反复刷。"
        eng_tasks.append({"title": "【暑假起】英一真题+作文启动", "content": content, "hours": "稳步提升"})

    # Stage 3: Final push (8 weeks)
    for w in range(8):
        if w == 0:
            content = "✅ 重点二刷错题。\n✅ 把作文模板练熟练透。\n⚠️ 持续背单词，绝对不能断！"
        else:
            content = "✅ 二刷阅读错题 + 默写作文模板，保证上了考场就能直接写。"
        eng_tasks.append({"title": "【冲刺期】二刷真题+练熟模板", "content": content, "hours": "决战时刻"})

    # === Politics Stages (41 weeks) ===
    pol_tasks = []
    for w in range(30):
        pol_tasks.append(None) # March to October
        
    for w in range(8):
        if w == 0:
            content = "⚠️ 远离徐涛冗长课，远离肖1000题！\n✅ 腿姐冲刺背诵手册（熟读）。\n✅《苍盾小程序》每天刷一套(30选择题)。\n✅ 熟读澄箫宇“政治一页纸”。"
        else:
            content = "腿姐背诵手册 + 苍盾小程序每日一套选择题。\n保持碎片化时间学习，别占数学时间。"
        pol_tasks.append({"title": "【10月起】腿姐+苍盾+一页纸", "content": content, "hours": "碎片时间"})
        
    for w in range(3):
        if w == 0:
            content = "✅ 肖四出版，直接背大题（背不住没关系，对成绩影响不大）。\n🔥 准备看B站“考研政治抄材料”绝杀技巧！"
        else:
            content = "死背肖四，练一练B站“抄材料技巧”，上了考场基本只能抄材料。"
        pol_tasks.append({"title": "【冲刺期】肖四+抄材料", "content": content, "hours": "背诵强化"})

    # Ensure all lists have 41 items
    eng_tasks = eng_tasks[:41]
    pol_tasks = pol_tasks[:41]

    # Contextual, human-like Weekly Tips
    # Instead of cycling indiscriminately, we tailor them to the general flow of the 41 weeks.
    weekly_messages = [
        "开始复习了。头几周最难熬，别去听机构几百小时的废话长课，直接做基础题，做不会了就看B站切片视频讲解，效率最高。",
        "基础阶段学数学，懂了和能亲自算对完全是两码事。遇到不懂的题，硬着头皮先自己在草稿纸上划拉两步。",
        "别忘了给自己最重要的专业课留出固定时间！公共课安排再紧，专业课也不能停，它是拉分的关键。",
        "做题如果卡住超过两三分钟毫无头绪，直接看答案，看完自己再顺着写一遍。前期别跟一道题死磕三十分钟，没意义。",
        "真题是唯一的王道！别被各种机构的偏难怪题搞破防了。历年真题做透，远远胜过刷一打乱七八糟的模拟卷。",
        "张宇“超实数”、微分算子法、压缩映射原理、海涅定理等等，这些生僻考点直接跳过！连考150分的大佬都不需要看。",
        "英语千万不要搞什么‘手写精翻’，纯纯感动自己浪费生命。这几天核心就是疯狂背《不背单词》，刷脸熟就行。",
        "数学遇到死活想不通的结，直接去B站搜播放量高的干货UP主（比如千羽、考研数学777等），他们讲得比大机构透彻多了。",
        "有些题你这周可能就是看不懂，先抄在错题本上。过两周二刷回头看的时候往往会突然顿悟，这就是所谓的‘书读百遍其义自见’。",
        "所有习题册和哪怕后期出的模拟卷，里面的证明题一律直接划掉不做！咱们只死磕历年真题里的证明题，能省下几百个小时。",
        "时间一晃基础大半个月过去了，回头翻翻最初错的题，是不是觉得当初错得很离谱？保持这种纠错手感。",
        "别把自己当成只进不出的听课机器。每天学习结束前，花十五分钟在脑子里过一遍今天学到的核心考点（尤其是线代）。",
        "线代的逻辑感非常强。做它的题，要在脑子里画树状图，把它和之前章节的矩阵关联起来想。",
        "概率论相对套路极强，只要能把前面高数的一重/二重积分算得明明白白，概率论就是送分的。只做计算题！",
        "要开启大观了！请死死记住：大观里他讲每道题之前，你必须按暂停，自己先死磕算出个结果！不然等于白看。",
        "马上要启动英语真题阅读和作文模板了。不要精翻，保持每天只做阅读和背单词，顺便积累点作文的万能词汇。",
        "开始刷660选择填空了。记住‘速刷’的奥义：这题你2分钟没懂，看答案！660本来就是让你暴露知识盲区的。",
        "这周数学继续填坑。660题做错一大半都是正常的，因为它的考察视角极度刁钻。错题做好标记，后面回过头重做。",
        "速刷收尾阶段。别纠结正确率，纠结的是这道题背后你忘了哪个基本定理。",
        "《真题一本通》降临！这就是你整个备考期最核心的宝贝，真题最香。一定要搞个专属错题本，把它当圣经来供着。",
        "前期积累的所有技巧，在真题面前都要经历检验。遇到不熟悉的真题类型，赶紧翻之前记的笔记查漏补缺。",
        "真题计算量大得很，不要看一眼思路觉得‘啊我会了’就跳过，你考场上可能因为算错而丢掉10分大题。",
        "这几天是不是感觉有点疲了？撑住。这段时间正是拉开差距的分水岭，谁先放弃谁就输了。",
        "真题里的证明题就是你唯一需要碰的证明题。分析一下真题证明题的突破口往往就在拉格朗日或者泰勒里。",
        "英语阅读是不是错很多？没关系，去摸清楚出题人的坑。单词APP换成《真题伴侣》，专门背真题里的生冷意思。",
        "一本通第一轮结束了吧？现在你手里那本厚厚的错题本，就是保送你上岸的最强武器。",
        "二刷大观！这次你看视频的视角完全不一样了，因为你被真题毒打过了。重点找他讲的技巧是怎么对应到真题身上的。",
        "串联知识点，线代是不是觉得瞬间通透了？这一道题怎么又能考特征值又能考二次型还能考正定？搞懂这层逻辑。",
        "数一真题成套刷开启！每天上午给自己掐表3个小时。不管做成什么狗屎样，3小时一到必须停笔对答案。",
        "错题本开始发挥威力了。把真题卷子上做错的题，去你的错题本上找同类项，归在一起，你就知道自己哪里最烂了。",
        "政治开始进场！请记住：千万别看长视频，也别碰肖1000。每天碎片时间刷刷苍盾小程序就行，重心依然是数学和专业课。",
        "这周上了李林模拟卷，可能会被虐得很惨。别在意分数，李林卷子就是用来让你考场上见到新题不慌的。",
        "哪怕模拟卷只能考80分也别放弃，认真把错的知识点吸收掉，考场上你就是120分。",
        "武忠祥选填技巧课加上你的错题本，这就是最后的‘抢分组合拳’。特值法、图形法全用上。",
        "这几天重点开始背政治手册和积累政治一页纸，这东西性价比极高，每天看半个钟头足够了。",
        "进入倒计时阶段。别碰以前没见过的新怪题了，你现在需要做的是把近3年的真题翻出来，感受那股原汁原味的考风。",
        "把以前错的计算题拿出来，不看答案，重新在一张白纸上算到底。计算手感这时候绝不能凉。",
        "英语作文模板是不是已经脱口而出了？平时拿两篇历年真题，强行把你的万能模板套进去写写看。",
        "肖四终于来了！拿到手别废话，直接看大题的加粗黑体字开背。背不下来别焦虑，这玩意儿就是给大家一点心理安慰的。",
        "这周务必去B站看懂‘考研政治抄材料’的终极技巧。一旦考场上遇到完全没见过的肖四题，就靠这招拿分了。",
        "最后一周，保持良好作息。再翻翻错题本的基础概念，把文具准备好。上了考场，哪怕遇到难题也要死死咬住算完！\n\n兄弟，这一趟走到底，绝对岸上见！"
    ]
    
    for i in range(41):
        cur = start_date + timedelta(days=i*7)
        nxt = start_date + timedelta(days=i*7+6)
        
        msg = weekly_messages[i] if i < len(weekly_messages) else "稳步推进，坚持就是胜利。"
        
        week_data = {
            "week": i + 1,
            "dates": f"{cur.strftime('%m.%d')} - {nxt.strftime('%m.%d')}",
            "theme": math_tasks[i]["title"].split("】")[0].replace("【", ""),
            "message": msg,
            "math": math_tasks[i],
            "english": eng_tasks[i]
        }
        
        if pol_tasks[i]:
            week_data["politics"] = pol_tasks[i]
            
        weeks.append(week_data)

    data = {"student": "李白白", "weeks": weeks}
    
    with open("D:/myblog/source/kaoyan/李白白/libaibai.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    html_template = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>李白白 2027考研全程深度定制规划</title>
    <style>
        :root {
            --bg-color: #0a0a0f;
            --card-bg: #12121a;
            --text-color: #e0e0e0;
            --accent: #d946ef;
            --accent-light: #f472b6;
            --border-color: #2a2a3a;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Inter', 'Noto Sans SC', sans-serif;
            background: var(--bg-color);
            color: var(--text-color);
            line-height: 1.6;
            min-height: 100vh;
        }
        .container { max-width: 900px; margin: 0 auto; padding: 20px; }
        header {
            text-align: center;
            padding: 40px 20px;
            background: linear-gradient(135deg, #1a1a2e 0%, #311b3d 100%);
            border-radius: 16px;
            margin-bottom: 30px;
            border: 1px solid var(--border-color);
        }
        header h1 {
            font-size: 2rem;
            background: linear-gradient(90deg, var(--accent), var(--accent-light));
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 15px;
        }
        .meta { color: #888; font-size: 0.95rem; }
        .meta span { margin: 0 10px; display: inline-block; }
        .overview {
            background: linear-gradient(135deg, #1a1a2e 0%, #311b3d 100%);
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 30px;
            border: 1px solid var(--border-color);
        }
        .overview h2 {
            color: var(--accent-light);
            margin-bottom: 20px;
            font-size: 1.3rem;
            border-left: 4px solid var(--accent);
            padding-left: 10px;
        }
        .strategy {
            margin-bottom: 16px; 
            padding: 12px; 
            background: rgba(217, 70, 239, 0.15); 
            border-radius: 8px; 
            border-left: 3px solid var(--accent);
            color: #fff; 
            line-height: 1.8;
            font-size: 1.05rem;
        }
        .grid-box { display: grid; gap: 16px; margin-bottom: 20px; }
        .grid-item { padding: 18px; border-radius: 8px; }
        .grid-math { background: rgba(244,114,182,0.08); border-left: 3px solid #f472b6; }
        .grid-english { background: rgba(52,211,153,0.08); border-left: 3px solid #34d399; }
        .grid-politics { background: rgba(251,191,36,0.08); border-left: 3px solid #fbbf24; }
        
        h3 { margin-bottom: 12px; font-size: 1.1rem; }
        .grid-math h3 { color: #f472b6; }
        .grid-english h3 { color: #34d399; }
        .grid-politics h3 { color: #fbbf24; }
        
        ul { margin-left: 20px; color: #ddd; }
        li { margin-bottom: 8px; }
        
        .week-card {
            background: var(--card-bg);
            border-radius: 12px;
            margin-bottom: 20px;
            border: 1px solid var(--border-color);
            overflow: hidden;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .week-card:hover { transform: translateY(-2px); box-shadow: 0 8px 30px rgba(217, 70, 239, 0.15); }
        .week-header {
            background: linear-gradient(90deg, rgba(217, 70, 239, 0.2), rgba(217, 70, 239, 0.05));
            padding: 16px 20px; display: flex; justify-content: space-between; align-items: center; cursor: pointer;
        }
        .week-header h3 { font-size: 1.1rem; color: var(--accent-light); margin: 0; }
        .week-header .dates { color: #aaa; font-size: 0.9rem; font-family: monospace; }
        .week-content { padding: 20px; display: none; }
        .week-content.active { display: block; }
        .message {
            background: rgba(217, 70, 239, 0.1); padding: 14px 18px; border-radius: 8px;
            margin-bottom: 20px; border-left: 3px solid var(--accent); font-style: italic; font-weight: bold; color: #fff;
        }
        .subject { background: rgba(255, 255, 255, 0.03); border-radius: 8px; padding: 16px; margin-bottom: 16px; border: 1px solid rgba(255,255,255,0.05); }
        .subject-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 8px; }
        .subject-name { font-weight: bold; font-size: 1.05rem; }
        .subject-name.math { color: #f472b6; }
        .subject-name.english { color: #34d399; }
        .subject-name.politics { color: #fbbf24; }
        .hours { background: rgba(255, 255, 255, 0.1); padding: 4px 12px; border-radius: 12px; font-size: 0.85rem; color: #ddd; }
        .subject-title { font-weight: bold; margin-bottom: 8px; color: #fff; }
        .subject-content { color: #bbb; white-space: pre-line; font-size: 0.95rem; line-height: 1.7; }
        .expand-all { text-align: center; margin-bottom: 25px; }
        .expand-all button {
            background: var(--accent); color: white; border: none; padding: 12px 28px;
            border-radius: 8px; cursor: pointer; font-size: 1rem; font-weight: bold; transition: background 0.2s;
        }
        .expand-all button:hover { background: var(--accent-light); }
        footer { text-align: center; padding: 30px; color: #666; font-size: 0.9rem; margin-top: 20px; border-top: 1px solid var(--border-color); }
        
        @media(max-width: 600px) { .week-header { flex-direction: column; align-items: flex-start; gap: 8px; } }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>李白白 2027考研全程深度定制规划</h1>
            <div class="meta">
                <span>🎯 南京邮电大学·物联网学院</span>
                <span>📅 周期：2026.03.05 - 2026.12 考前 (共41周)</span>
            </div>
            <div class="meta" style="margin-top: 8px;">
                <span>📚 必考：数学一 / 英语一 / 政治 / 统考专业课</span>
            </div>
        </header>

        <!-- 总体规划概览 -->
        <div class="overview">
            <h2>🎯 全局时间红线与死磕原则</h2>
            
            <p class="strategy">
                <strong>🔥 核心绝杀：所有科目都不准当「耐听王」！听课永远学不会，只有通过做题才能真正在考场上写出来！多想多算多做，务必落实到笔头上！</strong><br><br>
                <span style="color: #ffb86c;">⚠️ 时间分配：抛开专业课，公共课的学习精力比重大致为数学 60%、英语 30%、政治 10%。注意，务必在自己的日常排期中优先把【专业课】的雷打不动时间固定下来。</span>
            </p>
            
            <div class="grid-box">
                <div class="grid-item grid-math">
                    <h3>📐 数学一（占公共课精力 60%）</h3>
                    <ul>
                        <li><strong style="color: #fff;">果断弃课投题：</strong>不推荐长期看张宇的课程！做题时不会的直接去B站搜播放量高的干货UP主（千羽、考研数学777、没咋了等），这比大机构长线视频效率高十倍！</li>
                        <li><strong style="color: #fff;">不需要学的部分：</strong>张宇“超实数”、微分算子法、海涅定理、压缩映射原理、stolz法则。目标150分的人也完全不需要看这些！</li>
                        <li><strong style="color: #fff;">练习策略铁律：</strong>真题分类最优先 -> 习题册往后推 -> 模拟题少做。<br>所有习题册+模拟卷【全部跳过证明题】，只手写历年真题里的证明题！</li>
                    </ul>
                </div>
                
                <div class="grid-item grid-english">
                    <h3>📖 英语一（占公共课精力 30%）</h3>
                    <ul>
                        <li><strong style="color: #fff;">底线原则：</strong>绝不买手译本精翻文章！少听课或不听课。前期只搞阅读和记单词，暑假中后期再慢慢切作文，考场一样拿高分。</li>
                        <li><strong style="color: #fff;">背诵死命推：</strong>暑假前只能疯狂用《不背单词》背核心3000词，最少刷3遍！中后期转入《真题伴侣》，着重背阅读语境里的生僻含义。</li>
                    </ul>
                </div>
                
                <div class="grid-item grid-politics">
                    <h3>🏛️ 政治（占公共课精力 10%）</h3>
                    <ul>
                        <li><strong style="color: #f43f5e;">🚫 10月初前绝对不动：</strong>最早10月初进场！绝不去听徐涛等名师几百小时课，坚决不用肖1000题题海战术！</li>
                        <li><strong style="color: #fff;">短平快收尾：</strong>买好腿姐冲刺背诵手册+《苍盾小程序》碎片刷选择。12月死背肖四大题（背不下来也无妨，只管写满）。最后几天B站搜索政治抄材料绝杀操作直接上考场。</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="expand-all">
            <button onclick="toggleAll()">展开/收起全部计划周</button>
        </div>

        <div id="weeks-container"></div>
        
        <footer>
            <p>💪 这份时间线没有任何花里胡哨，全是前人踩过的雷总结出的干货，执行到底必定上岸！</p>
        </footer>
    </div>

    <script>
    const planData = ''' + json.dumps(data["weeks"], ensure_ascii=False) + ''';

    function renderWeeks() {
        const container = document.getElementById('weeks-container');
        planData.forEach((week, index) => {
            const card = document.createElement('div');
            card.className = 'week-card';

            let subjectsHtml = `
                <div class="subject">
                    <div class="subject-header">
                        <span class="subject-name math">📐 数学</span>
                        <span class="hours">${week.math.hours}</span>
                    </div>
                    <div class="subject-title">${week.math.title}</div>
                    <div class="subject-content">${week.math.content.replace(/\\n/g, '<br/>')}</div>
                </div>
                <div class="subject">
                    <div class="subject-header">
                        <span class="subject-name english">📖 英语</span>
                        <span class="hours">${week.english.hours}</span>
                    </div>
                    <div class="subject-title">${week.english.title}</div>
                    <div class="subject-content">${week.english.content.replace(/\\n/g, '<br/>')}</div>
                </div>
            `;

            if (week.politics) {
                subjectsHtml += `
                    <div class="subject">
                        <div class="subject-header">
                            <span class="subject-name politics">🏛️ 政治</span>
                            <span class="hours">${week.politics.hours}</span>
                        </div>
                        <div class="subject-title">${week.politics.title}</div>
                        <div class="subject-content">${week.politics.content.replace(/\\n/g, '<br/>')}</div>
                    </div>
                `;
            }

            card.innerHTML = `
                <div class="week-header" onclick="toggleWeek(${index})">
                    <h3>第 ${week.week} 周：${week.theme}</h3>
                    <span class="dates">${week.dates}</span>
                </div>
                <div class="week-content" id="week-${index}">
                    <div class="message">💡 ${week.message}</div>
                    ${subjectsHtml}
                </div>
            `;

            container.appendChild(card);
        });

        document.getElementById('week-0').classList.add('active');
    }

    function toggleWeek(index) {
        document.getElementById('week-' + index).classList.toggle('active');
    }

    let allExpanded = false;
    function toggleAll() {
        allExpanded = !allExpanded;
        document.querySelectorAll('.week-content').forEach(el => {
            el.classList.toggle('active', allExpanded);
        });
    }

    renderWeeks();
    </script>
</body>
</html>
'''

    with open("D:/myblog/source/kaoyan/李白白/libaibai.html", "w", encoding="utf-8") as f:
        f.write(html_template)
        
if __name__ == "__main__":
    build()
