from importlib.resources import contents
from tempfile import template
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template import context
from .models import *
from .forms import *
from users.models import UnitHead
# Create your views here.

def report_view(request):
    report = SubUnitReport.objects.all()
    context = {'report': report}
    template = 'cittu/report.html'
    return render(request, template, context)


def update_report_view(request, pk):
    report = SubUnitReport.objects.get(id=pk)
    report_type = ReportType.objects.all()


    if request.method == 'POST':
        SubUnitReport.objects.create(subUnitReport=report,report_type=report.report_type,
                                                introductions=report.introductions,
                                                 achievement=report.achievement,
                                                 challenge=report.challenge,
                                                  conclusion=report.conclusion
                                            )
        report_type_id = request.POST.get('report_type','')
        report_type_instance = ReportType.objects.get(id=report_type_id)
        introductions = request.POST.get('introductions','')
        achievement = request.POST.get('achievement','')
        challenge = request.POST.get('challenge','')
        conclusion = request.POST.get('conclusion','')

        report.introductions = introductions
        report.report_type = report_type_instance
        report.achievement= achievement
        report.challenge = challenge
        report.conclusion = conclusion
        report.save()
        return redirect('report')
    context = {'report':report, 'report_type':report_type}
    template = 'cittu/reportform.html'
    return render(request, template,context )






# def update_report_view(request, pk):
#     report = SubUnitReport.objects.get(id=pk)
#     form =ReportForm(instance=report)

#     if request.method =='POST':
#         form = ReportForm(request.POST, request.FILES, instance=report)
#         if form.is_valid():
#             form.save()
#             return redirect('report')
#     context = {'form': form, 'report':report}
#     template = 'cittu/reportform.html'
#     return render(request, template, context)


def reportform_view(request):
    report = ReportType.objects.all()

    if request.method == 'POST':
        report_type_id = request.POST.get('report_type','')
        report_type = ReportType.objects.get(id=report_type_id)
        introduction = request.POST.get('introductions','')
        achievement = request.POST.get('achievement','')
        challenge = request.POST.get('challenge','')
        conclusion = request.POST.get('conclusion','')
        data = SubUnitReport(report_type=report_type, introduction=introduction, achievement=achievement, challenge=challenge, conclusion=conclusion)
        data.save() 
        return redirect('report')
    context = {'report':report}  
    template = 'cittu/reportform.html'   
    return render(request, template, context)  





# def reportform_view(request):
#     form = ReportForm()
#     if request.method == 'POST':
#         form = ReportForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('report')
#     context = {'form':form}  
#     template = 'cittu/reportform.html'      
#     return render(request, template, context)


def collect_report(request):
    collect_report=None
    report_types = ReportType.objects.all()
    profiles = UnitHead.objects.all()

    get_report_type = request.GET.get('report_type')
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')

    if request.method == 'GET':
        if not get_report_type:
            messages.info(request, "Please select Report type and specify date range")
        else:
            collect_report = SubUnitReport.objects.filter(
                report_type_id=get_report_type,
                date_from__gte=date_from, date_to__lte=date_to
                )

    context = {'collect_report': collect_report, "report_types":report_types, "profiles":profiles}
    template = 'cittu/reportsummary.html'
    return render(request, template, context)
