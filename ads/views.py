from ads.models import Ad
from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from django.urls import reverse_lazy

# Create your views here.


class AdListView(OwnerListView):
    model = Ad
    template_name = "ads/ads_list.html"


class AdDetailView(OwnerDeleteView):
    model = Ad
    template_name = "ads/ad_detail.html"


class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'price', 'text']

    template_name = "ads/ad_form.html"
    success_url = reverse_lazy('ads:all')

class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'price', 'text']

    template_name = "ads/ad_form.html"
    success_url = reverse_lazy('ads:all')

class AdDeleteView(OwnerDeleteView):
    model = Ad

    template_name = "ads/ad_confirm_delete.html"
    success_url = reverse_lazy('ads:all')