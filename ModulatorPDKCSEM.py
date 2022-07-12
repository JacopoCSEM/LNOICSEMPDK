import nazca as nd


class MZI:
    cell_name = "EdgeCouplerDoubleTapper"
    number = 0  # number of instant initiated

    def __init__(self, cs_waveguide, width_top_1=130, width_top_2=130, width_top_3=60, width_top_4=45, width_top_5=60, width_top_6=12, spacing_top_1=20, spacing_top_2=5.8, length_top= 555, layer_metal_2=None):
        self.cs_waveguide = cs_waveguide
        self.width_top_1 = width_top_1
        self.width_top_2 = width_top_2
        self.width_top_3 = width_top_3
        self.width_top_4 = width_top_4
        self.width_top_5 = width_top_5
        self.width_top_6 = width_top_6
        self.spacing_top_1 = spacing_top_1
        self.spacing_top_2 = spacing_top_2
        self.length_top = length_top
        self.layer_opening = layer_metal_2 if layer_metal_2 is not None else "lay25"

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


# from LayerPDKCSEM import *
# EdgeCouplerDoubleTapper(cs["0.8"], 0.175, 3.8, 0.05, 100, 100, 20, width_opening=20).put()
# nd.export_gds(filename="test.gds")