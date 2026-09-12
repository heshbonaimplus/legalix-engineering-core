#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Legalix Dynamic Project & Matter Dispatcher (Smart Trigger Engine)
מנוע זיהוי טריגרים חכם: מפענח שמות יזמים, ערים, מספרי מגדלים, מזהי גוש-חלקה ומילות מפתח
"""

import re
import json

class LegalixProjectMatcher:
    def __init__(self):
        self.project_registry = {
            "lod_nir_zvi": {
                "canonical_name": "פרויקט לוד ניר צבי — עמרם אברהם",
                "triggers": [
                    "לוד", "ניר צבי", "ניר-צבי", "עמרם אברהם", "עמרם", "321", "339", "223",
                    "lod", "nir zvi", "nir-zvi", "amram", "tower 321", "tower 339",
                    "מגדל 321", "מגדל 339", "מבנה 223", "פודיום", "חניון לוד"
                ],
                "disciplines_count": 6,
                "total_findings": 146,
                "hold_point": True,
                "word_url": "https://drive.google.com/file/d/1adze8TVSSkGVRaTpBN4DBH-wW1iIjTkA/view?usp=sharing",
                "pdf_url": "https://drive.google.com/file/d/1cGDg9dLzV8nt1w2F-GVOLuQqKhxR9p-A/view?usp=sharing",
                "grand_master_url": "https://drive.google.com/file/d/1xJnOnKtKkPJPJ0b27aO5bf6hWA145paN/view?usp=sharing"
            },
            "or_yehuda_master": {
                "canonical_name": "פרויקט מגדלי אור יהודה",
                "triggers": ["אור יהודה", "אונו", "בקעת אונו", "or yehuda", "oryehuda", "17 קומות", "50 קומות"],
                "disciplines_count": 6,
                "total_findings": 38,
                "hold_point": True,
                "word_url": "https://drive.google.com/file/d/1adze8TVSSkGVRaTpBN4DBH-wW1iIjTkA/view?usp=sharing",
                "pdf_url": "https://drive.google.com/file/d/1cGDg9dLzV8nt1w2F-GVOLuQqKhxR9p-A/view?usp=sharing",
                "grand_master_url": "https://drive.google.com/file/d/1xJnOnKtKkPJPJ0b27aO5bf6hWA145paN/view?usp=sharing"
            }
        }

    def match_project(self, query_text):
        q = (query_text or "").lower().strip()
        if not q:
            return self.project_registry["lod_nir_zvi"]
            
        for p_key, p_data in self.project_registry.items():
            for trig in p_data["triggers"]:
                if trig.lower() in q:
                    return p_data
                    
        # Default to canonical primary project if no explicit keyword
        return self.project_registry["lod_nir_zvi"]

if __name__ == '__main__':
    matcher = LegalixProjectMatcher()
    for test_q in ["ניר צבי", "עמרם אברהם", "מגדל 321", "לוד", "שלד", "אור יהודה"]:
        matched = matcher.match_project(test_q)
        print(f"Query: '{test_q}' ➔ Matched Project: {matched['canonical_name']}")
