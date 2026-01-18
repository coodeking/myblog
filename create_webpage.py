
import json

# Load FINAL RESCUED Plan V4
with open(r'd:\myblog\source\kaoyan\wangsang_detail_v4.json', 'r', encoding='utf-8') as f:
    plan_data = json.load(f)

# HTML Template
html_template = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>汪桑 26考研全程定制规划 (终极版)</title>
    <style>
        :root { --primary: #2c3e50; --accent: #34495e; --bg: #f4f6f9; }
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; background: var(--bg); color: #333; line-height: 1.6; padding-bottom: 60px; }
        .container { max-width: 900px; margin: 0 auto; padding: 20px; }
        
        .header { text-align: center; padding: 40px 20px; background: white; border-radius: 8px; margin-bottom: 30px; border-top: 5px solid var(--primary); }
        .header h1 { font-size: 24px; color: var(--primary); margin-bottom: 8px; font-weight: 700; }
        .header p { color: #555; font-size: 14px; }
        
        .week-card { background: white; border-radius: 8px; padding: 20px; margin-bottom: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
        
        .week-top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; padding-bottom: 12px; border-bottom: 1px solid #eee; }
        .week-idx { font-size: 18px; font-weight: 700; color: var(--primary); }
        .week-date { font-size: 13px; color: #888; font-family: Consolas, monospace; }
        .week-theme { background: #eee; color: #555; padding: 2px 10px; border-radius: 4px; font-size: 13px; font-weight: 500; margin-left: 10px;}
        
        .mentor-note { background: #fdfdfd; color: #444; padding: 10px 14px; border-left: 3px solid #666; margin-bottom: 16px; font-size: 14px; font-style: italic; }
        
        .sub-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 12px; }
        .sub-box { background: #fafafa; padding: 14px; border-radius: 4px; border: 1px solid #eee; }
        
        .sub-head { display: flex; justify-content: space-between; margin-bottom: 6px; font-size: 14px; font-weight: 700; }
        .math { color: #c0392b; } .eng { color: #27ae60; } .pol { color: #8e44ad; }
        
        .sub-body h4 { font-size: 13px; margin: 0 0 4px 0; color: #333; font-weight: 600; }
        .sub-body p { font-size: 13px; color: #666; margin: 0; }
        
        .time-badge { font-size: 11px; background: #eee; color: #666; padding: 1px 6px; border-radius: 4px; font-weight: normal; }
        
        /* Mobile optimize */
        @media(max-width: 600px) { .sub-grid { grid-template-columns: 1fr; } .week-top { flex-direction: column; align-items: flex-start; gap: 6px; } }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>汪桑 2026考研全程定制规划</h1>
            <p>🎯 中山大学 085700 | 📅 48周全程陪跑计划 | 状态：终极定稿</p>
        </div>
        <div id="app"></div>
    </div>

    <script>
        const PLAN = """ + json.dumps(plan_data, ensure_ascii=False) + """;
        
        const render = () => {
            const app = document.getElementById('app');
            let html = '';
            
            PLAN.weeks.forEach(w => {
                html += `
                <div class="week-card">
                    <div class="week-top">
                        <div>
                            <span class="week-idx">第 ${w.week} 周</span>
                            <span class="week-theme">${w.theme}</span>
                        </div>
                        <span class="week-date">${w.dates}</span>
                    </div>
                    <div class="mentor-note">指导：${w.message}</div>
                    
                    <div class="sub-grid">
                        ${renderSub('math', '数 学', w.math)}
                        ${renderSub('eng', '英 语', w.english)}
                        ${renderSub('pol', '政 治', w.politics)}
                    </div>
                </div>`;
            });
            app.innerHTML = html;
        };
        
        const renderSub = (cls, name, data) => {
            if(!data) return '';
            
            return `
            <div class="sub-box">
                <div class="sub-head ${cls}">
                    <span>${name}</span>
                    ${data.hours ? `<span class="time-badge">约${data.hours}h</span>` : ''}
                </div>
                <div class="sub-body">
                    ${data.title ? `<h4>${data.title}</h4>` : ''}
                    <p>${data.content}</p>
                </div>
            </div>`;
        };
        
        render();
    </script>
</body>
</html>
"""

with open(r'd:\myblog\source\kaoyan\wangsang.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("Final webpage v4 generated.")
