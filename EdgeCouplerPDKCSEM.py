import nazca as nd
from enum import *


class EdgeCoupler(Enum):
    NONE = 0
    SINGLE = 1
    DOUBLE = 2


class EdgeCouplerDoubleTapper:
    cell_name = "EdgeCouplerDoubleTapper"
    number = 0  # number of instant initiated

    def __init__(self, cs_waveguide, width1, width3, width_top_tapper, length1, length2, length3, length_back_extend=None, length_front_extend=None, width2=None, width_opening=None, layer_opening=None, layer_second_etch=None):
        self.cs_waveguide = cs_waveguide
        self.width1 = width1
        self.width3 = width3
        self.width_top_tapper = width_top_tapper
        self.length1 = length1
        self.length2 = length2
        self.length3 = length3
        self.length_back_extend = length_back_extend if length_back_extend is not None else 10
        self.length_front_extend = length_front_extend if length_front_extend is not None else 5
        self.width_opening = width_opening if width_opening is not None else 50
        self.layer_opening = layer_opening if layer_opening is not None else "lay25"
        self.layer_second_etch = layer_second_etch if layer_second_etch is not None else "lay130"

        # calculate parameter
        self.length = self.length_front_extend/2+self.length1+self.length2+self.length3+self.length_back_extend
        if width2 is None:
            # fit the waveguide slope
            slope_first_waveguide = ((self.cs_waveguide.width-self.width_top_tapper)/2) / self.length2
            self.width2 = (self.width1/2+slope_first_waveguide*(self.length1+self.length2))*2
        else:
            self.width2 = width2

        # create the gds
        self._cell = self.create_gds()

    def create_gds(self):
        EdgeCouplerDoubleTapper.number += 1
        with nd.Cell(name=EdgeCouplerDoubleTapper.cell_name+"_"+str(EdgeCouplerDoubleTapper.number)) as cell:
            # first waveguide
            waveguide = self.cs_waveguide.strt(length=self.length_back_extend+self.length3, arrow=False).put(0, 0, 0)
            self.cs_waveguide.taper(length=self.length2, width2=self.width_top_tapper, arrow=False).put()

            # second waveguide
            nd.strt(length=self.length_back_extend, width=self.width3, layer=self.layer_second_etch).put(0, 0)
            nd.taper(length=self.length3, width1=self.width3, width2=self.width2, layer=self.layer_second_etch).put()
            nd.taper(length=self.length2+self.length1, width1=self.width2, width2=self.width1, layer=self.layer_second_etch).put()
            front_extend = nd.strt(length=self.length_front_extend, width=self.width1, layer=self.layer_second_etch).put()

            # opening
            nd.strt(length=self.length1+self.length2+self.length3+self.length_front_extend, width=self.width_opening, layer=self.layer_opening).put(self.length_back_extend, 0)

            # create pin
            nd.Pin('a0', pin=front_extend.pin['b0'].rot2ref().move(-self.length_front_extend/2, 0, 0), width=0).put()
            nd.Pin('b0', pin=waveguide.pin['a0'], width=0).put()
            nd.put_stub()
        return cell

    def put(self, *args, **kwargs):
        return self._cell.put(*args, **kwargs)

# EdgeCouplerDoubleTapper(cs["1.5"], 0.175, 5, 0.05, 20, 20, 10, width_opening=20).put()
# nd.export_gds(filename="test.gds")


class EdgeCouplerSingleTapper:
    cell_name = "EdgeCouplerSingleTapper"
    number = 0  # number of instant initiated

    def __init__(self, cs_waveguide, length, width, length_front_extend=None):
        self.cs_waveguide = cs_waveguide
        self.width = width
        self.length = length
        self.length_front_extend = length_front_extend if length_front_extend is not None else 5
        self.full_length = self.length_front_extend/2+self.length

        # create the gds
        self._cell = self.create_gds()

    def create_gds(self):
        EdgeCouplerDoubleTapper.number += 1
        with nd.Cell(name=EdgeCouplerDoubleTapper.cell_name+"_"+str(EdgeCouplerDoubleTapper.number)) as cell:
            # first waveguide
            waveguide = self.cs_waveguide.taper(length=self.length, width2=self.width, arrow=False).put(0, 0, 0)
            front_extend = self.cs_waveguide.strt(length=self.length_front_extend, width=self.width, arrow=False).put()

            # create pin
            nd.Pin('a0', pin=front_extend.pin['b0'].rot2ref().move(-self.length_front_extend / 2, 0, 0), width=0).put()
            nd.Pin('b0', pin=waveguide.pin['a0'], width=0).put()
            nd.put_stub()
        return cell

    def put(self, *args, **kwargs):
        return self._cell.put(*args, **kwargs)


# EdgeCouplerSingleTapper(cs["1.0"], 25, 0.2).put()
# nd.export_gds(filename="test.gds")


class EdgeCouplerNoneTapper:
    cell_name = "EdgeCouplerNoneTapper"
    number = 0  # number of instant initiated

    def __init__(self, cs_waveguide, length, length_front_extend=None):
        self.cs_waveguide = cs_waveguide
        self.length = length
        self.length_front_extend = length_front_extend if length_front_extend is not None else 5
        self.full_length = self.length_front_extend/2+self.length

        # create the gds
        self._cell = self.create_gds()

    def create_gds(self):
        EdgeCouplerNoneTapper.number += 1
        with nd.Cell(name=EdgeCouplerNoneTapper.cell_name+"_"+str(EdgeCouplerNoneTapper.number)) as cell:
            # first waveguide
            waveguide = self.cs_waveguide.strt(length=self.length, arrow=False).put(0, 0, 0)
            front_extend = self.cs_waveguide.strt(length=self.length_front_extend, arrow=False).put()

            # create pin
            nd.Pin('a0', pin=front_extend.pin['b0'].rot2ref().move(-self.length_front_extend / 2, 0, 0), width=0).put()
            nd.Pin('b0', pin=waveguide.pin['a0'], width=0).put()
            nd.put_stub()
        return cell

    def put(self, *args, **kwargs):
        return self._cell.put(*args, **kwargs)

# EdgeCouplerNoneTapper(cs["1000"], 200).put()
# nd.export_gds(filename="test.gds")
