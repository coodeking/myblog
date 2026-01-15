---
title: RAG技术详解：让大模型拥有最新知识
date: 2026-01-12 10:00:00
tags:
  - RAG
  - 大模型
  - 向量数据库
  - LangChain
categories:
  - 大模型
cover: https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800
description: 深入理解检索增强生成（RAG）技术，解决大模型知识过时和幻觉问题
ai: true
---

## 前言

大语言模型虽然强大，但存在两个核心问题：**知识截止日期**和**幻觉问题**。RAG（Retrieval-Augmented Generation，检索增强生成）技术正是解决这些问题的关键方案。

## 一、什么是RAG？

RAG是一种将检索系统与生成模型相结合的技术架构：

```
用户问题 → 检索相关文档 → 将文档与问题一起输入LLM → 生成答案
```

### 1.1 RAG的核心优势

| 优势 | 说明 |
|------|------|
| 知识更新 | 无需重新训练模型，只需更新知识库 |
| 减少幻觉 | 答案基于检索到的真实文档 |
| 可溯源 | 可以追踪答案的信息来源 |
| 成本低 | 比微调模型成本低得多 |

### 1.2 RAG vs 微调

```
┌─────────────────────────────────────────────────────────┐
│                    选择决策树                            │
├─────────────────────────────────────────────────────────┤
│  需要模型学习新的任务/风格？                              │
│      ├── 是 → 微调（Fine-tuning）                       │
│      └── 否 → 需要最新/私有知识？                        │
│              ├── 是 → RAG                               │
│              └── 否 → 直接使用基础模型                   │
└─────────────────────────────────────────────────────────┘
```

## 二、RAG系统架构

一个完整的RAG系统包含以下组件：

### 2.1 索引阶段（Indexing）

```python
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# 1. 加载文档
loader = DirectoryLoader('./docs', glob="**/*.md")
documents = loader.load()

# 2. 文本分块
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", "。", "，", " "]
)
chunks = text_splitter.split_documents(documents)

# 3. 向量化并存储
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)
```

### 2.2 检索阶段（Retrieval）

```python
# 基础检索
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}
)

# 混合检索（结合关键词和语义）
from langchain.retrievers import BM25Retriever, EnsembleRetriever

bm25_retriever = BM25Retriever.from_documents(chunks)
bm25_retriever.k = 5

ensemble_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, retriever],
    weights=[0.4, 0.6]
)
```

### 2.3 生成阶段（Generation）

```python
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# 自定义提示模板
template = """基于以下上下文信息回答问题。如果上下文中没有相关信息，请明确说明。

上下文：
{context}

问题：{question}

回答："""

prompt = PromptTemplate(
    template=template,
    input_variables=["context", "question"]
)

# 构建RAG链
llm = ChatOpenAI(model_name="gpt-4", temperature=0)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    chain_type_kwargs={"prompt": prompt},
    return_source_documents=True
)

# 查询
result = qa_chain({"query": "什么是RAG技术？"})
print(result["result"])
print("来源:", result["source_documents"])
```

## 三、RAG优化技巧

### 3.1 分块策略优化

分块大小直接影响检索质量：

| 分块大小 | 优点 | 缺点 |
|----------|------|------|
| 小（200-500字符） | 检索精准 | 可能丢失上下文 |
| 中（500-1000字符） | 平衡 | 通用选择 |
| 大（1000-2000字符） | 上下文完整 | 可能引入噪声 |

**最佳实践**：使用语义分块，按段落/章节切分

```python
from langchain.text_splitter import MarkdownHeaderTextSplitter

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

markdown_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on
)
```

### 3.2 检索增强

**重排序（Reranking）**：使用专门的重排序模型提升检索质量

```python
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import CohereRerank

compressor = CohereRerank()
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=retriever
)
```

### 3.3 查询优化

**查询扩展**：将用户问题改写为多个查询

```python
from langchain.retrievers.multi_query import MultiQueryRetriever

multi_query_retriever = MultiQueryRetriever.from_llm(
    retriever=retriever,
    llm=llm
)
```

**HyDE（Hypothetical Document Embeddings）**：

```python
# 先让LLM生成一个假设性回答，用这个回答去检索
hypothetical_answer = llm.predict(
    f"请简要回答：{question}"
)
# 用假设性回答进行检索
docs = retriever.get_relevant_documents(hypothetical_answer)
```

## 四、向量数据库选型

| 数据库 | 特点 | 适用场景 |
|--------|------|----------|
| Chroma | 轻量、易用 | 原型开发、小规模 |
| Pinecone | 托管服务、高性能 | 生产环境 |
| Milvus | 开源、可扩展 | 大规模、自部署 |
| Weaviate | 混合搜索 | 需要关键词+语义 |
| FAISS | Meta开源、纯向量 | 研究、大规模 |

## 五、评估RAG系统

### 5.1 评估指标

```python
from ragas import evaluate
from ragas.metrics import (
    faithfulness,      # 答案是否忠于文档
    answer_relevancy,  # 答案与问题的相关性
    context_precision, # 检索精度
    context_recall     # 检索召回
)

result = evaluate(
    dataset,
    metrics=[faithfulness, answer_relevancy, 
             context_precision, context_recall]
)
```

### 5.2 常见问题诊断

| 问题 | 可能原因 | 解决方案 |
|------|----------|----------|
| 答案不相关 | 检索质量差 | 优化Embedding、增加重排序 |
| 答案不完整 | 分块太小 | 增大分块、增加检索数量 |
| 答案有错误 | LLM幻觉 | 降低temperature、优化prompt |
| 速度太慢 | 检索/生成耗时 | 缓存、异步、减少检索量 |

## 六、生产环境最佳实践

1. **使用缓存**：对相同/相似查询缓存结果
2. **异步处理**：检索和生成异步执行
3. **监控告警**：记录检索质量、响应时间等指标
4. **版本管理**：管理Embedding模型和知识库版本
5. **安全过滤**：对输入输出进行安全检查

## 总结

RAG是当前最实用的大模型增强技术之一。通过合理的架构设计和持续优化，可以显著提升AI应用的准确性和可用性。

## 参考资料

1. Lewis, P., et al. "Retrieval-augmented generation for knowledge-intensive nlp tasks." NeurIPS 2020.
2. LangChain Documentation
3. LlamaIndex Documentation
