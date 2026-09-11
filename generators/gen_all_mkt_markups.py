import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

os.makedirs('/home/yogi/lod_project', exist_ok=True)

def generate_all_18_marketing_markups():
    markups_data = [
        ("markup_mkt_01_area_discrepancy_law.png", "MKT-ARA-001: Apartment Net/Paladium Area Discrepancy (Sales Law Limit 2.0%)", "Tower 321, 4-Room Apt Type A (Floors 3-8)", "Marketing Area 102.5 m² vs Built Area 98.2 m² -> 4.2% Area Deficit"),
        ("markup_mkt_02_balcony_area_reduction.png", "MKT-BLC-001: Sun Balcony Gross vs Net Area Reduction", "Tower 339, 5-Room Apt Type B", "Marketing Balcony 16.5 m² vs Built Net 13.8 m² (Column intrusion 2.7 m²)"),
        ("markup_mkt_03_ceiling_headroom_ac_drop.png", "MKT-HDR-001: Net Ceiling Height & AC Gypsum Drop Restrictions", "Apartment Living Room & Corridors", "Ceiling drop to 2.15m in hallway < 2.20m Legal Limit"),
        ("markup_mkt_04_bedroom_minimum_dimensions.png", "MKT-DIM-001: Bedroom Minimum Width (B >= 2.60m) & MAMAD Area", "Tower 321, Bedroom 2 & MAMAD", "Bedroom width 2.45m < 2.60m Limit / MAMAD net plaster 8.65 m² < 9.0 m²"),
        ("markup_mkt_05_unmarked_mep_shafts.png", "MKT-SFT-001: Unmarked Plumbing & HVAC Shafts Intruding Apartment Space", "Tower 321 Apt Kitchen & Master Bath", "Sewer & smoke shafts (0.80x0.50m) intrude into kitchen without contract disclosure"),
        ("markup_mkt_06_structural_column_protrusion.png", "MKT-COL-001: Structural Column Protrusions into Bedrooms & Living Rooms", "Tower 339, Master Bedroom", "Heavy 60x60cm column protrudes 35cm into wardrobe space"),
        ("markup_mkt_07_ac_condenser_ledge_size.png", "MKT-LND-001: AC Condenser Ledge Size & Laundry Screen Capacity", "Technical Laundry Balcony", "Ledge width 0.70m cannot fit multi-box VRF + water heater + dryer"),
        ("markup_mkt_08_laundry_screen_air_exhaust.png", "MKT-LND-002: Laundry Screen Hot Air Recirculation & Louver Free Area", "Laundry Balcony Louvers", "Louver free area 35% < 60% Required -> Condenser overheating"),
        ("markup_mkt_09_parking_stall_width_columns.png", "MKT-PRK-001: Deeded Parking Stall Width Adjacent to Concrete Columns", "Basement Parking Level -1, Stall #42", "Stall width 2.25m < 2.90m Required next to structural column"),
        ("markup_mkt_10_disabled_parking_unloading.png", "MKT-PRK-002: Dedicated Accessible Disabled Parking Stall Dimensions", "Basement Parking Level -1, Stall #01", "Width 2.80m without 1.30m unloading aisle < 3.50m Required"),
        ("markup_mkt_11_parking_stall_clear_headroom.png", "MKT-PRK-003: Clear Headroom Above Deeded Parking Stalls (H >= 2.20m)", "Basement Parking Level -2, Stalls #78-82", "Sewer & sprinkler pipes reduce clear headroom to 1.95m < 2.20m"),
        ("markup_mkt_12_storage_room_clear_access.png", "MKT-STR-001: Deeded Storage Unit Net Area & MEP Pipe Obstructions", "Basement Storage Unit S-14", "Main drainage pipe crossing through storage room at 1.40m height"),
        ("markup_mkt_13_window_natural_light_area.png", "MKT-WND-001: Natural Light & Ventilation Window Area (8% of Room)", "Tower 321, Bedroom 3", "Window glass area 0.75 m² < 0.96 m² (8% of 12 m² floor area)"),
        ("markup_mkt_14_garden_apt_vent_proximity.png", "MKT-GDN-001: Garden Apartment Window Proximity to Parking Smoke Vent", "Tower 339 Garden Apt #01", "Parking exhaust vent located 2.20m from garden patio"),
        ("markup_mkt_15_balcony_guardrail_height.png", "MKT-GRL-001: Sun Balcony Guardrail Height (H >= 1.10m per SI 1142)", "Floors 2 to 18 Balconies", "Guardrail height 1.02m < 1.10m Required above finished tile"),
        ("markup_mkt_16_spec_points_count_contract.png", "MKT-SPC-001: Technical Specification Electrical & Plumbing Points Count", "Apartment Kitchen & Living Room", "Contract promised 3-phase 3x25A induction point -> 1-phase in BIM"),
        ("markup_mkt_17_ev_charger_readiness.png", "MKT-SPC-002: EV Charger Infrastructure Readiness in Deeded Parking", "Basement Parking Stalls", "Contract promised EV conduit preparation -> Missing in electrical model"),
        ("markup_mkt_18_marketing_master_holdpoint.png", "MKT-HLD-001: Sales Contract & Marketing Brochure Plan Alignment Hold Point", "All 255 Residential Units & Parking", "Hold Point recommended prior to signing sales contracts to prevent legal claims")
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
        ax.text(50, 89, title, color="#ffffff", fontsize=10.5, fontweight="bold", ha="center", va="center")
        
        card_loc = patches.FancyBboxPatch((8, 68), 40, 12, boxstyle="round,pad=0.3", facecolor="#0b132b", edgecolor="#00b4d8", linewidth=1)
        ax.add_patch(card_loc)
        ax.text(28, 76, "LOCATION IN MODEL / CONTRACT", color="#00b4d8", fontsize=8.5, fontweight="bold", ha="center")
        ax.text(28, 71, loc, color="#ffffff", fontsize=8, ha="center")
        
        card_def = patches.FancyBboxPatch((52, 68), 40, 12, boxstyle="round,pad=0.3", facecolor="#3a0ca3", edgecolor="#f72585", linewidth=1)
        ax.add_patch(card_def)
        ax.text(72, 76, "DISCREPANCY / LEGAL EXPOSURE", color="#f72585", fontsize=8.5, fontweight="bold", ha="center")
        ax.text(72, 71, defect, color="#ffffff", fontsize=8, ha="center")
        
        cad_box = patches.Rectangle((8, 12), 84, 52, facecolor="#000814", edgecolor="#4cc9f0", linewidth=1.5)
        ax.add_patch(cad_box)
        
        for x in range(12, 90, 8):
            ax.plot([x, x], [14, 62], color="#1c2541", linestyle="--", linewidth=0.5)
        for y in range(16, 62, 8):
            ax.plot([10, 90], [y, y], color="#1c2541", linestyle="--", linewidth=0.5)
            
        cloud = patches.FancyBboxPatch((25, 24), 50, 28, boxstyle="round,pad=2", facecolor="#ef233c", alpha=0.25, edgecolor="#d90429", linewidth=2.5, linestyle="--")
        ax.add_patch(cloud)
        
        ax.annotate('SALES PLAN DISCREPANCY DETECTED', xy=(50, 38), xytext=(50, 52),
                    arrowprops=dict(facecolor='#ff0054', edgecolor='#ffffff', width=2, headwidth=8),
                    color='#ffffff', fontsize=9.5, fontweight='bold', ha='center', bbox=dict(boxstyle="round,pad=0.3", facecolor="#d90429", edgecolor="#ffffff"))
        
        stamp = patches.FancyBboxPatch((68, 6), 24, 6, boxstyle="round,pad=0.2", facecolor="#d90429", edgecolor="#ffffff", linewidth=1)
        ax.add_patch(stamp)
        ax.text(80, 9, "RED: CONTRACT UPDATE REQUIRED", color="#ffffff", fontsize=7, fontweight="bold", ha="center", va="center")
        
        plt.tight_layout()
        plt.savefig(p, bbox_inches='tight', pad_inches=0.1)
        plt.close(fig)
        generated.append(p)
        print(f"Generated marketing markup: {fn}")
        
    return generated

markups = generate_all_18_marketing_markups()
print(f"Total {len(markups)} marketing markups generated successfully!")
