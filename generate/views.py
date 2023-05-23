from django.shortcuts import render

from django.views.generic import View


# def home(request):
#     context = {}
#     if request.method == "POST":
#         name = request.POST.get("name", "")
#         car_plate = request.POST.get("car_plate", "")
#         visit_at = request.POST.get("visit_at", "")
#
#         context["post_input"] = f"{name},{car_plate},{visit_at}"
#
#     return render(request, "generate/home.html", context=context)


class HomeView(View):
    def get(self, request):
        context = {}
        return render(request, "generate/home.html", context=context)

    def post(self, request):
        context = {}
        name = request.POST.get("name", "")
        car_plate = request.POST.get("car_plate", "")
        visit_at = request.POST.get("visit_at", "")
        context["post_input"] = f"{name},{car_plate},{visit_at}"
        return render(request, "generate/home.html", context=context)
