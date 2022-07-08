import nazca as nd


class CSEMLogo:
    cell_name = "CSEMLogo"
    number = 0

    def __init__(self, text_layer=None):
        self.text_layer = text_layer if text_layer is not None else "lay125"

        # create the gds
        self._cell = self.create_gds()

    def create_gds(self):
        CSEMLogo.number += 1
        with nd.Cell(name=CSEMLogo.cell_name + "_" + str(CSEMLogo.number)) as cell:
            dot1 = [(-57.39500, 1.07700), (-58.40900, 1.28200), (-59.23700, 1.84100), (-59.79500, 2.66900), (-60.00000, 3.68300), (-59.79500, 4.69700), (-59.23700, 5.52500), (-58.40900, 6.08300), (-57.39500, 6.28800), (-56.38200, 6.08300), (-55.55400, 5.52500), (-54.99600, 4.69700), (-54.79100, 3.68300), (-54.99600, 2.66900), (-55.55400, 1.84100), (-56.38200, 1.28200)]
            dot2 = [(-49.74900, 1.07700), (-50.76200, 1.28200), (-51.59000, 1.84100), (-52.14900, 2.66900), (-52.35300, 3.68300), (-52.14900, 4.69700), (-51.59000, 5.52500), (-50.76200, 6.08300), (-49.74900, 6.28800), (-48.73400, 6.08300), (-47.90600, 5.52500), (-47.34700, 4.69700), (-47.14200, 3.68300), (-47.34700, 2.66900), (-47.90600, 1.84100), (-48.73400, 1.28200)]
            dot3 = [(-57.39500, -6.57000), (-58.40900, -6.36600), (-59.23700, -5.80700), (-59.79500, -4.97900), (-60.00000, -3.96600), (-59.79500, -2.95200), (-59.23700, -2.12300), (-58.40900, -1.56400), (-57.39500, -1.35900), (-56.38200, -1.56400), (-55.55400, -2.12300), (-54.99600, -2.95200), (-54.79100, -3.96600), (-54.99600, -4.98000), (-55.55400, -5.80800), (-56.38200, -6.36600)]
            dot4 = [(-49.74900, - 6.57000), (-50.76200, - 6.36600), (-51.59000, - 5.80800), (-52.14900, - 4.98000), (-52.35300, - 3.96600), (-52.14900, - 2.95200), (-51.59000, - 2.12300), (-50.76200, - 1.56400), (-49.74900, - 1.35900), (-48.73400, - 1.56400), (-47.90600, - 2.12300), (-47.34700, - 2.95200), (-47.14200, - 3.96600), (-47.34700, - 4.98000), (-47.90600, - 5.80800), (-48.73400, - 6.36600)]
            s = [(-25.486, -11.732), (-27.803, -11.478), (-29.933, -10.783), (-31.841, -9.696), (-33.486, -8.263), (-34.832, -6.533), (-35.84, -4.554), (-36.472, -2.372), (-36.692, -0.036), (-36.488, 2.239), (-35.915, 4.301), (-35.028, 6.136), (-33.881, 7.733), (-32.531, 9.079), (-31.032, 10.163), (-29.44, 10.97), (-27.811, 11.49), (-25.704, 11.737), (-23.141, 11.52), (-21.766, 11.174), (-20.372, 10.636), (-18.988, 9.879), (-17.647, 8.878), (-20.242, 6.35), (-21.0, 6.871), (-22.74, 7.666), (-23.923, 7.959), (-25.285, 8.073), (-26.804, 7.926), (-28.457, 7.435), (-29.443, 6.927), (-30.334, 6.274), (-31.121, 5.489), (-31.79, 4.582), (-32.331, 3.564), (-32.732, 2.448), (-32.981, 1.244), (-33.067, -0.036), (-32.937, -1.48), (-32.553, -2.91), (-31.927, -4.272), (-31.067, -5.51), (-29.984, -6.568), (-28.688, -7.393), (-27.189, -7.928), (-25.497, -8.118), (-24.11, -8.036), (-22.612, -7.7), (-21.05, -6.981), (-19.471, -5.747), (-16.924, -8.289), (-18.999, -9.923), (-21.07, -10.991), (-23.208, -11.569)]
            c = [(-5.838, -11.747), (-8.704, -11.552), (-11.179, -10.95), (-13.329, -9.919), (-15.22, -8.436), (-12.66, -5.909), (-11.424, -6.969), (-9.974, -7.688), (-8.156, -8.097), (-5.818, -8.226), (-3.932, -8.12), (-2.086, -7.654), (-1.305, -7.217), (-0.684, -6.608), (-0.275, -5.798), (-0.127, -4.761), (-0.388, -3.728), (-1.163, -2.979), (-2.444, -2.445), (-4.221, -2.061), (-7.391, -1.536), (-9.025, -1.178), (-10.405, -0.711), (-11.553, -0.144), (-12.49, 0.517), (-13.304, 1.371), (-13.88, 2.378), (-14.223, 3.544), (-14.336, 4.878), (-14.159, 6.354), (-13.647, 7.688), (-12.832, 8.861), (-11.746, 9.858), (-10.421, 10.663), (-8.888, 11.258), (-7.178, 11.627), (-5.324, 11.754), (-2.952, 11.585), (-0.869, 11.069), (1.031, 10.195), (2.853, 8.95), (0.295, 6.279), (-1.055, 7.197), (-2.462, 7.81), (-3.972, 8.152), (-5.628, 8.258), (-7.667, 8.024), (-9.265, 7.349), (-9.862, 6.859), (-10.306, 6.276), (-10.583, 5.603), (-10.679, 4.847), (-10.446, 3.744), (-9.74, 2.86), (-8.552, 2.192), (-6.872, 1.74), (-3.299, 1.112), (-0.645, 0.495), (0.52, 0.079), (1.538, -0.464), (2.38, -1.176), (3.018, -2.098), (3.422, -3.273), (3.563, -4.741), (3.392, -6.295), (2.887, -7.668), (2.055, -8.866), (0.908, -9.897), (-0.458, -10.698), (-2.054, -11.277), (-3.856, -11.629)]
            e = [(16.362, -11.754), (14.025, -11.546), (11.908, -10.937), (10.037, -9.948), (8.442, -8.6), (7.152, -6.915), (6.194, -4.914), (5.599, -2.619), (5.394, -0.051), (5.582, 2.375), (6.13, 4.607), (7.014, 6.605), (8.017, 8.053), (15.744, 8.053), (14.12, 7.868), (12.777, 7.367), (11.691, 6.627), (10.841, 5.727), (10.205, 4.745), (9.761, 3.76), (9.361, 2.092), (22.087, 2.092), (21.696, 3.76), (21.258, 4.745), (20.629, 5.727), (19.785, 6.627), (18.705, 7.367), (17.365, 7.868), (15.744, 8.053), (8.017, 8.053), (8.207, 8.328), (9.686, 9.737), (11.426, 10.793), (13.402, 11.456), (15.589, 11.685), (17.73, 11.466), (19.731, 10.819), (21.538, 9.756), (23.103, 8.293), (24.373, 6.444), (25.299, 4.221), (25.828, 1.641), (25.91, -1.285), (9.308, -1.283), (9.483, -2.872), (9.902, -4.279), (10.536, -5.496), (11.354, -6.512), (12.326, -7.318), (13.42, -7.906), (14.608, -8.265), (15.858, -8.387), (17.681, -8.237), (19.388, -7.781), (20.939, -7.009), (22.294, -5.91), (24.809, -8.459), (22.974, -9.984), (21.014, -11.004), (18.839, -11.575)]
            m = [(28.327, -11.724), (28.327, 1.596), (28.566, 4.323), (29.001, 6.057), (29.765, 7.641), (31.107, 9.224), (32.829, 10.525), (33.829, 11.027), (34.92, 11.407), (36.099, 11.647), (37.366, 11.731), (39.432, 11.49), (41.309, 10.77), (42.914, 9.575), (43.589, 8.8), (44.165, 7.909), (44.74, 8.8), (45.415, 9.575), (47.019, 10.77), (48.894, 11.49), (50.958, 11.731), (52.225, 11.647), (53.405, 11.407), (54.496, 11.027), (55.496, 10.525), (57.218, 9.224), (58.557, 7.642), (59.324, 6.057), (59.76, 4.323), (60.0, 1.596), (60.0, -11.724), (55.983, -11.724), (55.982, 1.442), (55.721, 3.985), (55.377, 5.11), (54.874, 6.098), (54.2, 6.918), (53.345, 7.541), (52.295, 7.937), (51.04, 8.076), (49.801, 7.935), (48.775, 7.533), (47.945, 6.903), (47.299, 6.076), (46.822, 5.085), (46.498, 3.961), (46.257, 1.442), (46.257, -11.724), (42.067, -11.724), (42.067, 1.442), (41.826, 3.961), (41.503, 5.085), (41.025, 6.076), (40.379, 6.903), (39.549, 7.533), (38.522, 7.935), (37.283, 8.076), (36.029, 7.937), (34.98, 7.541), (34.124, 6.918), (33.451, 6.098), (32.948, 5.11), (32.603, 3.985), (32.341, 1.442), (32.341, -11.724)]
            nd.Polygon(points=dot1, layer=self.text_layer).put(0, 0, 0)
            nd.Polygon(points=dot2, layer=self.text_layer).put(0, 0, 0)
            nd.Polygon(points=dot3, layer=self.text_layer).put(0, 0, 0)
            nd.Polygon(points=dot4, layer=self.text_layer).put(0, 0, 0)
            nd.Polygon(points=s, layer=self.text_layer).put(0, 0, 0)
            nd.Polygon(points=c, layer=self.text_layer).put(0, 0, 0)
            nd.Polygon(points=e, layer=self.text_layer).put(0, 0, 0)
            nd.Polygon(points=m, layer=self.text_layer).put(0, 0, 0)
        return cell

    def put(self, *args, **kwargs):
        return self._cell.put(*args, **kwargs)


class ELENALogo:
    cell_name = "ELENALogo"
    number = 0

    def __init__(self, text_layer=None):
        self.text_layer = text_layer if text_layer is not None else "lay125"

        # create the gds
        self._cell = self.create_gds()

    def create_gds(self):
        ELENALogo.number += 1
        with nd.Cell(name=ELENALogo.cell_name + "_" + str(ELENALogo.number)) as cell:
            e1 = [(-21.891, -7.281), (-22.314, -7.106), (-22.488, -6.683), (-22.488, 1.232), (-22.314, 1.654), (-21.891, 1.829), (-19.54, 1.829), (-19.34, 1.746), (-19.257, 1.546), (-19.257, 1.514), (-19.341, 1.314), (-19.54, 1.232), (-21.592, 1.232), (-21.804, 1.144), (-21.891, 0.933), (-21.891, -2.035), (-21.722, -2.203), (-19.591, -2.203), (-19.384, -2.289), (-19.298, -2.496), (-19.298, -2.508), (-19.383, -2.715), (-19.59, -2.8), (-21.722, -2.8), (-21.891, -2.969), (-21.891, -6.385), (-21.804, -6.596), (-21.592, -6.683), (-19.54, -6.683), (-19.34, -6.766), (-19.257, -6.966), (-19.257, -6.998), (-19.341, -7.198), (-19.54, -7.281)]
            l = [(-12.578, -7.281), (-12.612, -7.28), (-16.589, -7.28), (-17.091, -7.091), (-17.336, -6.597), (-17.336, 1.495), (-17.209, 1.715), (-16.973, 1.813), (-16.756, 1.727), (-16.664, 1.513), (-16.664, -6.391), (-16.572, -6.6), (-16.359, -6.683), (-12.612, -6.683), (-12.403, -6.784), (-12.314, -6.999), (-12.388, -7.195)]
            e2 = [(-10.146, -7.281), (-10.584, -7.1), (-10.765, -6.662), (-10.765, 1.21), (-10.584, 1.648), (-10.146, 1.829), (-6.155, 1.829), (-5.824, 1.692), (-5.687, 1.362), (-5.687, 1.326), (-5.824, 0.995), (-6.155, 0.858), (-9.41, 0.859), (-9.629, 0.768), (-9.72, 0.549), (-9.72, -1.899), (-9.565, -2.054), (-6.265, -2.054), (-5.935, -2.191), (-5.798, -2.521), (-5.798, -2.557), (-5.935, -2.888), (-6.265, -3.024), (-9.564, -3.024), (-9.72, -3.179), (-9.72, -6.001), (-9.629, -6.219), (-9.411, -6.31), (-6.155, -6.31), (-5.824, -6.447), (-5.687, -6.777), (-5.687, -6.813), (-5.824, -7.144), (-6.155, -7.281)]
            n = [(-3.077, -7.305), (-3.552, -7.108), (-3.749, -6.633), (-3.749, 0.663), (-3.659, 1.111), (-3.412, 1.477), (-3.046, 1.724), (-2.598, 1.814), (-2.597, 1.814), (-2.035, 1.668), (-1.616, 1.265), (2.491, -5.414), (2.612, -5.414), (2.564, -4.368), (2.526, -2.962), (2.526, 1.145), (2.723, 1.62), (3.198, 1.817), (3.674, 1.62), (3.87, 1.144), (3.871, -6.153), (3.78, -6.601), (3.533, -6.967), (3.168, -7.213), (2.72, -7.304), (2.154, -7.157), (1.733, -6.75), (-2.344, -0.038), (-2.522, -0.038), (-2.491, -0.443), (-2.405, -2.564), (-2.405, -6.632), (-2.602, -7.108)]
            a = [(5.946, -7.266), (5.506, -7.238), (5.191, -7.065), (5.066, -6.727), (5.066, -6.688), (5.221, -6.315), (5.594, -6.161), (5.6, -6.161), (6.182, -5.963), (6.598, -5.266), (8.891, 0.334), (9.339, 1.305), (9.807, 1.71), (10.343, 1.834), (10.405, 1.84), (10.479, 1.84), (10.539, 1.835), (11.077, 1.71), (11.545, 1.305), (11.993, 0.334), (14.286, -5.266), (14.703, -5.963), (15.285, -6.161), (15.291, -6.161), (15.662, -6.316), (15.816, -6.688), (15.816, -6.727), (15.692, -7.065), (15.377, -7.238), (14.937, -7.266), (14.312, -7.176), (13.822, -6.909), (13.427, -6.416), (13.087, -5.651), (10.891, -0.138), (10.522, 0.534), (10.518, 0.537), (10.36, 0.534), (9.991, -0.138), (8.365, -4.219), (10.676, -4.219), (11.075, -4.361), (11.285, -4.728), (11.292, -4.817), (11.116, -5.239), (10.694, -5.414), (7.89, -5.414), (7.796, -5.651), (7.457, -6.416), (7.061, -6.909), (6.571, -7.177)]
            extra1 = [(17.765, -1.808), (17.171, -1.724), (16.704, -1.471), (16.317, -0.99), (15.961, -0.223), (13.687, 5.51), (13.269, 6.305), (12.821, 6.533), (12.821, 6.534), (12.566, 6.639), (12.459, 6.894), (12.459, 6.926), (12.543, 7.158), (12.758, 7.279), (13.149, 7.305), (13.681, 7.182), (14.081, 6.796), (14.51, 5.896), (16.824, 0.089), (17.333, -0.819), (17.93, -1.031), (18.056, -1.031), (18.326, -1.133), (18.445, -1.397), (18.445, -1.411), (18.352, -1.658), (18.12, -1.784)]
            extra2 = [(17.876, -0.374), (17.6, 0.214), (17.583, 0.257), (18.898, 2.606), (19.17, 1.941)]
            extra3 = [(21.942, -1.824), (21.379, -1.685), (20.956, -1.244), (20.445, -0.138), (17.892, 6.113), (17.589, 6.662), (17.241, 6.827), (17.101, 6.82), (16.865, 7.007), (16.863, 7.03), (17.019, 7.235), (17.401, 7.285), (17.789, 7.202), (18.075, 6.953), (18.315, 6.513), (20.938, 0.129), (21.386, -0.888), (21.677, -1.248), (22.032, -1.357), (22.238, -1.347), (22.487, -1.542), (22.489, -1.571), (22.315, -1.791)]
            extra4 = [(19.996, 3.418), (19.72, 4.082), (21.438, 7.144), (21.682, 7.287), (21.817, 7.252), (21.95, 7.084), (21.926, 6.871)]
            elena = [e1, l, e2, n, a, extra1, extra2, extra3, extra4]
            for letter in elena:
                nd.Polygon(points=letter, layer=self.text_layer).put(0, 0, 0)
        return cell

    def put(self, *args, **kwargs):
        return self._cell.put(*args, **kwargs)


class Border:
    cell_name = "Border"
    text_offset = 20
    number = 0
    CSEM_logo = CSEMLogo()
    ELENA_logo = ELENALogo()

    def __init__(self, chip_size_x=None, chip_size_y=None, extra_size=None, radius=None, layer_border=None, number=None, text_bottom=None, text_top=None, text_layer=None):
        self.chip_size_x = chip_size_x if chip_size_x is not None else 5000
        self.chip_size_y = chip_size_y if chip_size_y is not None else 5000
        self.extra_size = extra_size if extra_size is not None else 150.0
        self.radius = radius if radius is not None else 200.0
        self.number = number if number is not None else 25
        self.layer_border = layer_border if layer_border is not None else "lay1"
        self.text_bottom = text_bottom if text_bottom is not None else "text_bottom"
        self.text_top = text_top if text_top is not None else "text_top"
        self.text_layer = text_layer if text_layer is not None else "lay200"

        # calculate parameter
        self.border_x = self.chip_size_x / 2 - self.radius
        self.border_y = self.chip_size_y / 2 - self.radius
        self.full_size_x = self.extra_size*2 + self.chip_size_x
        self.full_size_y = self.extra_size*2 + self.chip_size_y
        self._cell = self.create_gds()

    def create_gds(self):
        Border.number += 1
        with nd.Cell(name=Border.cell_name+"_"+str(Border.number)) as cell:
            square = [(-self.full_size_x / 2, 0), (-self.full_size_x / 2, self.full_size_y / 2), (self.full_size_x / 2, self.full_size_y / 2), (self.full_size_x / 2, -self.full_size_y / 2), (-self.full_size_x / 2, -self.full_size_y / 2), (-self.full_size_x / 2, 0)]
            old_circle = nd.geometries.circle(radius=self.radius, N=self.number * 4)
            circle = []
            for offset, x, y in ([(3, -self.border_x, self.border_y), (0, self.border_x, self.border_y), (1, self.border_x, -self.border_y), (2, -self.border_x, -self.border_y)]):
                circle += [(old_circle[index + offset * self.number][0] + x, old_circle[index + offset * self.number][1] + y) for index in range(self.number)]

                # add before and after point for safety
                index_extra = (offset+1) * self.number
                circle += [(old_circle[index_extra][0] + x, old_circle[index_extra][1] + y)]

            nd.Polygon(points=square + [(-self.chip_size_x / 2, 0)] + circle[::-1] + [(-self.chip_size_x / 2, 0)], layer=self.layer_border).put()
            text_height = 120
            nd.Font('cousine').text(text=self.text_bottom, height=text_height, align='cb', layer=self.text_layer).put(0, -self.chip_size_y / 2+self.text_offset)
            nd.Font('cousine').text(text=self.text_top, height=text_height, align='ct', layer=self.text_layer).put(0, self.chip_size_y / 2 - self.text_offset)

            # add the logo of CSEM and ELENA logo
            Border.CSEM_logo.put(self.chip_size_x/2-self.radius-300, self.chip_size_y / 2 - self.text_offset - text_height/2, scale= 5)
            Border.ELENA_logo.put(-(self.chip_size_x/2-self.radius-300), self.chip_size_y / 2 - self.text_offset - text_height/2, scale= 10)
        return cell

    def put(self, *args, **kwargs):
        return self._cell.put(*args, **kwargs)


# Border().put()
# nd.export_gds(filename="test.gds")