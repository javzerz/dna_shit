from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.views.generic import View
from .models import Data
from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate, login
import numpy as np
import pandas as pd

class UserFormView(View):
    form_class = UserForm
    template_name = 'upload_dna/registration_form.html'

    #display form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #add user
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('upload:home')

        return render(request, self.template_name, {'form': form})

class DataCreate(CreateView):
    model = Data
    fields = ['user', 'file']

def upload(request):
    return render(request, 'upload_dna/upload.html')

def home(request):
    return render(request, 'upload_dna/home.html')

def detail(request):
    all_data = Data.objects.all()
    posts = Data.objects.all().order_by('-created')[:5]
    latest_entry = posts[0]

    df = pd.read_csv('./media/AncestryDNA.txt', comment="#", sep='\s+',)
    df = df[["rsid","chromosome","position","allele1","allele2",]]
    data_table = df.to_html(index=False)

    args = {'all_data': all_data, 'posts': posts, 'latest_entry': latest_entry, 'df': df, 'data_table': data_table }

    return render(request, 'upload_dna/detail.html', args)
