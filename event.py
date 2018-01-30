#####################
# A class to simulate 
# a microlensing event
# @author P.McGill
#####################


import numpy as numpy
import uncertainties.umath as np
from scipy.optimize import minimize_scalar
from skyobj import skyobj
from uncertainties import ufloat

class event(object):

	def __init__(self,lens,source,lensMass,lensDist):

		self._lens = lens
		self._source = source
		self._lensMass = lensMass
		self._lesDist = lensDist

	

	def get_time_of_minSep(self):
		"""Gets time of closest approach in Julian Years
		"""

		minimum = minimize_scalar(self._lens.getSepNum,
			args=(self._source),bounds=(1901.0,2099.0))
		return minimum.x

	def get_min_sep(self):
		"""Returns minimum Separation
		"""

		minTime = self.get_time_of_minSep()
		return self._lens.getSep(minTime,self._source)



lensRa = ufloat(176.4549073,0.17862226 / (1000.0*3600.0))
lensDec = ufloat(-64.84295714,0.22230826 / (1000.0*3600.0))
lensPmra = ufloat(2662.03572627,0.15470192)
lensPmdec = ufloat(-345.18255501,0.15334393)
lensParallax = ufloat(215.782333,0.2727838)

sourceRa = ufloat(176.46360456,1.54734795 / (1000.0*3600.0))
sourceDec = ufloat(-64.84329779,2.29809596 / (1000.0*3600.0))
sourcePmra = ufloat(-14.0,3.0)
sourcePmdec = ufloat(-2.0,3.0)


lens = skyobj(1,lensRa,lensDec,lensPmra,lensPmdec,2015.0,parallax=lensParallax)
source = skyobj(2,sourceRa,sourceDec,sourcePmra,sourcePmdec,2015.0,parallax=None)


MicroEvent = event(lens,source,0.0,0.0)

print(MicroEvent.get_time_of_minSep())
print(MicroEvent.get_min_sep())
print(lens.getRaDec(2016.0))
print(source.getRaDec(2016.0))

