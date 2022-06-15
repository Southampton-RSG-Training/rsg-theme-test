from matplotlib import pyplot

import numpy

data = numpy.loadtxt(fname='../data/inflammation-01.csv', delimiter=',')

image  = pyplot.imshow(data)
pyplot.show(image)

ave_inflammation = data.mean(axis=0)
ave_plot = pyplot.plot(ave_inflammation)
pyplot.show(ave_plot)

max_plot = pyplot.plot(data.max(axis=0))
pyplot.show(max_plot)

min_plot = pyplot.plot(data.min(axis=0))
pyplot.show(min_plot)