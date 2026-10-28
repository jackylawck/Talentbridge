# 🏛️ 系統架構設計 (System Architecture)
## TalentBridge SH-HK: 三層可信 AI 數據生態圈

為了在跨國 (滬港) 數據流動中徹底消除 PII 洩露風險，本系統採用「零信任」的物理與邏輯隔離架構。

### Layer 1: 底層數據脫敏網關 (Data Minimization Gateway)
- **機制**: 部署於 HR 系統與 AI 模型之間的 Proxy 網關。
- **功能**: 強制攔截並利用 Regex 引擎進行實時去識別化 (De-identification)。
- **合規**: 確保送入大語言模型 (LLM) 的 Prompt 中，絕不包含 HKID、內地居民身份證或聯絡方式 (對齊 PIPL 第六條)。

### Layer 2: 中介行業基準層 (Industry Benchmark & RAG)
- **機制**: 檢索增強生成 (Retrieval-Augmented Generation)。
- **功能**: AI 模型僅基於脫敏後的「純技能特徵 (Skills & Competencies)」與權威行業智庫進行匹配，杜絕基於人口統計特徵的演算法偏見。

### Layer 3: 頂層隱私保護分析 (Privacy-Preserving Analytics)
- **機制**: K-匿名化 (k-Anonymity) 與差分隱私 (Differential Privacy)。
- **功能**: 輸出董事會級別的 HR 戰略熱力圖與風險評級 (AIIA)，在不暴露單一個體的前提下，提供高階決策支持 (對齊 ISO/IEC 42001)。
