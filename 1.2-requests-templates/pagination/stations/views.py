from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
import csv

from pagination.settings import BUS_STATION_CSV

def index(request):
    return redirect(reverse('bus_stations'))
#
# def bus_stations(request):
#     page_number = request.GET.get('page', 1)
#     stations_list = _get_stations_list()
#     paginator = Paginator(stations_list, 10)
#     page = paginator.get_page(page_number)
#     context = {
#         'page': page,
#         'bus_stations': paginator,
#     }
#     return render(request, 'stations/index.html', context)


        # print(row['Name'], row['Street'], row['District'])
        # bus_station.setdefault('Name', []).append(row['Name'])
        # bus_station.setdefault('Street', []).append(row['Street'])
        # bus_station.setdefault('District', []).append(row['District'])


def read_csv():
    bus_station = []
    with open(BUS_STATION_CSV, encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bus_station.append(row)
    return bus_station


def bus_stations(request):
    bus_station = read_csv()
    paginator = Paginator(bus_station, 10)
    page_number = int(request.GET.get('page', 1))
    page = paginator.get_page(page_number)
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    context = {
        'bus_stations': bus_station,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
