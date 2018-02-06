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
import microlens as m

class event(object):

	def __init__(self,lens,source,lensMass,lensDist,sourceDist=None):

		self._lens = lens
		self._source = source
		self._lensMass = lensMass
		self._lensDist = lensDist
		self._sourceDist = sourceDist

	

	def get_time_of_minSep(self):
		"""Gets time of closest approach in Julian Years
		"""

		minimum = minimize_scalar(self._lens.getSepNum,
			args=(self._source),bounds=(2015,2025),method='bounded')
		return minimum.x

	def get_min_sep(self):
		"""Returns minimum Separation
		"""

		minTime = self.get_time_of_minSep()
		return self._lens.getSep(minTime,self._source)
	
	def get_sep(self,epoch):
		
		return self._lens.getSep(epoch,self._source)


	def get_einstein_R(self):
		"""Returns the Enstien Radius [mas]

		"""

		return m.get_einstein_R(self._lensMass,self._lensDist,sourceDist=self._sourceDist)



	def get_max_resolved_centroid_shift(self):
		"""Returns the centriod shift due to mmajor image only.

		"""

		MinSep = self.get_min_sep()		

		return m.get_centriod_shift_resolved(self._lensMass,
					self._lensDist,MinSep,sourceDist=self._sourceDist)



	def get_resolved_centroid_shift_at_epoch(self,epoch):
		"""Returns unresolved centriod shift at epoch [mas]
		"""

		sep = self._lens.getSep(epoch,self._source)
		
		return m.get_centriod_shift_resolved(self._lensMass,
                                        self._lensDist,sep,sourceDist=self._sourceDist)			

