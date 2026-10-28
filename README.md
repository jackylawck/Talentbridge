# 🌐 TalentBridge SH-HK (滬港賢智匯) 
### Enterprise Cross-Border HR AI Governance Engine

[![Compliance: ISO/IEC 42001](https://img.shields.io/badge/Compliance-ISO%2FIEC%2042001-blue.svg)](./COMPLIANCE_AND_LEGAL_DISCLAIMER.md)
[![Framework: PDPO & PIPL](https://img.shields.io/badge/Framework-PDPO%20%7C%20PIPL-success.svg)](./COMPLIANCE_AND_LEGAL_DISCLAIMER.md)
[![Strategy: Governance-as-Code](https://img.shields.io/badge/Strategy-Governance--as--Code-purple.svg)]()

**[EN]** An enterprise-grade AI governance engine and Privacy-Enhancing Technology (PET) designed for cross-border HR talent acquisition. This repository open-sources the core compliance telemetry from the 2026 Shanghai-Hong Kong Open Data Challenge, bridging the gap between board-level regulatory mandates and technical enforcement.

**[CN]** 本儲存庫為 **2026年數據要素×滬港合作開放數據競賽** 專案《滬港賢智匯》之核心技術開源版本。專為跨國企業設計，旨在解決 AI 人才決策系統中的「數據隱私外洩」、「算法偏見黑箱」與「跨境數據流動」三大合規痛點。

---

## 🚀 核心特性 (Core Capabilities)

* 🛡️ **零信任數據最小化 (Zero-Trust Data Minimization)：** 內建中港兩地專屬 Regex 引擎，在數據送入外部 AI 模型前，強制且自動脫敏高風險 PII（包含香港身份證 HKID、內地居民身份證、中港聯絡方式）。
* 📊 **自動化風險遙測 (Automated Risk Telemetry)：** 基於 **ISO/IEC 42001** 標準，動態生成 AI 系統影響評估 (AIIA)，提供董事會級別 (Board-level) 的風險評級與強制管治建議 (如 Human-in-the-Loop)。
* ⚖️ **管治即代碼 (Governance-as-Code)：** 告別純紙本政策，將香港 **PDPO** 與內地 **PIPL** 的合規要求直接硬編碼 (Hardcoded) 為可執行的 Python 隱私防禦腳本。

---

## 🏗️ 快速啟動 (Quick Start)

只需標準 Python 3.8+ 環境，無需額外依賴包即可運行核心引擎：

```bash
# 啟動 AI 治理與數據脫敏引擎
python src/governance_engine.py

💡 預期終端機輸出 (Expected System Output)
=== 滬港賢智匯 AI 治理引擎啟動 ===

[數據脫敏結果]: Jacky Law, HKID: [MASKED_HKID], Email: [MASKED_EMAIL], Tel: [MASKED_PHONE]

[AI 風險評級]: HIGH RISK (需董事會簽批) (分數: 100)
[要求採取之管治行動]: [
  "強制實施 Human-in-the-Loop (HITL) 避免演算法招聘歧視。",
  "執行 PIPL 跨境傳輸標準合同與 PDPO 第33條合規審查。",
  "部署 K-匿名化 (K-Anonymity) 處理底層數據庫。"
]

📚 核心治理文檔 (Governance Documentation)
 * 🏛️ 系統架構與三層數據生態圈 (System Architecture)
 * ⚖️ 法規與標準映射表 (Compliance Mapping)
 * 🛡️ 法律、合規與 AI 治理聲明 (Legal & Compliance Disclaimer)


