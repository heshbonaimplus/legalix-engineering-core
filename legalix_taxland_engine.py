#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Legalix TaxLand Master Calculation & Planning Engine (Production V1.0)
מנוע תכנון מס מקרקעין, מס שבח, מס רכישה, סעיף 49ז ודירת מגורים מזכה
"""

import sys
import os
import json
import math
from datetime import datetime

class LegalixTaxLandEngine:
    def __init__(self):
        self.transition_date = datetime(2014, 1, 1) # יום המעבר לחישוב ליניארי מוטב
        self.purchase_tax_brackets_single_residence_2026 = [
            (2000000, 0.0),      # עד 2,000,000 ש"ח - 0%
            (2370000, 0.035),    # מ-2,000,000 עד 2,370,000 - 3.5%
            (6100000, 0.05),     # מ-2,370,000 עד 6,100,000 - 5.0%
            (20300000, 0.08),    # מ-6,100,000 עד 20,300,000 - 8.0%
            (float('inf'), 0.10) # מעל 20,300,000 - 10.0%
        ]
        self.purchase_tax_brackets_additional_residence_2026 = [
            (6100000, 0.08),     # עד 6,100,000 - 8.0%
            (float('inf'), 0.10) # מעל 6,100,000 - 10.0%
        ]

    def calculate_betterment_tax_linear(self, purchase_price, sale_price, purchase_date_str, sale_date_str, expenses=0, inflation_rate=0.0):
        """חישוב מס שבח ליניארי מוטב (סעיף 48א(ב2))"""
        p_date = datetime.strptime(purchase_date_str, "%Y-%m-%d")
        s_date = datetime.strptime(sale_date_str, "%Y-%m-%d")
        
        total_days = (s_date - p_date).days
        days_before_2014 = max(0, (self.transition_date - p_date).days)
        days_after_2014 = max(0, (s_date - self.transition_date).days)
        
        # שווי רכישה מתואם ורווח
        adjusted_purchase = purchase_price * (1.0 + inflation_rate) + expenses
        total_gain = max(0, sale_price - adjusted_purchase)
        
        if total_days <= 0:
            linear_gain_taxable = 0
            tax_rate_effective = 0
        elif p_date >= self.transition_date:
            # נרכשה אחרי 1.1.2014 - כל השבח חייב במס שבח ריאלי של 25%
            linear_gain_taxable = total_gain
            tax_rate_effective = 0.25
        else:
            # חישוב ליניארי מוטב - פטור על התקופה עד 1.1.2014
            taxable_fraction = days_after_2014 / total_days
            linear_gain_taxable = total_gain * taxable_fraction
            tax_rate_effective = 0.25 * taxable_fraction
            
        tax_amount = linear_gain_taxable * 0.25
        
        return {
            "total_gain": total_gain,
            "exempt_gain_pre_2014": total_gain - linear_gain_taxable,
            "taxable_gain_post_2014": linear_gain_taxable,
            "tax_amount": tax_amount,
            "effective_tax_rate": (tax_amount / total_gain * 100) if total_gain > 0 else 0.0
        }

    def calculate_section_49z(self, sale_price, value_without_building_rights, purchase_price, purchase_date_str, sale_date_str):
        """חישוב פיצול רעיוני לזכויות בנייה (סעיף 49ז)"""
        base_exempt_ceiling = 2400000 # תקרת כפל פטור בסיסית משוערת
        
        # שווי דירת מגורים ללא זכויות בנייה
        residence_value = min(sale_price, value_without_building_rights)
        building_rights_value = max(0, sale_price - residence_value)
        
        # תקרת הפטור per 49ז(א)(1) - כפל שווי דירה או תקרה
        exempt_residence_portion = min(residence_value * 2.0, base_exempt_ceiling, sale_price)
        taxable_rights_portion = max(0, sale_price - exempt_residence_portion)
        
        # חישוב מס על זכויות הבנייה (מס רגיל 25% ללא פטור ליניארי מלא)
        gain_rights = taxable_rights_portion * 0.70 # אומדן רווח יחסי
        tax_rights = gain_rights * 0.25
        
        return {
            "total_sale_price": sale_price,
            "exempt_residence_value": exempt_residence_portion,
            "taxable_building_rights_value": taxable_rights_portion,
            "estimated_tax_on_rights": tax_rights,
            "status": "פיצול רעיוני בוצע בהתאם לסעיף 49ז"
        }

    def calculate_purchase_tax(self, price, is_single_residence=True):
        """חישוב מס רכישה מדורג"""
        brackets = self.purchase_tax_brackets_single_residence_2026 if is_single_residence else self.purchase_tax_brackets_additional_residence_2026
        tax = 0.0
        prev_limit = 0.0
        
        for limit, rate in brackets:
            if price > prev_limit:
                taxable_in_bracket = min(price, limit) - prev_limit
                tax += taxable_in_bracket * rate
                prev_limit = limit
            else:
                break
                
        return {
            "price": price,
            "is_single_residence": is_single_residence,
            "purchase_tax_amount": tax,
            "effective_tax_rate": (tax / price * 100) if price > 0 else 0.0
        }

if __name__ == '__main__':
    engine = LegalixTaxLandEngine()
    print("Testing Linear Tax Calculation:")
    res = engine.calculate_betterment_tax_linear(
        purchase_price=800000, sale_price=3500000,
        purchase_date_str="2000-01-01", sale_date_str="2026-06-01", expenses=150000
    )
    print(json.dumps(res, indent=2, ensure_ascii=False))
