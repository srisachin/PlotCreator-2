# Copyright Sachin Srivastava

import PlotSea.PlotObj;
import seaborn as sns;
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import settings


class ScatterPlot(PlotSea.PlotObj.PlotObj):
	def plotExp(self,exp,myData):
		plt.figure();
		sns.regplot(exp[1]['xaxis'],exp[1]['yaxis'],data=myData);
		plt.savefig("plots/static/%d.png" %settings.count);
		plt.clf()
		plt.close()
		settings.count=settings.count+1;

	def check(self,myStr):
		return myStr=="scatter"
