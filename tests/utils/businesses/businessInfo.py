# coding=utf-8
from random import choice


utilitySegments = {"2", "3", "4"}
taxSegments = {"1", "5"}

taxes = [
    {
        "code": "5701",
        "segment": "1",
        "name": "PREFEITURA DA CIDADE DE SÃO PAULO",
        "time": "24H",
        "type": "iss",
    },
    {
        "code": "328",
        "segment": "5",
        "name": "SIMPLES NACIONAL",
        "time": "24H",
        "type": "das",
    },
    {
        "code": "64",
        "segment": "5",
        "name": "SECRETARIA DA RECEITA FEDERAL DO BRASIL",
        "time": "24H",
        "type": "darf",
    },
]

utilities = [
    {
        'code': '846',
        'segment': '2',
        'name': 'DEPARTAMENTO DE  AGUA E ESGOTO DE PORTO REAL',
        'time': '15H',
    },
    {
        'code': '158',
        'segment': '4',
        'name': 'CLARO RJ',
        'time': '19H',
    },
    {
        'code': '12',
        'segment': '2',
        'name': 'CASAL',
        'time': '15H',
    },
    {
        'code': '1143',
        'segment': '2',
        'name': 'PM ITAJU',
        'time': '15H',
    },
    {
        'code': '590',
        'segment': '2',
        'name': 'SAAE BOCA DA MATA',
        'time': '15H',
    },
    {
        'code': '19',
        'segment': '2',
        'name': 'COPASA CIA DE SANEAMENTO DE MINAS GERAIS',
        'time': '15H',
    },
    {
        'code': '1058',
        'segment': '2',
        'name': 'AGUAS SCHROEDER',
        'time': '15H',
    },
    {
        'code': '47',
        'segment': '3',
        'name': 'AMAZONAS ENERGIA ANTIGA ELETRONORTE',
        'time': '15H',
    },
    {
        'code': '74',
        'segment': '2',
        'name': 'SUPERINTENDENCIA DE  AGUA E ESGOTO DE ITUIUTABA',
        'time': '15H',
    },
    {
        'code': '1247',
         'segment': '2',
         'name': 'SISAR QUIXADA',
         'time': '15H',
    }
]

for utility in utilities:
    utility["type"] = "utility"

businessMap = {}

for business in utilities + taxes:
    businessMap.setdefault(business["segment"], {})[business["code"]] = business


def randomUtilityBusiness():
    return choice(utilities)


def randomTaxBusiness():
    return choice(taxes)


def randomBusiness():
    return choice(utilities + taxes)
