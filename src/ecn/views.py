from django.views import generic


class HomePage(generic.TemplateView):
    template_name = "home.html"


class SupportAndTraining(generic.TemplateView):
    template_name = "support_training.html"

class Management(generic.TemplateView):
    template_name = "management.html"
