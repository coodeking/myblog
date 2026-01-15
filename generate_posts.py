import os
import random
import datetime

# 目标目录
posts_dir = os.path.join('source', '_posts')
if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)

# 封面图库 (Unsplash 高质量技术/风景图)
covers = [
    "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800",
    "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800",
    "https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?w=800",
    "https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=800",
    "https://images.unsplash.com/photo-1504639725590-34d0984388bd?w=800",
    "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=800",
    "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800",
    "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800",
    "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800",
    "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800"
]

# 预设的高质量文章标题库 (覆盖AI, 前端, 后端, 算法)
titles_db = {
    "大模型": [
        "深入理解Transformer架构与源码实现", "GPT-4的技术演进与未来展望", "LangChain实战：构建企业级知识库助手",
        "大模型微调技术(LoRA/QLoRA)详解", "Multi-Agent智能体协作系统设计", "RAG检索增强生成技术最佳实践",
        "提示工程(Prompt Engineering)高级指南", "开源大模型LLaMA 3部署实战", "向量数据库Milvus与Pinecone对比",
        "大模型幻觉问题产生的机理与解决方案", "AI Agent在软件开发中的应用", "多模态大模型的技术原理与应用",
        "AutoGen框架实战：自动化AI代理工作流", "使用DeepSpeed加速大模型训练", "NLP中的Tokenization技术详解",
        "BERT与GPT：编码器与解码器的较量", "强化学习HFRL在大模型对齐中的应用", "大模型量化技术：从FP16到INT4",
        "Stable Diffusion原理解析与应用", "AI辅助编程工具Copilot深度测评"
    ],
    "后端架构": [
        "深入理解Java虚拟机(JVM)内存模型", "Redis持久化机制RDB与AOF详解", "Kafka消息队列高可用架构设计",
        "Spring Boot 3.0新特性全面解析", "微服务架构下的分布式事务解决方案", "MySQL索引优化与查询性能调优",
        "Docker容器化部署实战指南", "Kubernetes(K8s)核心概念与架构解析", "高并发系统设计之限流与熔断",
        "Elasticsearch倒排索引原理揭秘", "Go语言高并发编程实战", "Nginx负载均衡策略与配置详解",
        "MongoDB分片与副本集架构设计", "Reatful API设计最佳实践", "gRPC与Protobuf高性能RPC框架",
        "Netty高性能网络编程原理", "分布式锁的实现方案对比(Redis/Zookeeper)", "数据库读写分离与分库分表策略",
        "RocketMQ事务消息原理与实战", "Spring Cloud Alibaba全家桶实战"
    ],
    "前端开发": [
        "Vue3 组合式API(Composition API)实战", "React 18 并发模式(Concurrent Mode)详解", "TypeScript 高级类型编程指南",
        "前端性能优化：从输入URL到页面加载", "Webpack5 构建速度优化与配置", "Vite原理解析：新一代前端构建工具",
        "Next.js 服务端渲染(SSR)实战", "微前端架构qiankun实战与原理", "Node.js 事件循环(Event Loop)机制详解",
        "CSS3 Flexbox与Grid布局完全指南", "JavaScript闭包与原型链深度解析", "浏览器渲染原理与重绘重排",
        "前端工程化：ESLint/Prettier/Husky配置", "PWA渐进式Web应用开发指南", "Three.js 3D可视化开发入门",
        "Electron桌面应用开发实战", "Flutter跨平台开发最佳实践", "小程序性能优化与底层原理",
        "前端安全：XSS与CSRF攻击防御", "Rust在前端工具链中的应用"
    ],
    "算法与数据结构": [
        "动态规划(DP)解题套路与经典例题", "图论算法：Dijkstra与Floyd详解", "红黑树(RBTree)原理与手写实现",
        "十大经典排序算法动画演示与解析", "回溯算法解决全排列与N皇后问题", "贪心算法在区间调度中的应用",
        "KMP算法：字符串匹配的极致优化", "并查集(Union-Find)原理与应用", "LeetCode高频面试题刷题指南",
        "位运算技巧在算法竞赛中的应用", "LRU缓存淘汰算法设计与实现", "B+树在数据库索引中的应用原理",
        "一致性哈希算法原理与实现", "布隆过滤器(Bloom Filter)详解", "Trie树(字典树)在字符串处理中的应用"
    ],
    "生活与思考": [
        "程序员的自我修养：如何保持持续学习", "深度工作：如何在碎片化时代保持专注", "技术管理：从独立贡献者到团队Leader",
        "远程工作的一年：挑战与收获", "读书笔记：《黑客与画家》", "我的2025年终总结", "如何构建个人的知识体系",
        "时间管理：番茄工作法与GTD实践", "程序员的身体健康指南", "开源精神：参与开源社区的体验"
    ]
}

# 模板内容
content_templates = [
    """
## 前言

在当今快速发展的技术领域，{keyword} 已经成为了一个不可忽视的重要方向。本文将结合我的实际项目经验，深入探讨 {keyword} 的核心原理与应用实践。

## 核心概念

### 什么是 {keyword}？

简单来说，{keyword} 是一种... （此处省略500字技术细节）...

### 为什么选择它？

1. **高性能**：经过测试，效率提升了30%。
2. **易用性**：API设计极其人性化。
3. **社区活跃**：拥有庞大的开发者生态。

## 实战演示

下面我们通过一个具体的代码示例来演示：

```python
def main():
    print("Hello, {keyword}!")
    # 这里是核心逻辑实现
    # ...
```

## 遇到的坑与解决方案

### 问题一：内存泄漏

在早期版本中，我们发现...

**解决方案**：使用弱引用(WeakReference)解决...

## 总结

{keyword} 是一项非常值得投资的技术。希望本文能对大家有所帮助。

## 参考资料

1. 官方文档
2. GitHub Issues
    """,
    """
## 摘要

本文详细分析了 {keyword} 的技术架构，并对比了同类竞品的优劣势。

## 技术背景

随着业务规模的扩张，传统的解决方案已经无法满足需求，因此我们引入了 {keyword}。

## 架构设计

![架构图](https://images.unsplash.com/photo-1518770660439-4636190af475?w=800)

系统的核心模块包括：
- **接入层**：负责流量清洗
- **逻辑层**：处理核心业务
- **数据层**：持久化存储

## 深度解析

对于 {keyword} 的关键算法，我们进行了深度定制...

```java
public class Service {{
    public void run() {{
        // {keyword} 核心逻辑
    }}
}}
```

## 性能压测

我们使用 JMeter 进行了 1000 并发的压测...

## 结语

展望未来，{keyword} 还将在更多场景发挥作用。
    """
]

count = 0
total_target = 100
categories = list(titles_db.keys())

print(f"开始生成 {total_target} 篇博客文章...")

while count < total_target:
    # 随机选择分类
    category = random.choice(categories)
    
    # 获取该分类下的标题列表
    available_titles = titles_db[category]
    
    # 如果该分类还有特定标题，优先使用
    if len(available_titles) > 0:
        title = available_titles.pop(0)
    else:
        # 如果标题用完了，生成一个通用标题
        title = f"{category}领域的探索与实践 Part {random.randint(100, 999)}"
    
    # 生成文件名 (处理特殊字符)
    safe_title = title.replace(' ', '-').replace('/', '-').replace(':', '')
    file_name = f"{safe_title}.md"
    file_path = os.path.join(posts_dir, file_name)
    
    # 随机生成日期 (过去一年内)
    days_back = random.randint(0, 365)
    post_date = datetime.datetime.now() - datetime.timedelta(days=days_back)
    date_str = post_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # 随机选择封面
    cover_img = random.choice(covers)
    
    # 随机选择内容模板
    template = random.choice(content_templates)
    content = template.format(keyword=title.split('：')[0].split(' ')[0])
    
    # 构造Front Matter
    front_matter = f"""---
title: {title}
date: {date_str}
tags:
  - {category}
  - {title.split('：')[0]}
  - 技术分享
categories:
  - {category}
cover: {cover_img}
description: 本文深入探讨了{title}的核心原理与最佳实践，适合中高级开发者阅读。
ai: true
---
{content}
"""
    
    # 写入文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(front_matter)
        
    count += 1

print(f"成功生成 {count} 篇博客文章！")
