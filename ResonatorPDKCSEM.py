try:
    from EulerPDKCSEM import *
except:
    from .EulerPDKCSEM import *


class Resonator:
    length = 10
    cell_name = "Resonator"
    number = 0
    intra_length = 10

    def __init__(self, cs_bus_waveguide, cs_resonator_waveguide, radius, gap, angle=None, text_layer=None, length_straight=None, bend=None, is_text_enabled=None):
        self.cs_bus_waveguide = cs_bus_waveguide
        self.cs_resonator_waveguide = cs_resonator_waveguide
        self.angle = angle if angle is not None else 0
        self.radius = radius
        self.gap = gap
        self.text_layer = text_layer if text_layer is not None else "lay125"
        self.length_straight = length_straight if length_straight is not None else 0
        self.bend = bend if bend is not None else Bend.ARC
        self.is_text_enabled = is_text_enabled if is_text_enabled is not None else False

        # calculate new parameter
        self.width_bus_waveguide = self.cs_bus_waveguide.width
        self.width_resonator_waveguide = self.cs_resonator_waveguide.width
        self.total_gap = self.gap + self.width_bus_waveguide / 2 + self.width_resonator_waveguide / 2
        self.external_radius = self.radius + self.total_gap

        # create the gds
        self._cell = self.create_gds()

    def create_gds(self):
        Resonator.number += 1
        with nd.Cell(name=self.cell_name + "_" + str(Resonator.number)) as cell:
            if self.angle != 0:
                ## TODO angle with euler bend
                bus_waveguide_bend = self.cs_bus_waveguide.euler if self.bend is Bend.EULER else self.cs_bus_waveguide.bend
                # first part of the bend
                middle_structure = self.cs_bus_waveguide.bend(angle=self.angle / 2, radius=self.external_radius).put(0, 0, -90)
                self.cs_bus_waveguide.euler(angle=-self.angle / 2).put()
                input_resonator_straight = self.cs_bus_waveguide.strt(length=self.length).put()
                # second part of the bend
                self.cs_bus_waveguide.bend(angle=-self.angle / 2, radius=self.external_radius).put(middle_structure.pin["a0"])
                self.cs_bus_waveguide.euler(angle=self.angle / 2).put()
                output_resonator_straight = self.cs_bus_waveguide.strt(length=self.length).put()
            else:
                input_resonator_straight = middle_structure = self.cs_bus_waveguide.strt(length=self.length).put(0, 0, -90)
                output_resonator_straight = self.cs_bus_waveguide.strt(length=self.length).put(input_resonator_straight.pin["a0"])

            # resonator
            resonator_waveguide_bend = self.cs_resonator_waveguide.euler if self.bend is Bend.EULER else self.cs_resonator_waveguide.bend
            resonator = resonator_waveguide_bend(angle=90, radius=self.radius).put("b0", middle_structure.pin["a0"].move(0, -self.total_gap, 0))
            self.cs_resonator_waveguide.strt(length=self.length_straight).put(resonator.pin["a0"])
            resonator_other_side = resonator_waveguide_bend(angle=-90, radius=self.radius).put()
            third_bend = resonator_waveguide_bend(angle=90, radius=self.radius).put("b0")
            self.cs_resonator_waveguide.strt(length=self.length_straight).put(third_bend.pin["a0"])
            resonator_waveguide_bend(angle=-90, radius=self.radius).put()

            if self.is_text_enabled is True:
                # add text to the middle to know that is the gap and radius
                length_total = self.length_straight * 2 + resonator_waveguide_bend(angle=90, radius=self.radius).length_geo * 4
                text = ""
                text += "angle = " + str(self.angle) + " degree" if self.angle != 0 else ""
                text += "\n gap = " + str(self.gap * 1000) + " nm"
                text += "\n len_str = " + str(self.length_straight) + " um" if self.length_straight != 0 else ""
                text += "\n len_tot = " + "{:.2f}".format(length_total) + " um"
                nd.Font('cousine').text(text=text, height=self.radius / 8, align='cc', layer=self.text_layer).put(resonator.pin["b0"].move(0, self.radius, 90))

            # add pins for connectivity:
            nd.Pin('a0', pin=input_resonator_straight.pin['b0'], width=0).put()
            nd.Pin('b0', pin=output_resonator_straight.pin['b0'], width=0).put()
            nd.Pin('c0', pin=resonator_other_side.pin['b0'], width=0).put()
            nd.put_stub()
        return cell

    def put(self, *args, **kwargs):
        return self._cell.put(*args, **kwargs)


# Resonator(cs["0.8"], cs["1.0"], 100, 1, angle=30, length_straight=100, is_text_enabled=False).put()
# nd.export_gds(filename="test.gds")





