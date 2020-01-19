test_path = "R8,U5,L5,D3"
test_path2 = "U7,R6,D4,L4"
import copy

def get_points(path):
    points = [[0,0]]
    for step in path.split(","):
        point = copy.deepcopy(points[-1])
        direction, distance = step[:1], int(step[1:])
        if direction == "U": point[1] += distance
        elif direction == "D": point[1] -= distance
        elif direction == "R": point[0] += distance
        elif direction == "L": point[0] -= distance
        points.append(point)
    return points

def sort_points(points):
    if points[0][0] != points[1][0] and points[1][0] > points[0][0]: return [points[1],points[0]]
    elif points[1][1] > points[0][1]: return [points[1],points[0]]
    return points

def get_lines(points):
    lines = []
    i = 0
    while i + 1 < len(points):
        lines.append(sort_points([points[i],points[i+1]]))
        i += 1
    return lines


def main():
    lines = get_lines(get_points(test_path))
    lines2 = get_lines(get_points(test_path2))
    for line in lines:
        for line2 in lines2:
            print(line,line2)
            if line[0][0] != line[1][0] and line2[0][1] != line2[1][1]:
                print("wat")
                if line[0][0] > line2[0][0] and line2[0][0] > line[0][1] and line2[0][1] > line[0][1] and line[0][1] > line2[1][1]:
                    print("intersection")
            elif line2[0][0] != line2[1][0] and line[0][1] != line[1][1]:
                line, line2 = line2, line
                print("fuk")
                print("intersection")
        print()

main()
