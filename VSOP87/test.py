import temps as t
import position_planetes as pos
import DANGER as D

perigee = (2050, 7, 17)
apogee  = (2009, 2, 27)

#print(D.get_distance(pos.get_by_VSOP87('uranus', *apogee), pos.get_sun(*apogee)))

print(
D.get_angle(pos.get_by_VSOP87('uranus', *perigee), pos.get_sun(*perigee), pos.get_by_VSOP87('mercure', *t.gregorien(2459507.4984667003)))
)