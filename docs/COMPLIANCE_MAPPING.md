# ⚖️ 法規與標準映射表 (Compliance Mapping)

本專案《滬港賢智匯》治理引擎嚴格對標以下三大國際與區域合規框架：

| 模組名稱 | 映射法規 / 標準 | 具體條款與控制項 | 落實機制 |
| :--- | :--- | :--- | :--- |
| **Inbound PII Scrubber** | **PDPO (HK)** | 保障資料第1原則 (收集目的及方式) | 在數據進入 AI 模型前，強制正則攔截並抹除身份證、電話等直接識別碼。 |
| **Inbound PII Scrubber** | **PIPL (Mainland)** | 第六條 (數據最小化原則) | 確保僅處理與跨境 HR 匹配直接相關之非敏感特徵。 |
| **Risk Scorer** | **ISO/IEC 42001** | Annex A.5 (AI 系統風險評估) | 動態計算自動化決策 (ADM) 與跨境流動權重，自動輸出風險等級。 |
| **Governance Engine** | **ISO/IEC 27701** | Clause 6.2 (隱私設計) | 將合規邏輯直接硬編碼 (Hardcoded) 於數據流水線中，實現 Governance-as-Code。 |
