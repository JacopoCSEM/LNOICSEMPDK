import nazca as nd
import numpy as np
from enum import Enum
from scipy.special import fresnel
from scipy.optimize import minimize


class Bend(Enum):
    S_BEND = 0
    EULER = 2
    ARC = 3


def euler2_length_equation(angle, radius):
    _fresnel = fresnel(np.sqrt(abs((angle/2) * np.pi / 180) * 2.0 / np.pi))
    length = np.sqrt((np.power(_fresnel[0]*np.pi*radius, 2) + np.power(_fresnel[1]*np.pi*radius, 2)))
    _angle = np.arctan(_fresnel[0]/_fresnel[1])
    return length*np.sin(_angle) + length*np.sin(_angle*2+(angle/2) * np.pi / 180)


class SBendEuler:
    cell_name = "SBendEuler"
    number = 0  # number of instant initiated

    def __init__(self, cs_waveguide, offset, max_angle=None, radius=None):
        self.cs_waveguide = cs_waveguide
        self.offset = offset
        self.radius = self.cs_waveguide.radius if radius is None else radius
        self.max_angle = max_angle if max_angle is not None else 90
        self.pin = {}

        # create the gds
        self._cell = self.create_gds()

    def create_gds(self):
        SBendEuler.number += 1
        with nd.Cell(name=SBendEuler.cell_name+"_"+str(SBendEuler.number)) as cell:
            euler2_length = euler2_length_equation(self.max_angle, self.radius)
            if self.offset > 2*euler2_length:
                euler1 = self.cs_waveguide.euler2(radius=self.radius, angle=self.max_angle, arrow=False).put()
                self.cs_waveguide.strt((self.offset-2*euler2_length)/np.sin(np.radians(self.max_angle))).put()
                euler2 = self.cs_waveguide.euler2(radius=self.radius, angle=self.max_angle, arrow=False).put("b0")
            else:
                # find minimum of euler
                def minimize_euler_angle_equation(angle):
                    return np.power(euler2_length_equation(angle, self.radius) - self.offset/2, 2)

                if self.offset != 0:
                    _angle = minimize(minimize_euler_angle_equation, self.max_angle).x

                    euler1 = self.cs_waveguide.euler2(angle=_angle, radius=self.radius, arrow=False).put()
                    euler2 = self.cs_waveguide.euler2(angle=_angle, radius=self.radius, arrow=False).put("b0")
                else:
                    euler1 = self.cs_waveguide.strt(length=0, arrow=False).put()
                    euler2 = self.cs_waveguide.strt(length=0, arrow=False).put("b0")

            # create pin
            self.pin["a0"] = nd.Pin('a0', pin=euler1.pin['a0'], width=0).put()
            self.pin["b0"] = nd.Pin('b0', pin=euler2.pin['a0'], width=0).put()
        return cell

    def put(self, *args, **kwargs):
        return self._cell.put(*args, **kwargs)


# SBendEuler(cs["0.8"], 200).put()
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
            euler2_length = euler2_length_equation(90, self.radius)

            xya1 = self.pin1.xya()
            xya2 = self.pin2.xya()

            # connect them
            self.cs_waveguide.strt(length=np.abs(xya2[0] - xya1[0]) - euler2_length).put()
            self.cs_waveguide.euler2(radius=self.radius, angle=90).put()
            self.cs_waveguide.strt(length=np.abs(xya2[1] - xya1[1]) - euler2_length).put()
        return cell

    def put(self, *args):
        return self._cell.put(*args)
