import numpy as nm
import matplotlib.pyplot as plt


def getregre(x,y):
	#no. of observations
	n=nm.size(x)
	#mean of x and y vector
	m_x,m_y=nm.mean(x),nm.mean(y)
	#calculating cross deviation and deviation about x
	sxy=nm.sum(x*y)-n*m_x*m_y
	sxx=nm.sum(x*x)-n*m_x*m_x

	#definig theta1 and theta0
	theta1=sxy/sxx
	theta0=m_y-theta1*m_x
	return theta0,theta1

"""now defininf function to plot regression line"""
def plot_line(x,y,b):
	#plotting the actual point as scatter plot
	plt.scatter(x,y,color='m',marker=",",s=20)

	#response hypothesis
	y1=b[0]+b[1]*x

	#plotting the regression line
	plt.plot(x,y1,color="g")
	#now naming x and y axis
	plt.xlabel('x')
	plt.ylabel('y')




def main():
	x=nm.array([1,2,3,4,5,6])
	y=nm.array([14,6,1,2,8,9])
	#estimating parameters
	b=getregre(x,y)


	print("estimating value of theta0={} and theta1={}".format(b[0],b[1]))

	plot_line(x, y, b)

if __name__=="__main__":
	main()





