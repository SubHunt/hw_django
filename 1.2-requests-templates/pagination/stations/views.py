from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
import csv
import os
from pathlib import Path

from pagination.settings import BUS_STATION_CSV

BASE_DIR = Path(__file__).resolve().parent.parent
BUS_STATION_CSV = os.path.join(BASE_DIR, 'data-398-2018-08-30.csv')


def index(request):
    return redirect(reverse('bus_stations'))


def _get_stations_list():
    stations_list = []
    with open(BUS_STATION_CSV, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for stations in reader:
            stations_list.append(stations)
    return stations_list


def bus_stations(request):
    page_number = request.GET.get('page', 1)
    stations_list = _get_stations_list()
    paginator = Paginator(stations_list, 10)
    page = paginator.get_page(page_number)
    context = {
        'page': page,
    }
    return render(request, 'stations/index.html', context)



# bus_station = {}
# name = []
# street = []
# district = []
# with open(BUS_STATION_CSV, newline='', encoding="utf8") as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         # print(row['Name'], row['Street'], row['District'])
#         bus_station.setdefault('Name', []).append(row['Name'])
#         bus_station.setdefault('Street', []).append(row['Street'])
#         bus_station.setdefault('District', []).append(row['District'])
#     #     name.append(row['Name'])
#     #     street.append(row['Street'])
#     #     district.append(row['District'])
#     #
#     # bus_station['Name'] = name
#     # bus_station['Street'] = street
#     # bus_station['District'] = district
#     # for station in bus_station:
#     #     print(bus_station['Name'], bus_station['Street'], bus_station['District'])
#     # print(type(reader))
#     # bus_stations = reader
#     # print(reader)
#
#
# def index(request):
#     return redirect(reverse('bus_stations'))
#
#
# def bus_stations(request):
#     paginator = Paginator(bus_station['Name'], 10)
#     page = paginator.get_page(1)
#     # получите текущую страницу и передайте ее в контекст
#     # также передайте в контекст список станций на странице
#
#     context = {
#         'bus_stations': bus_station,
#         'page': page,
#     }
#     return render(request, 'stations/index.html', context)
