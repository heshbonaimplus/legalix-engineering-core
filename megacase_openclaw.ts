/**
 * src/skills/megacase_openclaw.ts
 *
 * חשיפת מערכת Legalix Mega-Case ו-13 סוכני חדר המלחמה ב-MCP Gateway עבור קלוד.
 */

import { spawn } from "node:child_process";
import path from "node:path";
import { fileURLToPath } from "node:url";
import type { ToolDefinition, ToolResult } from "../tools.js";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const BRIDGE = path.resolve(HERE, "megacase_openclaw_bridge.py");
const PYTHON = process.env.PYTHON_BIN ?? "python3";
const TIMEOUT_MS = 60_000;

function runBridge(command: string, payload: Record<string, unknown>): Promise<ToolResult> {
  return new Promise((resolve) => {
    const child = spawn(PYTHON, [BRIDGE, command, JSON.stringify(payload)]);
    let stdout = "";
    let stderr = "";

    const timer = setTimeout(() => {
      child.kill();
      resolve({
        content: [{ type: "text", text: JSON.stringify({ error: "MegaCase OpenClaw Bridge timeout" }) }],
        isError: true,
      });
    }, TIMEOUT_MS);

    child.stdout.on("data", (chunk) => { stdout += chunk.toString(); });
    child.stderr.on("data", (chunk) => { stderr += chunk.toString(); });

    child.on("close", (code) => {
      clearTimeout(timer);
      if (code !== 0) {
        resolve({
          content: [{ type: "text", text: JSON.stringify({ error: stderr || `Process exited with code ${code}` }) }],
          isError: true,
        });
      } else {
        resolve({
          content: [{ type: "text", text: stdout.trim() }],
        });
      }
    });
  });
}

export const tools: ToolDefinition[] = [
  {
    name: "legalix_mega_case_orchestrator",
    description: "הפעלת חדר המלחמה המשפטי של Legalix Mega-Case: ניתוח עומק אוטונומי של התיק, חילוץ סתירות כירורגיות, ציר זמן כרונולוגי, שומות נזקים והפקת אסטרטגיה מנצחת ע״י 13 סוכני-משנה מומחים.",
    inputSchema: {
      type: "object",
      properties: {
        case_id: { type: "string", description: "מזהה התיק (למשל: CASE-POLINER-62449-03-24)" },
        case_title: { type: "string", description: "שם התיק ובית המשפט" },
        task: { type: "string", description: "המשימה המבוקשת (ניתוח מלא / איתור סתירות / חקירה נגדית)" }
      },
      required: ["case_id"]
    },
    handler: (args) => runBridge("investigate", args as Record<string, unknown>),
  },
  {
    name: "legalix_mega_case_query_13_agents",
    description: "תשאול ישיר וממוקד של 13 מחסני הסוכנים בדרייב: עובדות, כספים, ציר זמן, סתירות, ראיות, שומות דמי שימוש וחקירה נגדית.",
    inputSchema: {
      type: "object",
      properties: {
        case_id: { type: "string", description: "מזהה התיק" },
        query: { type: "string", description: "שאלת החקירה או הנושא המבוקש" },
        target_agent: { type: "string", description: "מספר הסוכן או תחום (למשל: 04_contradictions, 02_financial)" }
      },
      required: ["case_id", "query"]
    },
    handler: (args) => runBridge("query_13_agents", args as Record<string, unknown>),
  },
  {
    name: "legalix_mega_case_batch_ingest",
    description: "קליטת תיק ענק מולטי-מודלי מ-Google Drive / Dropbox, הרצת Vision OCR מקבילי ברמת אות-אחר-אות וניתוב ל-13 המחסנים.",
    inputSchema: {
      type: "object",
      properties: {
        case_id: { type: "string", description: "מזהה התיק" },
        drive_folder_url: { type: "string", description: "קישור לתיקיית החומרים בדרייב" }
      },
      required: ["case_id", "drive_folder_url"]
    },
    handler: (args) => runBridge("ingest_batch", args as Record<string, unknown>),
  }
];
