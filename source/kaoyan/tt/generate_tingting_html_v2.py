# -*- coding: utf-8 -*-
import json

with open("D:/myblog/source/kaoyan/tt/tingting_v2.json", "r", encoding="utf-8") as f:
    data = json.load(f)

html_template = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>婷婷 2027考研全程深度定制规划</title>
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
        .meta { color: #888; font-size: 0.9rem; }
        .meta span { margin: 0 10px; }
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
            color: #e0e0e0; 
            line-height: 1.8;
        }
        .grid-box {
            display: grid; gap: 16px; margin-bottom: 20px;
        }
        .grid-item { padding: 16px; border-radius: 8px; }
        .grid-math { background: rgba(244,114,182,0.1); }
        .grid-english { background: rgba(52,211,153,0.1); }
        .grid-politics { background: rgba(251,191,36,0.1); }
        .grid-warning { background: rgba(139,92,246,0.1); }
        
        h3 { margin-bottom: 10px; }
        .grid-math h3 { color: #f472b6; }
        .grid-english h3 { color: #34d399; }
        .grid-politics h3 { color: #fbbf24; }
        .grid-warning h3 { color: #8b5cf6; }
        
        ul { margin-left: 20px; color: #ccc; }
        
        .week-card {
            background: var(--card-bg);
            border-radius: 12px;
            margin-bottom: 20px;
            border: 1px solid var(--border-color);
            overflow: hidden;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .week-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 30px rgba(217, 70, 239, 0.15);
        }
        .week-header {
            background: linear-gradient(90deg, rgba(217, 70, 239, 0.3), rgba(217, 70, 239, 0.1));
            padding: 15px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            cursor: pointer;
        }
        .week-header h3 { font-size: 1.1rem; color: var(--accent-light); }
        .week-header .dates { color: #888; font-size: 0.85rem; }
        .week-content { padding: 20px; display: none; }
        .week-content.active { display: block; }
        .message {
            background: rgba(217, 70, 239, 0.1);
            padding: 12px 16px;
            border-radius: 8px;
            margin-bottom: 20px;
            border-left: 3px solid var(--accent);
            font-style: italic;
        }
        .subject {
            background: rgba(255, 255, 255, 0.03);
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 15px;
        }
        .subject-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }
        .subject-name { font-weight: bold; }
        .subject-name.math { color: #f472b6; }
        .subject-name.english { color: #34d399; }
        .subject-name.politics { color: #fbbf24; }
        .hours {
            background: rgba(255, 255, 255, 0.1);
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 0.85rem;
        }
        .subject-title { font-weight: 600; margin-bottom: 8px; color: #fff; }
        .subject-content { color: #aaa; white-space: pre-line; font-size: 0.9rem; }
        .expand-all { text-align: center; margin-bottom: 20px; }
        .expand-all button {
            background: var(--accent);
            color: white;
            border: none;
            padding: 10px 24px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 0.9rem;
            transition: background 0.2s;
        }
        .expand-all button:hover { background: var(--accent-light); }
        footer { text-align: center; padding: 30px; color: #666; font-size: 0.85rem; }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>婷婷 2027考研全程深度定制规划</h1>
            <div class="meta">
                <span>🎯 国防科技大学·081100控制科学与工程·学硕</span>
                <span>📅 目标分数：380分 | 每日时间分配：弹性充足的 ~11h/天</span>
            </div>
            <div class="meta" style="margin-top: 10px;">
                <span>📚 考试科目：数学一 / 英语一 / 政治 / 851自动控制原理</span>
            </div>
        </header>

        <!-- 总体规划概览 -->
        <div class="overview">
            <h2>🎯 备考总纲</h2>
            
            <p class="strategy">
                <strong>🔥 核心绝密原则：所有科目都不准当「耐听王」，多想多算多做，一定要亲自落实到笔头上！</strong>
            </p>
            
            <div class="grid-box">
                <div class="grid-item grid-math">
                    <h3>📐 数学一（占总大盘60%核心分配）</h3>
                    <ul>
                        <li><strong style="color: #fff;">以练带学：</strong>不大量听课，听课永远学不会，靠做题才能发挥在考场上！</li>
                        <li><strong style="color: #fff;">遇到拦路虎：</strong>不会的题和知识点，【直接去B站搜播放量高的视频】（如千羽、考研数学777、没咋了均可），比听大机构拖沓的讲师要强百倍。</li>
                        <li><strong style="color: #f43f5e;">🚫 舍弃偏题：</strong>张宇“超实数”、微分算子法、海涅定理、压缩映射原理、stolz定理统统不要看！连想考150的都不看！</li>
                        <li><strong style="color: #fff;">资料优先级：</strong>第一轮《真题一本通》（于文涛）最重要 -> 结合「澄箫宇」大观系列（两天一个） -> 李林6+4（10套）。习题册、模拟卷【哪怕是压轴】也只做计算，不做证明题（除了真题的证明！）。</li>
                    </ul>
                </div>
                
                <div class="grid-item grid-english">
                    <h3>📖 英语一（占总大盘30%精力分配）</h3>
                    <ul>
                        <li><strong style="color: #fff;">不碰雷区：</strong>少听课或不听课！不精翻文章！绝对不买手译本！</li>
                        <li><strong style="color: #fff;">词汇狂魔：</strong>暑假前只有一个任务——疯狂背单词！《不背单词》APP背考研大纲核心三千词，至少刷三遍！</li>
                        <li><strong style="color: #fff;">真题神器：</strong>暑期开始两天一套英二真题（用《真题伴侣》生词本功能），背真题里的实际语境意思！</li>
                        <li><strong style="color: #fff;">作文保命：</strong>后半程报名《Monkey》作文模板课，死记硬背模板考场直接套，拿高分！</li>
                    </ul>
                </div>
                
                <div class="grid-item grid-politics">
                    <h3>🏛️ 政治（占总大盘10%后半程分配）</h3>
                    <ul>
                        <li><strong style="color: #f43f5e;">🚫 警惕长线：</strong>最早10月初才开始！远离徐涛等名师各种冗长废话课！远离肖1000题！</li>
                        <li><strong style="color: #fff;">效率核心：</strong>买腿姐冲刺背诵手册熟读；利用每天马桶碎片时间在【苍盾小程序】刷模拟卷选择题（只求广度不钻牛角尖）。</li>
                        <li><strong style="color: #fff;">绝命大招：</strong>12月等肖四大题出来直接死背！加上考研冲刺期间B站神级【抄材料】教程，考场基本只抄材料就能过线拿高分！</li>
                    </ul>
                </div>
                
                <div class="grid-item grid-warning">
                    <h3>⏱️ 全局时间红线（务必牢记）</h3>
                    <ul>
                        <li>每天需要保持运动健身，上午10:30后、中午休息、晚上吃饭。公共课每日纯学时约为6.5~7.5小时。</li>
                        <li><strong>⚠️ 专业课的隐藏大头：</strong>公共课之所以被精准压缩、强调舍弃无用模块，正是为了给你每天留出至少 <strong>3~4小时</strong> 以上的专业课（851自动控制原理）专属时间！</li>
                        <li>因为你的执行力很强但公式容易忘，切记：一切复习的核心是“动笔解题”而非“眼看懂了”！</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="expand-all">
            <button onclick="toggleAll()">展开/收起全部计划周</button>
        </div>

        <div id="weeks-container"></div>
        
        <footer>
            <p>💪 相信你强大的执行力。国防科技大学在前方等你！</p>
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
                        <span class="subject-name math">📐 数学一</span>
                        <span class="hours">${week.math.hours}h</span>
                    </div>
                    <div class="subject-title">${week.math.title}</div>
                    <div class="subject-content">${week.math.content}</div>
                </div>
                <div class="subject">
                    <div class="subject-header">
                        <span class="subject-name english">📖 英语一</span>
                        <span class="hours">${week.english.hours}h</span>
                    </div>
                    <div class="subject-title">${week.english.title}</div>
                    <div class="subject-content">${week.english.content}</div>
                </div>
            `;

            if (week.politics) {
                subjectsHtml += `
                    <div class="subject">
                        <div class="subject-header">
                            <span class="subject-name politics">🏛️ 政治</span>
                            <span class="hours">${week.politics.hours}h</span>
                        </div>
                        <div class="subject-title">${week.politics.title}</div>
                        <div class="subject-content">${week.politics.content}</div>
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

with open("D:/myblog/source/kaoyan/tingting.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("Tingting HTML V2 completed successfully!")
