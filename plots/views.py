#from django.shortcuts import render
from django.shortcuts import render_to_response
import pickle
#from django.http import HttpResponse
#from django.template import RequestContext, loader
import pandas as pd;
from collections import defaultdict;
from django.template.context_processors import csrf
import re;

def index(request):
	plots = defaultdict(list);    
    
	with open('/home/sachin/mysite/plots/static/plots/plots.pickle', 'rb') as handle:
	    	plots = pickle.load(handle)
 	
	with open('/home/sachin/mysite/plots/static/plots/scores.pickle', 'rb') as handle:
	    	scores = pickle.load(handle)
		

        if request.method == 'POST':
		X = plots['all'];
		T = [scores[i] for i in X];
		Y= [x for (t,x) in sorted(zip(T,X),reverse=True)];
		Y = map(str, Y)
		T = sorted(T,reverse=True)
		return render_to_response("plots/index.html", {'plots': Y, 'filename' : request.FILES['myfile']})

	if request.method == 'GET': # If the form is submitted		        	
		search_query = request.GET.get('search_box', None)
		X = plots[search_query];
		T = [scores[i] for i in X];
		Y= [x for (t,x) in sorted(zip(T,X),reverse=True)];
		Y = map(str, Y)
		T = sorted(T,reverse=True)
	return render_to_response('plots/index.html',
#                              {'plots': plots[search_query]})
				{'plots_scores': zip(Y,T)})
