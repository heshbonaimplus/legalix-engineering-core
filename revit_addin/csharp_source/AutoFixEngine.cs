using System;
using System.Collections.Generic;
using Autodesk.Revit.DB;
using Autodesk.Revit.DB.Plumbing;
using Autodesk.Revit.DB.Mechanical;
using Autodesk.Revit.UI;

namespace LegalixEngineering
{
    public class AutoFixEngine
    {
        public static bool ApplyRemediation(Document doc, string ruleId, ElementId elementId)
        {
            Element elem = doc.GetElement(elementId);
            if (elem == null) return false;

            using (Transaction t = new Transaction(doc, "Legalix Auto-Fix: " + ruleId))
            {
                t.Start();

                switch (ruleId)
                {
                    case "HVAC-JET-001":
                        // Deflector Vane Angle to -5 deg
                        Parameter deflectorParam = elem.LookupParameter("Deflector_Angle");
                        if (deflectorParam != null && !deflectorParam.IsReadOnly)
                            deflectorParam.Set(-5.0 * Math.PI / 180.0);
                        break;

                    case "PLB-SLP-001":
                        // Correct pipe slope to 1.5%
                        if (elem is Pipe pipe)
                        {
                            Parameter slopeParam = pipe.get_Parameter(BuiltInParameter.RBS_PIPE_SLOPE);
                            slopeParam.Set(0.015);
                        }
                        break;

                    case "ELEC-MMD-001":
                        // Elevate CBRN socket to +1.80m
                        Parameter elevParam = elem.get_Parameter(BuiltInParameter.INSTANCE_ELEVATION_PARAM);
                        if (elevParam != null && !elevParam.IsReadOnly)
                            elevParam.Set(1.80 / 0.3048);
                        break;

                    case "HVAC-CO-001":
                        // Lower CO sensor to +1.50m
                        Parameter coElev = elem.get_Parameter(BuiltInParameter.INSTANCE_ELEVATION_PARAM);
                        if (coElev != null && !coElev.IsReadOnly)
                            coElev.Set(1.50 / 0.3048);
                        break;

                    case "ST-TWR-009":
                        // Stagger column rebar lap splices by 75cm
                        Parameter staggerParam = elem.LookupParameter("Lap_Splice_Stagger_Offset");
                        if (staggerParam != null && !staggerParam.IsReadOnly)
                            staggerParam.Set(0.75 / 0.3048);
                        break;

                    default:
                        // General parameter override from Legalix payload
                        break;
                }

                t.Commit();
            }
            return true;
        }
    }
}
