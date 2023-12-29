from django.shortcuts import render
from rest_framework.filters import SearchFilter

from .models import *
from .serializers import *

from rest_framework.response import Response
from rest_framework.views import APIView

class SuvlarAPI(APIView):
    def get(self, request):
        suvlar = Suv.objects.all()
        serializer =SuvSerializer(suvlar, many=True)

        return Response(serializer.data)

    def post(self, request):
        suvlar = Suv.objects.all()
        serializer = SuvSerializer(suvlar, many=True)

        if serializer.is_valid():
            Suv.objects.create(
                serializer.save(suv=request.user)
            )
            return Response(serializer.data)
        return Response(serializer.errors)

class SuvAPI(APIView):
    def get(self, pk, request):
        suv = Suv.objects.get(id=pk)
        serializer =SuvSerializer(suv)

        return Response(serializer.data)

    def update(self, pk,  request):
        suv = Suv.objects.all()
        serializer = SuvSerializer(suv, data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data
            Suv.objects.filter(id=pk).update(
                brend = data.get('brend'),
                narx = data.get('narx'),
                litr = data.get('litr'),
                batafsil = data.get('batafsil'),
            )
            return Response(serializer.data)
        return Response(serializer.errors)

class MijozlarAPI(APIView):
    filter_backends = [SearchFilter]
    search_fields = ['ism', 'tel']
    def get(self, request):
        mijozlar = Mijoz.objects.all()
        serializer = MijozSerializer(mijozlar, many=True)

        return Response(serializer.data)

    def post(self, request):
        mijozlar = Suv.objects.all()
        serializer = SuvSerializer(mijozlar, many=True)

        if serializer.is_valid():
            Mijoz.objects.create(
                serializer.save(mijoz=request.user)
            )
            return Response(serializer.data)
        return Response(serializer.errors)

class MijozAPI(APIView):
    def get(self, pk, request):
        mijoz = Mijoz.objects.get(id=pk)
        serializer = MijozSerializer(mijoz)

        return Response(serializer.data)

    def update(self, pk,  request):
        mijoz = Mijoz.objects.all()
        serializer = MijozSerializer(mijoz, data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data
            Mijoz.objects.filter(id=pk).update(
                ism = data.get('ism'),
                tel = data.get('tel'),
                manzil = data.get('manzil'),
                qarz = data.get('qarz'),
                user = data.get('user')
            )
            return Response(serializer.data)
        return Response(serializer.errors)

class BuyurtmalarAPI(APIView):
    def get(self, request):
        buyurtmalar = Buyurtma.objects.all()
        serializer =BuyurtmaSerializer(buyurtmalar, many=True)

        return Response(serializer.data)

    def post(self, request):
        buyurtmalar = Buyurtma.objects.all()
        serializer = BuyurtmaSerializer(buyurtmalar, many=True)

        if serializer.is_valid():
            Buyurtma.objects.create(
                serializer.save(buyurtma=request.user)
            )
            return Response(serializer.data)
        return Response(serializer.errors)


class HaydovchilarAPI(APIView):
    def get(self, request):
        haydovchilar = Haydovchi.objects.all()
        serializer = HaydovchiSerializer(haydovchilar, many=True)

        return Response(serializer.data)

class AdminlarAPI(APIView):
    def get(self, request):
        adminlar = Admin.objects.all()
        serializer = AdminSerializer(adminlar, many=True)

        return Response(serializer.data)

class HaydovchiAPI(APIView):
    def get(self, pk, request):
        haydovchi = Haydovchi.objects.get(id=pk)
        serializer = HaydovchiSerializer(haydovchi)

        return Response(serializer.data)

class AdminAPI(APIView):
    def get(self, pk, request):
        admin = Admin.objects.get(id=pk)
        serializer = HaydovchiSerializer(admin)

        return Response(serializer.data)

