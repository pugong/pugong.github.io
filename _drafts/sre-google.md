# SRE - Google运维揭秘

## 方法论

+ 长期关注研发工作
+ 保障SLO的前提下最大化迭代数据
+ 监控系统
    - 报警 Alert
    - 工单 Ticket
    - 日志 Logging
+ 应急事件处理：关注MTTR
+ 变更管理
+ 需求预测和容量规划
+ 资源部署
+ 效率和性能


## 拥抱风险

管理服务的可靠性 = 管理风险  【引申：dalio？ 配置风险而不是配置资产】

### 度量风险

可用性 = 系统正常运行时间 / （系统正常运行时间+停机时间）

改进度量

可用性 = 成功请求数 / 总的请求数

+ 确定合理的可用性目标
+ 识别故障类型
+ 可用性 vs 成本

故障预算（Error Budgets）

预算不足的时候发布会被要求收紧

## 关键词

+ MTTR
+ SDN，OpenFlow
+ gRPC

| foo | bar |
|---|---|
| a   |    b |

Allowed unavailability window 

| Availability level | per year |  per quarter | per month  | per week | per day |per hour |
| ------ | ------ |  ------ | ------ | ------ | ------ | ------ |
| 90% | 36.5 days | 9 days | 3 days | 16.8 hours | 2.4 hours | 6 minutes |
| 95% | 18.25 days | 4.5 days | 1.5 days | 8.4 hours | 1.2 hours | 3 minutes |
| 99% | 3.65 days | 21.6 hours | 7.2 hours | 1.68 hours | 14.4 minutes | 36 seconds |
| 99.5% | 1.83 days | 10.8 hours | 3.6 hours | 50.4 minutes | 7.20 minutes | 18 seconds |
| 99.9% | 8.76 hours | 2.16 hours | 43.2 minutes | 10.1 minutes | 1.44 minutes | 3.6 seconds |
| 99.95% | 4.38 hours | 1.08 hours | 21.6 minutes | 5.04 minutes | 43.2 seconds | 1.8 seconds |
| 99.99% | 52.6 minutes | 12.96 minutes | 4.32 minutes | 60.5 seconds | 8.64 seconds | 0.36 seconds |
| 99.999% | 5.26 minutes | 1.30 minutes | 25.9 seconds | 6.05 seconds | 0.87 seconds | 0.04 seconds |