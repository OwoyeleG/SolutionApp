from django.contrib import auth
from django.urls.conf import path
from cittu.views import collect_report, report_view
from solutions.views import delete_list_view, solution_view
from problems.views import adopt_solutions_view, home_view, problem_exists_view, problem_view
from django.contrib import admin
from users import views
from users.views import login
from users.views import logout_view, register
from django.contrib.auth import views as auth_view
from users import views as user_views
from cittu.views import report_view, reportform_view, collect_report, update_report_view
from solutions .views import(
            problem_table_view, 
            solution_view,
            search_problem,
            solution_table_view,
            delete_list_view,
            update_list_view,
            adopted_solutions_list_view,
            adopted_solution_view,
            
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('problem', problem_view, name= 'problem'),
    path('solution/', solution_view, name='solution'),
    path('', home_view, name = 'home'),
    path('register/', user_views.register, name = 'register'),
    path('login/', auth_view.LoginView.as_view (template_name= 'users/login.html'), name='login'),
    path('logout/',logout_view, name='logout'),
    path('problem_list/', problem_table_view, name='problem_list'),
    path('solution_list/', solution_table_view, name='solution_list'),
    path('enter_solution/<id>/', solution_view, name='solution'),
    path('search_problem', search_problem, name='search-problem'),
    path('delete/<id>/', delete_list_view, name='delete'),
    path('update/<id>/', update_list_view, name='update'),
    path('adopt_solutions/<id>/', adopt_solutions_view, name='adopt_solutions'),
    path('adopted_solutions_list/', adopted_solutions_list_view, name='adopted_solutions_list'),
    path('adopted_solution/<id>/', adopted_solution_view, name='adopted_solution'),
    path('problem_exists/<id>/', problem_exists_view, name='problem_exists'),
    path('report', report_view, name='report'),  
    path('reportform', reportform_view, name='reportform'),
    path('reportsummary', collect_report, name='reportsummary'),  
    path('update_report/<str:pk>/', update_report_view, name='update_report'),
]

