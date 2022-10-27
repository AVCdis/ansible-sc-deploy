from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView

from budget.models import Budget
from budget.serializer import BudgetSerializer


class ListBudgetAPI(ListAPIView):
    """Retrieves all the budgets available in our database"""
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class CreateBudgetAPI(CreateAPIView):
    """Creates a new budget in our database"""
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class UpdateBudgetAPI(UpdateAPIView):
    """Update budget with the id sent through the request url path"""
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class DeleteBudgetAPI(DestroyAPIView):
    """Deletes a budget whose id has been sent through the url path"""
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
