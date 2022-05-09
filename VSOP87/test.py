import temps as t
import position_planetes as pos
import DANGER as D

# périphelion : 1881-02-02 
# 60 216,8 d = révol
perigee = (1881, 2, 2)
apogee  = t.gregorien(t.JJ(*(perigee))+(60_216.8/2))

print(f'peri {t.JJ(*perigee)}\napo {t.JJ(*apogee)}')

print("dist apo", D.get_distance(pos.get_by_VSOP87('neptune', *apogee), pos.get_sun(*apogee)))
print("dist peri", D.get_distance(pos.get_by_VSOP87('neptune', *perigee), pos.get_sun(*perigee)))

print("angle",
D.get_angle(pos.get_by_VSOP87('neptune', *perigee), pos.get_sun(*perigee), pos.get_by_VSOP87('mercure', *t.gregorien(2459507.4984667003)))
)