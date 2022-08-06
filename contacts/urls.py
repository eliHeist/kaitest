from django.urls import path

from contacts.views import BookingView, SuccessView, bookNow, sendMail
app_name = 'contacts'

urlpatterns = [
    # path('', ContactPage.as_view(), name='contactpage'),
    path('sendmail/', sendMail, name='send_mail'),
    path('booking/', BookingView.as_view(), name='book_now'),
    path('booking/success/', SuccessView.as_view(), name='success'),
]