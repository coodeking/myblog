# Supabase 配置指南

## 1. 创建项目

1. 访问 [supabase.com](https://supabase.com) 注册并登录
2. 点击 "New Project"
3. 设置项目名称（如 `kaoyan-plan`）
4. 设置数据库密码（记住它）
5. 选择区域（推荐 Singapore）
6. 等待项目创建完成（约2分钟）

## 2. 创建数据表

进入项目后，点击左侧 **SQL Editor**，运行以下 SQL：

```sql
-- 学生信息表
CREATE TABLE students (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMP DEFAULT now(),
    name TEXT NOT NULL,
    contact TEXT NOT NULL,
    target_school TEXT,
    exam_year INT,
    info_json JSONB NOT NULL,
    status TEXT DEFAULT '待处理'
);

-- 规划表
CREATE TABLE plans (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    student_id UUID REFERENCES students(id),
    created_at TIMESTAMP DEFAULT now(),
    updated_at TIMESTAMP DEFAULT now(),
    plan_json JSONB NOT NULL
);

-- 允许匿名插入学生数据
ALTER TABLE students ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Allow anonymous insert" ON students FOR INSERT WITH CHECK (true);
CREATE POLICY "Allow anonymous select" ON students FOR SELECT USING (true);

ALTER TABLE plans ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Allow select" ON plans FOR SELECT USING (true);
```

## 3. 获取 API 凭证

1. 点击左侧 **Settings** → **API**
2. 复制以下信息：
   - **Project URL**: `https://xxxx.supabase.co`
   - **anon public key**: `eyJhbGci...`

## 4. 配置表单页面

编辑 `source/kaoyan/form.html`，找到以下代码：

```javascript
const SUPABASE_URL = 'YOUR_SUPABASE_URL';
const SUPABASE_KEY = 'YOUR_SUPABASE_ANON_KEY';
```

替换为你的实际值。

同样编辑 `source/kaoyan/plan.html` 中的对应位置。

## 5. 部署测试

```bash
cd d:\myblog
hexo clean && hexo g && hexo s
```

访问 `http://localhost:4000/kaoyan/form.html` 测试表单提交。

## 6. 查看提交的数据

1. 在 Supabase 后台点击 **Table Editor**
2. 选择 `students` 表
3. 可以看到所有提交的学生信息

## 7. 插入规划数据

当你用 AI 生成规划后，在 **Table Editor** 的 `plans` 表点击 **Insert row**：

- `student_id`: 对应学生的 id
- `plan_json`: 粘贴规划 JSON

然后将链接 `https://coodeking.top/kaoyan/plan.html?id=规划ID` 发给学生。
