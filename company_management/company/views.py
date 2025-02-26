from django.shortcuts import render, redirect, get_object_or_404
from .models import Company
from .forms import CompanyForm

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'company/company_list.html', {'companies': companies})

def add_company(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm()
    return render(request, 'company/add_company.html', {'form': form})

def edit_company(request, company_id):
    company = get_object_or_404(Company, company_id=company_id)
    if request.method == "POST":
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm(instance=company)
    return render(request, 'company/edit_company.html', {'form': form})

def delete_company(request, company_id):
    company = get_object_or_404(Company, company_id=company_id)
    if request.method == "POST":
        company.delete()
        return redirect('company_list')
    return render(request, 'company/delete_company.html', {'company': company})
