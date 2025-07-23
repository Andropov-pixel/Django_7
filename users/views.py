from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


from users.forms import UserRegistrationForm
from users.models import User
from django.conf import settings


class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        response = super().form_valid(form)

        send_mail(
            subject='Добро пожаловать!',
            message='Спасибо за регистрацию на нашем сайте "SkyStore"',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[form.cleaned_data.get('email')],
            fail_silently=False,
        )

        return response