
import json

# Load plan data
with open(r'd:\myblog\source\kaoyan\wangsang_plan.json', 'r', encoding='utf-8') as f:
    plan_data = json.load(f)

# Load HTML template
with open(r'd:\myblog\source\kaoyan\plan.html', 'r', encoding='utf-8') as f:
    html_template = f.read()

# Prepare script replacement
# We want to replace the loadPlan() function entirely or just inject data
# The easiest way is to replace the `loadPlan()` call in window.onload (if it existed) or just rewrite the script section.
# Looking at plan.html, it calls loadPlan() likely? Wait, I didn't see where loadPlan is called in the previous view_file.
# Let's assume it's called at the end or I should add it.
# Actually, the previous view_file showed the script functions but not the execution line.
# I will simply Replace the entire <script>...</script> block with a new one that renders directly.

# Extract style and body
style_start = html_template.find('<style>')
style_end = html_template.find('</style>') + 8
body_start = html_template.find('<body>')
body_end = html_template.find('</body>') + 7

# Construct new HTML
new_html = html_template[:style_end] + "\n</head>\n<body>\n"
new_html += """
    <div class="container">
        <div class="header">
            <h1>📅 汪桑的考研周规划</h1>
            <p class="student-name">目标：中山大学 | 330分</p>
        </div>
        <div id="content"></div>
    </div>
    
    <script>
        const planData = """ + json.dumps(plan_data, ensure_ascii=False) + """;
        
        // Render Logic (Copied and adapted from plan.html)
        function renderPlan(data) {
            const weeks = data.weeks || [];
            let html = '<div class="week-grid" id="weekGrid">';
            weeks.forEach(week => {
                html += renderWeek(week);
            });
            html += '</div>';
            document.getElementById('content').innerHTML = html;
        }

        function renderWeek(week) {
             // Calculate hours (approximate from text if not explicit, but here we just render)
             // simplified render without complex hour calc if not in data
            return `
                <div class="week-card">
                    <div class="week-header">
                        <span class="week-number">第 ${week.week} 周</span>
                        <span class="week-date">${week.dates}</span>
                    </div>
                    <div class="subject-grid">
                        ${renderSubject('math', '📐 数学', week.items.find(i => i.name === '数学'))}
                        ${renderSubject('english', '📖 英语', week.items.find(i => i.name === '英语'))}
                        ${renderSubject('politics', '🏛️ 政治', week.items.find(i => i.name === '政治'))}
                        ${renderSubject('prof', '📚 专业课', week.items.find(i => i.name === '专业课'))}
                    </div>
                </div>
            `;
        }

        function renderSubject(type, title, data) {
            if (!data || data.content === '暂无') return '';
            const isPending = data.content.includes('暂不复习');
            const style = isPending ? 'opacity: 0.5;' : '';
            return `
                <div class="subject-card" style="${style}">
                    <div class="subject-title ${type}">${title}</div>
                    <div class="subject-topic">${data.content}</div>
                </div>
            `;
        }
        
        // Execute
        renderPlan(planData);
    </script>
</body>
</html>
"""

# We need to reuse the styles from plan.html to keep it beautiful
# I will manually inject the CSS logic 
css_content = html_template[style_start:style_end]

final_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>汪桑 26考研规划</title>
    {css_content}
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📅 汪桑26考研全程周规划</h1>
            <p class="student-name">目标：中山大学 085700 | 330分</p>
        </div>
        <div id="content"></div>
    </div>
    <script>
        const planData = {json.dumps(plan_data, ensure_ascii=False)};
        
        function renderPlan(data) {{
            const weeks = data.weeks || [];
            let html = '<div class="week-grid">';
            weeks.forEach(week => {{
                html += renderWeek(week);
            }});
            html += '</div>';
            document.getElementById('content').innerHTML = html;
        }}

        function renderWeek(week) {{
            return `
                <div class="week-card">
                    <div class="week-header">
                        <span class="week-number">第 ${{week.week}} 周</span>
                        <span class="week-date">${{week.dates}}</span>
                    </div>
                    <div class="subject-grid">
                        ${{renderSubject('math', '📐 数学', week.items.find(i => i.name === '数学'))}}
                        ${{renderSubject('english', '📖 英语', week.items.find(i => i.name === '英语'))}}
                        ${{renderSubject('politics', '🏛️ 政治', week.items.find(i => i.name === '政治'))}}
                         ${{renderSubject('prof', '📚 专业课', week.items.find(i => i.name === '专业课'))}}
                    </div>
                </div>
            `;
        }}

        function renderSubject(type, title, data) {{
            if (!data) return '';
            if (data.content.includes('暂不复习') && type === 'politics') {{
                 return `
                <div class="subject-card" style="opacity:0.6; border:1px dashed #555;">
                    <div class="subject-title ${{type}}">${{title}}</div>
                    <div class="subject-topic" style="font-size:12px; color:#888;">${{data.content}}</div>
                </div>
            `;
            }}
            
            return `
                <div class="subject-card">
                    <div class="subject-title ${{type}}">${{title}}</div>
                    <div class="subject-topic">${{data.content}}</div>
                </div>
            `;
        }}

        renderPlan(planData);
    </script>
</body>
</html>
"""

with open(r'd:\myblog\source\kaoyan\wangsang.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Webpage generated.")
