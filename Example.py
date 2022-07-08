from LayerPDKCSEM import *
from ResonatorPDKCSEM import *
from CouplerPDKCSEM import *
from EdgeCouplerPDKCSEM import *

cross_section = cs["0.8"]  # cross section already created, you can create yours (example in LayerPDKCSEM)

# create the edge coupler (From CSEM)
edge_coupler = EdgeCouplerDoubleTapper(cs_waveguide=cross_section, width1=0.175, width3=3.8, width_top_tapper=0.05,
                                       length1=100, length2=100, length3=20)

# put the edge coupler with (0,0,0) which correspond  to (x, y, angle) as position
edge_coupler.put(0, 0, 0)

# Add a directional coupler (From CSEM) and put to entry pin "a1"
directional_coupler = DirectionalCoupler(cs_waveguide=cross_section, length=100, gap=1, spacing=30)
directional_coupler_put = directional_coupler.put("a1")

# put a straight length (From Interconnect # Nazca cross_section) and put to direction coupler exit b1
straight_waveguide = cross_section.strt(length=150)
straight_waveguide.put(directional_coupler_put.pin["b0"])

# Add Resonator and put to direction coupler exit b1
resonator = Resonator(cs_bus_waveguide=cross_section, cs_resonator_waveguide=cross_section, radius=150, gap=1)
resonator_put = resonator.put()

# put 2 edge couplers at position (850, 400, -90)
edge_coupler_output1_put = edge_coupler.put(850, 400, -90)
edge_coupler_output2_put = edge_coupler.put(900, 400, -90)

# connect with semi-autorouting strt-bend-strt (From Interconnect # Nazca cross_section)
# directional coupler pin b1 and edge_coupler_output1
cross_section.strt_bend_strt_p2p(directional_coupler_put.pin["b1"], edge_coupler_output1_put.pin["b0"]).put()
# connect with semi-autorouting strt-euler2-strt (From CSEM) resonator pin b0 and edge_coupler_output2
StrtEuler2Strt(cs_waveguide=cross_section, pin1=resonator_put.pin["b0"], pin2=edge_coupler_output2_put.pin["b0"]).put(resonator_put.pin["b0"])

# save in GDS
nd.export_gds(filename="test.gds")

