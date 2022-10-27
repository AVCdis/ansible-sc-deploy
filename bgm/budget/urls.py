from django.urls import path

from budget import views

urlpatterns = [
    path("", views.ListBudgetAPI.as_view(), name="budget_list"),
    path("create/", views.CreateBudgetAPI.as_view(), name="create_budget"),
    path("update/<int:pk>/", views.UpdateBudgetAPI.as_view(), name="update_budget"),
    path("delete/<int:pk>/", views.DeleteBudgetAPI.as_view(), name="delete_budget")
]
