#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
taxland_openclaw_bridge.py
גשר פייתון עבור Legalix MCP Gateway — מפעיל את סוכן OpenClaw האוטונומי של TaxLand
"""

import sys
import json
import os

# Add paths to engine
sys.path.append("/opt/legalix")
sys.path.append("/home/yogi/lod_project")

try:
    from legalix_taxland_agent_runner import TaxLandAutonomousAgent
    from legalix_taxland_engine import LegalixTaxLandEngine
    from legalix_taxland_matcher import LegalixTaxLandMatcher
except ImportError:
    pass

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No command provided"}))
        return

    command = sys.argv[1]
    raw_payload = sys.argv[2] if len(sys.argv) > 2 else "{}"
    
    try:
        payload = json.loads(raw_payload)
    except Exception:
        payload = {}

    agent = TaxLandAutonomousAgent()
    engine = LegalixTaxLandEngine()

    if command == "autonomous_plan":
        res = agent.process_tax_matter(payload)
        print(json.dumps(res, ensure_ascii=False))

    elif command == "section_49z":
        sale_p = float(payload.get("sale_price", 0))
        val_no_rights = float(payload.get("value_without_rights", sale_p * 0.65))
        pur_p = float(payload.get("purchase_price", 0))
        pur_d = payload.get("purchase_date", "2005-01-01")
        sale_d = payload.get("sale_date", "2026-06-01")
        
        res = engine.calculate_section_49z(sale_p, val_no_rights, pur_p, pur_d, sale_d)
        print(json.dumps(res, ensure_ascii=False))

    elif command == "linear_betterment":
        sale_p = float(payload.get("sale_price", 0))
        pur_p = float(payload.get("purchase_price", 0))
        pur_d = payload.get("purchase_date", "2005-01-01")
        sale_d = payload.get("sale_date", "2026-06-01")
        exp = float(payload.get("expenses", 0))
        
        res = engine.calculate_betterment_tax_linear(pur_p, sale_p, pur_d, sale_d, exp)
        print(json.dumps(res, ensure_ascii=False))

    else:
        print(json.dumps({"error": f"Unknown command {command}"}))

if __name__ == "__main__":
    main()
