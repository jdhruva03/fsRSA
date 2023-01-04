from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseNotFound
from django.conf import settings

import RSA.RSA as rs

class Home(TemplateView):
    template_name = 'home.html'


def encrypt(request):

    context = {}
    
    if request.method == 'POST':

        if not(request.FILES):
            context['error'] = 1
            return render(request, 'encrypt.html', context)

        uploaded_file = request.FILES['document']

        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)

        # Encrpyt The file
        n,e,p,q,d, encrypted_file_name = rs.encrypt(fs.path(uploaded_file.name))
        context['url'] = fs.url(encrypted_file_name)
        
        context['n'] = n
        context['e'] = e
        context['p'] = p
        context['q'] = q
        context['d'] = d

        # Delete the uploaded file
        fs.delete(uploaded_file.name)

    # return response   
    return render(request, 'encrypt.html', context)



def decrypt(request):
    context = {}

    if request.method == 'POST':

        if not(request.FILES):
            context['error'] = 1
            return render(request, 'decrypt.html', context)
        
        uploaded_file = request.FILES['document']

        if not(request.POST['rsa_n'] and request.POST['rsa_e'] and request.POST['rsa_p'] and request.POST['rsa_q'] and request.POST['rsa_d']):
            context['invalid'] = 1
            return render(request, 'decrypt.html', context)
        


        n = int(request.POST['rsa_n'])
        e = int(request.POST['rsa_e'])
        p = int(request.POST['rsa_p'])
        q = int(request.POST['rsa_q'])
        d = int(request.POST['rsa_d'])

        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)

        decrypted_file_name = rs.decrypt(fs.path(uploaded_file.name), n, e, p, q, d)
        context['url'] = fs.url(decrypted_file_name)

        # Delete the uploaded file
        fs.delete(uploaded_file.name)

    
    # return response   
    return render(request, 'decrypt.html', context)