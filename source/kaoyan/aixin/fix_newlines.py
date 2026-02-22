"""
修复 aixin.html 中的换行符问题
将 \\n (反斜杠n字符串) 替换为实际的换行符
"""

# 读取文件
with open(r'D:\myblog\source\kaoyan\aixin.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 问题：文件中有两种不同的换行表示
# 1. 前10周: \\n (两个字符：反斜杠和n，在Python中表示为 '\\n')
# 2. 11周及之后: \n (实际换行符)

# 我们需要把所有的 \\n 替换为 \n
# 在Python中，文件里的 \\n 读进来就是 '\\n' (两个字符)
# 我们要把它替换为 '\n' (一个字符)

# 替换
new_content = content.replace('\\n', '\n')

# 写回文件
with open(r'D:\myblog\source\kaoyan\aixin.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ 换行符修复完成！")
