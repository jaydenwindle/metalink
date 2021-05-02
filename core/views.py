from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic import DetailView

from core.models import Link
from core.forms import LinkForm

class LinkCreateView(CreateView):
    model = Link
    fields = ("url", "title", 'description', 'image')

    def get_success_url(self) -> str:
        print(self)
        return reverse('link_success', kwargs={"slug": self.object.slug})


class LinkSuccessView(DetailView):
    model = Link
    template_name = "core/link_success.html"



def link(request, slug):
    link = Link.objects.get(slug=slug)

    scheme = request.is_secure() and "https" or "http"
    root_url = f"{scheme}://{request.get_host()}"

    return render(request, 'core/link.html', {"link": link, "root_url": root_url})
