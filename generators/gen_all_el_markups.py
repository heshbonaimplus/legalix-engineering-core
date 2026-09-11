import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

os.makedirs('/home/yogi/lod_project', exist_ok=True)

# Generate 23 High-Res Visual Markups for Electrical Discipline
def generate_all_23_electrical_markups():
    markups_data = [
        ("markup_el_01_msb_short_circuit.png", "ELEC-MSB-001: Main Switchboard Short Circuit Capacity & Arc Flash", "MSB-PR-01 (Basement -2)", "I_sc = 25 kA < 50 kA Required"),
        ("markup_el_02_fire_pump_rcd_bypass.png", "ELEC-FP-001: Fire Pump Dedicated Feed — RCD strictly prohibited", "FP-PMP-01 Panel", "RCD Installed -> Must be Magnetic Only"),
        ("markup_el_03_ev_charging_dlm_epo.png", "ELEC-EV-001: EV Charging Dynamic Load Management & EPO Trip", "EV-DB-01 / 45 Stations", "DLM Controller Missing / No EPO Fire Interlock"),
        ("markup_el_04_earthing_bonding_tn_s.png", "ELEC-EARTH-001: Foundation Earthing, Equipotential Busbar & Z_s", "Main Transformer & Grounding Grid", "Bonding Strap 30x3.5mm discontinuity at grid"),
        ("markup_el_05_ats_generator_interlock.png", "ELEC-ATS-001: Dual ATS Transfer Switch & Mechanical Interlock", "ATS-EMG-01 (t <= 10s)", "Transition t=18s > 10s / Interlock not certified"),
        ("markup_el_06_generator_fuel_system.png", "ELEC-GEN-002: Emergency Generator Fuel Supply & Leak Sensor", "Fuel Day Tank Bund (Basement -2)", "Fuel transfer pump power missing / No leak sensor"),
        ("markup_el_07_fire_resistant_cables.png", "ELEC-CBL-001: PH120 Fire-Resistant Cables & E90 Cable Trays", "Life Safety Risers (Basement to Tower)", "Standard PVC Cable specified instead of PH120"),
        ("markup_el_08_emergency_lighting_dali.png", "ELEC-EMG-001: Emergency Exit Signs & DALI Central Monitoring", "Egress Corridors & Stairwells", "Battery duration 60 min < 180 min (3h) Required"),
        ("markup_el_09_busbar_voltage_drop.png", "ELEC-BUS-001: Vertical Busbar Trunking & 3% Voltage Drop", "Tower 321 Electrical Shaft (18 Stories)", "Voltage drop Delta_V = 4.8% > 3.0% Max Allowed"),
        ("markup_el_10_electrical_shaft_firestop.png", "ELEC-FST-001: Electrical Shaft 120-min Firestop Barriers", "Floor penetrations (Floors 1 to 18)", "Unsealed floor openings / Missing 120-min collars"),
        ("markup_el_11_surge_protection_spd.png", "ELEC-SPD-001: 3-Stage Cascaded Surge Protection (SPD Type 1/2/3)", "MSB & Floor Distribution Boards", "SPD Type 1 missing at MSB / Sensitive boards unprotected"),
        ("markup_el_12_apartment_panel_rcd.png", "ELEC-DB-001: Residential Apartment Distribution Panel RCD 30mA", "Apartment DB (Typical Floors)", "Lighting circuits bypassing 30mA RCD protection"),
        ("markup_el_13_mamad_cbrn_power_socket.png", "ELEC-MMD-001: MAMAD CBRN Socket +1.80m (No RCD) & Blast LED", "Protected Room (MAMAD)", "Socket at +0.30m with RCD -> Must be +1.80m No RCD"),
        ("markup_el_14_mamad_roxtec_gas_seals.png", "ELEC-MMD-002: Modular Blast & Gas Seals in Electrical Sleeves", "MAMAD Concrete Penetration", "Foam sealant used -> Must be Roxtec R-75 (1.5 bar)"),
        ("markup_el_15_mamad_circuit_isolation.png", "ELEC-MMD-003: Dedicated MAMAD Electrical Sub-Circuit Isolation", "MAMAD Power Loop", "MAMAD daisy-chained with bedroom -> Must be isolated"),
        ("markup_el_16_facp_fire_matrix_interlock.png", "ELEC-FACP-001: Main Fire Alarm Control Panel (FACP) & Matrix", "Main Control Room / Fire Command", "Class B SLC loop -> Must be Class A Loop with Isolators"),
        ("markup_el_17_voice_evacuation_pava.png", "ELEC-PA-001: Voice Evacuation System (PA/VA) STI >= 0.50", "Public Corridors & Parking Levels", "Plastic horns used -> Must be Metal Fire Domes (EN 54)"),
        ("markup_el_18_warden_phone_bda_system.png", "ELEC-COM-001: Firefighter Warden Phone & BDA Radio Coverage", "Protected Stairwells & Basements", "BDA emergency radio repeater missing in basements"),
        ("markup_el_19_lightning_protection_lps.png", "ELEC-LPS-001: Lightning Protection System (LPS) Class II Mesh", "Tower Roof & Technical Floor", "Air terminal mesh 20x20m > 10x10m Class II Limit"),
        ("markup_el_20_cable_tray_superposition.png", "ELEC-SUP-001: Cable Tray Clearances vs HVAC & Headroom >= 2.40m", "Parking Level -1 Driving Aisle", "Cable tray below 2.10m / Zero gap from HVAC duct"),
        ("markup_el_21_seismic_bracing_cable_trays.png", "ELEC-SEIS-001: 45° Seismic Sway Bracing for Heavy Cable Trays", "Basement Trays (Width >= 300mm)", "Threaded rods only -> Must have 45° angle steel braces"),
        ("markup_el_22_flood_disconnect_basement.png", "ELEC-FLD-001: Basement -2 Flood Alarm & Automatic Power Trip", "Basement -2 Low Sockets & Distribution", "No flood sensor interlock / Sump pumps on shared RCD"),
        ("markup_el_23_commissioning_megger_holdpoint.png", "ELEC-TAB-001: Insulation Megger 1000V, Loop Impedance & Hold Point", "Complete Electrical Installation", "Hold Point recommended until 22 defects resolved in Rev 02")
    ]
    
    generated = []
    for fn, title, loc, defect in markups_data:
        p = os.path.join('/home/yogi/lod_project', fn)
        fig, ax = plt.subplots(figsize=(12, 8), dpi=180)
        ax.set_facecolor("#0b132b")
        fig.patch.set_facecolor("#0b132b")
        
        # Grid layout
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.axis('off')
        
        # Draw tech frame
        rect_outer = patches.Rectangle((2, 2), 96, 96, linewidth=2, edgecolor="#1c2541", facecolor="none")
        rect_inner = patches.Rectangle((4, 4), 92, 92, linewidth=1, edgecolor="#3a506b", facecolor="#1c2541", alpha=0.4)
        ax.add_patch(rect_outer)
        ax.add_patch(rect_inner)
        
        # Header Badge
        badge = patches.FancyBboxPatch((6, 84), 88, 10, boxstyle="round,pad=0.5", facecolor="#102c57", edgecolor="#48cae4", linewidth=1.5)
        ax.add_patch(badge)
        ax.text(50, 89, title, color="#ffffff", fontsize=11, fontweight="bold", ha="center", va="center")
        
        # Location & Defect Cards
        card_loc = patches.FancyBboxPatch((8, 68), 40, 12, boxstyle="round,pad=0.3", facecolor="#0b132b", edgecolor="#00b4d8", linewidth=1)
        ax.add_patch(card_loc)
        ax.text(28, 76, "LOCATION IN MODEL", color="#00b4d8", fontsize=9, fontweight="bold", ha="center")
        ax.text(28, 71, loc, color="#ffffff", fontsize=8.5, ha="center")
        
        card_def = patches.FancyBboxPatch((52, 68), 40, 12, boxstyle="round,pad=0.3", facecolor="#3a0ca3", edgecolor="#f72585", linewidth=1)
        ax.add_patch(card_def)
        ax.text(72, 76, "MEASURED DEFECT / GAP", color="#f72585", fontsize=9, fontweight="bold", ha="center")
        ax.text(72, 71, defect, color="#ffffff", fontsize=8.5, ha="center")
        
        # Visual CAD simulation box
        cad_box = patches.Rectangle((8, 12), 84, 52, facecolor="#000814", edgecolor="#4cc9f0", linewidth=1.5)
        ax.add_patch(cad_box)
        
        # Grid lines in CAD box
        for x in range(12, 90, 8):
            ax.plot([x, x], [14, 62], color="#1c2541", linestyle="--", linewidth=0.5)
        for y in range(16, 62, 8):
            ax.plot([10, 90], [y, y], color="#1c2541", linestyle="--", linewidth=0.5)
            
        # Draw audit markup cloud (Crimson)
        cloud = patches.FancyBboxPatch((25, 24), 50, 28, boxstyle="round,pad=2", facecolor="#ef233c", alpha=0.25, edgecolor="#d90429", linewidth=2.5, linestyle="--")
        ax.add_patch(cloud)
        
        # Arrow pointing to defect
        ax.annotate('AUDIT DEFECT DETECTED', xy=(50, 38), xytext=(50, 52),
                    arrowprops=dict(facecolor='#ff0054', edgecolor='#ffffff', width=2, headwidth=8),
                    color='#ffffff', fontsize=10, fontweight='bold', ha='center', bbox=dict(boxstyle="round,pad=0.3", facecolor="#d90429", edgecolor="#ffffff"))
        
        # Verification Stamp
        stamp = patches.FancyBboxPatch((70, 6), 22, 6, boxstyle="round,pad=0.2", facecolor="#d90429", edgecolor="#ffffff", linewidth=1)
        ax.add_patch(stamp)
        ax.text(81, 9, "RED: ACTION REQUIRED", color="#ffffff", fontsize=7.5, fontweight="bold", ha="center", va="center")
        
        plt.tight_layout()
        plt.savefig(p, bbox_inches='tight', pad_inches=0.1)
        plt.close(fig)
        generated.append(p)
        print(f"Generated markup: {fn}")
        
    return generated

markups = generate_all_23_electrical_markups()
print(f"Total {len(markups)} electrical markups successfully generated!")
