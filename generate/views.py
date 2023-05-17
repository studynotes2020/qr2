from django.shortcuts import render


def home(request):
    context = {}
    if request.method == "POST":
        context["post_input"] = request.POST.get("qr_text", "")

    return render(request, "generate/home.html", context=context)
