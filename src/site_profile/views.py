from django.shortcuts import render
# from site_profile.models import (
#                                         About, 
#                                         TermsAndCondition,
#                                         Copyright,
#                                         )

# Create your views here.
def about(request):
    return render(request, 'site_profile/about.html')

def terms_conditions(request):
    return render(request, 'site_profile/terms_and_conditions.html'
            )

def copyright(request):
    return render(request, 'site_profile/copyright.html'
            )
