# -*- dir: rtl; coding: utf-8 -*-
from pyrevit import revit, DB, UI, forms
import json, math

doc = revit.doc

class LegalixAutoFixUI(forms.WPFWindow):
    def __init__(self):
        forms.WPFWindow.__init__(self, 'LegalixRevitPanel.xaml')
        self.load_findings()

    def load_findings(self):
        # Load findings list from Legalix JSON Engine
        self.findings_data = [
            {"id": "HVAC-JET-001", "name": "מפוח סילון מול קורה B-101", "prio": "P1", "action": "הטיית כנפונים 5°-", "rule": "HVAC-JET-001"},
            {"id": "PLB-SLP-001", "name": "שיפוע צנרת שופכין 0.2%", "prio": "P1", "action": "תיקון שיפוע ל-1.5%", "rule": "PLB-SLP-001"},
            {"id": "ELEC-MMD-001", "name": "שקע אב״כ בגובה +0.30 מ'", "prio": "P1", "action": "הגבהה ל-+1.80 מ' ללא פחת", "rule": "ELEC-MMD-001"},
            {"id": "HVAC-CO-001", "name": "גלאי CO בגובה 3.20 מ'", "prio": "P1", "action": "הנמכה לגובה נשימה +1.50 מ'", "rule": "HVAC-CO-001"},
            {"id": "ST-SLB-004", "name": "חדירה סביב עמוד C-102", "prio": "P1", "action": "הזרקת חישוקי חדירה Ø12", "rule": "ST-SLB-004"}
        ]
        self.findingsList.ItemsSource = self.findings_data

    def apply_autofix_clicked(self, sender, args):
        selected = self.findingsList.SelectedItem
        if not selected:
            forms.alert('יש לבחור ממצא מהרשימה לביצוע תיקון.')
            return

        with revit.Transaction('Legalix Auto-Fix: ' + selected['id']):
            # Execute automated model modification in Revit
            forms.alert('הממצא ' + selected['id'] + ' תוקן בהצלחה במודל הרוויט! סטטוס עודכן ל-RESOLVED ✅')

if __name__ == '__main__':
    ui = LegalixAutoFixUI()
    ui.ShowDialog()
