try:
    from EulerPDKCSEM import *
except:
    from .EulerPDKCSEM import *


class Coupler(Enum):
    Y_JUNCTION = 0
    MMI = 1
    DIRECTIONAL_COUPLER = 2


class YJunction:
    cell_name = "YJunction"
    number = 0  # number of instant initiated

    def __init__(self, cs_waveguide, length, gap, spacing=None, bend=None, max_angle=90):
        self.cs_waveguide = cs_waveguide
        self.length = length
        self.gap = gap
        self.width = self.cs_waveguide.width
        self.layer = self.cs_waveguide.layer
        self.spacing = spacing if spacing is not None else gap
        self.bend = bend if bend is not None else Bend.S_BEND
        self.max_angle = max_angle if max_angle is not None else 90

        # create the gds
        self._cell = self.create_gds()

    def create_gds(self):
        YJunction.number += 1
        with nd.Cell(name=YJunction.cell_name+"_"+str(YJunction.number)) as cell:
            waveguide = self.cs_waveguide.strt(length=0, arrow=False).put(0, 0, 0)
            points1 = [(0, self.width/2), (self.length, self.width/2 + self.gap/2), (self.length, -self.width/2 + self.gap/2), (0, -self.width/2)]
            points2 = [(0, self.width/2), (self.length, self.width/2 - self.gap/2), (self.length, -self.width/2 - self.gap/2), (0, -self.width/2)]

            nd.Polygon(points=points1, layer=self.cs_waveguide.layer).put(0, 0, 0)
            nd.Polygon(points=points2, layer=self.cs_waveguide.layer).put(0, 0, 0)

            if self.bend is Bend.S_BEND:
                bend = self.cs_waveguide.sbend(offset=(self.spacing - self.gap) / 2, Amax=self.max_angle, arrow=False)
            elif self.bend is Bend.EULER:
                bend = SBendEuler(self.cs_waveguide, (self.spacing - self.gap) / 2, max_angle=self.max_angle)
            output2 = bend.put(self.length, self.gap/2)
            output1 = bend.put(self.length, -self.gap/2, flip=True)

            # create pin
            nd.Pin('a0', pin=waveguide.pin["a0"], width=0).put()
            nd.Pin('b0', pin=output1.pin["b0"], width=0).put()
            nd.Pin('b1', pin=output2.pin["b0"], width=0).put()
            nd.put_stub()
        return cell

    def put(self, *args, **kwargs):
        return self._cell.put(*args, **kwargs)


# YJunction(cs["0.8"], 25, 2, spacing=15).put()
# nd.export_gds(filename="test.gds")


class MMI:
    cell_name = "MMI"
    number = 0  # number of instant initiated

    def __init__(self, cs_waveguide, length, width, width_tapper, length_tapper, gap, spacing=None, bend=None, max_angle=None, radius=None):
        self.cs_waveguide = cs_waveguide
        self.length = length
        self.width = width
        self.width_tapper = width_tapper
        self.length_tapper = length_tapper
        self.gap = gap
        self.spacing = spacing if spacing is not None else gap
        self.bend = bend if bend is not None else Bend.S_BEND
        self.max_angle = max_angle if max_angle is not None else 90
        self.radius = self.cs_waveguide.radius if radius is not None else radius

        # create the gds
        self._cell = self.create_gds()

    def create_gds(self):
        MMI.number += 1
        with nd.Cell(name=MMI.cell_name+"_"+str(MMI.number)) as cell:
            input1 = self.cs_waveguide.taper(length=self.length_tapper, width2=self.width_tapper, arrow=False).put(0, 0, 0)
            _MMI = self.cs_waveguide.strt(length=self.length, width=self.width, arrow=False).put()
            tapper1 = self.cs_waveguide.taper(length=self.length_tapper, width1=self.width_tapper, width2=self.cs_waveguide.width, arrow=False).put(_MMI.pin["b0"].move(0, self.gap/2))
            tapper2 = self.cs_waveguide.taper(length=self.length_tapper, width1=self.width_tapper, width2=self.cs_waveguide.width, arrow=False).put(_MMI.pin["b0"].move(0, -self.gap / 2))
            if self.bend is Bend.S_BEND:
                bend = self.cs_waveguide.sbend(offset=(self.spacing-self.gap)/2, Amax=self.max_angle, arrow=False, radius=self.radius)
            elif self.bend is Bend.EULER:
                bend = SBendEuler(self.cs_waveguide, (self.spacing - self.gap) / 2, max_angle=self.max_angle, radius=self.radius)
            output2 = bend.put(tapper1.pin["b0"])
            output1 = bend.put(tapper2.pin["b0"], flip=True)

            # create pin
            nd.Pin('a0', pin=input1.pin['a0'], width=0).put()
            nd.Pin('b0', pin=output1.pin['b0'], width=0).put()
            nd.Pin('b1', pin=output2.pin['b0'], width=0).put()
            nd.put_stub()
        return cell

    def put(self, *args, **kwargs):
        return self._cell.put(*args, **kwargs)


# MMI(cs["800"], 20.75, 5.25, 1.6, 15, 2.8, 15, bend=Bend.EULER).put()
# nd.export_gds(filename="test.gds")


class DirectionalCoupler:
    cell_name = "DirectionalCoupler"
    number = 0  # number of instant initiated

    def __init__(self, cs_waveguide, length, gap, spacing, radius=None, bend=None, max_angle=None):
        self.cs_waveguide = cs_waveguide
        # self.cs_waveguide = nd.interconnects.Interconnect(xs=str(800), radius=50, width=800/1000)
        self.length = length
        self.gap = gap
        self.spacing = spacing
        self.radius = radius if radius is not None else cs_waveguide.radius
        self.bend = bend if bend is not None else Bend.S_BEND
        self.max_angle = max_angle if max_angle is not None else 90  # only valid for euler and arc bend

        # create the gds
        self._cell = self.create_gds()

    def create_gds(self):
        DirectionalCoupler.number += 1
        with nd.Cell(name=DirectionalCoupler.cell_name+"_"+str(DirectionalCoupler.number)) as cell:
            waveguide_up = self.cs_waveguide.taper(length=self.length, arrow=False).put(0, self.gap/2+self.cs_waveguide.width/2)
            waveguide_down = self.cs_waveguide.taper(length=self.length, arrow=False).put(0, - (self.gap / 2 + self.cs_waveguide.width / 2))
            offset = (self.spacing - self.gap - self.cs_waveguide.width) / 2

            # create s_bend
            if self.bend is Bend.S_BEND:
                bend = self.cs_waveguide.sbend(radius=self.radius, offset=offset, arrow=False, Amax=self.max_angle)
            elif self.bend is Bend.EULER:
                bend = SBendEuler(self.cs_waveguide, offset, max_angle=self.max_angle, radius=self.radius)
            output2 = bend.put(waveguide_up.pin["b0"])
            input2 = bend.put(waveguide_up.pin["a0"], flip=True)
            output1 = bend.put(waveguide_down.pin["b0"], flip=True)
            input1 = bend.put(waveguide_down.pin["a0"])

            # create pin
            nd.Pin('a0', pin=input1.pin["b0"], width=0).put()
            nd.Pin('a1', pin=input2.pin["b0"], width=0).put()
            nd.Pin('b0', pin=output1.pin["b0"], width=0).put()
            nd.Pin('b1', pin=output2.pin["b0"], width=0).put()
            nd.put_stub()
        return cell

    def put(self, *args, **kwargs):
        return self._cell.put(*args, **kwargs)

# DirectionalCoupler(cs["800"], 100, 1, 100, bend=Bend.EULER, max_angle=50).put()
# DirectionalCoupler(cs["800"], 20, 2, 15, bend=Bend.S_BEND, max_angle=90).put()
# nd.export_gds(filename="test.gds")
