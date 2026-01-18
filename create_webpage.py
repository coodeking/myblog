
import json

# Load FINAL RESCUED Plan
with open(r'd:\myblog\source\kaoyan\wangsang_detail_v2.json', 'r', encoding='utf-8') as f:
    plan_data = json.load(f)

# HTML Template
html_template = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>汪桑 26考研全程定制规划 (终极版)</title>
    <style>
        :root { --primary: #2c3e50; --accent: #3498db; --bg: #f8f9fa; }
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; background: var(--bg); color: #333; line-height: 1.6; padding-bottom: 60px; }
        .container { max-width: 900px; margin: 0 auto; padding: 20px; }
        
        .header { text-align: center; padding: 40px 20px; background: white; border-radius: 16px; margin-bottom: 30px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); }
        .header h1 { font-size: 26px; color: var(--primary); margin-bottom: 10px; }
        .header p { color: #666; font-size: 15px; }
        
        .week-card { background: white; border-radius: 12px; padding: 24px; margin-bottom: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.04); border-left: 4px solid var(--accent); }
        
        .week-top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #eee; }
        .week-idx { font-size: 18px; font-weight: 800; color: var(--primary); }
        .week-theme { background: #e3f2fd; color: #1565c0; padding: 4px 12px; border-radius: 20px; font-size: 13px; font-weight: 600; }
        
        .mentor-note { background: #fff8e1; color: #856404; padding: 12px 16px; border-radius: 8px; margin-bottom: 20px; font-size: 14px; position: relative; }
        .mentor-note::before { content: "💡"; margin-right: 8px; }
        
        .sub-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; }
        .sub-box { background: #f8f9fa; padding: 16px; border-radius: 8px; border: 1px solid #e9ecef; }
        
        .sub-head { display: flex; justify-content: space-between; margin-bottom: 8px; font-size: 15px; font-weight: 700; }
        .math { color: #c0392b; } .eng { color: #27ae60; } .pol { color: #8e44ad; }
        
        .sub-body h4 { font-size: 14px; margin: 0 0 4px 0; color: #444; }
        .sub-body p { font-size: 13px; color: #666; margin: 0; }
        
        .time-badge { font-size: 11px; background: #dfe6e9; color: #636e72; padding: 2px 6px; border-radius: 4px; font-weight: normal; }
        
        /* Mobile optimize */
        @media(max-width: 600px) { .sub-grid { grid-template-columns: 1fr; } .week-top { flex-direction: column; align-items: flex-start; gap: 8px; } }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>汪桑 2026考研全程定制规划</h1>
            <p>🎯 中山大学 085700 | 📅 48周全程陪跑计划</p>
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
                        <span class="week-idx">第 ${w.week} 周</span>
                        <span class="week-theme">${w.theme}</span>
                    </div>
                    <div class="mentor-note">建议：${w.message}</div>
                    
                    <div class="sub-grid">
                        ${renderSub('math', '📐 数学', w.math)}
                        ${renderSub('eng', '📖 英语', w.english)}
                        ${renderSub('pol', '🏛️ 政治', w.politics)}
                    </div>
                </div>`;
            });
            app.innerHTML = html;
        };
        
        const renderSub = (cls, name, data) => {
            if(!data) return '';
            const isSkip = data.content === '暂不复习';
            const style = isSkip ? 'opacity:0.5; border-style:dashed;' : '';
            
            return `
            <div class="sub-box" style="${style}">
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

print("Final webpage generated.")
