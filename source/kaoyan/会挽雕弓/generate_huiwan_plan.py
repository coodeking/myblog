import json
from datetime import datetime, timedelta

def get_full_plan():
    weeks = []
    start_date = datetime(2026, 3, 12)
    
    def get_date_str(week_idx):
        s = start_date + timedelta(days=(week_idx-1)*7)
        e = s + timedelta(days=6)
        return f"{s.strftime('%m.%d')} - {e.strftime('%m.%d')}"

    def add_week(week_num, theme, msg, math_task=None, eng_task=None, pol_task=None, mind_task=None):
        dates = get_date_str(week_num)
        week_data = {
            "week": week_num,
            "dates": dates,
            "theme": theme,
            "message": msg
        }
        if math_task: week_data["math"] = math_task
        if eng_task: week_data["english"] = eng_task
        if pol_task: week_data["politics"] = pol_task
        if mind_task: week_data["mindset"] = mind_task
        weeks.append(week_data)

    weekly_messages = [
        "考研不仅是知识的比拼，更是习惯的较量。这周起，每天规律作息，让身体进入每天要高强度思考的轨道。",
        "基础阶段学数学常常会觉得吃力。遇到卡壳的地方不要死磕，用好B站的高频解题UP主资源，效率能翻倍。",
        "背单词的核心只有一点：重复。不要企图一次性记住，要忍受遗忘的挫败感，让软件替你安排多轮滚动。",
        "做数学课后题时，切记要亲自动手算出最终结果。在演草纸上写下的每一步，才是真正属于你的实力。",
        "考研备考不需要大量无目的地听课。听课永远是被动输入，做题才是主动输出，考场上只看你的输出能力。",
        "英语前期如果实在想看点什么，可以稍微了解下长难句主谓宾成分分析，但千万不要去背厚重的语法书。",
        "数学的1000题基础篇重点是夯实概念。错题一定要在旁边标注：我是公式没记住，还是思路没打开？",
        "复习过程中不要去和别人比进度。每个人的基础和目标都不一样，守好自己的复习节奏，稳扎稳打。",
        "学习的至高境界是沉浸。学习时把手机放在视线之外的房间里，每天哪怕只有3小时的绝对专注，也远胜过8小时的假努力。",
        "英语单词进行到一定程度会遇到“看脸熟但想不起意思”的瓶颈。坚持下去，量变即将引起质变。",
        
        "数学大观的学习是思维方式的跃升。视频里的每一道题，必须暂停自己先尝试破解，这比听懂十道题更重要。",
        "做错的题目是宝藏。如果你把错题放任不管，那你在考场上大概率还会栽在它手里。复盘并二次攻克是关键。",
        "天气渐渐变热，人容易烦躁。这时候更需要心理的定力。把专业课的阅读和英语单词当成调节心情的读物。",
        "背单词千万不要陷入每个都精通的误区，考研英语是阅读为主，你能扫一眼英文反应出中文大概意思就足够了。",
        "澄箫宇的大观强度很高。遇到听得很吃力的集数，允许自己放慢速度，分两次消化，确保每一步梳理清晰。",
        "不要去过度钻研那些偏难怪的概念。诸如超实数、斯托尔茨定理这些，对于我们来说性价比极低，果断跳过。",
        
        "660题一阶速刷的核心是“速”。如果一道题两分钟内毫无头绪，说明这是你的盲区盲点，直接看解析标记这才是最高效的。",
        "暑期开始，正式踏入英语二的真题战场。这时候《真题伴侣》就是你的绝佳武器，在语境中去攻克生词。",
        "虽然660题都是填空和选择，但也要当成大题来算。对于计算失误导致的丢分，必须给自己敲响警钟。",
        "做英语早年真题时，重点去分析正确选项是如何在原文中进行“同义替换”的，这是英语最核心的出题套路。",
        "速刷阶段难免会受到打击。记住，这些练习册的错题不代表你考场上的分数，它们只是用来扫雷的工具。",
        
        "拿到真题一本通，意味着我们开始触摸真实的考场水准。这本资料是所有习题的核心，必须建立专属的真题错题本。",
        "英语阅读做完后，把妨碍你理解长难句的关键生词摘抄下来。千万不要去一字一句地通篇精翻，不要做无用功。",
        "于文涛的真题分类极具代表性。在做这些题时，要培养跨章节综合运用知识点的能力，学会建立属于自己的解题地图。",
        "持续三个多月的复习后可能会出现一段时间的疲惫厌学期。可以给自己放半天假彻底休息，回来再全速前进。",
        "英语真题里的干扰项通常都设计得很巧妙。学会识别哪些是“无中生有”，哪些是“张冠李戴”，提升解题敏锐度。",
        
        "二刷大观的时候，你的视角会和第一次完全不同。那些曾经生涩的方法，现在应该能自然而然地流淌在你的笔端。",
        "此时专业课应该已经进入了密集突破期。每天统筹好三门课程的时间，不要因为一科遇到困难就完全逃避不看。",
        "政治复习终于可以渐渐提上日程了。但记住，你的任务只是每天翻翻背诵手册磨眼睛，绝不需要去听长篇大论的基础课。",
        "英语作文也是一种固定输出。在跟 Monkey 老师的视频时，重点吸收他不同模板的搭建结构，然后开始整理属于自己的通用金句。",
        
        "十一月份，真题套卷的限时演练正式拉开帷幕。每天必须要扛住真实考卷带来的压力测试，不看分数只看纰漏。",
        "政治的选择题是决定性分数的下限护城河。利用苍盾小程序每天保持手感，遇到错题扫一眼解析记住知识点即可。",
        "成套真题容易暴露一些冷僻的边角料知识。比如物理应用等，这时候去看一些专门的选填技巧课或者冲刺视频精准补漏。",
        "英语作文模板不能仅仅停留在脑海里。从这周开始，必须保证每周亲手在纸上默写两次，熟悉版面和控制字迹清晰。",
        "每天早上定好闹钟，作息时间必须向正式考试靠拢。考场如同战场，不仅要比拼脑力，也是体力和生物钟的考验。",
        
        "李林模拟套卷的计算量会略大于真题。这是极好的抗压训练，教你在遇到完全做不出的题目时，如何果断放弃止损。",
        "冲刺阶段的疲惫感达到顶峰感冒频发。注意保暖健康第一，每天除了高压模拟就是看自己的专属错题本。",
        "政治开始利用澄箫宇的一页纸疯狂提炼关键年份和人物事件。不需要全篇背诵，只要提取能做对单选题的关键词语。",
        "越临近考试越容易自我怀疑。所有的焦虑都来源于想得太多做得太少。把你的目光重新聚焦到眼前这道题上。",
        
        "最后阶段，最重要的资料就是最近三年的真题和自己整理的错题本。把它们看透，比做任何新的押题卷都管用十倍。",
        "肖四终于出版了，拿起它疯狂狂热地背诵大题。即便到了考场上发现很多并不是原题，那些背过的术语也是你要写上去的基本分骨架。",
        "考前最后几天的必修课：系统学习B站最新的‘考研政治材料抄写绝技’，掌握如何结合材料和背诵过的术语组装出一片饱满的回答。上场，交卷，静候佳音！"
    ]

    # Phase 1: 1000题基础与三十讲 (W1-W10 / 3月中 - 5月中)
    for w in range(1, 11):
        add_week(
            w,
            f"基础复习与计算（第{w}周）",
            weekly_messages[w-1],
            {
                "title": "推进《基础三十讲》与1000题基础篇",
                "hours": "~60%",
                "content": "✅ 本周任务：以练带学，重点突破高数（或线代）基础模块。\n看三十讲讲义后立刻做课后题和1000题。不懂的地方不要看张宇长课，直接去B站搜‘千羽’、‘考研数学777’或‘没咋了’的针对性视频！\n🚫 禁忌法则：所有习题册不做证明题；果断跳过：超实数/微分算子法/海涅定理/压缩映射原理/stolz等超纲考点。"
            },
            {
                "title": "核心词汇背诵",
                "hours": "~30%",
                "content": "✅ 本周安排：只有一个任务——打开《不背单词》，刷大纲词汇。\n目标是在暑假前无论如何必须刷够3遍。不听英语基础课，不买手译本，不逐字精翻文章。"
            },
            None,
            {
                "title": "注意事项",
                "hours": "执行力",
                "content": "保持多算多练。除了数学和英语，记得按自己的进度安排专业课的学习。政治目前不用看。"
            }
        )

    # Phase 2: 澄箫宇大观首开 (W11-W16 / 5月下旬 - 6月下旬)
    for w in range(11, 17):
        add_week(
            w,
            f"大观学习阶段（第{w}周）",
            weekly_messages[w-1],
            {
                "title": "B站“澄箫宇”大观系列首刷",
                "hours": "~60%",
                "content": "✅ 本周任务：按每2天看明白一个“大观”的进度推进（共约7个大观）。\n⚠️ 纪律要求：讲每一道题之前必须暂停视频，自己在草稿纸上动手做一遍！听完后再理清做题思路。"
            },
            {
                "title": "持续背诵单词",
                "hours": "~30%",
                "content": "✅ 本周安排：离暑假不到一个月，英语依然专注维持词汇复习频率。\n坚持用碎片时间过词条，为暑假做真题打基础。"
            },
            None,
            {
                "title": "精力分配",
                "hours": "执行力",
                "content": "大观里面的综合题目比较耗费精力。如果在数学上卡住了，可以先去看看专业课换一下脑子。"
            }
        )

    # Phase 3: 660一阶速刷 (W17-W21 / 7月暑假伊始)
    for w in range(17, 22):
        add_week(
            w,
            f"一阶速刷与英语真题初探（第{w}周）",
            weekly_messages[w-1],
            {
                "title": "《660题》一阶速刷",
                "hours": "~60%",
                "content": "✅ 本周任务：开始速刷660选择题（同样不做证明题）。\n⚠️ 速刷判定律：看到题目，2分钟内没有思路的直接跳过看答案订正。把节约下来的时间用来巩固基础漏洞。"
            },
            {
                "title": "英语二真题入场（无作文版）",
                "hours": "~30%",
                "content": "✅ 本周安排：暑假正式开启，每两天做一套英语二真题（跳过作文），熟悉出题方向。\n要求配合使用《真题伴侣》APP，在刷真题的过程中直接把不认识的词标记反复背诵。\n（《不背单词》的日常复习同样不能断）"
            },
            None,
            {
                "title": "错题对待",
                "hours": "执行力",
                "content": "660做错很正常。把错题背后的共性考点提炼出来，多总结才是关键。"
            }
        )

    # Phase 4: 真题一本通 (W22-W26 / 8月期间)
    for w in range(22, 27):
        add_week(
            w,
            f"真题分类训练（第{w}周）",
            weekly_messages[w-1],
            {
                "title": "《真题一本通(于文涛)》",
                "hours": "~60%",
                "content": "✅ 本周任务：重点做真题一本通，这是整个考研期间最重要的习题册。\n👑 要求：建立真题错题本，按章节分类。平时练习的证明题只从真题里做，搞懂每一道错题是现阶段的核心任务。"
            },
            {
                "title": "真题阅读语境记忆",
                "hours": "~30%",
                "content": "✅ 本周安排：维持2天一套的真题（阅读为主）做题速度。\n利用这段时间把之前用APP里遇到的标记生词全部复习一遍，适应语境里的同义词替换。"
            },
            None,
            {
                "title": "学习状态",
                "hours": "执行力",
                "content": "进入8月后容易急躁。专业课的时间要稳定好，如果感觉累可以适当休息半天天调整一下。"
            }
        )

    # Phase 5: 大观二刷 (W27-W30 / 9月期间)
    for w in range(27, 31):
        add_week(
            w,
            f"大观二刷与作文开始（第{w}周）",
            weekly_messages[w-1],
            {
                "title": "澄箫宇“大观”二刷",
                "hours": "~60%",
                "content": "✅ 本周任务：二刷大观系列。\n做完真题后再来看大观总结的方法，体会他的思路。把新领悟的解题方法补到错题本旁边。"
            },
            {
                "title": "Monkey老师作文模板入场",
                "hours": "~30%",
                "content": "✅ 本周安排：真题阅读照旧推进。\n开始看《Monkey老师》考研英语作文模板课。只需要背他的模板即可，平时自己用本子累积图表、环保、哲理类的常用替换词。"
            },
            {
                "title": "政治初步开始",
                "hours": "~10%",
                "content": "✅ 本周安排：买一本《腿姐冲刺背诵手册》，不需要听长课。把它当睡前读物每天看一看，熟悉一下基本概念。"
            },
            {
                "title": "提醒",
                "hours": "执行力",
                "content": "9月份不要过度在意别人的进度，按部就班做自己的错题分析最重要。"
            }
        )

    # Phase 6: 套卷真题 09-26 (W31-W35 / 10月 - 11月上旬)
    for w in range(31, 36):
        add_week(
            w,
            f"成套真题演练（第{w}周）",
            weekly_messages[w-1],
            {
                "title": "数二成套真题练习",
                "hours": "~50%",
                "content": "✅ 本周任务：每天一套数二真题（09-26年）。最好在上午严格按照3小时测试。\n测试完整理错题本，并把暴露出来的弱势题型分类回看。"
            },
            {
                "title": "二刷真题与模板练习",
                "hours": "~30%",
                "content": "✅ 本周安排：进入英语真题二刷期，重点在理解错题。\n拿到作文模板后要动笔练习，将Monkey的模板套用在历年的真题上写两次。"
            },
            {
                "title": "小程序日测与一页纸",
                "hours": "~15%",
                "content": "✅ 本周安排：每天用《苍盾小程序》刷一套模拟卷的单选题（30个左右）。\n配合读澄箫宇《政治一页纸》，掌握重要事件。"
            },
            {
                "title": "心态提醒",
                "hours": "执行力",
                "content": "成套真题可能会出现分数不高的情况，重点是要发现盲区，而不是执着于分数。"
            }
        )

    # Phase 7: 李林6+4冲刺 (W36-W39 / 11月中旬 - 12月上旬)
    for w in range(36, 40):
        add_week(
            w,
            f"模拟卷测试与补漏（第{w}周）",
            weekly_messages[w-1],
            {
                "title": "《李林6+4》模拟卷",
                "hours": "~50%",
                "content": "✅ 本周任务：每天做一套李林预测卷适应强度。\n有空余时间可以看看武忠祥的选填技巧课。发现卷子里某个题型不会，就去B站找对应题型的网课短视频补充。"
            },
            {
                "title": "单词维持与熟练模板",
                "hours": "~30%",
                "content": "✅ 本周安排：做英语二没做完的几年真题。\n单词复习保持每天看，Monkey作文模板要非常熟练地能写出来。"
            },
            {
                "title": "政治选择题突击",
                "hours": "~15%",
                "content": "✅ 本周安排：小程序多留意时政部分，以及自己经常选错的多选题考点。"
            },
            {
                "title": "保暖与健康",
                "hours": "执行力",
                "content": "年底天气冷，注意保暖。专业课的背诵也要稳步推进。"
            }
        )

    # Phase 8: 近三年倒查与肖四起手 (W40-W42 / 考前12月中下旬)
    for w in range(40, 43):
        add_week(
            w,
            f"考前收尾冲刺（第{w}周）",
            weekly_messages[w-1],
            {
                "title": "近三年真题定盘与错题复盘",
                "hours": "~50%",
                "content": "✅ 终极任务：近3年的真题留到现在刷一遍熟悉考试卷面手感。\n剩下的时间只看错题本和模拟卷错题本。重点复习以前做错的题型。"
            },
            {
                "title": "英语模板默写",
                "hours": "~20%",
                "content": "✅ 终极任务：每天拿A4纸默写一遍图表作文、小书信模板，保证字迹清晰和排版。"
            },
            {
                "title": "肖四背诵与抄材料",
                "hours": "~20%",
                "content": "✅ 终极任务：肖四出版后，多重复背诵它的大题。\n务必在B站搜一下“考研政治怎么抄材料”。考场上如果没遇到原题，就要利用材料段落结合背过的术语来作答。"
            },
            {
                "title": "考前嘱咐",
                "hours": "执行力",
                "content": "调整好作息，上午看数学和政治，下午看英语和专业课，平稳坚持到考试结束。"
            }
        )

    data = {"student": "会挽雕弓", "weeks": weeks[:42]}
    
    # Generate HTML matching the Li Baibai dark theme layout perfectly
    html_template = '''---
title: 会挽雕弓 专属定制考研规划
date: 2026-03-12
password: weijian
message: 专属内容需校验密码
---
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>会挽雕弓 2027考研深度定制规划</title>
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
            font-size: 2.2rem;
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
        .grid-english { background: rgba(52,211,153,0.08); border-left: 3px solid #34d399; }
        .grid-politics { background: rgba(251,191,36,0.08); border-left: 3px solid #fbbf24; }
        .grid-math { background: rgba(59, 130, 246, 0.08); border-left: 3px solid #3b82f6; }
        
        h3 { margin-bottom: 12px; font-size: 1.1rem; }
        .grid-math h3 { color: #3b82f6; }
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
        .subject-name.math { color: #3b82f6; }
        .subject-name.english { color: #34d399; }
        .subject-name.politics { color: #fbbf24; }
        .subject-name.mindset { color: #8b5cf6; }
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
            <h1>会挽雕弓 2027考研全程深度定制规划</h1>
            <div class="meta">
                <span>🎯 目标院校：未定 (根据进度冲高)</span>
                <span>📅 周期：2026.03.12 - 2026.12 (共42周)</span>
            </div>
            <div class="meta" style="margin-top: 8px;">
                <span>📚 必考科目：专硕备考 / 数学二 / 英语二 / 政治 / 专业课安排于暗时间</span>
            </div>
        </header>
        
        <!-- 总体规划概览 -->
        <div class="overview">
            <h2>🎯 全局核心原则</h2>
            
            <p class="strategy">
                <strong>🔥 所有科目都不要光听不练！多想多算多做，一切落实到笔头上。很多内容不是听课能学会的，而是靠做题练会的！</strong><br><br>
                <span style="color: #ffb86c;">⚠️ 三科总时间分布（已经预留了专业课学习时间）：数学占绝对大头约 60% / 英语约 30% / 政治约 10%。</span>
            </p>
            
            <div class="grid-box">
                <div class="grid-item grid-math">
                    <h3>📐 数学复习建议</h3>
                    <ul>
                        <li><strong style="color: #fff;">以练带学：</strong>不要大量看张宇的长课！自己先看基础三十讲讲义，然后直接做课后题 + 《1000题》基础。如果遇到不懂的知识点才选择性看网课。</li>
                        <li><strong style="color: #fff;">UP主救场：</strong>不会做的题以及对应的知识点，去B站找播放高、讲得清楚的短视频，推荐UP主：<strong>千羽、考研数学777、没咋了</strong>，远胜传统大机构。</li>
                        <li><strong style="color: #fff;">跳过超纲知识点：</strong>想考150也不需要看张宇的“超实数”、微分算子法、海涅定理、压缩映射原理、stolz！</li>
                        <li><strong style="color: #fff;">习题要求：</strong>除最后真题卷外，所有的平时练习册与模拟卷，<strong>只专注计算，全都不做证明题</strong>！真题必须按套死磕《真题一本通》（于文涛）。</li>
                    </ul>
                </div>
                
                <div class="grid-item grid-english">
                    <h3>📖 英语二复习建议</h3>
                    <ul>
                        <li><strong style="color: #fff;">减少听课：</strong>考研英语少听课或者不听课！不精翻文章，千万不要去买巨厚的手译本！</li>
                        <li><strong style="color: #fff;">重视单词：</strong>暑假前唯一的任务就是《不背单词》APP过三遍。暑假开始，利用《真题伴侣》APP在刷真题的过程中精准背诵阅读原版文里的生词。</li>
                        <li><strong style="color: #fff;">作文模板：</strong>后期直接看《Monkey老师》英语作文模板课，只要背下他的底层逻辑和模板套路，加上自己搜集替换词，最后考场默写即可。</li>
                    </ul>
                </div>
                
                <div class="grid-item grid-politics">
                    <h3>🏛️ 政治复习建议</h3>
                    <ul>
                        <li><strong style="color: #f43f5e;">控制时间：</strong>最早10月初才开始。远离各类名师的百时大课，抛弃厚重的肖1000题。</li>
                        <li><strong style="color: #fff;">前期准备：</strong>用《腿姐冲刺背诵手册》熟读，再结合澄箫宇“政治一页纸”。练习只用《苍盾小程序》每日随手刷一天一套选择题巩固考点。</li>
                        <li><strong style="color: #fff;">冲刺阶段：</strong>后期只背肖四大题，背不完也无妨。一定要在B站学会<strong>“考研政治抄材料怎么抄”</strong>的技巧，直接带着材料与原理上考场。</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="expand-all">
            <button onclick="toggleAll()">展开/收起全部计划周</button>
        </div>

        <div id="weeks-container"></div>
        
        <footer>
            <p>💪 这份时间线抛弃了一切形式主义的花哨包装。执行比完美更重要，别再只看不练，向着岸边冲刺吧！</p>
        </footer>
    </div>

    <script>
    const planData = ''' + json.dumps(data["weeks"], ensure_ascii=False) + ''';

    function renderWeeks() {
        const container = document.getElementById('weeks-container');
        planData.forEach((week, index) => {
            const card = document.createElement('div');
            card.className = 'week-card';

            let subjectsHtml = '';
            
            if (week.math) {
                subjectsHtml += `
                    <div class="subject">
                        <div class="subject-header">
                            <span class="subject-name math">📐 数学二</span>
                            <span class="hours">${week.math.hours}</span>
                        </div>
                        <div class="subject-title">${week.math.title}</div>
                        <div class="subject-content">${week.math.content.replace(/\\n/g, '<br/>')}</div>
                    </div>
                `;
            }

            if (week.english) {
                subjectsHtml += `
                    <div class="subject">
                        <div class="subject-header">
                            <span class="subject-name english">📖 英语二</span>
                            <span class="hours">${week.english.hours}</span>
                        </div>
                        <div class="subject-title">${week.english.title}</div>
                        <div class="subject-content">${week.english.content.replace(/\\n/g, '<br/>')}</div>
                    </div>
                `;
            }

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

            if (week.mindset) {
                subjectsHtml += `
                    <div class="subject">
                        <div class="subject-header">
                            <span class="subject-name mindset">💡 阶段指北</span>
                            <span class="hours">${week.mindset.hours}</span>
                        </div>
                        <div class="subject-title">${week.mindset.title}</div>
                        <div class="subject-content">${week.mindset.content.replace(/\\n/g, '<br/>')}</div>
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

    with open("D:/myblog/source/kaoyan/会挽雕弓.html", "w", encoding="utf-8") as f:
        f.write(html_template)
        
if __name__ == "__main__":
    get_full_plan()
