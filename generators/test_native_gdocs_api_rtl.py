import json, os, requests
from test_gdocs_api import get_google_services

docs_s, drive_s = get_google_services()

# Let's test creating a genuine Google Doc via Docs API and setting paragraphStyle.direction = RIGHT_TO_LEFT
doc = docs_s.documents().create(body={'title': '⚡ בדיקת כיווניות RTL אמיתית — Google Docs API'}).execute()
doc_id = doc.get('documentId')
print(f"Created Doc with ID: {doc_id}")

# Public permission
drive_s.permissions().create(fileId=doc_id, body={'type': 'anyone', 'role': 'reader'}).execute()

# Insert text
text_to_insert = (
    "דוח הנחיות תיקון וסגירת ממצאים למתכנן החשמל\n"
    "פרויקט: לוד ניר צבי — עמרם אברהם\n"
    "תאריך: ספטמבר 2026 | מהדורה: סבב 01 לקראת Rev 02\n\n"
    "1. תקציר מנהלים\n"
    "דוח זה נבנה ככלי עבודה מעשי עבור מתכנן החשמל לסגירת כל 22 הממצאים שאותרו במודל.\n"
    "• אזור 1: מה נמצא במודל — מיקום, אלמנט ופער נמדד.\n"
    "• אזור 2: מה לעשות עכשיו — הפעולה המומלצת המועדפת ומה לעדכן ב-Rev 02.\n"
    "• אזור 3: איך נסגור את הממצא — קריטריון סגירה אוטומטי.\n\n"
    "ELEC-FP-001 | הזנת כוח למשאבות כיבוי אש — איסור מוחלט על ממסר פחת (RCD)\n"
    "סטטוס: 🔴 RED – נדרש תיקון | עדיפות: P1 | זמן משוער: 10–15 דקות\n"
    "הממצא: במעגל ההזנה למשאבת כיבוי האש סומן מפסק מגן מזרם דלף (פחת RCD 300mA).\n"
    "הפעולה המומלצת: ביטול ממסר הפחת והגדרת מפסק בעל הגנה מגנטית בלבד עם נעילת Padlock במצב ON.\n"
    "מה בדיוק לעדכן ב-Rev 02: למחוק את סימון ה-RCD ממעגל משאבת הכיבוי בלוח החירום.\n"
    "קריטריון סגירה אוטומטי: ביטול ממסר הפחת והגדרת הגנה מגנטית בלבד במעגל משאבת הכיבוי.\n"
)

# Insert text request
req_insert = {
    'insertText': {
        'location': {'index': 1},
        'text': text_to_insert
    }
}
docs_s.documents().batchUpdate(documentId=doc_id, body={'requests': [req_insert]}).execute()

# Now fetch the updated document length
doc_updated = docs_s.documents().get(documentId=doc_id).execute()
end_idx = doc_updated['body']['content'][-1]['endIndex'] - 1

# Force RIGHT_TO_LEFT direction and START (Right in RTL) alignment on the WHOLE document!
req_rtl = {
    'updateParagraphStyle': {
        'range': {
            'startIndex': 1,
            'endIndex': end_idx
        },
        'paragraphStyle': {
            'direction': 'RIGHT_TO_LEFT',
            'alignment': 'START',
            'spaceAbove': {'magnitude': 4, 'unit': 'PT'},
            'spaceBelow': {'magnitude': 4, 'unit': 'PT'}
        },
        'fields': 'direction,alignment,spaceAbove,spaceBelow'
    }
}

docs_s.documents().batchUpdate(documentId=doc_id, body={'requests': [req_rtl]}).execute()

link = f"https://docs.google.com/document/d/{doc_id}/edit?usp=sharing"
print(f"\nSUCCESS! 100% Native Right-to-Left Google Doc created via API:")
print(link)
