import nazca as nd

# create layer
nd.add_layer(name='lay1', layer=1)  # DEEP_GRID
nd.add_layer(name='lay25', layer=25)  # WG2_ACC
nd.add_layer(name='lay123', layer=123)  # WG1
nd.add_layer(name='lay125', layer=125)  # TXT_LOGO
nd.add_layer(name='lay130', layer=130)  # CLD_OPEN
nd.add_layer(name='lay200', layer=200)  # MET1
# ...

# create cross-section
cs = {}
for _width in list(range(500, 1100, 100))+[1500, 2000, 2500]:
    _width /= 1000
    nd.add_xsection(str(_width))
    nd.add_layer2xsection(xsection=str(_width), layer="lay123")
    cs[str(_width)] = nd.interconnects.Interconnect(xs=str(_width), radius=50, width=_width, layer="lay123")
