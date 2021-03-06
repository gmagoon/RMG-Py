#!/usr/bin/python
# -*- coding: utf-8 -*-

################################################################################
#
#	RMG - Reaction Mechanism Generator
#
#	Copyright (c) 2002-2009 Prof. William H. Green (whgreen@mit.edu) and the
#	RMG Team (rmg_dev@mit.edu)
#
#	Permission is hereby granted, free of charge, to any person obtaining a
#	copy of this software and associated documentation files (the 'Software'),
#	to deal in the Software without restriction, including without limitation
#	the rights to use, copy, modify, merge, publish, distribute, sublicense,
#	and/or sell copies of the Software, and to permit persons to whom the
#	Software is furnished to do so, subject to the following conditions:
#
#	The above copyright notice and this permission notice shall be included in
#	all copies or substantial portions of the Software.
#
#	THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#	FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#	DEALINGS IN THE SOFTWARE.
#
################################################################################

"""
Contains a number of settings to be used throughout RMG.

These can be modified at runtime, for example by reading in a settings file.
Their values will be stored in this module.
"""

# Global variables: important directories

#: The directory used for output of results
outputDirectory = '.'

#: The directory used for temporary scratch files
scratchDirectory = '.'

#: The directory with libraries in?
libraryDirectory = '.'

# Global variables: options

#: Whether to draw pictures of the molecules.
drawMolecules = False

#: Whether to make plots of simulations.
generatePlots = False

#: Whether to estimate spectral data for species.
spectralDataEstimation = False

#: Whether to process unimolecular (pressure-dependent) reaction networks.
unimolecularReactionNetworks = False

# Global variables: RMG initialization time in seconds since the epoch
# (generated by a call to time.time())
#: Time at which the program execution was started (seconds since the epoch)
initializationTime = 0.0

#: Maximum time that RMG should run for in seconds
wallTime = 0