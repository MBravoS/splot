#### Definition of all wrappers for 1D plotting

#Histogram
def hist(data,bin_num=None,dens=True,norm=None,xlim=None,ylim=None,xinvert=False,yinvert=False,xlog=False,ylog=True,
			title=None,xlabel=None,ylabel=None,plabel=None,lab_loc=0,ax=None,plot_par={},multi=False):
	
	"""1D histogram function.
	
	The plotting is done with pyplot.plot(), so histograms are shown with interpolated curves instead of the
	more common stepwise curve. For this reason splotch.histstep is a better choice for small datasets. 
	
	Parameters
	----------
	data : array-like or list
		If list it is assumed that each elemement is array-like.
	bin_num : int or list, optional
		Number of bins.
	dens :  bool or list, optional
		If false the histogram returns raw counts.
	norm : float or list, optional
		Normalization of the counts.
	xlim : tuple-like, optional
		Defines the limits of the x-axis, it must contain two elements (lower and higer limits).
	ylim : tuple-like, optional
	xinvert : bool or list, optional
		If true inverts the x-axis.
		Defines the limits of the y-axis, it must contain two elements (lower and higer limits).
	yinvert : bool or list, optional
		If true inverts the y-axis.
	xlog : bool or list, optional
		If True the scale of the x-axis is logarithmic.
	ylog : bool or list, optional
		If True the scale of the x-axis is logarithmic.
	title : str, optional
		Sets the title of the plot
	xlabel : str, optional
		Sets the label of the x-axis.
	ylabel : str, optional
		Sets the label of the y-axis.
	plabel : str, optional
		Sets the legend for the plot.
	lab_loc : int, optional
		Defines the position of the legend
	ax : pyplot.Axes, optional
		Use the given axes to make the plot, defaults to the current axes.
	plot_par : dict, optional
		Passes the given dictionary as a kwarg to the plotting function.
	multi : bool, optional
		If True, holds the application of x/ylog, x/yinvert and grid, to avoid duplication.
	
	Returns
	-------
	None
	"""
	
	import numpy as np
	import matplotlib.colors as clr
	import matplotlib.pyplot as plt
	from .base_func import axes_handler,binned_axis,dict_splicer,plot_finalizer
	
	if ax is not None:
		old_axes=axes_handler(ax)
	if type(data) is not list:
		data=[data]
	L=len(data)
	if bin_num is None:
		bin_num=[int((len(d))**0.4) for d in data]
	if type(bin_num) is not list:
		bin_num=[bin_num+1]*L
	if type(dens) is not list:
		dens=[dens]*L
	if type(norm) is not list:
		norm=[norm]*L
	if type(plabel) is not list:
		plabel=[plabel]*L
	plot_par=dict_splicer(plot_par,L,[len(x) for x in data])
	for i in range(L):
		temp_data,bins_hist,bins_plot=binned_axis(data[i],bin_num[i],log=xlog)
		y=np.histogram(temp_data,bins=bins_hist,density=dens[i])[0]
		if dens[i]:
			if norm[i]:
				y*=1.0*len(data[i])/norm[i]
		plt.plot((bins_plot[0:-1]+bins_plot[1:])/2,y,label=plabel[i],**plot_par[i])
	if plabel[0] is not None:
		plt.legend(loc=lab_loc)
	if not multi:
		plot_finalizer(xlog,ylog,xlim,ylim,title,xlabel,ylabel,xinvert,yinvert)
	if ax is not None:
		old_axes=axes_handler(old_axes)

#Step histogram
def histstep(data,bin_num=None,dens=True,xlim=None,ylim=None,xinvert=False,yinvert=False,xlog=False,ylog=True,
			title=None,xlabel=None,ylabel=None,plabel=None,lab_loc=0,ax=None,plot_par={},multi=False):
	
	"""'Clasic' 1D histogram function.
	
	This function is designed around pyplot.hist(), so it lacks the functionality to use arbitraty y-axis
	normalisation of splotch.hist().
	It is better choice for small datasets, as it plots with stepwise curves, instead of the interpolated
	ones of splotch.hist().
	
	Parameters
	----------
	data : array-like or list
		If list it is assumed that each elemement is array-like.
	bin_num : int or list, optional
		Number of bins.
	dens :  bool or list, optional
		If false the histogram returns raw counts.
	xlim : tuple-like, optional
		Defines the limits of the x-axis, it must contain two elements (lower and higer limits).
	ylim : tuple-like, optional
		Defines the limits of the y-axis, it must contain two elements (lower and higer limits).
	xinvert : bool or list, optional
		If true inverts the x-axis.
	yinvert : bool or list, optional
		If true inverts the y-axis.
	xlog : bool or list, optional
		If True the scale of the x-axis is logarithmic.
	ylog : bool or list, optional
		If True the scale of the x-axis is logarithmic.
	title : str, optional
		Sets the title of the plot
	xlabel : str, optional
		Sets the label of the x-axis.
	ylabel : str, optional
		Sets the label of the y-axis.
	plabel : str, optional
		Sets the legend for the plot.
	lab_loc : int, optional
		Defines the position of the legend
	ax : pyplot.Axes, optional
		Use the given axes to make the plot, defaults to the current axes.
	plot_par : dict, optional
		Passes the given dictionary as a kwarg to the plotting function.
	multi : bool, optional
		If True, holds the application of x/ylog, x/yinvert and grid, to avoid duplication.
	
	Returns
	-------
	None
	"""
	
	import numpy as np
	import matplotlib.colors as clr
	import matplotlib.pyplot as plt
	from .base_func import axes_handler,dict_splicer,plot_finalizer
	
	if ax is not None:
		old_axes=axes_handler(ax)
	if type(data) is not list:
		data=[data]
	L=len(data)
	if bin_num is None:
		bin_num=[int((len(d))**0.4) for d in data]
	if type(bin_num) is not list:
		bin_num=[bin_num+1]*L
	if type(plabel) is not list:
		plabel=[plabel]*L
	plot_par=dict_splicer(plot_par,L,[len(x) for x in data])
	for i in range(L):
		temp_data,bins,temp=binned_axis(data[i],bin_num[i],log=xlog)
		plt.hist(temp_data,bins=bins,density=dens,label=plabel[i],**plot_par[i])
	if plabel[0] is not None:
		plt.legend(loc=lab_loc)
	if not multi:
		plot_finalizer(xlog,ylog,xlim,ylim,title,xlabel,ylabel,xinvert,yinvert)
	if ax is not None:
		old_axes=axes_handler(old_axes)


# Generalized lines
def axline(x=None,y=None,m=None,c=None,ax=None,line_par={}):
	
	"""Generalised axis lines.
	
	This function aims to generalise the usage of axis lines calls (axvline/axhline) together and to allow
	lines to be specified by a slope/intercept.
	
	Parameters
	----------
	x : int or list, optional 
		x position(s) in data coordinates for a vertical line(s).
	y : int or list, optional
		y position(s) in data coordinates for a horizontal line(s).
	m : int or list, optional
		Slope(s) of diagonal axis line(s), defaults to 1 if not specified when c is given.
	c : int or list, optional
		Intercept points(s) of diagonal axis line(s), defaults to 0 if not specified when m is given.
	ax : pyplot.Axes, optional
		Use the given axes to make the plot, defaults to the current axes.
	line_par : dict, optional
		Passes the given dictionary as a kwarg to the plotting function. Valid kwargs are Line2D properties.
	Returns
	-------
	None
	"""
	    
	import numpy as np
	import matplotlib.pyplot as plt
	from .base_func import axes_handler,plot_finalizer,dict_splicer
	
	if ax is not None:
		old_axes=axes_handler(ax)
	else:
		ax=plt.gca()
		old_axes=ax        
	
	if (not any([x,y,m,c])): # If nothing has been specified
		raise TypeError("axline() missing one of optional arguments: 'x', 'y', 'm' or 'c'")
	    
	for i, val in enumerate([x,y,m,c]):
		if (val is not None):
			try: # Test whether the parameter is iterable
				temp=(k for k in val)
			except TypeError: # If not, convert to a list
				if   (i == 0): x = [x]
				elif (i == 1): y = [y]
				elif (i == 2): m = [m]
				elif (i == 3): c = [c]
	
	if (x is not None and y is not None): # Check whether both x and y were specified
		raise ValueError("'x' and 'y' cannot be both specified")
	
	if (x is not None): # Check conditions if x specified
		if (any([m,c])): # Should not specify m or c, if x given.
			raise ValueError("'{0}' cannot be specified if x specified".format('m' if m else 'c'))
		L = len(x)
	    
	if (y is not None): # Check conditions if y specified
		if (any([m,c])): # Should not specify m or c, if y given.
			raise ValueError("'{0}' cannot be specified if y specified".format('m' if m else 'c'))
		L = len(y)
	
	if (m is not None):
		if (c is None): # If no intercept specified
			c = [0]*len(m) # set c to 0 for all m
		else:
			if (len(c) == 1):
				c = [c[0]]*len(m)
			elif (len(c) != len(m)):
				if (len(m) == 1):
					m = [m[0]]*len(c)
				else:
					raise ValueError("Length of c ({0}) and length of m ({1}) must be equal or otherwise 1".format(len(c),len(m)))
		L = len(m)
	elif (c is not None):
		if (m is None): # If no slope specified
			m = [1]*len(c) # set m to 1 for all c
		L = len(c)
	
	# Organise the line parameters dictionary    
	line_par=dict_splicer(line_par,L,[1]*L) 
	    
	if (x is not None):
		for ii, xx in enumerate(x):
			ax.axvline(x=xx,**line_par[ii])
	if (y is not None):
		for ii, yy in enumerate(y):
			ax.axhline(y=yy,**line_par[ii])
	if (m is not None):
		for ii, pars in enumerate(zip(m,c)):
			mm = pars[0]; cc = pars[1]
			
			xLims = ax.get_xlim()
			yLims = ax.get_ylim()
			
			ax.plot([xLims[0],xLims[1]],[mm*xLims[0]+cc,mm*xLims[1]+cc],**line_par[ii])
			
			ax.set_xlim(xLims)
			ax.set_ylim(yLims)
			
	if ax is not None:
		old_axes=axes_handler(old_axes)

#Plots
def plot(x,y=None,xlim=None,ylim=None,xinvert=False,yinvert=False,xlog=False,ylog=False,title=None,xlabel=None,ylabel=None,
			plabel=None,lab_loc=0,ax=None,plot_par={},multi=False):
	import numpy as np
	import matplotlib.pyplot as plt
	from .base_func import axes_handler,dict_splicer,plot_finalizer
	
	"""Base plotting function.
	
	This is a wrapper for pyplot.plot().
	
	Parameters
	----------
	x : array-like or list
		If list it is assumed that each elemement is array-like. If y is not given, the given values pass to y and a
		numpy array is generated with numpy.arange() for the x values.
	y : array-like or list, optional
		If list it is assumed that each elemement is array-like.
	xlim : tuple-like, optional
		Defines the limits of the x-axis, it must contain two elements (lower and higer limits).
	ylim : tuple-like, optional
		Defines the limits of the y-axis, it must contain two elements (lower and higer limits).
	xinvert : bool or list, optional
		If true inverts the x-axis.
	yinvert : bool or list, optional
		If true inverts the y-axis.
	xlog : bool or list, optional
		If True the scale of the x-axis is logarithmic.
	ylog : bool or list, optional
		If True the scale of the x-axis is logarithmic.
	title : str, optional
		Sets the title of the plot
	xlabel : str, optional
		Sets the label of the x-axis.
	ylabel : str, optional
		Sets the label of the y-axis.
	plabel : str, optional
		Sets the legend for the plot.
	lab_loc : int, optional
		Defines the position of the legend
	ax : pyplot.Axes, optional
		Use the given axes to make the plot, defaults to the current axes.
	plot_par : dict, optional
		Passes the given dictionary as a kwarg to the plotting function.
	multi : bool, optional
		If True, holds the application of x/ylog, x/yinvert and grid, to avoid duplication.
	
	Returns
	-------
	None
	"""
	
	if ax is not None:
		old_axes=axes_handler(ax)
	if type(x) is not list:
		x=[x]
	L=len(x)
	if y is None:
		y=x
		x=[np.arange(len(x[i])) for i in range(L)]
	else:
		if type(y) is not list:
			y=[y]
	if type(plabel) is not list:
		plabel=[plabel]*L
	plot_par=dict_splicer(plot_par,L,[len(i) for i in x])
	for i in range(L):
		plt.plot(x[i],y[i],label=plabel[i],**plot_par[i])
	if plabel[0] is not None:
		plt.legend(loc=lab_loc)
	if not multi:
		plot_finalizer(xlog,ylog,xlim,ylim,title,xlabel,ylabel,xinvert,yinvert)
	if ax is not None:
		old_axes=axes_handler(old_axes)

