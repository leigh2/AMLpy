from event import event
from skyobj import skyobj
from uncertainties import ufloat


lensRa = ufloat(176.4549073,0.17862226 / (1000.0*3600.0))
lensDec = ufloat(-64.84295714,0.22230826 / (1000.0*3600.0))
lensPmra = ufloat(2662.03572627,0.15470192)
lensPmdec = ufloat(-345.18255501,0.15334393)
lensParallax = ufloat(215.782333,0.2727838)
lensMass = ufloat(0.61,0.01)
lensDist = ufloat(4.63,0.03)



sourceRa = ufloat(176.46360456,1.54734795 / (1000.0*3600.0))
sourceDec = ufloat(-64.84329779,2.29809596 / (1000.0*3600.0))
sourcePmra = ufloat(-14.0,3.0)
sourcePmdec = ufloat(-2.0,3.0)


lens = skyobj(1,lensRa,lensDec,lensPmra,lensPmdec,2015.0,parallax=lensParallax)
source = skyobj(2,sourceRa,sourceDec,sourcePmra,sourcePmdec,2015.0,parallax=None)

MicroEvent = event(lens,source,lensMass,lensDist)

#print(MicroEvent.get_time_of_minSep())
#print(MicroEvent.get_min_sep())
#print(MicroEvent.get_max_resolved_centroid_shift())
#print(MicroEvent.get_resolved_centroid_shift_at_epoch(2018.0))

