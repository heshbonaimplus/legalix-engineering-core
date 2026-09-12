#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Legalix TaxLand Master Trigger & Knowledge Router (Dynamic Tax Dispatcher)
מנוע טריגרים חכם למיסוי מקרקעין, מס שבח, מס רכישה, היטל השבחה, פטורים וחוות דעת
"""

import re
import json

class LegalixTaxLandMatcher:
    def __init__(self):
        self.tax_triggers = {
            "linear_betterment": [
                "מס שבח", "שבח", "ליניארי", "ליניארי מוטב", "48א", "חישוב שבח", "שומה עצמית",
                "מכירת דירה", "דירת מגורים", "רווח הון מקרקעין", "ניכוי הוצאות", "סעיף 39",
                "פחת", "אינפלציה", "שבח ריאלי", "שבח אינפלציוני"
            ],
            "section_49z": [
                "49ז", "סעיף 49ז", "זכויות בנייה", "בנייה נוספת", "פיצול רעיוני",
                "כפל פטור", "תקרת 49ז", "בית פרטי עם זכויות", "מגרש עם בית"
            ],
            "purchase_tax": [
                "מס רכישה", "רכישה", "מדרגות מס רכישה", "דירה יחידה", "דירה נוספת",
                "רכישת מגרש", "מס רכישה 2026", "מס רכישה 2024", "מס רכישה 2025"
            ],
            "exemptions_and_inheritances": [
                "פטור", "פטור דירת מגורים", "49ב", "49ב(2)", "49ב(5)", "ירושה", "דירת ירושה",
                "העברה ללא תמורה", "מתנה", "עסקת קרובים", "הסכם חלוקת עיזבון", "צוואה"
            ],
            "betterment_levy_and_planning": [
                "היטל השבחה", "השבחה", "שומת השבחה", "שמאי מכריע", "תוספת שלישית",
                "תב״ע משביחה", "הקלה", "שימוש חורג", "פיצויים 197"
            ],
            "tax_opinion_and_planning": [
                "תכנון מס", "חוות דעת", "חוות דעת מיסויית", "מזכר מס", "בדיקת כדאיות מס",
                "אסטרטגיית מס", "חלופות מס", "פריסת מס שבח", "פריסה"
            ]
        }

    def match_tax_intent(self, query_text):
        q = (query_text or "").lower().strip()
        matched_categories = []
        
        for category, triggers in self.tax_triggers.items():
            for trig in triggers:
                if trig.lower() in q:
                    matched_categories.append(category)
                    break
                    
        if not matched_categories:
            matched_categories = ["linear_betterment", "tax_opinion_and_planning"]
            
        return {
            "matched_categories": matched_categories,
            "primary_category": matched_categories[0],
            "requires_full_opinion": any(c in matched_categories for c in ["tax_opinion_and_planning", "section_49z", "exemptions_and_inheritances"]),
            "authority_references": [
                "חוק מיסוי מקרקעין (שבח ורכישה) תשכ״ג-1963",
                "ספרי פרופ' אהרן נמדר (מס שבח, פטור דירת מגורים, היטל השבחה)",
                "פסיקת בית המשפט העליון ו-ועדות הערר לפיצויים והיטלי השבחה"
            ]
        }

if __name__ == '__main__':
    matcher = LegalixTaxLandMatcher()
    for test_q in [
        "אני רוצה תכנון מס למכירת בית פרטי עם זכויות בנייה נוספות",
        "כמה מס רכישה אני אשלם על דירה שניה ב-4 מיליון שח",
        "האם יש פטור על דירה שקיבלתי בירושה מאבא",
        "תכין לי חוות דעת מיסויית למכירת דירה עם חישוב ליניארי מוטב"
    ]:
        res = matcher.match_tax_intent(test_q)
        print(f"שאלה: '{test_q}' ➔ זיהוי קטגוריות: {res['matched_categories']} | חוות דעת: {res['requires_full_opinion']}")
