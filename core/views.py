from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request,nome,idade):
    return HttpResponse('<h1>Hello {} de {} anos. </h1>' .format(nome, idade))

def soma(request,num1,num2):
    resultado = num1 + num2
    return HttpResponse('<h2>Aqui está a soma entre {} e {}: {}. </h2>' .format(num1, num2, resultado))

def subtracao(request,num1,num2):
    resultado = num1 - num2
    return HttpResponse('<h2>Aqui está a subtração entre {} e {}: {}. </h2>' .format(num1, num2, resultado))

def multiplicacao(request,num1,num2):
    resultado = num1 * num2
    return HttpResponse('<h2>Aqui está a multiplicação entre {} e {}: {}. </h2>' .format(num1, num2, resultado))

def divisao(request,num1,num2):
    resultado = num1 / num2
    return HttpResponse('<h2>Aqui está a divisão entre {} e {}: {}. </h2>' .format(num1, num2, resultado))