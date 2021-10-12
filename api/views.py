from rest_framework.parsers import JSONParser
from rest_framework import status
from .serializers import *
from django.http import JsonResponse
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def laptop_detail(request, pk):
    laptop_info = Laptop.objects.get(id=pk)
    serializer = LaptopSerializer(laptop_info)
    return JsonResponse(serializer.data)


@api_view(['GET'])
def laptops(request):
    company = Laptop.objects.all()
    serializer = LaptopSerializer(company, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def company_detail(request):
    company_id = request.GET.get("id")
    company_info = Company.objects.get(id=company_id)
    serializer = CompanySerializer(company_info)
    return JsonResponse(serializer.data)


@api_view(['GET'])
def companies(request):
    company = Company.objects.all()
    serializer = CompanySerializer(company, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def add_company(request):
    company_data = JSONParser().parse(request)
    company_serializer = CompanySerializer(data=company_data)
    if company_serializer.is_valid():
        company_serializer.save()
        return JsonResponse(data="success", safe=False, status=status.HTTP_201_CREATED)
    return JsonResponse(data="failure", safe=False, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_laptop(request):
    laptop_data = JSONParser().parse(request)
    company_Name = laptop_data.get('companyName')
    try:
        company = Company.objects.get(companyName=company_Name)
    except BaseException as error:
        company_serializer = CompanySerializer(data={'companyName': company_Name})
        if company_serializer.is_valid():
            company_serializer.save()
    laptop_serializer = LaptopSerializer(data=laptop_data)
    if laptop_serializer.is_valid():
        laptop_serializer.save()
        return JsonResponse(data=laptop_serializer.data, safe=False, status=status.HTTP_201_CREATED)
    return JsonResponse(data="failure", safe=False, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def update_laptop(request):
    laptop_data = JSONParser().parse(request)
    laptop_id = laptop_data.get('id')
    try:
        laptop = Laptop.objects.get(id=laptop_id)
    except BaseException as error:
        return JsonResponse(data=error.__str__(), safe=False)
    laptop_serializer = LaptopSerializer(laptop, data=laptop_data, partial=True)
    if laptop_serializer.is_valid():
        laptop_serializer.save()
        return JsonResponse(data=laptop_serializer.data, safe=False)
    return JsonResponse(data="failure", safe=False, status=status.HTTP_400_BAD_REQUEST)
