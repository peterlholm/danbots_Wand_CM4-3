"Calculate spot position"
from math import sin, cos, pi

#   221227  PLH     First version
#   230403  PLH     Update CM4-3 version

# caluclate spot  position given dias etc information

# dias

# PERIOD_DEGREE = 1.3   # degree pr period
# IMAGE_SIZE = 4.233  # mm
# IMAGE_PERIODS = 17

# spot length in mm

SPOT_CENTER = 23.5      # L1 spot center to front of plastic
SPOT_2_CAMERA = 6.0     # L2 distance from plastic front to camera centrum
CAMERA_HIGHT = 11.0     # CH Camera height from projector center

# mirror

MIRROR_ANGLE = 30                       # v  Mirror angle to lodret
#MIRROR_ANGLE_SPOT = 90 - MIRROR_ANGLE   # to light
CAMERA_2_MIRROR = 9                     # L3 x distance from camera to mirrrortomm

print("\nProjektor Basis Parameters")

print(f"Spot center from front\t{SPOT_CENTER:3} mm")
print(f"Spot front to camera\t{SPOT_2_CAMERA:3} mm")

# print("\nDias parameters")


# print(f"Struct light pr period\t {PERIOD_DEGREE:3} degree")
# print(f"Image Size \t\t {IMAGE_SIZE:3} mm")
# print(f"Periods on Image\t{IMAGE_PERIODS:3}")


# calculate spot coordinates

D = SPOT_CENTER + SPOT_2_CAMERA + CAMERA_2_MIRROR

print(f"Dist spot to dias\t{D:3} mm")

#  x =sin(v) x L
#  y = cos(v) * L
#v = 90-2*MIRROR_ANGLE
v = MIRROR_ANGLE
#print("v",v)
RAD= 2 * v / 180 * pi
dx = cos(RAD) * D
dy = sin(RAD) * D
Sx = - CAMERA_2_MIRROR - dx
Sy = dy - CAMERA_HIGHT

print(f"Angle \t{v} degree")
print(f"Coordsystem with camera in 0,0")
print(f"Spot pos mirror:\t({dx:4.1f},{dy:4.1f})")

print(f"Spot ABS pos:\t\t({Sx:4.1f},{Sy:4.1f})")
print(f"Degree to x \t\t{v:3.1f} grader")
