import nazca as nd

# create layer
nd.add_layer(name='lay0', layer=0)  # PAYLOAD
nd.add_layer(name='lay1', layer=1)  # DEEP_GRID
nd.add_layer(name='lay2', layer=2)  # EFF_AREA
nd.add_layer(name='lay5', layer=5)  # ALMARK_PROTECT
nd.add_layer(name='lay10', layer=10)  # COUPON_CUT
nd.add_layer(name='lay25', layer=25)  # WG2_ACC
nd.add_layer(name='lay123', layer=123)  # WG1
nd.add_layer(name='lay125', layer=125)  # TXT_LOGO
nd.add_layer(name='lay130', layer=130)  # CLD_OPEN
nd.add_layer(name='lay200', layer=200)  # MET1
nd.add_layer(name='lay201', layer=201)  # TXT_LOGO_MET1
nd.add_layer(name='lay210', layer=210)  # MET2
# ...

# create cross-section
cs = {}
for _width in list(range(500, 1100, 100))+[1500, 2000, 2500]:
    _width /= 1000
    nd.add_xsection(str(_width))
    nd.add_layer2xsection(xsection=str(_width), layer="lay123")
    cs[str(_width)] = nd.interconnects.Interconnect(xs=str(_width), radius=50, width=_width, layer="lay123")

# cs["0.8"].euler2(radius=30, angle=90).put(0, 0, 0)
# # cs["0.8"].euler(radius=30, angle=45).put(0, 0, 0)
# cs["0.8"].bend(radius=50, angle=90).put(0, 0, 0)
# nd.export_gds(filename="test.gds")
