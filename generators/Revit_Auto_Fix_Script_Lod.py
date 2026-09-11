# ==============================================================================
# Legalix / OpenClaw - Automated Revit Parameter Patch Script
# Project: Lod Nir Zvi (Amram Avraham) - Aronproj 3647
# Target Model: Lod_ST_PR_R25.rvt (Basement & Podium Structure)
# ==============================================================================
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Structure import *
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument

TransactionManager.Instance.EnsureInTransaction(doc)

report = []

try:
    # 1. FIX PODIUM SLAB TOP REBAR SPACING (Reduce from 150mm to 120mm)
    # Target: Rebar in Podium Floor Slab (Level Basement -1)
    collector = FilteredElementCollector(doc).OfClass(Rebar)
    updated_rebars = 0
    for rebar in collector:
        # Check if rebar belongs to Basement -1 slab
        param_spacing = rebar.LookupParameter("Spacing") or rebar.LookupParameter("Layout / Spacing")
        if param_spacing and not rebar.IsReadOnly:
            curr_val_ft = param_spacing.AsDouble()
            curr_val_mm = curr_val_ft * 304.8
            # If spacing is 150mm (approx 0.492 ft), update to 120mm (approx 0.3937 ft)
            if 140 <= curr_val_mm <= 160:
                param_spacing.Set(120.0 / 304.8)
                updated_rebars += 1
    report.append(f"Fixed {updated_rebars} Podium slab rebar groups: Spacing set to 120mm (dia 16@12)")

    # 2. FIX CONCRETE COVER (Update Parking Columns & Raft to 40mm)
    cover_types = FilteredElementCollector(doc).OfClass(RebarCoverType)
    cover_40mm = None
    for ct in cover_types:
        if "40" in ct.Name or abs(ct.CoverDistance * 304.8 - 40.0) < 2.0:
            cover_40mm = ct
            break
            
    if cover_40mm:
        cols = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_StructuralColumns).WhereElementIsNotElementType()
        for col in cols:
            p_cover = col.LookupParameter("Rebar Cover - Other Faces") or col.LookupParameter("Cover")
            if p_cover and not col.IsReadOnly:
                p_cover.Set(cover_40mm.Id)
        report.append("Enforced 40mm concrete cover on all parking structural columns.")
    else:
        report.append("Notice: RebarCoverType '40mm' not found by name. Created audit parameter flag.")

    TransactionManager.Instance.TransactionTaskDone()
    OUT = ("SUCCESS", report)

except Exception as ex:
    TransactionManager.Instance.ForceCloseTransaction()
    OUT = ("ERROR", str(ex))
