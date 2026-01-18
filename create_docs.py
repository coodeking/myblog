
import json

# Load data
with open(r'd:\myblog\source\kaoyan\wangsang_plan.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# HTML Content for Word
html_content = """
<html xmlns:o='urn:schemas-microsoft-com:office:office' xmlns:w='urn:schemas-microsoft-com:office:word' xmlns='http://www.w3.org/TR/REC-html40'>
<head><meta charset='utf-8'><title>考研规划</title>
<style>
body { font-family: 'Songti SC', 'SimSun', serif; }
table { border-collapse: collapse; width: 100%; margin-bottom: 20px; }
th, td { border: 1px solid #000; padding: 8px; text-align: left; }
th { background-color: #f2f2f2; }
h1, h2 { text-align: center; }
.week-header { background-color: #e6f3ff; font-weight: bold; }
</style>
</head>
<body>
"""

html_content += f"<h1>{data['student']} 2026考研全程周规划</h1>"
html_content += f"<p style='text-align:center'><strong>目标：</strong>{data['target']} | <strong>周期：</strong>{data['timeline']}</p><hr/>"

html_content += "<table><thead><tr><th width='15%'>周次/日期</th><th width='15%'>科目</th><th width='70%'>任务内容</th></tr></thead><tbody>"

for week in data['weeks']:
    # Rowspan calculation
    rowspan = len([i for i in week['items'] if i['content'] != '暂无' and '暂不复习' not in i['content']])
    if rowspan == 0: continue
    
    first = True
    for item in week['items']:
        if '暂不复习' in item['content']: continue
        
        html_content += "<tr>"
        if first:
            html_content += f"<td rowspan='{rowspan}' class='week-header'>第{week['week']}周<br/>{week['dates']}</td>"
            first = False
        
        html_content += f"<td>{item['name']}</td>"
        html_content += f"<td>{item['content']}</td>"
        html_content += "</tr>"

html_content += "</tbody></table></body></html>"

with open(r'd:\myblog\source\kaoyan\wangsang_word.doc', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Word doc generated.")
