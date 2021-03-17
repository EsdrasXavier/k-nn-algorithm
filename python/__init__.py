import math

COLORS_BASE = [
    [1, 10, 200, 1],
    [2, 20, 230, 1],
    [6, 25, 150, 1],
    [7, 45, 100, 1],
    [10, 50, 125, 1],
    [3, 24, 111, 1],
    [100, 4, 10, 2],
    [250, 7, 50, 2],
    [243, 5, 68, 2],
    [210, 2, 90, 2],
    [200, 1, 95, 2],
    [215, 0, 68, 2],
    [56, 200, 1, 3],
    [79, 234, 3, 3],
    [80, 210, 8, 3],
    [95, 200, 10, 3],
    [80, 210, 4, 3],
    [49, 207, 1, 3],
]

COLORS_TABLE = [
    [1, 2, 100],
    [10, 20, 30],
    [8, 5, 20],
    [237, 45, 100],
    [1, 50, 101],
    [67, 121, 12],
]


class RGB():
    def __init__(self, r, g, b, _class=0, *arg, **kwrg):
        self.r = r
        self.g = g
        self.b = b
        self._class = _class

    def distance(self, obj):
        return math.sqrt(
            math.pow(obj.r - self.r, 2) +
            math.pow(obj.g - self.g, 2) +
            math.pow(obj.b - self.b, 2)
        )

    def __str__(self):
        return 'RGB({}, {}, {})'.format(self.r, self.g, self.b)


def execute_knn(knn, base_obj, data_sample):
    obj_list = []
    for base in data_sample:
        obj_list.append(RGB(base[0], base[1], base[2], base[3]))

    sorted_by_distance = sorted(
        obj_list, key=lambda x: x.distance(base_obj), reverse=False)

    obj_count = {}
    for obj in sorted_by_distance[:knn]:
        if obj._class in obj_count:
            obj_count[obj._class] = obj_count[obj._class] + 1
        else:
            obj_count[obj._class] = 1

    majority = max(obj_count, key=lambda k: obj_count[k])
    print('{} | k = {} -> class {}'.format(str(base_obj), knn, majority))


def main():
    knn_input = [3, 5, 7]
    for sample_row in COLORS_TABLE:
        base_obj = RGB(sample_row[0], sample_row[1], sample_row[2])
        for knn in knn_input:
            execute_knn(knn, base_obj, COLORS_BASE)

if __name__ == '__main__':
    main()
