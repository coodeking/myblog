"""
爱心考研规划生成脚本
整合四阶段数据，生成完整的 JSON、DOC 和 HTML 文件
"""
import json
import os
import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_stage_data():
    """加载所有阶段数据"""
    all_weeks = []
    
    # 加载第一阶段
    with open(os.path.join(BASE_DIR, 'stage1_data.json'), 'r', encoding='utf-8') as f:
        stage1 = json.load(f)
        all_weeks.extend(stage1['weeks'])
    
    # 加载第二阶段
    with open(os.path.join(BASE_DIR, 'stage2_data.json'), 'r', encoding='utf-8') as f:
        stage2 = json.load(f)
        all_weeks.extend(stage2['weeks'])
    
    # 加载第三阶段
    with open(os.path.join(BASE_DIR, 'stage3_data.json'), 'r', encoding='utf-8') as f:
        stage3 = json.load(f)
        all_weeks.extend(stage3['weeks'])
    
    # 加载第四阶段
    with open(os.path.join(BASE_DIR, 'stage4_data.json'), 'r', encoding='utf-8') as f:
        stage4 = json.load(f)
        all_weeks.extend(stage4['weeks'])
    
    return {
        "student": "爱心",
        "target": "南京邮电大学·电子信息·专硕",
        "exam_subjects": "数学二 + 英语二 + 政治",
        "duration": "46周 (2026.02.07 - 2026.12.20)",
        "strategy": "数学60% / 英语30% / 政治10%",
        "weeks": all_weeks
    }

def generate_json(data):
    """生成完整 JSON 文件"""
    output_path = os.path.join(BASE_DIR, 'aixin_detail.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ JSON 文件已生成: {output_path}")

def generate_doc(data):
    """生成 Word 文档 (HTML 格式)"""
    html = """
    <html xmlns:o='urn:schemas-microsoft-com:office:office' xmlns:w='urn:schemas-microsoft-com:office:word' xmlns='http://www.w3.org/TR/REC-html40'>
    <head>
        <meta charset="utf-8">
        <title>爱心 2027考研全程深度定制规划</title>
        <style>
            body { font-family: 'SimSun', 'Microsoft YaHei', sans-serif; }
            h1 { text-align: center; color: #000; margin-bottom: 20px;}
            .info { text-align: center; color: #444; margin-bottom: 30px; border-bottom: 2px solid #000; padding-bottom: 10px;}
            .week-block { border: 1px solid #999; padding: 10px; margin-bottom: 15px; page-break-inside: avoid; }
            .week-header { background: #eee; padding: 5px 10px; font-weight: bold; border-bottom: 1px solid #999; display: flex; justify-content: space-between; }
            .msg { padding: 8px 10px; font-style: italic; color: #333; margin-top: 5px; margin-bottom: 5px; background: #fafafa;}
            table { width: 100%; border-collapse: collapse; margin-top: 5px;}
            td { padding: 8px; border: 1px solid #ccc; vertical-align: top; font-size: 10.5pt; }
            .sub-name { width: 15%; font-weight: bold; background-color: #f9f9f9;}
            .sub-hours { width: 10%; text-align: center; white-space: nowrap; }
        </style>
    </head>
    <body>
        <h1>爱心 2027考研全程深度定制规划</h1>
        <div class="info">
            <p><strong>目标院校：</strong>南京邮电大学 (电子信息·专硕) &nbsp;|&nbsp; <strong>规划周期：</strong>46周 (2026.02.07 - 2026.12.20)</p>
            <p><strong>核心策略：</strong>数学60% / 英语30% / 政治10%</p>
        </div>
    """
    
    for week in data['weeks']:
        html += f"""
        <div class="week-block">
            <div class="week-header">
                <span>第 {week['week']} 周：{week['theme']}</span>
                <span style="font-weight:normal; font-size: 0.9em;">{week['dates']}</span>
            </div>
            <div class="msg">💡 指导：{week['message']}</div>
            <table>
                <tr>
                    <td class="sub-name">数 学</td>
                    <td>
                        <strong>{week['math']['title']}</strong><br/>
                        {week['math']['content'].replace(chr(10), '<br/>')}
                    </td>
                    <td class="sub-hours">{week['math']['hours']}h</td>
                </tr>
                <tr>
                    <td class="sub-name">英 语</td>
                    <td>
                        <strong>{week['english']['title']}</strong><br/>
                        {week['english']['content'].replace(chr(10), '<br/>')}
                    </td>
                    <td class="sub-hours">{week['english']['hours']}h</td>
                </tr>
        """
        
        # 如果有政治课程
        if 'politics' in week:
            html += f"""
                <tr>
                    <td class="sub-name">政 治</td>
                    <td>
                        <strong>{week['politics']['title']}</strong><br/>
                        {week['politics']['content'].replace(chr(10), '<br/>')}
                    </td>
                    <td class="sub-hours">{week['politics']['hours']}h</td>
                </tr>
            """
        
        html += "</table></div>"
    
    html += "</body></html>"
    
    output_path = os.path.join(BASE_DIR, 'aixin_plan.doc')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ Word 文档已生成: {output_path}")

def generate_html(data):
    """生成专属网页"""
    html = """<!DOCTYPE html>
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
        .strategy {
            display: inline-block;
            background: rgba(99, 102, 241, 0.2);
            padding: 8px 16px;
            border-radius: 20px;
            margin-top: 15px;
            font-size: 0.9rem;
            color: var(--accent-light);
        }
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
            <div class="strategy">📊 核心策略：数学60% / 英语30% / 政治10%</div>
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
    const planData = """ + json.dumps(data['weeks'], ensure_ascii=False) + """;
    
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
"""
    
    output_path = os.path.join(BASE_DIR, 'aixin.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ HTML 网页已生成: {output_path}")

if __name__ == '__main__':
    print("正在生成爱心考研规划文件...")
    data = load_stage_data()
    generate_json(data)
    generate_doc(data)
    generate_html(data)
    print("\\n🎉 全部文件生成完成！")
