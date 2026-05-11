
## 从 Vibe Coding 到 SDD：安全工程师的技能升维实战
### 以 OpenSpec + OpenCode 为例，融合 Harness Engineering & Ralph Loop

---

## 今天我们聊什么

| 环节 | 内容 |
|------|------|
| 🔍 问题 | Vibe Coding 的天花板在哪 |
| 🧠 理念 | SDD + Harness Engineering + Ralph Loop |
| 🛠️ 工具 | OpenSpec（写规格）+ OpenCode（让规格跑起来） |
| 🏋️ 模块一 | 零基础编码速成 |
| 🛡️ 模块二 | 安全场景实战四步法 |
| 🔥 模块三 | 综合实战 |

**今天的目标**：带走一份能跑在 CI/CD 里的安全策略规格文件

---

## 热身：你的"感觉"准不准

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

✍️ 写出你觉得**"不太对劲"**的地方（30秒）

---

## 什么是 Vibe Coding

**Vibe Coding** = 凭借感觉、经验、记忆来做事

- 🔧 运维：凭记忆敲命令，行就行，不行再换
- 🛡️ 安全："我记得上次查过这个，应该没问题"
- 🧪 QA："凭经验这几个边界值容易出问题"
- 🏗️ 架构师："图画完了，具体落地你们看着办"

**不是贬义词，是技术人的肌肉记忆。**
**但——肌肉记忆无法大规模、持续生效。**

---

## Vibe 的痛点——我们都有体会

| 问题 | 后果 |
|------|------|
| 📋 不成体系 | 查出漏洞，但很难"证明"标准是什么 |
| 👤 不可传承 | 你休假了，你的感觉别人没有 |
| ✅ 不可验证 | 三个月后这条规则还在吗？无法自证 |
| 📈 无法规模化 | 100 个仓库要重复检查多少遍？ |

```
你的经验 → 查出问题 → 发邮件 → 等研发改 → 再查 → 再发邮件 → 循环……
```

> **你的经验是你最大的资产，也是你最大的单点故障。**

---

## 从 Vibe 到 SDD：核心思维跃迁

| Vibe："我做了什么步骤" | SDD："最终状态必须是什么" |
|---------------------------|----------------------------|
| 凭直觉判断"这里可能有问题" | 写规则定义"什么是对，什么是错" |
| 追着研发发整改邮件 | 策略卡在 CI 入口，不合规不能上线 |
| 人工抽查几个接口 | 所有符合 scope 的接口自动检查 |
| 安全基线在 Word 文档里 | 安全策略在 Git 仓库里，可执行、可审计 |

> **SDD = Specification-Driven Development**
> 先定义"系统必须满足什么"，再由工具去满足这个定义。

---

## SDD 的四个核心概念

| 概念 | 作用 | 一句话 |
|------|------|--------|
| 📐 OpenSpec | 写规格 | 定义"对的是什么样" |
| 🛠️ Harness Engineering | 定边界 | 给 AI 上好缰绳 |
| 🔄 OpenCode | 驱动工具 | 把规格翻译成可执行脚本 |
| 🔁 Ralph Loop | 自动执行 | 持续迭代直到合规，不完成不许停 |

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

## 什么是 Harness Engineering？

**Harness = AI 的"缰绳"**

| 概念 | 类比赛马 |
|------|----------|
| 🐎 AI 模型 | 一匹强壮的马，跑得快但不知道往哪跑 |
| 🏇 人类工程师 | 骑手，指引方向 |
| 🛠️ Harness（马具） | 约束、护栏、反馈回路 |

**Dario Amodei（Anthropic CEO）**：
> "Agent = Model + Harness + Context"
> 真正的工程能力在 Harness——你如何约束它、引导它、验证它。

> 💡 **对安全工程师来说，OpenSpec 规格文件就是你的 Harness。**

---

## Harness 在安全场景的落地

| Harness 组件 | 对应 OpenSpec 结构 | 作用 |
|-------------|-------------------|------|
| 🎯 目标定义 | `## Purpose` | AI 要知道"我要达成什么" |
| 📏 行为边界 | `### Requirement: ... SHALL/MUST` | "只能在这个范围内动手" |
| 🔍 验证条件 | `#### Scenario: GIVEN/WHEN/THEN` | "满足这些条件才算合规" |
| 🚦 约束等级 | SHALL（强制）vs SHOULD（建议） | "违规了是拦还是告警" |

> **你不需要控制 AI 的每一步。你只需要定义好边界。**

---

## 什么是 Ralph Loop？

**Ralph Loop = 让 AI "不完成不许下班"**

**起源**：澳洲开发者 Geoffery Huntley 在农场写出的 5 行 Bash：

```bash
while :; do 
    cat PROMPT.md | claude-code
done
```

**核心逻辑**：
读取任务 → AI 执行 → 检查结果 → 不通过就重来 → 直到完成

**名字来自《辛普森一家》**的 Ralph Wiggum：
> "Me fail English? That's unpossible!"
> "I'm in danger!"

**三个关键设计**：
- 🔄 每轮全新上下文
- 🎯 人类定义"完成"
- 👤 人类最终审批

---

## 模块一：零基础编码速成

**目标**：能阅读简单代码，找到安全问题位置

| 你不需要 | 你只需要 |
|----------|----------|
| 从零搭建 Web 服务 | 能认出"这段代码在处理用户输入" |
| 手写完美算法 | 能认出"这里返回了敏感字段" |
| 理解框架底层 | 能认出"这个函数没有权限检查" |
| 记住所有语法 | 知道去哪查，能看懂大致逻辑 |

> **安全工程师学编码的核心是"识别坏味道"。**

---

## 代码的本质：给计算机的"精确菜谱"

**给人写的菜谱**：
> "西红柿炒鸡蛋，先炒蛋盛出，再炒西红柿，混合调味。"

**给计算机写的代码**：
> "鸡蛋 2 个，打入碗中，筷子搅拌 30 秒。油温 180°C，倒入蛋液，翻炒 60 秒，盛出备用……"

代码就是**精确到每一步、每一条指令的菜谱**。

---

## 五大核心概念速览（1）

```python
# 1. 变量：给数据起名字
user_name = "张三"
login_attempts = 0
is_admin = False

# 2. 函数：一段有名字的操作
def mask_phone(phone):
    return phone[:3] + "****" + phone[7:]

# 3. 条件判断：做决策
if login_attempts > 5:
    print("账号已锁定")
else:
    print("请重试")
```

---

## 五大核心概念速览（2）

```python
# 4. 数据结构：装东西的容器
user_info = {
    "name": "张三",
    "phone": "13812345678",
    "email": "zhangsan@example.com"
}
sensitive_fields = ["phone", "email", "id_card"]

# 5. HTTP 请求处理
@app.route("/api/user/profile")
def get_profile(user_id):
    user = database.find(user_id)
    return user  # ⚠️ 返回了什么？脱敏了吗？
```

---

## 互动练习：找出有问题的代码

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

**安全问题**：
- ❌ `phone` 明文返回
- ❌ `id_card` 明文返回
- ❌ 没有鉴权检查
- ❌ 没有输入校验

---

## 认识项目结构

```
user-api/
├── main.py            # 入口文件
├── handlers/          # 处理 HTTP 请求
│   ├── login.py       # 登录逻辑
│   ├── profile.py     # 用户信息查询 ← 重点盯这里
│   └── admin.py       # 管理员功能
├── config.yaml        # 配置文件
└── README.md
```

> **handlers/ 的每个文件 = 一个或一组 API 端点**
> **OpenSpec 文件格式和 README.md 一样是 Markdown**

---

## 你不需要成为程序员

**安全工程师的代码能力 = "阅读 + 模式识别"**

| 你的能力 | 代码场景的应用 |
|----------|---------------|
| 👁️ 识别异常 | 认出不正常的返回值、缺失的检查 |
| 🔍 模式匹配 | 认出"这和上次出事的代码长得一样" |
| 📋 规则思维 | 把安全基线转化为可检查的条件 |
| 🤔 批判性阅读 | "这个函数真的做了鉴权吗？" |

---

## 模式识别：安全问题的代码特征

| 安全问题 | 代码特征（坏味道） |
|----------|-------------------|
| 🔴 明文敏感信息 | `return user` 没经过 `mask()` |
| 🔴 权限缺失 | 函数开头没有 `if not is_admin:` |
| 🔴 SQL 注入 | `"SELECT * FROM users WHERE id = " + user_id` |
| 🔴 硬编码密钥 | `password = "admin123"` |
| 🔴 日志泄露 | `print(token)` |
| 🔴 缺少限流 | 没有 `rate_limit()` 调用 |

---

## 模块二：安全场景实战

**四步法**：从直觉到自动运行的安全策略

```
Step 1: 唤醒 Vibe → Step 2: 写成规格 → Step 3: 理解闭环 → Step 4: 构建策略集
  (直觉判断)        (OpenSpec MD)   (OpenCode+Ralph)      (完整资产)
```

> **每一步都让你离"人盯"更远，离"系统自动盯"更近。**

---

## 真实业务场景

**背景**：
- 公司 100+ 个内部微服务 API
- 安全团队仅 3 人
- 安全基线在 Word 文档里

**出的事故**：
- 5 个 API 没做鉴权
- 3 个返回明文手机号和身份证
- 2 个登录接口没限流，被暴力破解

**今天的目标**：
把"人追人" → 改成"规格驱动 + AI 循环执行 → 不合规自动拦截"

---

## 第一步：唤醒 Vibe 直觉

**任务**：快速审视 `user-api` 项目，列出 5 个安全检查点

**思考脚手架**：
- 🔐 鉴权：admin 接口谁都能调吗？
- 📊 数据：profile 返回了什么字段？脱敏了吗？
- ⚙️ 配置：config.yaml 里有没有密码？
- 🌐 传输：HTTP 还是 HTTPS？
- 🔍 输入：有没有做参数校验？

> **这些是你脑子里的安全经验——宝贵的起点。下面把它外化出来。**

---

## 第二步：把"感觉"写成"规格"

**核心转变**：安全判断从一句话 → 结构化 Markdown 规格

**示例**：
> "API 不能返回明文手机号。"

**OpenSpec 的做法**：
写一份 Markdown 文件，用 Purpose 描述目标，用 Requirement 声明强制约束，用 Scenario 定义可验证的测试场景。

> **规格文件既给人读，也给机器解析——是人和 AI 之间的公共语言。**

---

## OpenSpec 正确格式速览

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
```

**关键规则**：
- Requirements 必须包含 SHALL 或 MUST
- 每个 Requirement 至少一个 Scenario
- Scenario 用 GIVEN/WHEN/THEN 描述

---

## 规格推导四维度

| 维度 | 要回答的问题 | OpenSpec 对应 |
|------|-------------|--------------|
| 🎯 目标 | 这条规则要达到什么目的？ | `## Purpose` |
| 📏 约束 | 系统必须做什么？ | `### Requirement: ... SHALL/MUST` |
| 🔍 验证 | 什么算合规、什么算违规？ | `#### Scenario:` GIVEN/WHEN/THEN |
| ⚠️ 边界 | 有没有例外情况？ | 在 Scenario 中定义边界条件 |

---

## OpenSpec 规格示例：数据脱敏规范

```markdown
# 数据脱敏规范

## Purpose
确保所有 API 响应中的用户敏感数据经过脱敏处理。

## Requirements

### Requirement: 手机号脱敏
系统 SHALL 对所有包含用户信息的 API 响应进行手机号脱敏处理。

#### Scenario: 查询用户信息时返回脱敏手机号
- **GIVEN** 用户信息中存在 "phone": "13812345678"
- **WHEN** 通过用户查询接口返回该用户信息
- **THEN** 手机号字段显示为 "phone": "138****5678"
- **AND** 原始完整手机号不在响应中出现
```

> **这就是你的 Harness。每个 Scenario 都是机器可解析的验证条件。**

---

## 动手：写第一份 OpenSpec（10分钟）

**任务**：从以下安全要求中选一条，写出 OpenSpec 规格文件

- 🔐 所有管理接口必须有 JWT 鉴权
- 🔒 API 响应中不得包含明文身份证号
- ⏱️ 登录接口限制请求频率
- 🚫 禁止硬编码密码

**产出物**：一份 `spec.md` 文件，包含：
- YAML front matter
- `## Purpose`
- 至少一个 `### Requirement`（含 SHALL/MUST）
- 每个 Requirement 至少一个 `#### Scenario`（GIVEN/WHEN/THEN）

---

## 第三步：理解执行闭环

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
   │ 扫描 → 对照 Scenario 验证 │
   │   ↓                     │
   │ 违规 → 生成修复建议     │
   │   ↓                     │
   │ 验证修复 → 不通过就重来 │
   │   ↓                     │
   │ 全部通过 → 放行 ✅      │
   └─────────────────────────┘
```

---

## 演示 A：规格 → CI 检查脚本

```bash
opencode generate \
  --from security/data-masking.spec.md \
  --target ci-script \
  --output ci/check-phone-masking.sh
```

**自动生成**：
```bash
#!/bin/bash
# 对应 Scenario: 查询用户信息时返回脱敏手机号
PATTERN='"phone":\s*"1[3-9]\d{9}"'

if grep -P "$PATTERN" "$API_RESPONSE_FILE"; then
  echo "FAIL: 检测到明文手机号"
  exit 1
fi
echo "PASS: 手机号脱敏合规"
```

> **你只写了 Markdown，脚本自动生成。每个 Scenario 对应一段检查逻辑。**

---

## 演示 B：规格 → 测试用例

```bash
opencode generate \
  --from security/data-masking.spec.md \
  --target test-case \
  --framework pytest \
  --output tests/test_data_masking.py
```

**自动生成**：
- 明文手机号 → 预期 Scenario 失败
- 已脱敏手机号 → 预期 Scenario 通过
- 非手机号数字不误报 → 边界 Scenario
- 空响应、嵌套数据等边界情况

> **一份规格，多方消费。QA 也能用。**

---

## 演示 C：规格合规报告

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
      - handlers/profile.py:47: FAILED
      - handlers/admin.py:112: FAILED
  Remediation: 使用 phone_mask() 函数脱敏
```

> **以前的流程**：发现漏洞 → 写邮件 → 追着改
> **现在的流程**：Scenario 自动验证 → 失败即报告具体行号

---

## Ralph Loop 在安全场景的落地

```
OpenSpec 规格（定义每个 Scenario）
           ↓
OpenCode 生成检查脚本
           ↓
Ralph Loop 执行引擎 ——
  ├─ 🔍 逐条验证 Scenario
  ├─ 🚨 THEN 不满足 → 违规
  ├─ 🔧 生成修复建议 → 修复后重验
  └─ ✅ 全部 Scenario 通过 → 放行
```

**Harness 的缰绳作用**：
- 🔄 每轮全新上下文
- 🎯 Scenario 的 THEN 就是"完成"的定义
- 👤 最终部署由人审批

> **你的 Scenario 就是派出去的 24 小时值班安全员。**

---

## 第四步：构建安全策略集

**小组任务**（3-4 人一组）

**维度**（至少选三个）：
- 🔐 鉴权与授权
- 🔒 数据保护（脱敏）
- ⏱️ 速率限制
- 🛡️ 输入校验

**产出物**：
- 每个维度的 `.spec.md` 文件
- 策略索引 README

---

## 小组展示任务（5分钟/组）

**展示内容**：
- 选了哪条 Requirement？
- 对应项目的哪段代码？
- Scenario 如何定义"对"和"错"？

**评价标准**：
- ✅ Purpose 清楚吗？
- ✅ SHALL/MUST 用得对吗？
- ✅ Scenario 的 THEN 可验证吗？
- ✅ 边界 Scenario 考虑了吗？

---

## 模块三：综合实战

**场景**：新项目 `order-api` 需上线前安全检查

| 阶段 | 任务 | 时间 |
|------|------|------|
| 🔍 代码审计 | 找出安全问题（预埋 5 个） | 15 分钟 |
| 📋 编写规格 | 选 2 个问题写 OpenSpec | 15 分钟 |
| 🎤 展示汇报 | 问题→代码位置→Requirement→Scenario | 15 分钟 |

**预埋问题**：明文身份证号、无鉴权、SQL 拼接、日志泄露 token、硬编码密码

---

## 从 Vibe 到 SDD：完整路径回顾

**Vibe 时代（靠人盯）**：
经验在脑子里 → 人工抽查 → 发邮件 → 追着改 → 祈祷别忘 → 再抽查 → 循环……

**SDD 时代（靠系统跑）**：
经验写成 OpenSpec → 提交 Git → CI 解析 Scenario → Ralph Loop 验证 → 不满足 THEN 就拦截 ✅

| 以前 | 以后 |
|------|------|
| 🔍 漏洞发现者 | 📐 安全标准定义者 |
| 📧 整改督促员 | 🤖 策略自动化运营者 |
| 👤 依赖个人经验 | 🏛️ 安全能力变成组织资产 |

---

## 你今天学到的完整技术栈

```
安全经验（在脑子里）
         ↓
    OpenSpec 规格文件（Markdown）
         = Harness 定义
         ↓
    OpenCode 生成（Scenario → 检查逻辑）
         ↓
    Ralph Loop 循环（逐条验证 THEN）
         = Harness 执行
         ↓
    安全合规报告 ✅
```

| 技术 | 解决的问题 |
|------|-----------|
| 📐 OpenSpec | "规是什么" |
| 🛠️ Harness | "边界在哪" |
| 🔄 OpenCode | "怎么翻译" |
| 🔁 Ralph Loop | "怎么做到位" |

---

## 今天你带走的不只是一份 MD

- 🧠 能读懂简单代码，定位安全问题
- 📋 能把安全经验转化为 OpenSpec 规格
- 🔧 理解 Scenario 如何变成自动化检查
- 🔄 理解 Harness + Ralph Loop 的 7×24 运转
- 🚀 获得从"靠人盯"到"靠系统跑"的迁移路径

> **你写下的每个 Scenario，在你睡觉时仍然在被 Ralph Loop 逐条验证。**

---

## 回到岗位后的第一件事

**本周**：
1. 找出团队最头疼的一个安全问题
2. 用 OpenSpec 格式写出第一份规格文件
3. 跑一次 `opencode audit`
4. 在团队分享会上展示

**一个月**：
- TOP 3 安全事件 → OpenSpec 规格
- 接入 CI，至少一条实现"不合规不能上线"
- 建立团队规格仓库

> **哪怕只有一个 Scenario 跑起来，都是一次职业能力的实质性升维。**

---

## Q&A / 附录资源

**随堂资料**：
- 📋 代码速查卡（Python 语法）
- 🕵️ 安全模式匹配表
- 📐 OpenSpec 格式速查卡
- 🗂️ 模拟项目仓库地址

**延伸阅读**：
- OpenSpec 官方文档
- Harness Engineering（Anthropic 博客）
- Ralph Loop 社区演进
- GIVEN/WHEN/THEN 在 BDD 中的应用

---

**谢谢！欢迎随时交流 🛡️**

> **Harness 定义"什么是对的"，Ralph Loop 确保"对的一定被验证"。**
> **安全工程师的未来，不是做更多的检查，而是定义让系统自动遵守的边界。**

---
