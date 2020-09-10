import numpy
import matplotlib.pyplot as plt
x = numpy.linspace(-5*numpy.pi,5*numpy.pi,500)
plt.plot(x, x, 'b')
plt.plot(x, -x, 'b')
plt.plot(x, numpy.sin(x), 'g', linewidth=2)
plt.plot(x, x*numpy.sin(x), 'r', linewidth=3)
plt.legend(['x', '-x', 'sin(x)', 'xsin(x)'])
plt.annotate('origin', xy = (0, 0))
plt.xlim(-5*numpy.pi, 5*numpy.pi)
plt.ylim(-5*numpy.pi, 5*numpy.pi)
plt.show()
