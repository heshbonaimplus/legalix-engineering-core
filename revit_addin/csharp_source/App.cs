using System;
using System.Reflection;
using Autodesk.Revit.UI;
using Autodesk.Revit.DB;

namespace LegalixEngineering
{
    public class App : IExternalApplication
    {
        public Result OnStartup(UIControlledApplication application)
        {
            // Create Ribbon Tab
            string tabName = "Legalix Engineering";
            try { application.CreateRibbonTab(tabName); } catch { }

            RibbonPanel panel = application.CreateRibbonPanel(tabName, "BIM Co-Pilot & QA");

            string thisAssemblyPath = Assembly.GetExecutingAssembly().Location;

            // Add Audit Dashboard Button
            PushButtonData btnAudit = new PushButtonData("btnLegalixAudit", "Audit Model", thisAssemblyPath, "LegalixEngineering.CmdAuditModel");
            btnAudit.ToolTip = "Scan open BIM model against Legalix Engineering 2026 Rules Library";
            panel.AddItem(btnAudit);

            // Add One-Click Auto-Fix Button
            PushButtonData btnFix = new PushButtonData("btnLegalixAutoFix", "One-Click Fix", thisAssemblyPath, "LegalixEngineering.CmdAutoFix");
            btnFix.ToolTip = "Automatically apply approved engineering remediation in Revit";
            panel.AddItem(btnFix);

            return Result.Succeeded;
        }

        public Result OnShutdown(UIControlledApplication application)
        {
            return Result.Succeeded;
        }
    }
}
