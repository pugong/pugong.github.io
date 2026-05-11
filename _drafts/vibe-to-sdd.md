好的，以下是更新整份 Slides 后的完整文稿，已修正所有 OpenSpec 格式为正确的 Markdown + YAML front matter 结构。

---

## 从 Vibe Coding 到 SDD：安全工程师的技能升维实战

### ——以 OpenSpec + OpenCode 为例，融合 Harness Engineering & Ralph Loop

---

### 幻灯片概览

| 序号 | 内容 |
|------|------|
| 1 | 封面 |
| 2 | 今天我们聊什么 |
| 3 | 热身：你的“感觉”准不准 |
| 4 | 什么是 Vibe Coding |
| 5 | Vibe 的痛点——我们都有体会 |
| 6 | 从 Vibe 到 SDD：核心思维跃迁 |
| 7 | SDD 的四个核心概念 |
| 8 | 什么是 Harness Engineering？ |
| 9 | Harness 在安全场景的落地 |
| 10 | 什么是 Ralph Loop？ |
| 11 | 模块一：零基础编码速成 |
| 12 | 代码的本质：给计算机的“精确菜谱” |
| 13 | 五大核心概念速览（1） |
| 14 | 五大核心概念速览（2） |
| 15 | 互动练习：找出有问题的代码 |
| 16 | 认识项目结构 |
| 17 | 你不需要成为程序员 |
| 18 | 模式识别：安全问题的代码特征 |
| 19 | 模块二：安全场景实战 |
| 20 | 真实业务场景 |
| 21 | 第一步：唤醒 Vibe 直觉 |
| 22 | 第二步：把“感觉”写成“规格” |
| 23 | OpenSpec 正确格式速览 |
| 24 | 规格推导四维度 |
| 25 | OpenSpec 规格示例：数据脱敏规范 |
| 26 | 动手：写第一份 OpenSpec |
| 27 | 第三步：理解执行闭环 |
| 28 | 演示 A：规格 → CI 检查脚本 |
| 29 | 演示 B：规格 → 测试用例 |
| 30 | 演示 C：规格合规报告 |
| 31 | Ralph Loop 在安全场景的落地 |
| 32 | 第四步：构建安全策略集 |
| 33 | 小组展示任务 |
| 34 | 模块三：综合实战 |
| 35 | 从 Vibe 到 SDD：完整路径回顾 |
| 36 | 你今天学到的完整技术栈 |
| 37 | 今天你带走的不只是一份 MD |
| 38 | 回到岗位后的第一件事 |
| 39 | Q&A / 附录资源 |

---

## 正片内容

---

### Slide 1：封面

**从 Vibe Coding 到 SDD**
安全工程师的技能升维实战

**副标题**：
以 OpenSpec + OpenCode 为例
融合 Harness Engineering & Ralph Loop — 让安全策略 7×24 小时自动运行

日期 · 讲师姓名

---

### Slide 2：今天我们聊什么

**痛点 → 理念 → 工具 → 实操**

| 环节 | 内容 |
|------|------|
| 🔍 问题 | Vibe Coding 的天花板在哪 |
| 🧠 理念 | SDD（规格驱动开发）+ Harness Engineering + Ralph Loop |
| 🛠️ 工具 | OpenSpec（写规格）+ OpenCode（让规格跑起来） |
| 🏋️ 模块一 | 零基础编码速成（看懂代码就够了） |
| 🛡️ 模块二 | 安全场景实战四步法 |
| 🔥 模块三 | 综合实战：发现漏洞 → 编写策略 → 验证闭环 |

**今天的目标**：
带走一份能跑在 CI/CD 里的安全策略规格文件，理解“定义约束 → 自动执行”的完整链路。

---

### Slide 3：热身：你的“感觉”准不准

**看一下这个 API 响应**：

```json
{
  "code": 200,
  "data": {
    "name": "张三",
    "phone": "13812345678",
    "id_card": "310101199001011234",
    "email": "zhangsan@example.com"
  }
}
```

用手边的便签纸，写出你觉得**“不太对劲”**的地方。

30 秒，开始 ✍️

---

### Slide 4：什么是 Vibe Coding

**Vibe Coding** = 凭借感觉、经验、记忆来做事

典型场景：
- 🔧 运维：凭记忆敲命令，行就行，不行再换
- 🛡️ 安全：“我记得上次查过这个，应该没问题”
- 🧪 QA：“凭经验这几个边界值容易出问题”
- 🏗️ 架构师：“图画完了，具体落地你们看着办”

**不是贬义词，是技术人的肌肉记忆。**
**但——肌肉记忆无法大规模、持续生效。**

---

### Slide 5：Vibe 的痛点——我们都有体会

| 问题 | 后果 |
|------|------|
| 📋 不成体系 | 查出漏洞，但很难“证明”标准是什么 |
| 👤 不可传承 | 你休假了，你的感觉别人没有 |
| ✅ 不可验证 | 三个月后这条规则还在吗？无法自证 |
| 📈 无法规模化 | 100 个仓库要重复检查多少遍？ |

```
你的经验
↓
查出问题 → 发邮件 → 等研发改 → 再查 → 再发邮件
    ↑___________________________________________↓
              无限循环，全靠人盯
```

> **你的经验是你最大的资产，也是你最大的单点故障。**

---

### Slide 6：从 Vibe 到 SDD：核心思维跃迁

| Vibe：“我做了什么步骤” | SDD：“最终状态必须是什么” |
|---------------------------|----------------------------|
| 凭直觉判断“这里可能有问题” | 写规则定义“什么是对，什么是错” |
| 追着研发发整改邮件 | 策略卡在 CI 入口，不合规不能上线 |
| 人工抽查几个接口 | 所有符合 scope 的接口自动检查 |
| 安全基线在 Word 文档里 | 安全策略在 Git 仓库里，可执行、可审计 |

> **SDD = Specification-Driven Development**
> 先定义“系统必须满足什么”，再由工具去满足这个定义。

---

### Slide 7：SDD 的四个核心概念

| 概念 | 作用 | 一句话 |
|------|------|--------|
| 📐 **OpenSpec** | 写规格 | 定义“对的是什么样” |
| 🛠️ **Harness Engineering** | 定边界 | 给 AI 上好缰绳，让它按约束行动 |
| 🔄 **OpenCode** | 驱动工具 | 把规格翻译成可执行脚本 |
| 🔁 **Ralph Loop** | 自动执行 | 持续迭代直到合规，不完成不许停 |

```
OpenSpec（规格 = Harness 定义）
       ↓
OpenCode（翻译层）
       ↓
Ralph Loop（执行引擎：扫描→修复→验证→通过/重来）
       ↓
安全合规 ✅
```

---

### Slide 8：什么是 Harness Engineering？

**Harness = AI 的“缰绳”**

| 概念 | 类比赛马 |
|------|----------|
| 🐎 **AI 模型** | 一匹强壮的马，跑得快但不知道往哪跑 |
| 🏇 **人类工程师** | 骑手，指引方向 |
| 🛠️ **Harness（马具）** | 约束、护栏、反馈回路——把蛮力转化为生产力 |

**来自 Anthropic CEO Dario Amodei 的核心洞察**：
> “Agent = Model + Harness + Context”
> 一个靠谱的 AI 系统，模型只占三分之一。真正的工程能力在 Harness——**你如何约束它、引导它、验证它。**

> 💡 **对安全工程师来说，OpenSpec 规格文件就是你的 Harness。你不需要驯马，你只需要定义缰绳。**

---

### Slide 9：Harness 在安全场景的落地

**你的 OpenSpec 规格文件 = 安全场景的 Harness**

| Harness 组件 | 对应 OpenSpec 结构 | 作用 |
|-------------|-------------------|------|
| 🎯 目标定义 | `## Purpose` | AI 要知道“我要达成什么” |
| 📏 行为边界 | `### Requirement: ... SHALL/MUST` | “只能在这个范围内动手” |
| 🔍 验证条件 | `#### Scenario: GIVEN/WHEN/THEN` | “满足这些条件才算合规” |
| 🚦 约束等级 | SHALL（强制）vs SHOULD（建议） | “违规了是拦还是告警” |

**核心哲学**：
> 你不需要控制 AI 的每一步。你只需要定义好边界，告诉它——“墙在这里，你只能在墙内跑。跑出去就自动拉回来。”

---

### Slide 10：什么是 Ralph Loop？

**Ralph Loop = 让 AI “不完成不许下班”**

**起源**：澳洲开发者 Geoffery Huntley 在农场“铲羊粪间隙”，写出了最原始的 Ralph Loop——只有 5 行 Bash：

```bash
while :; do 
    cat PROMPT.md | claude-code
done
```

**核心逻辑**：
- 读取任务文件 → 交给 AI 执行 → 检查结果 → 不通过就重新来 → 直到完成
- AI 每次看到上一轮的错误和反馈，会自动修正、迭代

**Ralph 的名字来自《辛普森一家》**：
一个天真但异常执着的小学生。他的经典台词：
> **“Me fail English? That's unpossible!”**
> **“I'm in danger!”**

——和 AI 屡败屡战、在循环中不断修正自己的精神完美契合。

**Ralph Loop 的三个关键设计**：
1. 🔄 **每轮全新上下文**：避免“上下文腐烂”
2. 🎯 **人类定义“完成”**：测试通过 / 合规报告无告警
3. 👤 **人类最终审批**：AI 创建检查管道，人审核结果

---

### Slide 11：模块一：零基础编码速成

**目标**：能阅读简单代码，找到安全问题位置

**不讲语法大全，只讲“读懂所需的最小概念集”**

> **安全工程师学习编码的核心是“识别坏味道”，就像福尔摩斯不必成为化学家，但必须能识别毒药。**

| 你不需要 | 你只需要 |
|----------|----------|
| 从零搭建一个 Web 服务 | 能认出“这段代码在处理用户输入” |
| 手写完美的算法 | 能认出“这里返回了敏感字段” |
| 理解框架底层原理 | 能认出“这个函数没有做权限检查” |
| 记住所有语法 | 知道去哪查，能看懂大致逻辑 |

---

### Slide 12：代码的本质：给计算机的“精确菜谱”

**给人写的菜谱**：
> “西红柿炒鸡蛋，先炒蛋盛出，再炒西红柿，混合调味。”

**给计算机写的代码**：
> “鸡蛋 2 个，打入碗中，筷子搅拌 30 秒。油温 180°C，倒入蛋液，翻炒 60 秒，盛出备用。再加油，倒入切块西红柿，翻炒 120 秒。加入蛋、盐 3 克、糖 2 克，翻炒 30 秒。出锅。”

代码就是**精确到每一步、每一条指令的菜谱**。没有任何模糊地带。

---

### Slide 13：五大核心概念速览（1）

```python
# 1. 变量：给数据起名字
user_name = "张三"          # 字符串
login_attempts = 0          # 数字
is_admin = False            # 布尔值（真/假）

# 2. 函数：一段有名字的操作
def mask_phone(phone):
    """把手机号中间四位变成****"""
    return phone[:3] + "****" + phone[7:]

# 3. 条件判断：做决策
if login_attempts > 5:
    print("账号已锁定")
else:
    print("请重试")
```

---

### Slide 14：五大核心概念速览（2）

```python
# 4. 数据结构：装东西的容器
user_info = {                    # 字典：键值对
    "name": "张三",
    "phone": "13812345678",
    "email": "zhangsan@example.com"
}
sensitive_fields = ["phone", "email", "id_card"]  # 列表

# 5. HTTP 请求处理：Web 服务最常见场景
@app.route("/api/user/profile")   # 当有人访问这个网址时
def get_profile(user_id):         # 执行下面这个函数
    user = database.find(user_id)
    return user                   # ⚠️ 返回了什么？脱敏了吗？
```

---

### Slide 15：互动练习：找出有问题的代码

```python
@app.route("/api/user/profile")
def get_profile(user_id):
    user = {
        "name": "张三",
        "phone": "13812345678",
        "id_card": "310101199001011234"
    }
    return user
```

**请圈出你可能担心的安全问题。**（30 秒思考）

**答案**：
- `phone` 明文返回（应脱敏为 `138****5678`）
- `id_card` 明文返回（应脱敏）
- 没有鉴权检查（谁都能调这个接口）
- 没有输入校验（`user_id` 没做任何检查）

---

### Slide 16：认识项目结构

```
user-api/
├── main.py                    # 入口文件，程序启动的地方
├── handlers/                  # 处理 HTTP 请求的函数
│   ├── login.py               # 登录逻辑
│   ├── profile.py             # 用户信息查询 ← 你的策略重点盯这里
│   └── admin.py               # 管理员功能
├── config.yaml                # 配置文件（数据库地址、密钥等）
└── README.md
```

**关键认知**：
- `handlers/` 的一个文件 = 一个或一组 API 端点
- 安全策略要盯的就是这些文件里的函数
- Markdown 格式的 OpenSpec 文件，和 README.md **长得几乎一样**——它本就是给人读、也给机器解析的文档

---

### Slide 17：你不需要成为程序员

**安全工程师的代码能力 = “阅读 + 模式识别”，不是“创造”**

| 你的能力 | 代码场景的应用 |
|----------|---------------|
| 👁️ 识别异常 | 认出不正常的返回值、缺失的检查 |
| 🔍 模式匹配 | 认出“这和上次出事的代码长得一样” |
| 📋 规则思维 | 把安全基线转化为可检查的条件 |
| 🤔 批判性阅读 | “这个函数真的做了鉴权吗？” |

---

### Slide 18：模式识别：安全问题的代码特征

| 安全问题 | 代码特征（坏味道） |
|----------|-------------------|
| 🔴 明文敏感信息 | `return user` 没经过 `mask()` 或 `filter()` |
| 🔴 权限缺失 | 函数开头没有 `if not is_admin: return 403` |
| 🔴 SQL 注入 | `“SELECT * FROM users WHERE id = ” + user_id` |
| 🔴 硬编码密钥 | `password = “admin123”` 写在代码或配置里 |
| 🔴 日志泄露 | `print(token)` / `log.info(user)` 打印敏感数据 |
| 🔴 缺少限流 | 登录接口没有调用 `rate_limit()` 或类似注解 |

> **你是模式匹配专家。不过以前匹配的是日志、报警、异常行为，现在增加了一种模式：代码模式。**

---

### Slide 19：模块二：安全场景实战

**四步法**：从直觉到自动运行的安全策略

```
Step 1: 唤醒 Vibe → Step 2: 写成规格 → Step 3: 理解执行闭环 → Step 4: 构建策略集
  (直觉判断)        (OpenSpec MD)   (OpenCode + Ralph Loop)      (完整资产)
```

**核心理念**：
> 每一步都让你离“人盯”更远，离“系统自动盯”更近。

---

### Slide 20：真实业务场景

**背景设定**：
- 公司 100+ 个内部微服务 API
- 安全团队仅 3 人
- 安全基线存在 Word 文档里：“大家看过了吧？”

**出的事故**：
- 5 个 API 没做鉴权，谁都能调
- 3 个返回了明文手机号和身份证
- 2 个登录接口没限流，被暴力破解

**今天的目标**：
把“人追人”模式 → 改成“规格驱动 + AI 循环执行 → 不合规自动拦截”

---

### Slide 21：第一步：唤醒 Vibe 直觉

**任务**：快速审视 `user-api` 项目，列出你认为的 5 个安全检查点

**思考脚手架**：
- 🔐 鉴权：admin.go 里谁都能调吗？
- 📊 数据：profile.go 返回了什么字段？脱敏了吗？
- ⚙️ 配置：config.yaml 里有没有密码？
- 🌐 传输：HTTP 还是 HTTPS？
- 🔍 输入：有没有做参数校验？

> **这些是你脑子里的安全经验——宝贵的起点。下面把它外化出来，变成可执行的规则。**

---

### Slide 22：第二步：把“感觉”写成“规格”

**核心转变**：安全判断从一句话 → 结构化 Markdown 规格文件

**示例**：
> 安全要求：“API 不能返回明文手机号。”

**OpenSpec 的做法**：
写一份 Markdown 文件，用 Purpose 描述目标，用 Requirement 声明强制约束，用 Scenario 定义可验证的测试场景。

> OpenSpec 的核心理念：**规格文件既给人读，也给机器解析。** 它不是传统的需求文档，而是人和 AI 之间的公共语言。

---

### Slide 23：OpenSpec 正确格式速览

**OpenSpec 规范文件 = Markdown + YAML front matter**

```markdown
---
title: 规范名称
version: 1.0.0
status: approved
domain: security
---

# <能力名称>规范

## Purpose
对这个能力/模块的高层描述。

## Requirements

### Requirement: <需求名称>
系统 SHALL/MUST <行为描述>

#### Scenario: <场景名称>
- **GIVEN** <前置条件>
- **WHEN** <触发动作>
- **THEN** <预期结果>
- **AND** <附加预期>（可选）
```

**关键规则**：
- Requirements 必须包含 **SHALL** 或 **MUST** 关键字
- 每个 Requirement 至少有一个 Scenario
- Scenario 用 **GIVEN/WHEN/THEN** 描述可验证场景
- YAML front matter 存储元数据（标题、版本、状态等）

---

### Slide 24：规格推导四维度

将安全需求的思考，映射到 OpenSpec 结构：

| 维度 | 要回答的问题 | OpenSpec 对应 |
|------|-------------|--------------|
| 🎯 目标 | 这条规则要达到什么目的？ | `## Purpose` |
| 📏 约束 | 系统必须做什么？ | `### Requirement: ... SHALL/MUST` |
| 🔍 验证 | 什么算合规、什么算违规？ | `#### Scenario:` + GIVEN/WHEN/THEN |
| ⚠️ 边界 | 有没有例外情况？ | 在 Scenario 中定义边界条件 |

> 💡 小技巧：先从你最确定的那几个接口开始，不要追求一次全覆盖。

---

### Slide 25：OpenSpec 规格示例：数据脱敏规范

```markdown
---
title: 数据脱敏策略
version: 1.0.0
status: approved
domain: security
owner: 安全团队
created: 2026-05-11
---

# 数据脱敏规范

## Purpose
确保所有 API 响应中的用户敏感数据（手机号、身份证号等）
经过脱敏处理，防止敏感信息通过接口泄露。

## Requirements

### Requirement: 手机号脱敏
系统 SHALL 对所有包含用户信息的 API 响应进行手机号脱敏处理。

#### Scenario: 查询用户信息时返回脱敏手机号
- **GIVEN** 用户信息中存在手机号字段 `"phone": "13812345678"`
- **WHEN** 通过用户查询接口返回该用户信息
- **THEN** 手机号字段显示为 `"phone": "138****5678"`
- **AND** 原始完整手机号不在响应中出现

#### Scenario: 非用户接口返回数据不受影响
- **GIVEN** 接口返回的统计数据中包含数字 `13900001111`
- **WHEN** 该数字不属于手机号上下文
- **THEN** 不对该数字进行脱敏处理

### Requirement: 敏感字段检测阻断
系统 MUST 在 CI/CD 流水线中对代码进行敏感字段检测，
发现违规时阻断构建。

#### Scenario: 代码包含明文敏感字段时阻断构建
- **GIVEN** 代码中存在未脱敏的手机号
- **WHEN** CI 流水线执行安全扫描
- **THEN** 构建失败并提示具体违规字段和位置
- **AND** 输出修复建议
```

> 这就是你的 Harness——你给 AI 上的缰绳。每个 Scenario 都是机器可解析的验证条件，AI 只能在这个框架内执行检查。

---

### Slide 26：动手：写第一份 OpenSpec（10 分钟）

**任务**：从以下安全要求中选一条，写出 OpenSpec 规格文件

1. 🔐 所有管理接口（admin）必须有 JWT 鉴权
2. 🔒 API 响应中不得包含明文身份证号
3. ⏱️ 登录接口限制请求频率（防暴力破解）
4. 🚫 禁止在代码或配置中硬编码密码

**产出物**：一份 `spec.md` 文件，必须包含：
- YAML front matter（title/domain/status）
- `## Purpose` 概述
- 至少一个 `### Requirement`（含 SHALL 或 MUST 关键词）
- 每个 Requirement 至少一个 `#### Scenario`（GIVEN/WHEN/THEN 格式）

---

### Slide 27：第三步：理解执行闭环

**OpenCode + Ralph Loop 如何协同工作**

```
你的 OpenSpec 规格文件（= 安全 Harness）
           ↓
        OpenCode 解析
           ↓
  ┌────────┼────────┬──────────┐
  ↓        ↓        ↓          ↓
CI 脚本  测试用例  合规报告  WAF 规则
  ↓        ↓        ↓          ↓
  └────────┴────────┴──────────┘
           ↓
      Ralph Loop 引擎
           ↓
   ┌─────────────────────────┐
   │ 扫描代码                 │
   │   ↓                     │
   │ 对照 Scenario 逐条验证   │
   │   ↓                     │
   │ 发现违规 → 生成修复建议  │
   │   ↓                     │
   │ 验证修复结果            │
   │   ↓                     │
   │ 不通过？→ 重新循环      │
   │ 通过 → 放行 ✅          │
   └─────────────────────────┘
```

> OpenSpec 的每个 Scenario 就是自动验证的测试用例。OpenCode 解析它们，Ralph Loop 反复执行直到全部通过。

---

### Slide 28：演示 A：规格 → CI 检查脚本

**命令**：
```bash
opencode generate \
  --from security/data-masking.spec.md \
  --target ci-script \
  --output ci/check-phone-masking.sh
```

**自动生成的脚本**（关键部分）：
```bash
#!/bin/bash
# Auto-generated from security/data-masking.spec.md
# Scenario: 查询用户信息时返回脱敏手机号

API_RESPONSE_FILE=$1
PATTERN='"phone":\s*"1[3-9]\d{9}"'

if grep -P "$PATTERN" "$API_RESPONSE_FILE"; then
  echo "FAIL: Scenario '查询用户信息时返回脱敏手机号' 未通过"
  echo "检测到明文手机号，请脱敏为 138****5678 格式"
  exit 1
fi
echo "PASS: 手机号脱敏合规"
```

> 你只写了 Markdown 规格，bash 脚本自动生成。每个 Scenario 对应一段检查逻辑。

---

### Slide 29：演示 B：规格 → 测试用例

**命令**：
```bash
opencode generate \
  --from security/data-masking.spec.md \
  --target test-case \
  --framework pytest \
  --output tests/test_data_masking.py
```

**生成的测试用例自动包含**：
- 明文手机号的响应 → 对应 Scenario 失败
- 已脱敏手机号的响应 → 对应 Scenario 通过
- 非手机号数字不误报 → 对应边界 Scenario
- 空响应、无手机号字段、数组嵌套等边界情况

> QA 同事也能用这份规格生成测试。一份规格，多方消费。

---

### Slide 30：演示 C：规格合规报告

**命令**：
```bash
opencode audit \
  --specs security/*.spec.md \
  --repo ../user-api \
  --format report
```

**输出**：
```
规范: 数据脱敏策略 (v1.0.0)
  Status: FAILED
  Requirement: 手机号脱敏 [SHALL]
    Scenario: 查询用户信息时返回脱敏手机号
      - handlers/profile.py:47: FAILED → "phone": "13812345678"
    Scenario: 非用户接口返回数据不受影响
      - PASSED

  Requirement: 敏感字段检测阻断 [MUST]
    Scenario: 代码包含明文敏感字段时阻断构建
      - handlers/admin.py:112: FAILED → "contact": "13987654321"

  Remediation: 
    - 在 handlers/profile.py:47 使用 phone_mask() 函数
    - 在 handlers/admin.py:112 使用 phone_mask() 函数
```

> 以前的流程：发现漏洞 → 写邮件 → 追着研发改 → 不知道改没改。
> 现在的流程：每条 Scenario 自动验证 → 失败则报告具体行号和修复建议。

---

### Slide 31：Ralph Loop 在安全场景的落地

**用 Ralph 思维做安全验证**：

```
OpenSpec 规格（= Harness，定义每个 Scenario）
           ↓
OpenCode 生成检查脚本（每个 Scenario → 一个检查步骤）
           ↓
Ralph Loop 执行引擎启动 ——
  ├─ 🔍 逐条验证 Scenario
  ├─ 🚨 GIVEN/WHEN 匹配 → THEN 不满足 → 违规
  ├─ 🔧 生成修复建议
  ├─ ❌ 修复后重新验证 → 仍有 Scenario 未通过 → 再来一轮
  └─ ✅ 全部 Scenario 通过 → 放行
```

**关键设计**（Harness 的缰绳作用）：
- 🔄 每轮都用全新上下文，避免“上下文腐烂”
- 🎯 Scenario 的 THEN 子句就是“完成”的定义——所有 THEN 满足才算过
- 👤 最终部署依旧由人审批——AI 创建检查管道，人审核结果

> **Ralph Loop 让安全验证变成 7×24 的自动化流水线。你的 Scenario 就是你派出去的 24 小时值班安全员。**

---

### Slide 32：第四步：构建安全策略集

**小组任务**（3-4 人一组）

**目标**：为 `user-api` 项目构建一套安全策略规格

**维度要求**（至少选三个）：
- 🔐 鉴权与授权
- 🔒 数据保护（脱敏）
- ⏱️ 速率限制
- 🛡️ 输入校验

**产出物清单**：
1. 每个维度的 OpenSpec 规格文件（`.spec.md`）
2. 策略索引 README（列出每个 spec 的一句话 Purpose）
3. 可选：尝试运行 `opencode audit`，看合规报告

---

### Slide 33：小组展示任务（5 分钟/组）

**展示内容**：
1. 你们选了哪条 Requirement？
2. 它对应项目的哪段代码？（指出具体文件和行号）
3. 你的 Scenario 是如何定义“对”和“错”的？

**评价标准**：
- ✅ Purpose 清楚吗？（新成员一看就懂这条策略管什么）
- ✅ Requirement 的 SHALL/MUST 用得对吗？（约束等级明确）
- ✅ Scenario 的 THEN 可验证吗？（机器能自动判断通过/失败）
- ✅ 边界 Scenario 考虑了吗？（不会误报正常数据）

---

### Slide 34：模块三：综合实战

**场景**：新项目 `order-api` 提交代码，需上线前安全检查

| 阶段 | 任务 | 时间 |
|------|------|------|
| 🔍 代码审计 | 找出代码中的安全问题（已预埋 5 个） | 15 分钟 |
| 📋 编写规格 | 选 2 个问题写 OpenSpec 规格文件 | 15 分钟 |
| 🎤 展示汇报 | 问题 → 代码位置 → Requirement → Scenario → 验证逻辑 | 15 分钟 |

**预埋的安全问题**：
1. 响应中返回明文身份证号
2. 管理接口没有鉴权检查
3. SQL 拼接（模拟注入风险）
4. 日志中打印了 JWT token
5. 配置文件硬编码了数据库密码

---

### Slide 35：从 Vibe 到 SDD：完整路径回顾

```
Vibe 时代（靠人盯）：
  经验在脑子里 → 人工抽查 → 发邮件 → 追着研发改 → 祈祷别忘 → 再抽查
     ↑______________________________________________________________↓
                              永远在循环

SDD 时代（靠系统跑）：
  经验写成 OpenSpec MD → 提交到 Git → CI 自动解析 Scenario →
  Ralph Loop 逐条验证 → 不满足 THEN 就拦截 → 审计报告自动生成 ✅
```

| 以前 | 以后 |
|------|------|
| 🔍 漏洞发现者 | 📐 安全标准定义者 |
| 📧 整改督促员 | 🤖 策略自动化运营者 |
| 👤 依赖个人经验 | 🏛️ 安全能力变成组织资产 |
| 😰 人下班安全就下班 | 😴 你睡觉，Ralph Loop 还在逐条验证 Scenario |

---

### Slide 36：你今天学到的完整技术栈

**从 Vibe Coding 到 SDD 的技术全景图**：

```
安全经验（在脑子里）
         ↓ 外化为结构化文档
    OpenSpec 规格文件（Markdown）
         = Harness 定义
         ↓ 机器解析
    OpenCode 生成（每个 Scenario → 检查逻辑）
         ↓ 自动执行
    Ralph Loop 循环（逐条验证 THEN）
         = Harness 执行
         ↓ 产出
    安全合规报告 ✅
```

**四者的分工**：

| 技术 | 解决的问题 | 在安全场景的体现 |
|------|-----------|-----------------|
| 📐 **OpenSpec** | “规是什么” | Purpose + Requirement + Scenario |
| 🛠️ **Harness Engineering** | “边界在哪” | SHALL/MUST 定义强制约束，Scenario 定义边界条件 |
| 🔄 **OpenCode** | “怎么翻译” | 将每个 Scenario 翻译为检查脚本、测试用例 |
| 🔁 **Ralph Loop** | “怎么做到位” | 循环验证所有 Scenario 的 THEN，不通过就再来 |

**核心公式**：
```
安全自动化 = OpenSpec 规格（定义边界）
            + OpenCode 解析（翻译为可执行逻辑）
            + Ralph Loop 循环（逐 Scenario 执行直到通过）
            + Harness Engineering（始终在 SHALL/MUST 约束内）
```

---

### Slide 37：今天你带走的不只是一份 MD

**你的新能力**：

- 🧠 能读懂简单代码，定位安全问题
- 📋 能把安全经验转化为 OpenSpec 规格文件（Markdown 格式）
- 🔧 理解 Scenario 如何变成自动化检查（OpenCode 解析 + Ralph Loop 执行）
- 🔄 理解 Harness + Ralph Loop 如何让安全策略 7×24 小时自动运转
- 🚀 获得从“靠人盯”到“靠系统跑”的迁移路径

> **这不是抢研发的饭碗。**
> **这是让你的安全判断不再依赖你本人 24 小时在线。**
> **你写下的每个 Scenario，在你睡觉时仍然在被 Ralph Loop 逐条验证。**
> **每次 THEN 不满足，系统自动拦截——就像你亲自站在 CI 门口。**

---

### Slide 38：回到岗位后的第一件事

**本周可以做的**：

1. 📋 找出团队最头疼的一个安全问题
2. 📝 用 OpenSpec 格式写出第一份规格文件（Purpose + 至少一个 Requirement + Scenario）
3. 🔧 放到测试项目里跑一次 `opencode audit`
4. 👥 在下次团队分享会上展示成果

**一个月可以做的**：
- 把生产环境 TOP 3 安全事件对应的检测逻辑，转化为 OpenSpec 规格文件
- 接入 CI 流水线，至少一条 Requirement 实现“不合规不能上线”
- 建立团队 OpenSpec 规格仓库，鼓励所有人提交策略 MR

> **哪怕只有一个 Scenario 真正跑起来，你都完成了一次职业能力的实质性升维。**
> **Harness 定义了“对”的边界，Ralph 确保“对”被持续验证。**

---

### Slide 39：Q&A / 附录资源

**随堂资料**：
- 📋 代码速查卡（Python 常见语法）
- 🕵️ 安全模式匹配表（问题 → 代码特征）
- 📐 OpenSpec 格式速查卡（Purpose / Requirement / Scenario 模板）
- 🗂️ 模拟项目仓库地址

**延伸阅读**：
- OpenSpec 官方文档与社区规范
- Harness Engineering 理念（Anthropic 技术博客）
- Ralph Loop 原始实现与社区演进
- 从 Vibe Coding 到 AI 协作：技术人的新护城河
- GIVEN/WHEN/THEN 格式在 BDD 中的应用

---

**谢谢！欢迎随时交流 🛡️**

**核心 takeaway**：
> *你写下的每个 Scenario，都是派出去的安全哨兵。*
> *Harness 定义“什么是对的”，Ralph Loop 确保“对的一定被验证”。*
> *安全工程师的未来，不是做更多的检查，而是定义让系统自动遵守的边界。*

---

如需我进一步导出 Markdown 文件、PPT 兼容格式，或对某一页做更详细的讲稿注释，随时告诉我。