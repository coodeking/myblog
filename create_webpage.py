
import json

# Load detailed plan data
with open(r'd:\myblog\source\kaoyan\wangsang_detail.json', 'r', encoding='utf-8') as f:
    plan_data = json.load(f)

# HTML Template with enhanced styling for humanized content
html_template = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>汪桑 26考研深度定制规划</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: #f5f7fa;
            color: #333;
            line-height: 1.6;
            padding-bottom: 50px;
        }
        .container { max-width: 900px; margin: 0 auto; padding: 20px; }
        
        /* Header */
        .header {
            text-align: center;
            padding: 40px 0;
            background: linear-gradient(135deg, #2c3e50, #3498db);
            color: white;
            border-radius: 12px;
            margin-bottom: 30px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        .header h1 { font-size: 28px; margin-bottom: 10px; font-weight: 700; }
        .header p { opacity: 0.9; font-size: 16px; }
        
        /* Week Card */
        .week-card {
            background: white;
            border-radius: 12px;
            padding: 25px;
            margin-bottom: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            border-left: 5px solid #3498db;
            transition: transform 0.2s;
        }
        .week-card:hover { transform: translateY(-3px); box-shadow: 0 5px 20px rgba(0,0,0,0.08); }
        
        .week-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
            padding-bottom: 15px;
            border-bottom: 1px solid #eee;
        }
        .week-title { font-size: 20px; font-weight: bold; color: #2c3e50; }
        .week-theme { 
            background: #e8f4f8; 
            color: #2980b9; 
            padding: 4px 12px; 
            border-radius: 20px; 
            font-size: 14px; 
            font-weight: 600;
        }
        
        .tutor-message {
            background: #fff8e1;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            font-style: italic;
            color: #795548;
            border: 1px dashed #ffc107;
            position: relative;
        }
        .tutor-message::before {
            content: "💡";
            position: absolute;
            left: -10px;
            top: -10px;
            font-size: 24px;
            background: white;
            border-radius: 50%;
        }

        /* Subject Grid */
        .subject-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }
        .subject-item {
            background: #f8f9fa;
            border-radius: 8px;
            padding: 15px;
            border: 1px solid #e9ecef;
        }
        .subject-name {
            font-weight: bold;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
            font-size: 16px;
        }
        .math { color: #e74c3c; }
        .english { color: #27ae60; }
        .politics { color: #8e44ad; }
        
        .subject-content h4 { margin: 8px 0 4px; font-size: 14px; color: #555; }
        .subject-content p { font-size: 14px; color: #666; margin-bottom: 6px; }
        .subject-content strong { color: #333; }
        
        .hours-tag {
            font-size: 12px;
            background: #dfe6e9;
            padding: 2px 8px;
            border-radius: 4px;
            color: #636e72;
        }
        
        @media (max-width: 600px) {
            .header { padding: 30px 15px; }
            .week-header { flex-direction: column; align-items: flex-start; gap: 8px; }
            .subject-grid { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>汪桑 2026考研全称定制规划</h1>
            <p>目标：中山大学 (330分) | 状态：深度定制版</p>
        </div>
        
        <div id="plan-content"></div>
    </div>

    <script>
        const planData = """ + json.dumps(plan_data, ensure_ascii=False) + """;

        function render() {
            const container = document.getElementById('plan-content');
            let html = '';
            
            planData.weeks.forEach(week => {
                html += `
                <div class="week-card">
                    <div class="week-header">
                        <span class="week-title">第 ${week.week} 周</span>
                        <span class="week-theme">${week.theme}</span>
                    </div>
                    
                    <div class="tutor-message">
                        ${week.message}
                    </div>
                    
                    <div class="subject-grid">
                        ${renderSubject('math', '📐 数学', week.math)}
                        ${renderSubject('english', '📖 英语', week.english)}
                        ${renderSubject('politics', '🏛️ 政治', week.politics)}
                    </div>
                </div>
                `;
            });
            
            container.innerHTML = html;
        }
        
        function renderSubject(type, name, data) {
            if (!data) return '';
            
            // If content is just "暂不复习" style
            if(data.content === '暂不复习') {
                 return `
                <div class="subject-item" style="opacity:0.6; border-style:dashed;">
                    <div class="subject-name ${type}">${name}</div>
                    <div class="subject-content"><p>暂不复习</p></div>
                </div>`;
            }

            return `
            <div class="subject-item">
                <div class="subject-name ${type}">
                    ${name}
                    ${data.hours ? `<span class="hours-tag">约${data.hours}h</span>` : ''}
                </div>
                <div class="subject-content">
                    ${data.title ? `<h4>${data.title}</h4>` : ''}
                    ${data.content}
                </div>
            </div>
            `;
        }
        
        render();
    </script>
</body>
</html>
"""

with open(r'd:\myblog\source\kaoyan\wangsang.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("Customized webpage generated.")
