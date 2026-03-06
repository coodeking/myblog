# -*- coding: utf-8 -*-
import json
from datetime import datetime, timedelta

def get_full_plan_student_6():
    weeks = []
    # 兔子起始日期 2026年3月6日
    start_date = datetime(2026, 3, 6)
    
    def get_date_str(week_idx):
        s = start_date + timedelta(days=(week_idx-1)*7)
        e = s + timedelta(days=6)
        return f"{s.strftime('%m.%d')} - {e.strftime('%m.%d')}"

    def add_week(week_num, theme, msg, eng, pol=None, mind=None):
        dates = get_date_str(week_num)
        week_data = {
            "week": week_num,
            "dates": dates,
            "theme": theme,
            "message": msg,
            "english": eng
        }
        if pol:
            week_data["politics"] = pol
        if mind:
            week_data["mindset"] = mind
        weeks.append(week_data)

    # 41个真实的干货经验补充（语气客观、平实）
    tips = [
        "（复习建议：备考初期不需要制定过于完美的计划，每天只要能打开学习资料坚持看一会儿就好，执行比计划重要。）",
        "（复习建议：考研英语二的核心在于认识词汇。不需要默写拼写，也不要花时间逐字逐句翻译，那样效率不高。）",
        "（复习建议：每天的基本任务必须明确。比如遇到突发情况，其他任务可以缩减，但每天规定的50个单词最好看完。）",
        "（复习建议：基础较弱的同学初期会觉得单词记不住，这是正常的。用背单词软件反复多过几次，慢慢就有印象了。）",
        "（复习建议：英语阅读理解占分很大。早期可以通过分析简单文章里的句子主谓宾结构来预热，不用买很厚实的语法书。）",
        "（复习建议：复习资料选几套好的就行，不用买太多。选定《不背单词》或《真题伴侣》等工具，坚持用到底即可。）",
        "（复习建议：第一轮背单词时，只用看软件提供的最常见意思，一词多义的问题等后期做真题时自然会遇到并解决。）",
        "（复习建议：周末是拉开差距的好时间。平时保持单词不间断，周末则可以用来处理稍微耗时的专业课基础阅读或难点拆解。）",
        "（复习建议：遇到看不懂的长句，不需要弄懂每个从句的名字。只要能分辨主语和它发出的动作，能猜出大概意思就可以了。）",
        "（复习建议：前期不需要把时间和精力花在英语完型填空上，性价比太低。先把时间留给背单词和做阅读理解。）",
        "（复习建议：政治复习在8月份之前不需要启动。太早背政治容易遗忘，而且也会占用复习专业课的时间。）",
        "（复习建议：专业课的分数占比很高。建议每天在日程表里划出一段固定的时间，专门用来学习专业课基础知识。）",
        "（复习建议：随着词汇量的累积，可能会在某段时间感觉什么都记不住。这是学习的正常瓶颈期，坚持看下去就能突破。）",
        "（复习建议：英语二阅读理解的真题是最好的资料。不要去做市面上自己编的模拟题，只要反复研究真题即可。）",
        "（复习建议：刚上手真题阅读理解时错得比较多是正常的。我们要重点分析是因为单词不认识导致的，还是自己想偏了掉进了陷阱。）",
        "（复习建议：英语二的正确答案往往是对原文的同义替换。做完真题后，可以重点把题干、正确选项与原文的替换词记下来。）",
        "（复习建议：偶尔因为事情打断了复习可以理解。如果某天没学习，第二天接着之前的进度继续看就行，不要因此觉得要全盘放弃。）",
        "（复习建议：阅读速度的提升不在于读得多快，而在于定位准确。带着题目的关键词去原文里找，能省下不少时间。）",
        "（复习建议：如果做真题时总是错同一种类型的题，建议去网上搜索唐迟老师相关的阅读技巧讲解，调整一下做题思路。）",
        "（复习建议：基础打好后，借助《真题伴侣》这类专门提取真卷文章单词的软件，能直接高效地解决试卷上的生词问题。）",
        "（复习建议：完型填空和新题型（比如多项对应）通常等到第一遍真题阅读（10年以上）刷完后再集中看看，掌握方法后再做会容易点。）",
        "（复习建议：考研英语的错题本不需要抄写很长的句子，只要记录原文中妨碍你理解的生僻词，以及可能用到的作文句型就可以。）",
        "（复习建议：英语二的翻译是一整个段落，连贯性比较强。训练时多注意前后的语境，只要翻译出来的句子通顺即可给分。）",
        "（复习建议：英语二的大作文大多是图表作文（如饼图、柱状图）。平时注意多积累描述“上升、下降、保持平稳”等趋势的词语。）",
        "（复习建议：英语作文不需要自己去创造太难的新句型。可以参考王江涛或刘晓艳的范文结构，多练习几次，考场上直接套用能省时间。）",
        "（复习建议：周末抽半个小时出来，在纸上凭记忆写一遍自己常用的作文框架，看看有没有基础的拼写错误。）",
        "（复习建议：政治开始复习的时候，如果觉得书本有些枯燥，可以听徐涛的课当成入门；如果有一定基础，直接看书做题也可以。）",
        "（复习建议：政治的选择题是得分的关键。平时多用《苍盾小程序》或肖1000题做练习，通过错题来巩固那些细碎的知识点。）",
        "（复习建议：政治前期不需要大段地背诵课文，尤其是马哲部分，关键在于理解。背诵任务主要留到后期的冲刺阶段进行。）",
        "（复习建议：复习很考验精力的安排。晚上感觉比较疲惫时，适合刷刷政治选择题或者背背单词这样难度不大的学习任务。）",
        "（复习建议：英语阅读如果遇到看了解析也完全弄不懂的难题，可以直接跳过。考试允许有一定的容错率，不用对一道题钻牛角尖。）",
        "（复习建议：再次做英语真题的时候，尽量不要凭记忆直接选答案，要试着在原文中重新找一次依据，验证一下自己的做题逻辑。）",
        "（复习建议：10月份以后，可以买一本《腿姐冲刺背诵手册》，利用零散的时间拿出来翻看，慢慢理清政治知识点的脉络。）",
        "（复习建议：到了11月，建议每三到四天做一套完整的英语二真题，控制在3小时以内做完，培养好考场的做题节奏。）",
        "（复习建议：冲刺阶段一定多动笔。平时练习写英语作文时，拿出一张类似的答题卡网格纸去认真写，感受真实的字距大小。）",
        "（复习建议：对于政治时政热点不用过于心急。大部分辅导老师会在11月出相关的时政总结，到时候直接看他们归纳好的重点就行了。）",
        "（复习建议：英语完型填空如果实在做不顺手，考场上把觉得有把握的选了，剩下的不要耗太久，争取把时间留给阅读和作文。）",
        "（复习建议：12月《肖四》出来后，抓紧背诵里面的大题。只要能把加粗的标题和骨干句子背熟，在考场上就能有话可写。）",
        "（复习建议：政治主观题是有答题方法的。考试时如果遇到没准备的题目，要学会结合阅读材料和政治术语进行分点作答来获得一定的分数。）",
        "（复习建议：临近考试时，尽量把作息规律调整得和考试时间一致，保证上午考政治和下午考英语的时候，自己的精神状态是最好的。）",
        "（复习建议：考试时遇到生词或偏难题，直接先跳过去做下一道。首要任务是把那些自己能平稳拿下的分数全都装进口袋。）"
    ]

    # ================= 基础词汇与初级探索期 (Week 1-22) 政治不启动 =================
    
    add_week(1, "习惯养成：零基础起步", 
             "备考初期的核心是建立每天学习的习惯，不要间断。本周唯一的重点是把单词看起来。\n" + tips[0],
             {"title": "词汇破冰：只看不深究", "content": "✅ 核心任务：下载《不背单词》或扇贝等软件，设定每天词汇量任务。\n操作建议：完全不需要拼写。只需要看一眼英文能条件反射出它的中文意思就可以。如果想不出来，直接看答案，交给软件去安排复习。平时可以准备个小本子，随手记下几个最容易忘的重点词汇以便睡前复看。"},
             None,
             {"title": "日常精力建议", "content": "把需要大块时间的复习内容放在周末或者假期。平时下班或课余时间，就执行背单词这类简单、不用深度思考的任务，降低学习的启动阻力。晚上学习时可以在桌上放杯水，让自己安静下来。"})

    add_week(2, "词汇循环：克服遗忘焦虑", 
             "单词背了忘是很正常的，不需要为此感到挫败。英语考的就是我们在长期重复中的坚持。\n" + tips[1],
             {"title": "持续复习大纲单词", "content": "✅ 核心任务：每天完成APP里分配的新词和复习词。\n不需要买手译本来逐字精翻。如果碰巧阅读到带有刚刚背过生词的短文，留意一下单词在句子里的实际用法会更好。"},
             None,
             {"title": "心态调整", "content": "允许自己有复习状态不好的日子。只要每天坚持翻看，进度就会稳步前进。周末的时候可以把这一周没完成的小任务稍微补齐一下。"})

    add_week(3, "阅读预热：了解句子的基本骨架", 
             "单词输入两周后，可以尝试大概了解最基础的语法拆分方式，主要是为了看懂长句子。\n" + tips[8],
             {"title": "简单了解长难句成分", "content": "✅ 任务：如果觉得看英语长句有点晕，可以去B站搜几个讲“如何划分主谓宾”的短视频。\n目标：能看出这句话的主语是谁，做了一个什么动作就行了，其他修饰的词当作形容词来看待就好。看完视频可以在早年真题里找一两句话练练手，巩固一下对主谓宾的印象。"},
             None,
             {"title": "专业课安排提示", "content": "专业课分数很高，每天请务必抽出一点时间（甚至只是看十分钟书）来保持专业课的学习进度，并在日程表上勾选完成情况。"})

    for i in range(4, 14):
        msg = tips[i-1]
        add_week(i, f"词汇持续积累期 (第{i}周)", 
                 "这段时间复习比较单调。现在还不背政治，就是拼每天背单词和看书的毅力。\n" + msg,
                 {"title": "单词继续滚动", "content": "✅ 任务：继续跟着单词软件稳步复习，目标是把大纲词汇仔细过完第一遍。\n可以在背单词的间隙多看一眼它的常见搭配词组。平时看到专业课文献里的英文时也可以顺便留心一下它。"},
                 None,
                 {"title": "整块时间利用", "content": "利用周末或休息日去处理专业课教材中需要深度理解的复杂部分。平时就用单词复习来保持大脑里的英语语感。"})

    # ================= 英语真题阅读初期 (Week 14-23) 此阶段政治依然不加 =================

    add_week(14, "英语二真题实战：正式起步", 
             "词汇量上来以后，可以开始用往年真题来熟悉真实的考题风格了。\n" + tips[13],
             {"title": "早期真题慢速解析", "content": "✅ 安排：开始做英语二早些年（如2010年-2015年左右）的阅读题。建议慢慢做，不用急。\n方法：做完以后对照解析，把不认识的词圈一圈，看看之前学的主谓宾划分能不能套用在文章的长句里。遇到稍微有趣的生词，也可以记在手机备忘录里方便查看。"},
             None,
             {"title": "错误率预期", "content": "第一次做真题错多错少都不重要，这主要是一个适应过程。不要太把分数放在心上，弄懂每道题为什么错才是关键。"})

    for i in range(15, 23):
        msg = tips[i-1]
        add_week(i, f"探索真题出题规律 (第{i}周)", 
                 "只做真题就行，重点在于摸清它考的逻辑和出题的角度。\n" + msg,
                 {"title": "真题阅读专项训练", "content": "✅ 任务：继续保持一定的早期真卷阅读进度。\n如果遇到总是读不懂的单词，可以使用《真题伴侣》等工具来查单词。\n总结一下正确选项是怎么对原文进行同义替换的。看完一篇文章后，用自己的话简单在心里复述一下段落大意，有助于提高理解力。"},
                 None,
                 {"title": "日常与学习的平衡", "content": "如果遇到生活里比较忙的时候，阅读题可以暂停，但每天的单词复习尽量不要断。之后有空的时候再把落下的真题安排上。"})

    # ================= 政治启动及双线双轨期 (Week 23-29) =================
    
    add_week(23, "政治初步接触", 
             "现在可以开始看看政治了，主要是了解一下书本的框架体系，不需要马上去死记硬背。\n" + tips[26],
             {"title": "阅读二刷与翻译尝试", "content": "✅ 任务：早期阅读第一遍做完以后，可以尝试看一下翻译部分。英二是整个段落的翻译，注意语句要通顺。可以每周试着写几篇翻译，感受中文和英文的区别。"},
             {"title": "政治零基础入门", "content": "✅ 安排：每天晚上留点时间听听名师的基础课（比如徐涛老师的课），当成听故事一样了解一下马哲或是近代史的脉络即可。听完每一节课后，可以在本子上随手画一个最简单的纲概图帮助记忆。"},
             {"title": "合理分配精力", "content": "现在加入了政治，需要更合理地安排精力。不用在政治初期分配过多时间，主要精力还是给阅读理解和专业课。"})

    add_week(24, "政治客观题试手", 
             "政治不仅要听课，选择题也是得分的重点方向。\n" + tips[27],
             {"title": "英语二作文素材预备", "content": "✅ 建议：英二多数是图表作文，可以慢慢开始积累一些描述图表升降趋势的英文单词。平时看到别人写的好句子，也可以考虑摘抄下来以后备用。"},
             {"title": "政治选择题初步练习", "content": "✅ 安排：根据听过的章节进度，在《苍盾小程序》上刷点选择题。刷错的时候看看解析即可，不需要大段抄字。遇到很有代表性的错题，可以用截图保存到相册集中复习。"},
             {"title": "执行力聚焦", "content": "每天确认自己完成了一两项小任务（比如政治单选加英语单词）就算是合格的一天。保持一个连贯的状态就行。"})

    for i in range(25, 30):
        msg = tips[i-1]
        add_week(i, f"英语总结与政治双修 (第{i}周)", 
                 "公共课的复习进入了一个重复和巩固的时期。英语通过真题提高，政治通过小程序熟悉。\n" + msg,
                 {"title": "真题二刷与作文起步", "content": "✅ 任务：二刷英语真题时，重点看看上次错的题这次能不能做对。对于作文，可以参考一些名校的范文结构整理出自己的通用段落。有空的话，尝试按照这个结构默写一两个通用开头段。"},
                 {"title": "政治框架继续推进", "content": "✅ 任务：利用零散的时间刷刷题，重点搞清楚各个时期的重要会议和文件内容。也可以和同学交流一下互相抽查几个知识点加深印象。"},
                 {"title": "专业课冲锋", "content": "这段时间专业课是非常重要的。尽量把大脑最活跃的时候拿来记忆专业课的核心知识，并且定期默写关键要点进行自测。"})

    # ================= 冲刺阶段：政治发力与英语收官 (Week 30-41) =================

    add_week(30, "政治加速：阅读背诵手册", 
             "此时政治的复习可以慢慢转向浓缩的背诵手册。英语也进入成套复习阶段。\n" + tips[32],
             {"title": "英语套卷综合演练", "content": "✅ 安排：可以开始做近5年的英语完整真题了，最好控制在完整的三小时内做完，看看自己的时间安排准不准确。做完套卷后，抽出一点时间单独分析一下哪些题型用时比预计多了。"},
             {"title": "熟悉政治小册子", "content": "✅ 选择：可以买一本类似于腿姐冲刺背诵手册的资料，放在手边每天翻一翻，理顺各章节的重点。多翻几次混个眼熟以后背起来就会顺畅很多。"},
             {"title": "拒绝盲目比较", "content": "不必理会别人说专业课看了几遍，重点看自己的真题正确率和复习扎实度，按部就班走好自己的路即可。"})

    for i in range(31, 35):
        msg = tips[i-1]
        add_week(i, f"全面总结与查漏补缺 (第{i}周)", 
                 "对经常犯错的政治知识点和英语题型进行有针对性的复习。\n" + msg,
                 {"title": "英语作文动笔练习", "content": "✅ 核心任务：别只在心里默背作文框架，一定要拿笔在纸上写一写，检查有没有简单的拼写错误。建议写历年大作文真题的对应范文，提前感受真题思路。"},
                 {"title": "政治重点记忆", "content": "✅ 任务：配合手册，着重记一记具有总结意味的常见考点，那是选择题容易出的地方。平时坐公交或排队时都可以拿手机出来看两眼知识简图巩固。"},
                 {"title": "减少焦虑", "content": "觉得书背不完是大家都会有的感觉。尽力拿好基础分，不要在偏、怪题上浪费很多时间。平时多给自己一些积极的心理暗示。"})

    add_week(35, "时政了解与模拟训练", 
             "留意一下当年的时政新闻，也可以做一些名师的政治模拟卷来热热身。\n" + tips[35],
             {"title": "英语近些年真题测试", "content": "✅ 安排：把留作最终测试的真题卷拿出来按时间做一次。如果有很多错题，继续把错题本和单词复习一遍就行。别忘了总结作文在这套卷子里的适用情况。"},
             {"title": "做些政治名家模拟卷", "content": "✅ 选择：可以开始做像肖八这样的模拟题。主要做选择题部分，错得多了也不用心慌，多看解答当成积累知识点即可。对上面的大题题目有印象就行，暂时不用全文背。"},
             {"title": "作息微调", "content": "早晨稍微起早一点开始看书，把个人的精神高峰期渐渐调整到白天的考试时间段。"})

    for i in range(36, 38):
        msg = tips[i-1]
        add_week(i, f"考前梳理复习 (第{i}周)", 
                 "不建议再去研究全新的难题，看自己已经基本掌握或者差一点就懂的内容。\n" + msg,
                 {"title": "英语词汇和作文保温", "content": "✅ 任务：每天保持一点早期真题的阅读以维持对题目的手感。并且保证作文模板能流畅书写即可。可以在草稿本上每天随手写一句鼓励自己的英文作为练字和保持状态的手法。"},
                 {"title": "政治核心重点复看", "content": "✅ 任务：继续通过背诵小册子过一遍考试重点提纲。拿一张白纸自己试着画一下各个科目的核心层级关系网。"},
                 {"title": "生活准备", "content": "把考场周围的交通和住宿事情提前定下来，别在最后一周为了这些小事影响复习心情。"})

    add_week(38, "重点背诵：政治主观题阶段", 
             "备考最后的背诵时段，重点可以放在各种大题要点上。\n" + tips[37],
             {"title": "英语状态维持", "content": "每天花个半个小时看看易错单词，稍稍回忆几句重要模板。保持轻松的心情看真题错点就行。"},
             {"title": "集中记忆《肖四》大题", "content": "✅ 任务：平时不用太紧张，等拿到《肖四》之后，核心任务就是多读多背里面的大题。只要记住加粗的名词、熟悉句子结构就可以了。可以找个不打扰别人的地方朗读出来，增加脑中记忆印象。"},
             {"title": "专业课最后归纳", "content": "在背肖四的同时，利用每天固定的时间做做专业课的最后提纲归纳和记忆。"})

    add_week(39, "政治考前答题技巧梳理", 
             "在背诵之余，适当了解如果在考场上没遇到原题怎么运用手头材料。\n" + tips[38],
             {"title": "计划好英语答题规律", "content": "想清楚自己在考场上的答题顺序，比如先写作文、再阅读，最后写翻译完型等，时间分配合理最重要。最好平时掐表试几次这样的顺序，做到心中有数。"},
             {"title": "学习答大题思路", "content": "可以在网上找相关短视频学习一下：政治如果没有碰到见过的题目，怎么结合阅读材料组织出比较条理清晰的分点回答。看完以后可以在空白的肖四卷面上模拟组织几条答案试试。"},
             {"title": "最后模拟", "content": "找个整段的时间，给自己创造一个没有人干扰的简单自考环境，体验一遍整个考试流程。"})

    add_week(40, "最后调整与确认事项", 
             "快考试了，就不用再去学什么新知识点了，把自己会的内容稳住最重要。\n" + tips[39],
             {"title": "温习英语旧知识", "content": "平心静气地看看自己平时记录的各种英语错题与常错点就好，不用额外多做题。"},
             {"title": "回溯政治知识逻辑", "content": "在脑子里大致过一遍肖四的大题骨干部分，确保如果在卷子上遇到能够回忆出相关词语，睡前躺在床上回忆效果更好点。"},
             {"title": "相关物品确认", "content": "确认一下考试用的准考证和各类文具。稍微放松一点调整好状态。考前不要吃太容易拉肚子的东西。"})

    add_week(41, "正式考试", 
             "平时好好复习了，考场上平常心面对就好，坚持写完最后一场考试。\n" + tips[40],
             {"title": "英语：合理安排保基础", "content": "碰见太难没看懂的英语文章别着急，可以先挑有把握的题选，保障会做的部分都拿分。深呼吸几次平复情绪也有利于接下来的做题状态。"},
             {"title": "政治：结合材料尽量作答", "content": "认真看卷子给的材料，把背过的内容和材料里的点结合在一起去答题，尽量不要出现大片字数的空白。哪怕是把材料换个说法分一条写上也很重要。"},
             {"title": "考完全程", "content": "考完一科不要对答案了。准备好下一科的必需品，把后面的考试好好完成。"})

    data = {"student": "兔子", "weeks": weeks[:41]}
    
    with open("D:/myblog/source/kaoyan/兔子/TuziStylePlan.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    html_template = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>兔子 2027考研全程定制规划</title>
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
        .grid-english { background: rgba(52,211,153,0.08); border-left: 3px solid #34d399; }
        .grid-politics { background: rgba(251,191,36,0.08); border-left: 3px solid #fbbf24; }
        .grid-mindset { background: rgba(139,92,246,0.08); border-left: 3px solid #8b5cf6; }
        
        h3 { margin-bottom: 12px; font-size: 1.1rem; }
        .grid-english h3 { color: #34d399; }
        .grid-politics h3 { color: #fbbf24; }
        .grid-mindset h3 { color: #8b5cf6; }
        
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
            <h1>兔子 2027考研全程复习规划</h1>
            <div class="meta">
                <span>🎯 目标院校：曲阜师范大学·学科英语专硕</span>
                <span>📅 周期：2026.03.06 - 2026.12 (共41周)</span>
            </div>
            <div class="meta" style="margin-top: 8px;">
                <span>📚 必考科目：英语二 / 政治 / 专业课</span>
            </div>
        </header>

        <!-- 总体规划概览 -->
        <div class="overview">
            <h2>🎯 考研全程复习策略</h2>
            
            <p class="strategy">
                <strong>🔥 复习原则：日常排表时，建议将整块连续的时间优先安排给专业课。公共课可以穿插着在平时日常进行学习，重点抓真题来拿分。</strong><br><br>
                <span style="color: #ffb86c;">⚠️ 时间分配提示：3月至7月的公共课专注复习【英语二词汇与真题阅读】。政治科目的复习【建议在8月之前不用着急启动】，前期把复习精力多留给专业课和英语。</span>
            </p>
            
            <div class="grid-box">
                <div class="grid-item grid-english">
                    <h3>📖 英语二复习思路</h3>
                    <ul>
                        <li><strong style="color: #fff;">词汇过熟：</strong>前期（3-6月）不用看厚实的语法长课，只需使用《不背单词》稳妥地背诵考研大纲核心语，“看其形知其义”即可，不用买一大本卷子全文翻译。</li>
                        <li><strong style="color: #fff;">阅读掌握考法：</strong>英语二阅读通常会同义替换。多做真题去体会这种同义替换方式，对于很难的句子也可以看相关的阅读技巧视频。</li>
                        <li><strong style="color: #fff;">作文平时积累：</strong>英二大作文常常考图表（柱类/饼类）。平时可以先记下常用的框架以及“上升、下降、占多少比例”等基本单词。</li>
                    </ul>
                </div>
                
                <div class="grid-item grid-politics">
                    <h3>🏛️ 政治复习思路</h3>
                    <ul>
                        <li><strong style="color: #f43f5e;">🚫 前期不用着急：</strong>8月份前不需要花费太多精力背政治书，前期如果想了解，可以听徐涛老师的基础课程简单当做课外补充。</li>
                        <li><strong style="color: #fff;">做题为主：</strong>可以用《苍盾小程序》之类的方法在平时闲暇做几道基础题。中后期再买一本类似《腿姐冲刺小册子》的小书看看就行。</li>
                        <li><strong style="color: #fff;">最后冲刺背熟：</strong>12月《肖四》出版后认真背熟。考前也可以去考研网站上搜一下考研政治怎么利用自带的资料组织出通顺答案的方法，以便拿到基础分数。</li>
                    </ul>
                </div>

                <div class="grid-item grid-mindset">
                    <h3>💡 常规学习建议</h3>
                    <ul>
                        <li><strong style="color: #fff;">坚持完成日任务比完美更重要：</strong>每天生活难免有变化。不要求每天都能完美复习，但请确立一个比如“哪怕再累每天最少背50个英语单词才睡觉”的习惯。</li>
                        <li><strong style="color: #fff;">双休日集中推进：</strong>平时碎片时间多，那么完整的休息日就是补充学习短板的关键。把那些需要连贯阅读的专业课大章节或真题模拟都安排在周围！</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="expand-all">
            <button onclick="toggleAll()">展开/收起全部计划周</button>
        </div>

        <div id="weeks-container"></div>
        
        <footer>
            <p>💪 这份时间线旨在给出按部就班的复习节奏。只要坚持跟着复习方向，就能稳步准备好初试。</p>
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
            
            if (week.english) {
                subjectsHtml += `
                    <div class="subject">
                        <div class="subject-header">
                            <span class="subject-name english">📖 英语二</span>
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
                            <span class="subject-name mindset">💡 学习建议及安排</span>
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

    with open("D:/myblog/source/kaoyan/兔子/TuziStylePlan.html", "w", encoding="utf-8") as f:
        f.write(html_template)
        
if __name__ == "__main__":
    get_full_plan_student_6()
