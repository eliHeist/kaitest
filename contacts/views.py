from django.conf import settings
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, FormView

from contacts.forms import BookingForm, ContactForm
from contacts.models import Receipient


# Create your views here.
# class ContactPage(FormView):
#    form_class = ContactForm
#    success_url = '/contact/success/'
#    template_name = "contacts/contactpage.html"

class BookingView(FormView):
   form_class = BookingForm
   success_url = '/contact/booking/success'
   template_name = 'contacts/booking.html'

   def post(self, request, *args, **kwargs):
      form_class = self.get_form_class()
      form = self.get_form(form_class)

      if form.is_valid():
         return self.form_valid(form)
      print('here2')
      return self.form_invalid(form)

   def form_valid(self, form):
      form.send_mail()
      return super(BookingView, self).form_valid(form)

   def form_invalid(self, form):
      # form.send_mail()
      return super(BookingView, self).form_invalid(form)


@api_view(['POST'])
def sendMail(request):
   if request.method == 'POST':
      data = request.data
      print(data)
      message = f"Name: {data.get('your_name')}\nEmail: {data.get('your_email')}\nMore info: {data.get('your_message')}"
      print("\n\nmessage\n"+message)
      receipients = Receipient.objects.all()

      try:
         send_mail(
            subject='Sent from footer form',
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[receipient.email for receipient in receipients]
         )

         return Response('SUCCESS')
      except Exception as e:
         print(f'Exception: {e}')
         return Response('Failed')


# @api_view(['POST'])
def bookNow(request):
   message = 'Successfully sent your booking'
   context = {
      'message': message
   }
   template_name = 'contacts/status.html'
   
   if request.method == 'POST':
      data = request.data
      print(data)
      message = f'''Name: {data.get('fname')} {data.get('lname')}
      \nEmail: {data.get('email')} \t Phone number: {data.get('phone')}
      \nWhen are you planning to visit: {data.get('date')}
      \nHow many are you?: {data.get('single_number')}
      \nIf a group, How many People are in the group?: {data.get('group_number')}
      \nWhich Tour or Visit are you intrested in?: {data.get('tour')}
      \nWhat's the best way to contact you?: {data.get('fav-means')}
      \nIf phone what is the best time to call you?: {data.get('fav-time')}
      \nAnything Else we should know: {data.get('anything_else')}
      '''
      print("\n\nmessage\n"+message)
      receipients = Receipient.objects.all()

      try:
         send_mail(
            subject='Booking',
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[receipient.email for receipient in receipients]
         )

      except Exception as e:
         print(f'Exception: {e}')
         message = "Failed, try again later"

   return render(request, template_name, context)


class SuccessView(TemplateView):
   template_name = "contacts/success.html"
