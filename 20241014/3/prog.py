width = len(input()) - 2
gas_layer = 0
liquid_layer = 0

while True:
    line = input()
    if line[1] != '.':
        break
    gas_layer += 1

while line[1] == '~':
    liquid_layer += 1
    line = input()

total_height = gas_layer + liquid_layer
gas_area = gas_layer * width
liquid_area = liquid_layer * width
max_length = max(len(str(gas_area)), len(str(liquid_area)))
print("#" * (total_height + 2))

for _ in range(gas_area // total_height):
    print("#" + "." * total_height + "#")

for _ in range((liquid_area + total_height - 1) // total_height):
    print("#" + "~" * total_height + "#")

print("#" * (total_height + 2))

total_area = gas_area + liquid_area
gas_percent = round(20 * gas_area / max(gas_area, liquid_area))
liquid_percent = round(20 * liquid_area / max(gas_area, liquid_area))

print(f"{'.' * gas_percent:<20} {gas_area:>{max_length}}/{total_area}")
print(f"{'~' * liquid_percent:<20} {liquid_area:>{max_length}}/{total_area}")
