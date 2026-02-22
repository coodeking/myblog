"""
优化爱心规划前10周内容 - 修复版
确保换行符正确转义
"""
import json
import re

# 读取原始HTML文件（从备份或使用正确的数据）
# 先读取汪桑的HTML文件作为结构参考
with open(r'D:\myblog\source\kaoyan\wangsang.html', 'r', encoding='utf-8') as f:
    ref_html = f.read()

# 读取aixin.html
with open(r'D:\myblog\source\kaoyan\aixin.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# 优化前10周的内容 - 确保使用 \\n 而不是实际换行
optimized_weeks = [
    {
        "week": 1,
        "dates": "2月7日 - 2月13日",
        "theme": "高数基础：极限与连续",
        "message": "寒假时间别浪费，趁现在有整块时间赶紧把极限这块啃下来。极限计算是后面所有内容的基础，现在多花点功夫，后面会轻松很多。",
        "math": {
            "title": "张宇30讲：第1-2讲课后题",
            "content": "先做30讲课后题，不会的直接B站搜讲解。\\n推荐UP主：千羽、考研数学777、没咋了。\\n⚠️ 超实数、海涅定理这些不用看，考试不考。\\n📌 技巧：七种未定式要熟练，等价无穷小替换表要背熟。",
            "hours": 18
        },
        "english": {
            "title": "背单词启动",
            "content": "用《不背单词》开始背考研核心词，每天100个新词。\\n你六级500+的底子，背起来不会太难。\\n📌 方法：遮住中文看英文，1秒内反应不出来就标记。",
            "hours": 8
        }
    },
    {
        "week": 2,
        "dates": "2月14日 - 2月20日",
        "theme": "高数基础：导数与微分",
        "message": "导数是后面积分、微分方程的基础。这周把求导练到条件反射的程度，看到函数脑子里自动就有导数形式。",
        "math": {
            "title": "张宇30讲：第3-5讲课后题",
            "content": "完成课后题，不看视频课。\\n遇到不会的题B站搜'1000题讲解'。\\n📌 重点：导数定义题、隐函数求导是真题常考点。\\n📌 注意：复合函数求导要画树状图，链式法则别搞混。",
            "hours": 16
        },
        "english": {
            "title": "单词打卡",
            "content": "继续背单词，复习比新学更重要。\\n看到英文能瞬间反应中文即可，不用管拼写。\\n寒假结束前争取完成第一轮。",
            "hours": 8
        }
    },
    {
        "week": 3,
        "dates": "2月21日 - 2月27日",
        "theme": "高数基础：中值定理",
        "message": "中值定理是很多人的心理障碍，但数二不考太难的证明。你只需要会用定理解决计算问题，不用深究证明过程。",
        "math": {
            "title": "张宇30讲：第6-7讲课后题",
            "content": "30讲课后题为主。\\n习题册不做证明题，只做真题里的证明题。\\n📌 罗尔定理、拉格朗日中值定理的条件要记清楚。\\n📌 技巧：构造辅助函数是考察重点，常见的构造方法要积累。",
            "hours": 16
        },
        "english": {
            "title": "单词积累",
            "content": "每天早晚各30分钟背单词。\\n不精翻文章，不买手译本。\\n这阶段只有一个任务：背单词。",
            "hours": 8
        }
    },
    {
        "week": 4,
        "dates": "2月28日 - 3月6日",
        "theme": "高数基础：不定积分",
        "message": "不定积分比求导难很多，没有捷径。这周开始就是硬刷题，刷到看到积分题就有感觉为止。",
        "math": {
            "title": "张宇30讲：第8讲课后题",
            "content": "把基本积分公式表打印出来贴桌上。\\n遇到不会的积分题直接看B站讲解。\\n📌 常用技巧：凑微分、分部积分、有理函数拆分。\\n📌 注意：三角函数积分的万能公式虽然通用但计算量大，优先用其他方法。",
            "hours": 16
        },
        "english": {
            "title": "单词积累",
            "content": "第一遍背诵通常最痛苦，遗忘率高是正常现象。\\n坚持刷下去，六级500+的底子会慢慢发挥作用。\\n📌 艾宾浩斯曲线：隔天复习效果最好。",
            "hours": 8
        }
    },
    {
        "week": 5,
        "dates": "3月7日 - 3月13日",
        "theme": "高数基础：定积分",
        "message": "定积分的重点是计算。变上限积分求导是每年必考，这个必须练到不出错。",
        "math": {
            "title": "张宇30讲：第9-12讲课后题",
            "content": "牛顿-莱布尼茨公式要熟练。\\n变上限积分求导是真题必考点，必须练到从不失误。\\n📌 技巧：定积分遇到周期函数、奇偶函数可以用对称性简化。\\n📌 注意：分段函数的定积分要分区间处理。",
            "hours": 14
        },
        "english": {
            "title": "单词积累",
            "content": "暑假前只做一件事：背单词。\\n不要被别人的'做阅读'进度干扰。\\n六级词汇和考研词汇重叠多，背起来会越来越快。",
            "hours": 8
        }
    },
    {
        "week": 6,
        "dates": "3月14日 - 3月20日",
        "theme": "高数基础：微分方程",
        "message": "微分方程是送分章节，全是套路。只要能识别方程类型，代公式就能解出来。",
        "math": {
            "title": "张宇30讲：第13-15讲课后题",
            "content": "二阶常系数非齐次方程的特解设法表格必须死记。\\n把几种方程的通解公式默写在笔记本扉页，每天看一遍。\\n📌 常考类型：可分离变量、一阶线性、二阶常系数。\\n📌 技巧：齐次方程先算特征根，判断是否重根再套公式。",
            "hours": 14
        },
        "english": {
            "title": "单词积累",
            "content": "持续背单词，可以试着带入例句增加记忆维度。\\n作为老师，课间休息时间可以刷几个单词。",
            "hours": 8
        }
    },
    {
        "week": 7,
        "dates": "3月21日 - 3月27日",
        "theme": "高数基础：多元微分",
        "message": "从一元到多元，思维方式有变化。重点理清连续、可偏导、可微三者的关系。",
        "math": {
            "title": "张宇30讲：第16-17讲课后题",
            "content": "重点练习链式求导法则，画树状图是解决复杂复合函数求导的好方法。\\n隐函数求导在真题中出现频率高，多练几道。\\n📌 概念：可微推可偏导，但可偏导不一定可微。\\n📌 技巧：偏导数的定义式考察是送分题，直接用定义算。",
            "hours": 14
        },
        "english": {
            "title": "单词积累",
            "content": "持续背诵，第一轮进度应该过半了。\\n暑假前要刷三遍，保持节奏。",
            "hours": 8
        }
    },
    {
        "week": 8,
        "dates": "3月28日 - 4月3日",
        "theme": "高数基础：二重积分",
        "message": "二重积分是计算大户，这一章学不好后面真题会很痛苦。高数基础阶段到此结束。",
        "math": {
            "title": "张宇30讲：第18讲课后题",
            "content": "高数基础部分完结！\\n熟练掌握交换积分次序、利用区域对称性简化计算。\\n📌 技巧：遇到圆域优先想极坐标变换。\\n📌 注意：数二不考三重积分和曲线曲面积分，省下这部分时间。",
            "hours": 14
        },
        "english": {
            "title": "单词积累",
            "content": "第一轮核心词背诵收尾，准备开启第二轮。\\n第二轮速度会快很多。",
            "hours": 8
        }
    },
    {
        "week": 9,
        "dates": "4月4日 - 4月10日",
        "theme": "刷题阶段：1000题-极限",
        "message": "光听课不行，刷题才是检验真功夫。开始《张宇1000题》基础篇。",
        "math": {
            "title": "张宇1000题：基础篇-极限",
            "content": "完成第一章。不推荐看张宇课程，直接刷题。\\n不会的题看B站UP主讲解：千羽、考研数学777、没咋了。\\n📌 刷题原则：先做会做的，不会的标记后看解析，不做证明题。\\n📌 错题整理：错题要记录错因，是概念不清还是计算失误。",
            "hours": 16
        },
        "english": {
            "title": "词汇二刷",
            "content": "开始第二轮背诵。\\n要求：遮住中文，看到英文1秒内反应出核心意思。\\n反应不过来的划入生词本。",
            "hours": 8
        }
    },
    {
        "week": 10,
        "dates": "4月11日 - 4月17日",
        "theme": "刷题阶段：1000题-微积分",
        "message": "导数和积分计算量大，不要眼高手低。看答案觉得简单，自己算就错，说明计算力不够。",
        "math": {
            "title": "张宇1000题：基础篇-导数与积分",
            "content": "完成导数与积分章节。\\n养成草稿纸分块书写的习惯，步骤清晰。\\n📌 常见问题：积分符号弄丢、dx变换忘记换、分部积分符号算错。\\n📌 技巧：复杂计算分步做，每步都验算，提高准确率。",
            "hours": 16
        },
        "english": {
            "title": "词汇二刷",
            "content": "持续背单词，要像吃饭睡觉一样自然。\\n工作虽忙，碎片时间要利用好。",
            "hours": 8
        }
    }
]

# 读取aixin_detail.json获取完整数据
with open(r'D:\myblog\source\kaoyan\aixin_detail.json', 'r', encoding='utf-8') as f:
    full_data = json.load(f)

plan_data = full_data['weeks']

# 替换前10周
for i in range(10):
    plan_data[i] = optimized_weeks[i]

# 生成新的planData字符串 - 确保在一行
new_plan_data_str = json.dumps(plan_data, ensure_ascii=False, separators=(',', ': '))

# 读取原始aixin.html模板结构
# 重新生成完整HTML
html_template = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>爱心 2027考研全程深度定制规划</title>
    <style>
        :root {
            --bg-color: #0a0a0f;
            --card-bg: #12121a;
            --text-color: #e0e0e0;
            --accent: #6366f1;
            --accent-light: #818cf8;
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
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
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
            box-shadow: 0 8px 30px rgba(99, 102, 241, 0.15);
        }
        .week-header {
            background: linear-gradient(90deg, rgba(99, 102, 241, 0.3), rgba(99, 102, 241, 0.1));
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
            background: rgba(99, 102, 241, 0.1);
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
        .subject-name {
            font-weight: bold;
            color: var(--accent-light);
        }
        .subject-name.math { color: #f472b6; }
        .subject-name.english { color: #34d399; }
        .subject-name.politics { color: #fbbf24; }
        .hours {
            background: rgba(255, 255, 255, 0.1);
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 0.85rem;
        }
        .subject-title { font-weight: 600; margin-bottom: 8px; }
        .subject-content { color: #aaa; white-space: pre-line; font-size: 0.9rem; }
        .expand-all {
            text-align: center;
            margin-bottom: 20px;
        }
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
        footer {
            text-align: center;
            padding: 30px;
            color: #666;
            font-size: 0.85rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>爱心 2027考研全程深度定制规划</h1>
            <div class="meta">
                <span>🎯 南京邮电大学·电子信息·专硕</span>
                <span>📅 46周 (2026.02.07 - 2026.12.20)</span>
            </div>
        </header>
        
        <div class="expand-all">
            <button onclick="toggleAll()">展开/收起全部</button>
        </div>
        
        <div id="weeks-container"></div>
        
        <footer>
            <p>💪 坚持就是胜利！祝你金榜题名！</p>
        </footer>
    </div>
    
    <script>
    const planData = ''' + new_plan_data_str + ''';
    
    function renderWeeks() {
        const container = document.getElementById('weeks-container');
        planData.forEach((week, index) => {
            const card = document.createElement('div');
            card.className = 'week-card';
            
            let subjectsHtml = `
                <div class="subject">
                    <div class="subject-header">
                        <span class="subject-name math">📐 数学</span>
                        <span class="hours">${week.math.hours}h</span>
                    </div>
                    <div class="subject-title">${week.math.title}</div>
                    <div class="subject-content">${week.math.content}</div>
                </div>
                <div class="subject">
                    <div class="subject-header">
                        <span class="subject-name english">📚 英语</span>
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
        
        // 默认展开第一周
        document.getElementById('week-0').classList.add('active');
    }
    
    function toggleWeek(index) {
        const content = document.getElementById('week-' + index);
        content.classList.toggle('active');
    }
    
    let allExpanded = false;
    function toggleAll() {
        allExpanded = !allExpanded;
        document.querySelectorAll('.week-content').forEach(el => {
            if (allExpanded) {
                el.classList.add('active');
            } else {
                el.classList.remove('active');
            }
        });
    }
    
    renderWeeks();
    </script>
</body>
</html>
'''

# 写入文件
with open(r'D:\myblog\source\kaoyan\aixin.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("✅ HTML文件已修复并更新！")
