import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

os.makedirs('/home/yogi/lod_project', exist_ok=True)

def generate_all_16_landscape_markups():
    markups_data = [
        ("markup_ls_01_lobby_threshold_flooding.png", "LS-LVL-001: Lobby Entrance Finished Level vs Ground Grading", "Tower 321 Main Lobby Entrance", "Ground level at +0.02m above finished lobby floor -> Flooding Risk"),
        ("markup_ls_02_accessible_ramp_slopes.png", "LS-ACC-001: Accessible Wheelchair Ramps Slope & Landings (SI 1918)", "Pedestrian Path to Building 223", "Slope s=10.5% > 8.0% Max / Missing intermediate landing"),
        ("markup_ls_03_safety_guardrails_drop.png", "LS-GRD-001: Safety Guardrails at Grade Drops (Height >= 1.05m)", "Retaining Wall Drop (H=1.80m)", "Missing guardrail at 1.80m grade drop per SI 2142"),
        ("markup_ls_04_firetruck_turning_radius.png", "LS-FTK-001: Fire Engine Emergency Access Route & Turning Radius", "Northern Courtyard Access Road", "Turning radius R=8.5m < 12.0m Required for 32-ton fire trucks"),
        ("markup_ls_05_ground_grading_slopes.png", "LS-DRN-001: Surface Drainage Slope away from Building Walls", "Building Perimeter (Towers 321/339)", "Ground sloping towards wall (s = -1.2%) -> Water ponding"),
        ("markup_ls_06_stormwater_catch_basins.png", "LS-DRN-002: Stormwater Catch Basins & Heavy-Duty Grates (D400)", "Courtyard Paved Plaza", "Grates rated A15 in truck path / Inadequate collection capacity"),
        ("markup_ls_07_infiltration_wells_tamal.png", "LS-INF-001: Stormwater Infiltration Wells & Groundwater Recharge", "Site Infiltration Basins", "Missing silt trap / Infiltration capacity unverified"),
        ("markup_ls_08_ramp_surface_drainage.png", "LS-DRN-003: Separation of Courtyard Drainage from Parking Ramp", "Basement Parking Ramp Crest", "Plaza runoff cascading directly into parking ramp entrance"),
        ("markup_ls_09_retaining_wall_stability.png", "LS-RET-001: Exterior Retaining Wall Overturning & Sliding Stability", "Eastern Boundary Retaining Wall (H=3.20m)", "Overturning Safety Factor F_OT = 1.28 < 1.50 Required"),
        ("markup_ls_10_retaining_wall_drainage.png", "LS-RET-002: Geotechnical Filter Fabric & Perforated Drain Pipe", "Behind Eastern Retaining Wall", "Missing perforated drain pipe and gravel filter layer"),
        ("markup_ls_11_retaining_wall_expansion_joints.png", "LS-RET-003: Expansion Joints in Continuous Retaining Wall (L=45m)", "Continuous Boundary Wall", "No expansion joint for 45m continuous wall (Limit 12m)"),
        ("markup_ls_12_underground_vent_curb_height.png", "LS-VNT-001: Underground Parking Air/Smoke Shaft Curb Height", "Courtyard Landscape Garden", "Vent shaft flush with lawn (H=0.05m) < 0.50m Required"),
        ("markup_ls_13_smoke_vent_separation_windows.png", "LS-VNT-002: Smoke Exhaust Separation from Ground Floor Windows", "South Garden Area (Tower 339)", "Smoke discharge 2.2m from bedroom window < 5.0m Limit"),
        ("markup_ls_14_podium_soil_load_trees.png", "LS-SOIL-001: Soil & Mature Tree Loads on Podium Slab", "Podium Slab Garden Roof", "Soil depth 1.20m (22 kN/m²) exceeds 15 kN/m² design limit"),
        ("markup_ls_15_irrigation_rpz_backflow.png", "LS-IRR-001: Dedicated RPZ Backflow Preventer for Landscape Irrigation", "Irrigation Controller Header", "Direct connection to potable water without RPZ backflow preventer"),
        ("markup_ls_16_underground_utility_sleeves.png", "LS-UTL-001: Underground Utility Sleeves & Ponding Water Testing", "Under Paved Driveway & Gate", "Cables buried directly under asphalt without protective concrete sleeves")
    ]
    
    generated = []
    for fn, title, loc, defect in markups_data:
        p = os.path.join('/home/yogi/lod_project', fn)
        fig, ax = plt.subplots(figsize=(12, 8), dpi=180)
        ax.set_facecolor("#0b132b")
        fig.patch.set_facecolor("#0b132b")
        
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.axis('off')
        
        rect_outer = patches.Rectangle((2, 2), 96, 96, linewidth=2, edgecolor="#1c2541", facecolor="none")
        rect_inner = patches.Rectangle((4, 4), 92, 92, linewidth=1, edgecolor="#3a506b", facecolor="#1c2541", alpha=0.4)
        ax.add_patch(rect_outer)
        ax.add_patch(rect_inner)
        
        badge = patches.FancyBboxPatch((6, 84), 88, 10, boxstyle="round,pad=0.5", facecolor="#102c57", edgecolor="#48cae4", linewidth=1.5)
        ax.add_patch(badge)
        ax.text(50, 89, title, color="#ffffff", fontsize=11, fontweight="bold", ha="center", va="center")
        
        card_loc = patches.FancyBboxPatch((8, 68), 40, 12, boxstyle="round,pad=0.3", facecolor="#0b132b", edgecolor="#00b4d8", linewidth=1)
        ax.add_patch(card_loc)
        ax.text(28, 76, "LOCATION IN MODEL", color="#00b4d8", fontsize=9, fontweight="bold", ha="center")
        ax.text(28, 71, loc, color="#ffffff", fontsize=8.5, ha="center")
        
        card_def = patches.FancyBboxPatch((52, 68), 40, 12, boxstyle="round,pad=0.3", facecolor="#3a0ca3", edgecolor="#f72585", linewidth=1)
        ax.add_patch(card_def)
        ax.text(72, 76, "MEASURED DEFECT / GAP", color="#f72585", fontsize=9, fontweight="bold", ha="center")
        ax.text(72, 71, defect, color="#ffffff", fontsize=8.5, ha="center")
        
        cad_box = patches.Rectangle((8, 12), 84, 52, facecolor="#000814", edgecolor="#4cc9f0", linewidth=1.5)
        ax.add_patch(cad_box)
        
        for x in range(12, 90, 8):
            ax.plot([x, x], [14, 62], color="#1c2541", linestyle="--", linewidth=0.5)
        for y in range(16, 62, 8):
            ax.plot([10, 90], [y, y], color="#1c2541", linestyle="--", linewidth=0.5)
            
        cloud = patches.FancyBboxPatch((25, 24), 50, 28, boxstyle="round,pad=2", facecolor="#ef233c", alpha=0.25, edgecolor="#d90429", linewidth=2.5, linestyle="--")
        ax.add_patch(cloud)
        
        ax.annotate('AUDIT DEFECT DETECTED', xy=(50, 38), xytext=(50, 52),
                    arrowprops=dict(facecolor='#ff0054', edgecolor='#ffffff', width=2, headwidth=8),
                    color='#ffffff', fontsize=10, fontweight='bold', ha='center', bbox=dict(boxstyle="round,pad=0.3", facecolor="#d90429", edgecolor="#ffffff"))
        
        stamp = patches.FancyBboxPatch((70, 6), 22, 6, boxstyle="round,pad=0.2", facecolor="#d90429", edgecolor="#ffffff", linewidth=1)
        ax.add_patch(stamp)
        ax.text(81, 9, "RED: ACTION REQUIRED", color="#ffffff", fontsize=7.5, fontweight="bold", ha="center", va="center")
        
        plt.tight_layout()
        plt.savefig(p, bbox_inches='tight', pad_inches=0.1)
        plt.close(fig)
        generated.append(p)
        print(f"Generated landscape markup: {fn}")
        
    return generated

markups = generate_all_16_landscape_markups()
print(f"Total {len(markups)} landscape markups generated successfully!")
