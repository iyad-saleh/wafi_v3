from django.urls import path, include
from .views import dashboard



urlpatterns =[
    path('',dashboard, name='dashboard'),
    path('account/', include('account.urls')),
    # path('box/', include('box.urls')),
    path('international/', include('international.urls')),
    path('companys/', include('company.urls')),

    path('airline/', include('airline.urls')),
    # path('expenses/', include('expense.urls')),
    # path('employee/', include('employee.urls')),
    # path('reservation/', include('reservation.urls'),name='reservation'),
    path('passport/', include('passport.urls')),
    # path('customer/', include('customer.urls')),
    # path('trip/', include('trip.urls')),
    path('entry/', include('entry.urls')),

   ]


