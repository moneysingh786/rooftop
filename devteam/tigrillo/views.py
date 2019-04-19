from django.views.generic import TemplateView, ListView
from django.core.paginator import EmptyPage, Paginator
from django.http import Http404
from .models import Orders,OrderItem
from django.http import JsonResponse
# class OrderView(TemplateView):
#     template_name = "iccinfo.html"


class SafePaginator(Paginator):
    def validate_number(self, number):
        try:
            return super(SafePaginator, self).validate_number(number)
        except EmptyPage:
            if number > 1:
                return self.num_pages
            else:
                raise


class OrderView(ListView):
    paginator_class = SafePaginator
    model = OrderItem
    template_name = 'iccinfo.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'orders'  # Default: object_list
    paginate_by = 10
    queryset = OrderItem.objects.all()  # Default: Model.objects.all()


def searchorder(request):
    if request.method == "GET":
        search_text = request.GET['searchtext']
        if search_text is not None and search_text != u"":
            search_text = request.GET['searchtext']
            print(search_text)
            order_status = OrderItem.objects.all().filter(ItemDescription__icontains=search_text)[:10]
            order_list = []
            for os in order_status:
                order_details = {}
                order_details["ID"] = os.ID
                order_details["Desc"] = str(os.ItemDescription)
                order_details["Type"] = str(os.ItemType)
                order_details["FullDesc"] = str(os.ItemFullDescription)
                order_list.append(order_details)
            print(order_list)
        else:
            order_list = []
    return JsonResponse(order_list,safe=False)
