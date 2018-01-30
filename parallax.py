#################
# Code to calculate 
# parallax Motion
# @author P.McGill
#################


import uncertainties.umath as np
from astropy import units as u
from astropy.coordinates import get_sun
from astropy.time import Time
import numpy as numpy

deg2rad = numpy.pi / 180.0 
rad2deg = 180.0 / numpy.pi

def get_earth_observer_vector(time):
	"""Calculate the position vector of and on earth observer in 
	heliocentric ecliptic corrdinates at epoch=time

        Args:
           time (obj:astropy:time) : Time at which the position of the obsever 
			is to be measured

        return:

           positon (obj:numpy:array) : position vector in AU

        """
    
	sunPos = get_sun(time)
	sunPos.representation = "cartesian"

	return numpy.array([-sunPos.x / u.AU,-sunPos.y / u.AU,-sunPos.z/  u.AU])

def angular_to_cartesian(ra,dec):
	"""Calculates unit cartesian vector of angular coordinates Right 
	acession and declination [degrees]

	"""

	ra = ra * deg2rad
	dec = dec * deg2rad

	return numpy.array([np.cos(ra) * np.cos(dec), np.sin(ra) * np.cos(dec),
		np.sin(dec)])

def cartesian_to_angular(x,y,z):
	"""Converts from cartesian to angular coordinates
	"""	

	
	norm = np.sqrt(x**2+y**2+z**2)

	x = x / norm
	y = y / norm
	z = z / norm


	dec = np.asin(z)
	ra = np.atan2(y,x)


	ra = ra * rad2deg
	dec = dec * rad2deg

	return numpy.array([ra,dec])


def get_motion_vector(ra,dec, pmra, pmdec, parallax):
        # Return the space motion vector of a star
        # Requirements:
        #   - astropy coordinate object
        #   - proper motion in ra and dec (mas per year)
        #   - parallax (mas)
        #   - radial velocity (km/s)
        # Returns astropy cartesian representation of space motion vector
        # see eqns.
        #   - 11.2
        #   - 12.36
        # in 'Spherical Astronomy' by R.M. Green


	ra = ra * deg2rad
	dec = dec * deg2rad


	vt_ra = pmra / parallax
	vt_dec = pmdec / parallax

	
	Vtan = numpy.array([
		- vt_ra * np.sin(ra) - vt_dec * np.cos(ra) * np.sin(dec),
		vt_ra * np.cos(ra) - vt_dec * np.sin(ra) * np.sin(dec),
		vt_dec * np.cos(dec)
		])

	return Vtan

def parallax_to_au(parallax):
	"""Takes Parallax in [mas]
	"""
	
	return 648000000.0 / (numpy.pi * parallax)



