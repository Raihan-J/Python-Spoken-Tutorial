from numpy import linspace, pi, sin
from matplotlib.pyplot import plot, legend, show, title
from matplotlib.pyplot import xlabel, ylabel

x = linspace(-2*pi,2*pi,100)
plot(x,sin(x))
legend(['sin(x)'])
title('Sine plot')
xlabel('x')
ylabel('sin(x)')
show()
