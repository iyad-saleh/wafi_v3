from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# from employee.models import Employee
# from customer.models import Customer
# from account.models import Account



@login_required
def dashboard(request):
    # if hasattr( request.user  ,'is_MANAGER' ) :


        # customers = Customer.objects.all()
        # accounts = Account.objects.all()
        # employees = Employee.objects.all()
        # flightSchedules = FlightSchedule.objects.all()
    return render(request, 'dashboard/admin_home.html',
            {

            # 'customers':customers,
            # 'accounts':accounts,
            # 'employees':employees,
            # 'flightSchedules':flightSchedules,
            })
    # return HttpResponse(
    #     status=403,
    #     headers={
    #         'HX-Trigger': json.dumps({

    #            "customerListChanged": None,
    #         })
    #     })