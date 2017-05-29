from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect,HttpResponseForbidden
from booking.models import Booking
from booking.forms import BookingCreateForm,BookingEditForm
from django.views.generic.edit import UpdateView

@login_required
def bookingCreate(request):
    args={}
    error='Ошибка при заполнении формы'
    form=BookingCreateForm()
    if request.method == 'POST':
        form = BookingCreateForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.user = request.user
            response.status = "1"
            response.room = '0'
            response.price = '0'
            response.save()
            return HttpResponseRedirect('/')
        return render(request, 'bookingCreate.html', {'form': form,'error': error})
    return render(request, 'bookingCreate.html', {'form': form})

@login_required
def bookingList(request):
    if request.user.status == 'M':
        bookingList=Booking.objects.all().order_by('-date')
    else:
        bookingList=Booking.objects.filter(user_id=request.user.id)
    return render(request,'bookingList.html',{'bookingList':bookingList})

@login_required
def bookingDetail(request,booking_id):
    bookingDetail=get_object_or_404(Booking,pk=booking_id)
    return render(request, 'bookingDetail.html', {'bookingDetail': bookingDetail})

class BookingEdit(UpdateView):
    form_class = BookingEditForm
    model = Booking
    template_name = 'bookingEdit.html'
    success_url = '/booking/list'
    pk_url_kwarg = 'booking_id'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        task = super(BookingEdit, self).get_object()
        if self.request.user.status != "M":
            return HttpResponseForbidden()
        return UpdateView.dispatch(self, request, *args, **kwargs)
        
