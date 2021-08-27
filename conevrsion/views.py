from django.http import HttpResponse
from django.views.generic import FormView
from .forms import *
import pytesseract    # ======= > Add
from PIL import Image


# Create your views here.

class HomeView(FormView):
    form_class = UploadForm
    template_name = 'index.html'
    success_url = '/'

    def form_valid(self, form):
        upload = self.request.FILES['file']
        return HttpResponse(pytesseract.image_to_string(Image.open(upload)))
