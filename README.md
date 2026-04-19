# Cold Plate Thermal Model

A simple thermal resistance model for estimating chip temperature in a direct-to-chip cold plate cooling concept.

## Overview

This project provides a first-pass analytical model for a cold plate design using basic heat transfer relationships. It is intended as a sanity-check tool before higher-fidelity CFD or conjugate heat transfer simulation.

The model estimates junction or base temperature using:

- Applied heat load
- Chip contact area
- Copper conduction path
- Convective heat transfer to coolant

## Purpose

This repository supports early-stage thermal design work by translating physical assumptions into a fast engineering calculation. It is especially useful for:

- comparing design assumptions
- estimating temperature rise
- understanding dominant thermal resistances
- building intuition before simulation

## Example physics

The total temperature rise is estimated using a thermal resistance network:

\[
R_{\text{total}} = R_{\text{cond}} + R_{\text{conv}}
\]

\[
\Delta T = Q \cdot R_{\text{total}}
\]

Where:

- \(Q\) = heat load
- \(R_{\text{cond}}\) = conduction resistance through copper
- \(R_{\text{conv}}\) = convection resistance to coolant

## Inputs

- Heat load [W]
- Chip area [m²]
- Copper thickness [m]
- Copper thermal conductivity [W/m·K]
- Convective coefficient [W/m²·K]
- Coolant inlet temperature [°C]

## Outputs

- Conduction resistance
- Convection resistance
- Total thermal resistance
- Estimated surface temperature

## Notes

This is a simplified lumped model and does not replace CFD, detailed conjugate heat transfer, or flow distribution analysis.

## Author

Audrey Enriquez
