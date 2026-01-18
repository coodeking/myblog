
import json

# Load FINAL RESCUED Plan V6
with open(r'd:\myblog\source\kaoyan\wangsang_detail_final.json', 'r', encoding='utf-8') as f:
    plan_data = json.load(f)

# HTML Template
html_template = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>汪桑 26考研全程深度定制规划</title>
    <style>
        :root { --primary: #1a1a1a; --secondary: #4a4a4a; --bg: #f4f6f9; }
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; background: var(--bg); color: #333; line-height: 1.6; padding-bottom: 60px; }
        .container { max-width: 960px; margin: 0 auto; padding: 20px; }
        
        .header { text-align: center; padding: 40px 20px; background: white; border-radius: 8px; margin-bottom: 30px; border-bottom: 4px solid #1a1a1a; }
        .header h1 { font-size: 28px; color: var(--primary); margin-bottom: 12px; font-weight: 800; letter-spacing: 0.5px; }
        .header p { color: #666; font-size: 15px; font-weight: 500; }
        
        .week-card { background: white; border-radius: 8px; padding: 24px; margin-bottom: 24px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); border: 1px solid #e1e4e8; }
        
        .week-top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #eee; }
        .week-idx { font-size: 20px; font-weight: 800; color: #000; }
        .week-date { font-size: 14px; color: #666; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, monospace; font-weight: 500; }
        .week-theme { background: #333; color: #fff; padding: 4px 12px; border-radius: 4px; font-size: 13px; font-weight: 600; margin-left: 12px;}
        
        .mentor-note { background: #fffdf0; color: #856404; padding: 16px; border: 1px solid #fff3cd; border-radius: 6px; margin-bottom: 20px; font-size: 15px; line-height: 1.6; font-weight: 500; }
        
        .sub-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; }
        .sub-box { background: #fff; padding: 0; }
        
        .sub-head { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; font-size: 16px; font-weight: 800; border-bottom: 2px solid #f0f0f0; padding-bottom: 8px; }
        .math .sub-head { color: #c0392b; border-color: #fcebe9; } 
        .eng .sub-head { color: #27ae60; border-color: #e9fbf0; } 
        .pol .sub-head { color: #8e44ad; border-color: #f7eefb; }
        
        .sub-body h4 { font-size: 15px; margin: 0 0 8px 0; color: #222; font-weight: 700; line-height: 1.4; }
        .sub-body p { font-size: 14px; color: #555; margin: 0; text-align: justify; white-space: pre-wrap; }
        
        .time-badge { font-size: 12px; font-family: monospace; background: #f1f3f5; color: #495057; padding: 2px 8px; border-radius: 4px; font-weight: 600; }
        
        /* Mobile optimize */
        @media(max-width: 600px) { .sub-grid { grid-template-columns: 1fr; } .week-top { flex-direction: column; align-items: flex-start; gap: 8px; } .week-theme { margin-left: 0; margin-top: 4px; display: inline-block; } }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>汪桑 2026考研全程深度定制规划</h1>
            <p>🎯 中山大学 085700 | 📅 48周 | 深度定制</p>
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
                    <div class="mentor-note">💡 <strong>每周指导：</strong>${w.message.replace(/\\n/g, '<br/>')}</div>
                    
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
            <div class="sub-box ${cls}">
                <div class="sub-head">
                    <span>${name}</span>
                    ${data.hours ? `<span class="time-badge">${data.hours}h</span>` : ''}
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

print("Final webpage V6 generated.")
