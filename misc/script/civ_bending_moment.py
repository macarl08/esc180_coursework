# civ_bending_moment.py
# CIV102 Bridge Project

# Fall 2021
# Group 403
# Group Members:
#  - Carl Ma
#  - Abdullah Fawzy
#  - Albert Zhang


# ------------------------------ IMPORT MODULES ------------------------------ #

import math

# ------------------------------ CONSTANTS: Material Property ------------------------------ #

T_STRENGTH = 30
C_STRENGTH = 6
SHEAR_STRENGTH = 4
YOUNG = 4000
POISSON = 0.2
CEMENT_SHEAR = 2

# ------------------------------ CONSTANTS: Structure Property ------------------------------ #

height = None

# ------------------------------ 4.4-4.6 Bending moment ------------------------------ #

# 4.4 Bending moment causing matboard tension failure
# 4.5 Bending moment causing matboard compression failure
# 4.6 Bending moment causing matboard flexural buckling failure

def set_height(h):
	global height
	height = h

def get_sigma_ultimate(force):
	if force == "tension":
		return T_STRENGTH
	if force == "compression":
		return -1*C_STRENGTH

def get_bending_moment(y_global, I, sigma, curvature):
	if sigma>0 and curvature == "concave up":
		return I*sigma/y_global
	if sigma<0 and curvature == "concave up":
		return I*sigma/(height-y_global)
	if sigma>0 and curvature == "concave down":
		return I*sigma/(height-y_global)
	if sigma<0 and curvature == "concave down":
		return I*sigma/y_global

def get_sigma_critical(k, t, b):
	return k * (math.pi)**2 * YOUNG / 12 / (1-POISSON**2) * (t/b)**2