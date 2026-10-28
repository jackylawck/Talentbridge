"""
Project: TalentBridge SH-HK (滬港賢智匯) - HR AI Governance Engine
Framework Alignment: HK PDPO, Mainland China PIPL, ISO/IEC 42001
Author: 羅子淇 (Jacky Law)
"""

import re
import json

class HRDataDeidentifier:
    """落實 PIPL/PDPO 數據最小化原則 (Data Minimization)"""
    def __init__(self):
        # 企業級中港敏感個資正則表達式
        self.patterns = {
            "HKID": re.compile(r'[A-Z]{1,2}\d{6}\([\dA]\)', re.IGNORECASE),
            "CN_ID": re.compile(r'\b\d{18}|\d{15}|\d{17}[X_x]\b'),
            "EMAIL": re.compile(r'[\w\.-]+@[\w\.-]+\.\w+'),
            "PHONE": re.compile(r'\b(?:[23456789]\d{7}|1[3-9]\d{9})\b')
        }

    def mask_pii(self, text: str) -> str:
        text = self.patterns["HKID"].sub("[MASKED_HKID]", text)
        text = self.patterns["CN_ID"].sub("[MASKED_CN_ID]", text)
        text = self.patterns["EMAIL"].sub("[MASKED_EMAIL]", text)
        text = self.patterns["PHONE"].sub("[MASKED_PHONE]", text)
        return text

class AIRiskScorer:
    """AI 合規影響評估與風險計分 (AI Impact Assessment)"""
    def evaluate_hr_system(self, ad_enabled: bool, cross_border: bool, sensitive_data: bool) -> dict:
        score = 0
        mitigations = []

        if ad_enabled:
            score += 40
            mitigations.append("強制實施 Human-in-the-Loop (HITL) 避免演算法招聘歧視。")
        if cross_border:
            score += 30
            mitigations.append("執行 PIPL 跨境傳輸標準合同與 PDPO 第33條合規審查。")
        if sensitive_data:
            score += 30
            mitigations.append("部署 K-匿名化 (K-Anonymity) 處理底層數據庫。")

        tier = "HIGH RISK (需董事會簽批)" if score >= 70 else "MEDIUM RISK" if score >= 40 else "LOW RISK"
        
        return {
            "risk_score": score,
            "risk_tier": tier,
            "governance_actions": mitigations
        }

if __name__ == "__main__":
    print("=== 滬港賢智匯 AI 治理引擎啟動 ===")
    
    # 模擬 1: CV 去識別化
    scrubber = HRDataDeidentifier()
    raw_cv = "Jacky Law, HKID: A123456(7), Email: jacky@example.com, Tel: 13912345678"
    print(f"\n[數據脫敏結果]: {scrubber.mask_pii(raw_cv)}")
    
    # 模擬 2: 董事會風險計分
    scorer = AIRiskScorer()
    assessment = scorer.evaluate_hr_system(ad_enabled=True, cross_border=True, sensitive_data=True)
    print(f"\n[AI 風險評級]: {assessment['risk_tier']} (分數: {assessment['risk_score']})")
    print(f"[要求採取之管治行動]: {json.dumps(assessment['governance_actions'], ensure_ascii=False, indent=2)}")
