power_levels = [100, 200, 300, 400]
double_power_levels = []

for pow in power_levels:
    double_power_levels.append(pow * 2)

print(double_power_levels)

double_power_levels = [pow * 2 for pow in power_levels if pow != 300]
print(double_power_levels)
