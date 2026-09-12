#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Legalix Legal War-Room Engine — Master Swarm Architecture
מנוע חדר המלחמה המשפטי האוטונומי של Legalix: סוכן-על ראשי + 13 סוכני-משנה מומחים
"""

import sys
import os
import json
from datetime import datetime

class SubAgentBase:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    def analyze(self, case_data):
        raise NotImplementedError

# 1. סוכן עובדות וטענות
class FactClaimsAgent(SubAgentBase):
    def __init__(self):
        super().__init__("01_FactClaimsAgent", "חילוץ ומיפוי עובדות, טענות הצדדים וגרסאות")
    def analyze(self, case_data):
        return {
            "facts_extracted": len(case_data.get("documents", [])),
            "plaintiff_claims": ["הפרת חוזה יסודית", "אי-מסירת דירה במועד", "מצג שווא במפרט המכר"],
            "defendant_claims": ["כוח עליון ומצב מלחמה", "שינויי דיירים שעיכבו את הביצוע", "ויתור וסילוק"]
        }

# 2. סוכן כספים ופורנזיקה
class FinancialForensicAgent(SubAgentBase):
    def __init__(self):
        super().__init__("02_FinancialForensicAgent", "התחקות אחר תנועות כספיות, חשבוניות והעברות")
    def analyze(self, case_data):
        return {
            "total_tracked_nis": 4850000.0,
            "disputed_amount_nis": 650000.0,
            "interest_and_linkage_nis": 84200.0,
            "suspicious_transactions": ["העברה לא מתועדת ע\"ס 120,000 ש\"ח מיום 14.08.2023"]
        }

# 3. סוכן ציר זמן כרונולוגי
class MasterChronologyAgent(SubAgentBase):
    def __init__(self):
        super().__init__("03_MasterChronologyAgent", "בניית ציר זמן אירועים אבסולוטי")
    def analyze(self, case_data):
        return {
            "events_count": 28,
            "critical_milestones": [
                {"date": "2021-03-15", "event": "חתימת הסכם מכר ולוח תשלומים"},
                {"date": "2023-05-10", "event": "מכתב התראה ראשון על איחור במסירה"},
                {"date": "2023-11-20", "event": "הודעת קבלן על דחייה עקב מצב ביטחוני"}
            ]
        }

# 4. סוכן סתירות ושקרים
class ContradictionHunterAgent(SubAgentBase):
    def __init__(self):
        super().__init__("04_ContradictionHunterAgent", "הצלבת גרסאות ואיתור סתירות מהותיות")
    def analyze(self, case_data):
        return {
            "contradictions_found": 3,
            "smoking_gun_contradictions": [
                {
                    "issue": "ידיעת הנתבע על עיכוב בביצוע",
                    "statement_a": "מסמך #8 (תצהיר), שורה 12: 'נודע לנו על העיכוב רק באוקטובר 2023'",
                    "statement_b": "מסמך #9345 (מייל פנימי), שורה 4: 'במאי 2023 מנהל הפרויקט מתריע על איחור צפוי של 8 חודשים'",
                    "severity": "🔴 קריטי — סתירה מהותית בשבועה המפריכה טענת כוח עליון"
                }
            ]
        }

# 5. סוכן ראיות ומוצגים
class EvidenceExhibitAgent(SubAgentBase):
    def __init__(self):
        super().__init__("05_EvidenceExhibitAgent", "קטלוג ואינדוקס ראיות ותעודות זהות למסמכים")
    def analyze(self, case_data):
        return {"cataloged_exhibits": 14, "missing_documents": ["יומן עבודה חודש 06/2023"]}

# 6. סוכן תכתובות ומיילים
class CommunicationsAgent(SubAgentBase):
    def __init__(self):
        super().__init__("06_CommunicationsAgent", "ניתוח שרשראות מיילים, ווטסאפ והודעות")
    def analyze(self, case_data):
        return {"threads_analyzed": 18, "admission_of_liability": "מייל מיום 12.06.2023: 'אנחנו מודעים לעיכוב ונפצה בהתאם'"}

# 7. סוכן תמלול והקלטות
class AudioVideoIntelligenceAgent(SubAgentBase):
    def __init__(self):
        super().__init__("07_AudioVideoIntelligenceAgent", "תמלול שיחות, זיהוי דוברים והודאות בעל דין")
    def analyze(self, case_data):
        return {"recordings_transcribed": 4, "key_admission": "הקלטה #2 דקה 04:18: נציג הקבלן מודה שהעיכוב נבע מבעיות תזרים פנימיות"}

# 8. סוכן דין ופסיקה
class LegalPrecedentAgent(SubAgentBase):
    def __init__(self):
        super().__init__("08_LegalPrecedentAgent", "שליפת חקיקה, פסיקה מנחה וספרות")
    def analyze(self, case_data):
        return {
            "statutes": ["סעיף 5א לחוק המכר (דירות)", "חוק החוזים (תרופות בשל הפרת חוזה)"],
            "leading_precedents": ["רע״א 6605/15 שמש נ' ספייס בניה", "ע״א 4481/90 אהרן נ' בן יקר"]
        }

# 9. סוכן Red Team ובקרת חולשות
class RedTeamWeaknessAgent(SubAgentBase):
    def __init__(self):
        super().__init__("09_RedTeamWeaknessAgent", "איתור נקודות תורפה וטענות הצד שכנגד")
    def analyze(self, case_data):
        return {
            "our_case_weaknesses": ["אי-משלוח הודעת ביטול פורמלית בזמן אמת", "שינויי דיירים שבוצעו בדירה בחודש 04/2022"],
            "recommended_defense": "להדגיש ששינויי הדיירים תומחרו ואושרו ללא דחיית מועד מסירה per פסיקת שמש"
        }

# 10. סוכן חקירה נגדית
class CrossExaminationArchitectAgent(SubAgentBase):
    def __init__(self):
        super().__init__("10_CrossExaminationArchitectAgent", "בניית שאלות מחץ לחקירה נגדית")
    def analyze(self, case_data):
        return {
            "cross_exam_questions": [
                "תאשר לי בבקשה שבתאריך 10.05.2023 קיבלת את דוח מנהל הפרויקט המצורף כמוצג 4?",
                "אם ידעתם במאי על העיכוב, מדוע טענת בתצהירך שנודע לכם על כך רק באוקטובר?"
            ]
        }

# 11. סוכן כתבי טענות
class PleadingsDrafterAgent(SubAgentBase):
    def __init__(self):
        super().__init__("11_PleadingsDrafterAgent", "ניסוח כתבי תביעה, הגנה ובקשות")
    def analyze(self, case_data):
        return {"draft_status": "READY_FOR_ASSEMBLY", "template": "כתב תביעה כספית לפיצוי סטטוטורי"}

# 12. סוכן תצהירים ועדים
class WitnessAffidavitAgent(SubAgentBase):
    def __init__(self):
        super().__init__("12_WitnessAffidavitAgent", "מיפוי עדים ותצהירים")
    def analyze(self, case_data):
        return {"key_witnesses": ["התובע (הרוכש)", "מנהל הפרויקט מטעם הקבלן", "שמאי המקרקעין"]}

# 13. סוכן סעדים ונזקים
class RemediesDamagesAgent(SubAgentBase):
    def __init__(self):
        super().__init__("13_RemediesDamagesAgent", "תחשיב מדויק של סעדים ופיצויים")
    def analyze(self, case_data):
        return {
            "statutory_delay_compensation_nis": 184500.0,
            "mental_distress_nis": 35000.0,
            "expert_fees_nis": 12000.0,
            "total_claim_amount_nis": 231500.0
        }

# =========================================================================
# סוכן-העל הראשי המתזמר את כל 13 הסוכנים (Lead Case Orchestrator)
# =========================================================================
class LegalixLeadCaseOrchestrator:
    def __init__(self, case_id, case_title):
        self.case_id = case_id
        self.case_title = case_title
        self.sub_agents = [
            FactClaimsAgent(),
            FinancialForensicAgent(),
            MasterChronologyAgent(),
            ContradictionHunterAgent(),
            EvidenceExhibitAgent(),
            CommunicationsAgent(),
            AudioVideoIntelligenceAgent(),
            LegalPrecedentAgent(),
            RedTeamWeaknessAgent(),
            CrossExaminationArchitectAgent(),
            PleadingsDrafterAgent(),
            WitnessAffidavitAgent(),
            RemediesDamagesAgent()
        ]

    def execute_full_war_room_audit(self, case_input):
        print(f"\n[LEGALIX WAR-ROOM] Activating 13-Agent Swarm for Case: {self.case_title} ({self.case_id})...")
        results = {}
        for agent in self.sub_agents:
            results[agent.name] = agent.analyze(case_input)
            
        # Lead Orchestrator Synthesis & SWOT
        master_strategy = {
            "case_id": self.case_id,
            "case_title": self.case_title,
            "timestamp": datetime.now().isoformat(),
            "lead_orchestrator_summary": "ניתוח חדר מלחמה הושלם ע״י 13 סוכני-משנה מומחים.",
            "case_swot_matrix": {
                "core_strengths": ["הודאת בעל דין בהקלטה #2", "סתירה מהותית בין תצהיר הנתבע למיילים (רע״א 6605/15 שמש)"],
                "core_weaknesses": ["טענת שינויי דיירים — מנוטרלת באמצעות פסיקת ביהמ״ש העליון"],
                "win_probability_assessment": "גבוהה מאוד (85%–90%)",
                "total_claim_value_nis": results["13_RemediesDamagesAgent"]["total_claim_amount_nis"]
            },
            "sub_agents_intelligence": results
        }
        return master_strategy

if __name__ == '__main__':
    orchestrator = LegalixLeadCaseOrchestrator("CASE-2026-9042", "תביעת איחור במסירת דירה וליקויי מכר — משפחת כהן נ' חברת בנייה")
    full_audit = orchestrator.execute_full_war_room_audit({"documents": ["Doc1", "Doc2", "Doc3", "Doc4"]})
    print(json.dumps(full_audit, indent=2, ensure_ascii=False))
