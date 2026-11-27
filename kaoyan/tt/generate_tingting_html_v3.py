# -*- coding: utf-8 -*-
import json

with open("D:/myblog/source/kaoyan/tt/tingting_v3.json", "r", encoding="utf-8") as f:
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
            font-size: 1.05rem;
        }
        .grid-box { display: grid; gap: 16px; margin-bottom: 20px; }
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
        .week-card:hover { transform: translateY(-2px); box-shadow: 0 8px 30px rgba(217, 70, 239, 0.15); }
        .week-header {
            background: linear-gradient(90deg, rgba(217, 70, 239, 0.3), rgba(217, 70, 239, 0.1));
            padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; cursor: pointer;
        }
        .week-header h3 { font-size: 1.1rem; color: var(--accent-light); }
        .week-header .dates { color: #888; font-size: 0.85rem; }
        .week-content { padding: 20px; display: none; }
        .week-content.active { display: block; }
        .message {
            background: rgba(217, 70, 239, 0.1); padding: 12px 16px; border-radius: 8px;
            margin-bottom: 20px; border-left: 3px solid var(--accent); font-style: italic; font-weight: bold;
        }
        .subject { background: rgba(255, 255, 255, 0.03); border-radius: 8px; padding: 15px; margin-bottom: 15px; }
        .subject-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }
        .subject-name { font-weight: bold; }
        .subject-name.math { color: #f472b6; }
        .subject-name.english { color: #34d399; }
        .subject-name.politics { color: #fbbf24; }
        .hours { background: rgba(255, 255, 255, 0.1); padding: 4px 12px; border-radius: 12px; font-size: 0.85rem; }
        .subject-title { font-weight: 600; margin-bottom: 8px; color: #fff; }
        .subject-content { color: #aaa; white-space: pre-line; font-size: 0.95rem; }
        .expand-all { text-align: center; margin-bottom: 20px; }
        .expand-all button {
            background: var(--accent); color: white; border: none; padding: 10px 24px;
            border-radius: 8px; cursor: pointer; font-size: 0.9rem; transition: background 0.2s;
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
                <span>📅 周期：2026.02.23 - 2026考前</span>
            </div>
            <div class="meta" style="margin-top: 10px;">
                <span>📚 必考：数学一 / 英语一 / 政治 / 851自动控制原理</span>
            </div>
        </header>

        <!-- 总体规划概览 -->
        <div class="overview">
            <h2>🎯 备考总纲与时间红线</h2>
            
            <p class="strategy">
                <strong>🔥 核心原则：所有科目都不准当「耐听王」，多想多算多做，一定要亲自落实到笔头上！</strong>
            </p>
            
            <div class="grid-box">
                <div class="grid-item grid-warning">
                    <h3>⏱️ 全局比例与隐藏红线</h3>
                    <ul>
                        <li><strong style="color: #fff;">时间安排务必合理：</strong> 公共课整体占比以数学为核心，**数学占60%时间，英语30%时间，政治10%时间**。</li>
                        <li><strong style="color: #f43f5e;">⚠️ 这里的时间100%是排除了专业课！</strong> 专业课的学习时间默认比数学少一点，必须自行预留在总体日程表里！（下文细项不再提及专业课，请自行保证落实）</li>
                    </ul>
                </div>
                
                <div class="grid-item grid-math">
                    <h3>📐 数学一（占除专业课的总大盘60%时间！）</h3>
                    <ul>
                        <li><strong style="color: #fff;">以练带学：</strong>不大量听课，听课永远学不会！不推荐看张宇的课程！做题时不会的，直接去B站搜1000题讲解（千羽、考研数学777、没咋了 均可）。比很多大机构老师讲得好！</li>
                        <li><strong style="color: #f43f5e;">🚫 舍弃偏废内容：</strong>张宇“超实数”、微分算子法、海涅定理、压缩映射原理、stolz定理统统不要看！连想考150的也不需要看！</li>
                        <li><strong style="color: #fff;">练习序列：</strong>第一轮真题《真题一本通》（于文涛）最优先 -> 结合「澄箫宇」大观系列 -> 模拟少做（只做李林6+4）。所有习题册+模拟卷均不做证明题，只写真题的证明题！</li>
                    </ul>
                </div>
                
                <div class="grid-item grid-english">
                    <h3>📖 英语一（占除专业课的总大盘30%时间！）</h3>
                    <ul>
                        <li><strong style="color: #fff;">词汇狂魔：</strong>暑假前只有一个任务：疯狂背单词！《不背单词》APP背核心三千词，暑假前最好刷三遍！</li>
                        <li><strong style="color: #fff;">真题启动：</strong>暑期开始两天一套英二真题（先不写作文）。用《真题伴侣》生词本功能，背真题里的实际语境意思！</li>
                        <li><strong style="color: #fff;">不碰雷区：</strong>少听或不听课！不精翻文章！不买手译本！最后听《Monkey》作文模板课背框架，平时多积累主题词。</li>
                    </ul>
                </div>
                
                <div class="grid-item grid-politics">
                    <h3>🏛️ 政治（占除专业课的总大盘10%时间！）</h3>
                    <ul>
                        <li><strong style="color: #f43f5e;">🚫 避坑名师长线：</strong>最早10月初才开始！远离徐涛等名师各种课！远离肖1000题！</li>
                        <li><strong style="color: #fff;">效率工具：</strong>买腿姐冲刺背诵手册熟读；利用《苍盾小程序》刷模拟卷（每天1套30个选择即可）。熟读澄箫宇“政治一页纸”。</li>
                        <li><strong style="color: #fff;">大题绝杀：</strong>12月死背肖四大题（背不住没关系！）。最后几天去B站务必学会【考研政治抄材料】视频技巧，这是考场的唯一保命招式！</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="expand-all">
            <button onclick="toggleAll()">展开/收起全部计划周</button>
        </div>

        <div id="weeks-container"></div>
        
        <footer>
            <p>💪 按照以上极度精简的路线走。执行力是你通关国防科大唯一的钥匙！</p>
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
                        <span class="hours">${week.math.hours}</span>
                    </div>
                    <div class="subject-title">${week.math.title}</div>
                    <div class="subject-content">${week.math.content}</div>
                </div>
                <div class="subject">
                    <div class="subject-header">
                        <span class="subject-name english">📖 英语一</span>
                        <span class="hours">${week.english.hours}</span>
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
                            <span class="hours">${week.politics.hours}</span>
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
print("V3 HTML populated from V3 JSON.")
