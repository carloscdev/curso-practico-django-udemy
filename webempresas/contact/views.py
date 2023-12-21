from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            content = request.POST.get("content")
            # send email and redirect
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-reply@mailtrap.io",
                ["carlos_cdo@outlook.com"],
                reply_to=[email]
            )
            try:
                email.send()
                # everything ok
                return redirect(reverse("contact")+"?ok")
            except:
                # something went wrong
                return redirect(reverse("contact")+"?error")

    return render(request, "contact/contact.html", {'form':contact_form})