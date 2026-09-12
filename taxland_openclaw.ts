/**
 * src/skills/taxland_openclaw.ts
 *
 * חשיפת סוכן OpenClaw האוטונומי של TaxLand ב-MCP Gateway עבור קלוד.
 */

import { spawn } from "node:child_process";
import path from "node:path";
import { fileURLToPath } from "node:url";
import type { ToolDefinition, ToolResult } from "../tools.js";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const BRIDGE = path.resolve(HERE, "taxland_openclaw_bridge.py");
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
        content: [{ type: "text", text: JSON.stringify({ error: "TaxLand OpenClaw Bridge timeout" }) }],
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
    name: "legalix_taxland_autonomous_agent",
    description: "הפעלת סוכן OpenClaw האוטונומי של TaxLand: ניתוח עסקת נדל״ן, הפקת 3 חלופות מס (ליניארי מוטב 48א, פיצול 49ז, פריסת מס 48א(ה)), בקרת חשיפות Red Team, ושליפת פסיקת נמדר.",
    inputSchema: {
      type: "object",
      properties: {
        query: { type: "string", description: "תיאור העסקה או שאלת הלקוח" },
        sale_price: { type: "number", description: "שווי המכירה בש״ח" },
        purchase_price: { type: "number", description: "שווי הרכישה ההיסטורי בש״ח" },
        purchase_date: { type: "string", description: "יום הרכישה (YYYY-MM-DD)" },
        sale_date: { type: "string", description: "יום המכירה (YYYY-MM-DD)" },
        expenses: { type: "number", description: "סך הוצאות מוכרות לפי סעיף 39 בש״ח" }
      },
      required: ["sale_price", "purchase_price"]
    },
    handler: (args) => runBridge("autonomous_plan", args as Record<string, unknown>),
  },
  {
    name: "legalix_taxland_section_49z_calculator",
    description: "חישוב מדויק של פיצול רעיוני לזכויות בנייה נוספות לפי סעיף 49ז לחוק מיסוי מקרקעין.",
    inputSchema: {
      type: "object",
      properties: {
        sale_price: { type: "number", description: "סך שווי המכירה הכולל" },
        value_without_rights: { type: "number", description: "שווי הדירה ללא זכויות בנייה נוספות" },
        purchase_price: { type: "number", description: "שווי הרכישה" },
        purchase_date: { type: "string", description: "יום הרכישה" },
        sale_date: { type: "string", description: "יום המכירה" }
      },
      required: ["sale_price", "purchase_price"]
    },
    handler: (args) => runBridge("section_49z", args as Record<string, unknown>),
  }
];
