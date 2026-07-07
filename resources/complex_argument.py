#!/usr/bin/env python3
"""
Generate a diagram showing the argument (angle) of a complex number on the complex plane.
Outputs to complex-argument.png in the same directory.
"""

import matplotlib.pyplot as plt
import numpy as np

# Create figure with subplots showing different quadrants
fig, axes = plt.subplots(2, 2, figsize=(12, 12), dpi=150)

# Define example complex numbers in each quadrant
examples = [
    (3, 2, '3 + 2i', 0),      # Q1
    (-2, 2.5, '-2 + 2.5i', 1),  # Q2
    (-2.5, -1.5, '-2.5 - 1.5i', 2),  # Q3
    (2.5, -2, '2.5 - 2i', 3),  # Q4
]

for idx, (real, imag, label, ax_idx) in enumerate(examples):
    ax = axes[ax_idx // 2, ax_idx % 2]
    ax.set_aspect('equal')
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
    ax.axhline(y=0, color='k', linewidth=1.5)
    ax.axvline(x=0, color='k', linewidth=1.5)
    
    # Axis labels
    ax.set_xlabel('Re', fontsize=11, fontweight='bold')
    ax.set_ylabel('Im', fontsize=11, fontweight='bold')
    ax.tick_params(labelsize=9)
    
    # Draw radius line
    r = np.sqrt(real**2 + imag**2)
    ax.plot([0, real], [0, imag], 'r-', linewidth=2.5)
    ax.plot(real, imag, 'ro', markersize=8)
    
    # Compute argument
    arg_rad = np.arctan2(imag, real)
    arg_deg = np.degrees(arg_rad)
    
    # Draw arc for angle
    if arg_rad >= 0:
        arc_angles = np.linspace(0, arg_rad, 50)
    else:
        arc_angles = np.linspace(arg_rad, 0, 50)
    
    arc_r = 0.8
    ax.plot(arc_r * np.cos(arc_angles), arc_r * np.sin(arc_angles), 'b--', linewidth=2)
    
    # Label the angle
    if arg_rad >= 0:
        angle_label_x = 1.1 * np.cos(arg_rad / 2)
        angle_label_y = 1.1 * np.sin(arg_rad / 2)
    else:
        angle_label_x = 1.1 * np.cos(arg_rad / 2)
        angle_label_y = 1.1 * np.sin(arg_rad / 2)
    ax.text(angle_label_x, angle_label_y, r'$\arg(z)$', fontsize=11, color='blue', fontweight='bold')
    
    # Label the point
    ax.text(real + 0.3, imag - 0.3, label, fontsize=11, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
    
    # Show computed argument
    arg_text = f'arg(z) = {arg_rad:.3f} rad ({arg_deg:.1f}°) '
    ax.text(0.02, 0.98, arg_text, transform=ax.transAxes, fontsize=10, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7),
            verticalalignment='top')
    
    # Mark quadrant
    quadrant_names = ['Quadrant I: 0 to $\\frac{\\pi}{2}$ rad (0° to 90°)', 'Quadrant II: $\\frac{\\pi}{2}$ rad to $\\pi$ rad (90° to 180°)', 'Quadrant III: -$\\pi$ rad to -$\\frac{\\pi}{2}$ rad (-180° to -90°)', 'Quadrant IV: -$\\frac{\\pi}{2}$ rad to 0 rad (-90° to 0°)']
    ax.text(0.02, 0.88, quadrant_names[ax_idx], transform=ax.transAxes, fontsize=9, style='italic',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))

plt.tight_layout()
plt.savefig('complex-argument.png', dpi=150, bbox_inches='tight', facecolor='white')
print("Generated: complex-argument.png")
plt.close()
