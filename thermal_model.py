"""
cold-plate-thermal-model
Simple thermal resistance model for a direct-to-chip cold plate concept.

Author: Audrey Enriquez
"""

from dataclasses import dataclass


@dataclass
class ColdPlateInputs:
    heat_load_w: float
    chip_area_m2: float
    copper_thickness_m: float
    copper_k_w_mk: float
    h_conv_w_m2k: float
    coolant_temp_c: float


@dataclass
class ColdPlateResults:
    r_cond_k_w: float
    r_conv_k_w: float
    r_total_k_w: float
    delta_t_c: float
    estimated_surface_temp_c: float


def conduction_resistance(thickness_m: float, conductivity_w_mk: float, area_m2: float) -> float:
    """Calculate 1D conduction resistance through copper."""
    if conductivity_w_mk <= 0 or area_m2 <= 0:
        raise ValueError("Conductivity and area must be greater than zero.")
    return thickness_m / (conductivity_w_mk * area_m2)


def convection_resistance(h_conv_w_m2k: float, area_m2: float) -> float:
    """Calculate convection resistance to coolant."""
    if h_conv_w_m2k <= 0 or area_m2 <= 0:
        raise ValueError("Convection coefficient and area must be greater than zero.")
    return 1.0 / (h_conv_w_m2k * area_m2)


def solve_cold_plate(inputs: ColdPlateInputs) -> ColdPlateResults:
    """Solve the simplified cold plate thermal resistance network."""
    r_cond = conduction_resistance(
        inputs.copper_thickness_m,
        inputs.copper_k_w_mk,
        inputs.chip_area_m2,
    )
    r_conv = convection_resistance(
        inputs.h_conv_w_m2k,
        inputs.chip_area_m2,
    )
    r_total = r_cond + r_conv
    delta_t = inputs.heat_load_w * r_total
    surface_temp = inputs.coolant_temp_c + delta_t

    return ColdPlateResults(
        r_cond_k_w=r_cond,
        r_conv_k_w=r_conv,
        r_total_k_w=r_total,
        delta_t_c=delta_t,
        estimated_surface_temp_c=surface_temp,
    )


def main() -> None:
    # Example values for a high-power direct-to-chip cooling case
    inputs = ColdPlateInputs(
        heat_load_w=1200.0,
        chip_area_m2=0.044 * 0.044,      # 44 mm x 44 mm
        copper_thickness_m=0.001,        # 1 mm conduction path
        copper_k_w_mk=391.0,             # copper thermal conductivity
        h_conv_w_m2k=15000.0,            # assumed strong liquid cooling coefficient
        coolant_temp_c=25.0,
    )

    results = solve_cold_plate(inputs)

    print("=== Cold Plate Thermal Model Results ===")
    print(f"Conduction resistance:      {results.r_cond_k_w:.6f} K/W")
    print(f"Convection resistance:      {results.r_conv_k_w:.6f} K/W")
    print(f"Total thermal resistance:   {results.r_total_k_w:.6f} K/W")
    print(f"Temperature rise:           {results.delta_t_c:.2f} °C")
    print(f"Estimated surface temp:     {results.estimated_surface_temp_c:.2f} °C")


if __name__ == "__main__":
    main()
