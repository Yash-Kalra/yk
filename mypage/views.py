from django.shortcuts import render
# from django .template import loader
from .models import cdetails, ldetails
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect, request, Http404
#from django.shortcuts import get_object_or_404, render

# Create your views here.
# class IndexView(generic.ListView):
#     template_name = 'cinfo.html'
#     context_object_name = 'latest_name_list'

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return cdetails.objects.order_by('cname')[:5]
def index(request):
     all_det = cdetails.objects.all()
 # for loader   template = loader.get_template('home.html')
     context= {
         'all_det':all_det,

     }
     return render(request,'home.html',context)
 # for loader   return HttpResponse(template.render(context), request)
    

class CDetailView(generic.DetailView):
    template_name = 'cinfo.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('name')[:5]


class LDetailView(generic.DetailView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


def CD(request, cdetalis_id):
    try:
        m1=cdetails.objects.get(pk=cdetalis_id)
    except cdetails.DoesNotExist:
        raise Http404("this id not present in database")
    return render(request,'home1.html',{'m2':m1})
        
    #return HttpResponse("<hi> welcome id "+str(cdetalis_id)+"</h1>")
    

# def index(request):
#      all_det = cdetails.objects.all()
#      for a in all_det:
#         url='/mypage/'+ str(a.id)
#         html= '<a href=" '+url+' ">' +a.cname + "---" + a.cdet + '</a><br>'

#      return HttpResponse(html)
