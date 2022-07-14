import nazca as nd
import numpy as np
from enum import Enum
from scipy.special import fresnel
from scipy.optimize import minimize


class Bend(Enum):
    S_BEND = 0
    EULER = 2
    ARC = 3


def xy_euler2(cs, angle, radius):
    euler2 = cs.euler2(angle=angle, radius=radius)
    input_xya = euler2.pin["a0"].xya()
    output_xya = euler2.pin["b0"].xya()
    return output_xya[0]-input_xya[0], output_xya[1]-input_xya[1]


class SBendEuler:
    cell_name = "SBendEuler"
    number = 0  # number of instant initiated

    def __init__(self, cs_waveguide, offset, max_angle=None, radius=None, arrow=False, length=None):
        self.cs_waveguide = cs_waveguide
        self.offset = offset
        self.radius = self.cs_waveguide.radius if radius is None else radius
        self.max_angle = max_angle if max_angle is not None else 90
        self.arrow = arrow
        self.length = length
        self.pin = {}

        # create the gds
        self._cell = self.create_gds()

    def create_gds(self):
        SBendEuler.number += 1
        with nd.Cell(name=SBendEuler.cell_name+"_"+str(SBendEuler.number)) as cell:
            length_x, length_y = xy_euler2(self.cs_waveguide, self.max_angle, self.radius)
            if self.offset > 2*length_y:
                euler1 = self.cs_waveguide.euler2(radius=self.radius, angle=self.max_angle, arrow=self.arrow).put()
                self.cs_waveguide.strt((self.offset-2*length_y)/np.sin(np.radians(self.max_angle))).put()
                euler2 = self.cs_waveguide.euler2(radius=self.radius, angle=self.max_angle, arrow=self.arrow).put("b0")
            else:
                # find minimum of euler
                def minimize_euler_angle_equation_spacing(angle):
                    length_x, length_y = xy_euler2(self.cs_waveguide, angle, self.radius)
                    return np.power(length_y - self.offset/2, 2)

                def minimize_euler_angle_equation_spacing_length(angle, radius):
                    length_x, length_y = xy_euler2(self.cs_waveguide, angle, radius)
                    return np.power(length_y - self.offset/2, 2) + np.power(length_x - self.offset/2, 2)

                if self.offset != 0:
                    if self.length is None:
                        _angle = minimize(minimize_euler_angle_equation_spacing, self.max_angle).x
                    else:
                        # TODO
                        _angle, _radius = minimize(minimize_euler_angle_equation_spacing_length, [self.max_angle, self.radius], method='Nelder-Mead').x

                    euler1 = self.cs_waveguide.euler2(angle=_angle, radius=self.radius, arrow=self.arrow).put()
                    euler2 = self.cs_waveguide.euler2(angle=_angle, radius=self.radius, arrow=self.arrow).put("b0")
                else:
                    euler1 = self.cs_waveguide.strt(length=0, arrow=self.arrow).put()
                    euler2 = self.cs_waveguide.strt(length=0, arrow=self.arrow).put("b0")

            # create pin
            self.pin["a0"] = nd.Pin('a0', pin=euler1.pin['a0'], width=0).put()
            self.pin["b0"] = nd.Pin('b0', pin=euler2.pin['a0'], width=0).put()
        return cell

    def put(self, *args, **kwargs):
        return self._cell.put(*args, **kwargs)

# from LayerPDKCSEM import *
# SBendEuler(cs["0.8"], 200, arrow=True).put()
# nd.export_gds(filename="test.gds")


# TODO add euler bend with angle different than 90
class StrtEuler2Strt:
    cell_name = "StrtEuler2Strt"
    number = 0  # number of instant initiated

    def __init__(self, cs_waveguide, pin1, pin2, radius=None):
        self.cs_waveguide = cs_waveguide
        self.radius = self.cs_waveguide.radius if radius is None else radius
        self.pin1 = pin1
        self.pin2 = pin2

        # create the gds
        self._cell = self.create_gds()

    def create_gds(self):
        StrtEuler2Strt.number += 1
        with nd.Cell(name=StrtEuler2Strt.cell_name+"_"+str(StrtEuler2Strt.number)) as cell:
            length_x, length_y = xy_euler2(self.cs_waveguide, 90, self.radius)

            xya1 = self.pin1.xya()
            xya2 = self.pin2.xya()

            # connect them
            self.cs_waveguide.strt(length=np.abs(xya2[0] - xya1[0]) - length_y).put()
            self.cs_waveguide.euler2(radius=self.radius, angle=90).put()
            self.cs_waveguide.strt(length=np.abs(xya2[1] - xya1[1]) - length_y).put()
        return cell

    def put(self, *args, **kwargs):
        return self._cell.put(self.pin1, *args, **kwargs)
