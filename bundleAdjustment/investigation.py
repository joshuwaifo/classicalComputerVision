import json
import pprint

file_1 = json.load(open("data/noisy-calibrations-and-accurate-world-points.json"))
file_2 = json.load(open("data/noisy-calibrations-and-world-points.json"))
file_3 = json.load(open("data/projection-check.json"))

# what are cameras?
file_1['cameras']

# since this example has 13 dictionaries inside  it does it mean there are 13 cameras here?



# what are world points?
file_1['worldPoints']

# since this example has 204 lists inside it does that mean it has 204 world points

# each list has 3 elements is that the x-coordinate, y-coordinate and the z-coordinate

# what would both of these look like in blender and is there a way to visualise it so I can feel it better

pprint.pprint(file_1)

# import cameras from calibration files