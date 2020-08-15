# coding=utf-8
from random import choice

segmentMap = {
    "1": "Prefeituras",
    "2": "Saneamento",
    "3": "Energia Elétrica e Gás",
    "4": "Telecomunicações",
    "5": "Órgãos Governamentais",
    "6": "Carnes e Assemelhados ou demais empresas",
    "7": "Multas de trânsito",
    "9": "Uso exclusivo do banco",
}

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
    # {
    #     "code": "270",
    #     "segment": "5",
    #     "name": "INSTITUTO NACIONAL DO SEGURO SOCIAL",
    #     "time": "24H",
    #     "type": "gps",
    # },
    # {
    #     "code": "179",
    #     "segment": "5",
    #     "name": "FUNDO DE GARANTIA POR TEMPO DE SERVIÇO",
    #     "time": "24H",
    #     "type": "gfr",
    # },
]

utilities = [
    {
        "code": "97",
        "segment": "2",
        "name": "SABESP",
        "time": "19H"
    },
    {
        "code": "5",
        "segment": "3",
        "name": "CEB DISTRIBUICAO SA",
        "time": "19H"
    },
    {
        "code": "22",
        "segment": "3",
        "name": "ELEKTRO ELETRICIDADE E SERVICOS SA",
        "time": "19H"
    },
    {
        "code": "40",
        "segment": "3",
        "name": "CPFL CIA PAULISTA DE FORCA E LUZ",
        "time": "19H"
    },
    {
        "code": "48",
        "segment": "3",
        "name": "ELETROPAULO METROPOLITANA DE ELETRICIDADE DE SP",
        "time": "19H"
    },
    {
        "code": "53",
        "segment": "3",
        "name": "LIGHT SERVICOS DE ELETRICIDADE",
        "time": "19H"
    },
    {
        "code": "56",
        "segment": "3",
        "name": "CEG CIA ESTADUAL DE GAS",
        "time": "19H"
    },
    {
        "code": "110",
        "segment": "3",
        "name": "COMPANHIA PIRATININGA DE FORCA E LUZ SA",
        "time": "19H"
    },
    {
        "code": "2",
        "segment": "4",
        "name": "BRASILTELECOM FILIAL RS",
        "time": "19H"
    },
    {
        "code": "5",
        "segment": "4",
        "name": "BRASIL TELECOM FILIAL PELOTAS",
        "time": "19H"
    },
    {
        "code": "6",
        "segment": "4",
        "name": "EMBRATEL EMPRESA BRASILEIRA DE TELECOMUNICACOES",
        "time": "19H"
    },
    {
        "code": "11",
        "segment": "4",
        "name": "BRASIL TELECOM FILIAL AC",
        "time": "19H"
    },
    {
        "code": "13",
        "segment": "4",
        "name": "TELEMAR BA TELEBA",
        "time": "19H"
    },
    {
        "code": "14",
        "segment": "4",
        "name": "BRASIL TELECOM FILIAL BRA",
        "time": "19H"
    },
    {
        "code": "16",
        "segment": "4",
        "name": "BRASIL TELECOM FILIAL GO",
        "time": "19H"
    },
    {
        "code": "17",
        "segment": "4",
        "name": "BRASIL TELECOM FILIAL MT",
        "time": "19H"
    },
    {
        "code": "18",
        "segment": "4",
        "name": "TELEMAR MG TELEMIG",
        "time": "19H"
    },
    {
        "code": "20",
        "segment": "4",
        "name": "BRASIL TELECOM FILIAL PARANA",
        "time": "19H"
    },
    {
        "code": "24",
        "segment": "4",
        "name": "TELEMAR RJ",
        "time": "19H"
    },
    {
        "code": "25",
        "segment": "4",
        "name": "TELEMAR RN",
        "time": "19H"
    },
    {
        "code": "26",
        "segment": "4",
        "name": "BRASIL TELECOM FILIAL RO",
        "time": "19H"
    },
    {
        "code": "27",
        "segment": "4",
        "name": "BRASIL TELECOM FILIAL SC",
        "time": "19H"
    },
    {
        "code": "41",
        "segment": "4",
        "name": "VIVO",
        "time": "19H"
    },
    {
        "code": "47",
        "segment": "4",
        "name": "VIVO DF",
        "time": "19H"
    },
    {
        "code": "48",
        "segment": "4",
        "name": "VIVO RJ",
        "time": "19H"
    },
    {
        "code": "64",
        "segment": "4",
        "name": "VIVO MG",
        "time": "19H"
    },
    {
        "code": "69",
        "segment": "4",
        "name": "VIVO SC",
        "time": "19H"
    },
    {
        "code": "79",
        "segment": "4",
        "name": "VIVO RS",
        "time": "19H"
    },
    {
        "code": "80",
        "segment": "4",
        "name": "VIVO",
        "time": "19H"
    },
    {
        "code": "82",
        "segment": "4",
        "name": "GVT",
        "time": "19H"
    },
    {
        "code": "113",
        "segment": "4",
        "name": "OI CEL RJ",
        "time": "19H"
    },
    {
        "code": "158",
        "segment": "4",
        "name": "CLARO RJ",
        "time": "19H"
    },
    {
        "code": "159",
        "segment": "4",
        "name": "CLARO SP",
        "time": "19H"
    },
    {
        "code": "160",
        "segment": "4",
        "name": "CLARO DF",
        "time": "19H"
    },
    {
        "code": "161",
        "segment": "4",
        "name": "CLARO RS",
        "time": "19H"
    },
    {
        "code": "162",
        "segment": "4",
        "name": "CLARO SP",
        "time": "19H"
    },
    {
        "code": "163",
        "segment": "4",
        "name": "CLARO SC",
        "time": "19H"
    },
    {
        "code": "165",
        "segment": "4",
        "name": "CLARO BA",
        "time": "19H"
    },
    {
        "code": "221",
        "segment": "4",
        "name": "CLARO NORTE",
        "time": "19H"
    },
    {
        "code": "296",
        "segment": "4",
        "name": "NET SERVICOS DE COMUNICACAO SA",
        "time": "19H"
    },
    {
        "code": "305",
        "segment": "4",
        "name": "CLARO TV",
        "time": "19H"
    },
    {
        "code": "1029",
        "segment": "4",
        "name": "TELEFONICA SP",
        "time": "19H"
    },
    {
        "code": "1",
        "segment": "2",
        "name": "AGESPISA S A",
        "time": "15H"
    },
    {
        "code": "2",
        "segment": "2",
        "name": "CAEMA",
        "time": "15H"
    },
    {
        "code": "4",
        "segment": "2",
        "name": "CAER",
        "time": "15H"
    },
    {
        "code": "5",
        "segment": "2",
        "name": "CAERD",
        "time": "15H"
    },
    {
        "code": "6",
        "segment": "2",
        "name": "CAERN",
        "time": "15H"
    },
    {
        "code": "7",
        "segment": "2",
        "name": "CAESA",
        "time": "15H"
    },
    {
        "code": "8",
        "segment": "2",
        "name": "CAESB CIA AGUA E ESGOTO DE BRASiLIA",
        "time": "15H"
    },
    {
        "code": "9",
        "segment": "2",
        "name": "CAGECE",
        "time": "15H"
    },
    {
        "code": "10",
        "segment": "2",
        "name": "CAGEPA",
        "time": "15H"
    },
    {
        "code": "12",
        "segment": "2",
        "name": "CASAL",
        "time": "15H"
    },
    {
        "code": "13",
        "segment": "2",
        "name": "CASAN CIA CATARINENSE  AGUA E SANEAMENTO",
        "time": "15H"
    },
    {
        "code": "14",
        "segment": "2",
        "name": "CEDAE CIA ESTADUAL  AGUA E ESGOTO",
        "time": "15H"
    },
    {
        "code": "15",
        "segment": "2",
        "name": "CESAMA",
        "time": "15H"
    },
    {
        "code": "16",
        "segment": "2",
        "name": "CESAN",
        "time": "15H"
    },
    {
        "code": "17",
        "segment": "2",
        "name": "CODAU UBERABA",
        "time": "15H"
    },
    {
        "code": "18",
        "segment": "2",
        "name": "COMPESA CIA PERNAMBUCANA DE SANEAMENTO",
        "time": "15H"
    },
    {
        "code": "19",
        "segment": "2",
        "name": "COPASA CIA DE SANEAMENTO DE MINAS GERAIS",
        "time": "15H"
    },
    {
        "code": "21",
        "segment": "2",
        "name": "COSAMA",
        "time": "15H"
    },
    {
        "code": "22",
        "segment": "2",
        "name": "COSANPA",
        "time": "15H"
    },
    {
        "code": "24",
        "segment": "2",
        "name": "DAAE ARARAQUARA",
        "time": "15H"
    },
    {
        "code": "26",
        "segment": "2",
        "name": "DAAE RIO CLARO",
        "time": "15H"
    },
    {
        "code": "27",
        "segment": "2",
        "name": "DAE AMERICANA",
        "time": "15H"
    },
    {
        "code": "29",
        "segment": "2",
        "name": "DAE BAURU",
        "time": "15H"
    },
    {
        "code": "31",
        "segment": "2",
        "name": "DAE JUNDIAI",
        "time": "15H"
    },
    {
        "code": "32",
        "segment": "2",
        "name": "DAE MARILIA",
        "time": "15H"
    },
    {
        "code": "33",
        "segment": "2",
        "name": "DAE SANTA BARBARA D OESTE",
        "time": "15H"
    },
    {
        "code": "34",
        "segment": "2",
        "name": "DAE SANTANA LIVRAMENTO",
        "time": "15H"
    },
    {
        "code": "35",
        "segment": "2",
        "name": "DAE S CAETANO DO SUL",
        "time": "15H"
    },
    {
        "code": "36",
        "segment": "2",
        "name": "DAE SUMARE",
        "time": "15H"
    },
    {
        "code": "37",
        "segment": "2",
        "name": "DAE DE VALINHOS",
        "time": "15H"
    },
    {
        "code": "38",
        "segment": "2",
        "name": "Departamento de Agua, Arroios e Esgoto de Bage",
        "time": "15H"
    },
    {
        "code": "39",
        "segment": "2",
        "name": "DAEMO OLIMPIA",
        "time": "15H"
    },
    {
        "code": "40",
        "segment": "2",
        "name": "DAERP RIBEIRAO PRETO",
        "time": "15H"
    },
    {
        "code": "41",
        "segment": "2",
        "name": "DESO",
        "time": "15H"
    },
    {
        "code": "42",
        "segment": "2",
        "name": "DMAE POCOS DE CALDAS",
        "time": "15H"
    },
    {
        "code": "43",
        "segment": "2",
        "name": "DMAE PORTO ALEGRE",
        "time": "15H"
    },
    {
        "code": "44",
        "segment": "2",
        "name": "DMAE",
        "time": "15H"
    },
    {
        "code": "46",
        "segment": "2",
        "name": "EMASA ITABUNA",
        "time": "15H"
    },
    {
        "code": "47",
        "segment": "2",
        "name": "EMBASA",
        "time": "15H"
    },
    {
        "code": "50",
        "segment": "2",
        "name": "SAAE AGUAS DE LINDOIA",
        "time": "15H"
    },
    {
        "code": "51",
        "segment": "2",
        "name": "SAAE DE AMPARO",
        "time": "15H"
    },
    {
        "code": "52",
        "segment": "2",
        "name": "SAAE DE ARACRUZ",
        "time": "15H"
    },
    {
        "code": "53",
        "segment": "2",
        "name": "SAAE ATIBAIA",
        "time": "15H"
    },
    {
        "code": "55",
        "segment": "2",
        "name": "SAAE DE BARRA BONITA",
        "time": "15H"
    },
    {
        "code": "56",
        "segment": "2",
        "name": "SAAE BARRETOS",
        "time": "15H"
    },
    {
        "code": "58",
        "segment": "2",
        "name": "SAAEMB BURITAMA",
        "time": "15H"
    },
    {
        "code": "59",
        "segment": "2",
        "name": "FOZ CACHOEIRO ALTERADA PARA ODEBRECHT AMBIENTAL",
        "time": "15H"
    },
    {
        "code": "60",
        "segment": "2",
        "name": "SAAE DE CACOAL",
        "time": "15H"
    },
    {
        "code": "61",
        "segment": "2",
        "name": "SAAE DE CANDIDO MOTA",
        "time": "15H"
    },
    {
        "code": "62",
        "segment": "2",
        "name": "SAAE CAPIVARI",
        "time": "15H"
    },
    {
        "code": "65",
        "segment": "2",
        "name": "SAAE DE COSTA RICA",
        "time": "15H"
    },
    {
        "code": "66",
        "segment": "2",
        "name": "SERV AUT DE AGUA E ESGOTO DE EXTREMOZ",
        "time": "15H"
    },
    {
        "code": "68",
        "segment": "2",
        "name": "SAAE GARCA",
        "time": "15H"
    },
    {
        "code": "69",
        "segment": "2",
        "name": "SAAE GUARULHOS",
        "time": "15H"
    },
    {
        "code": "70",
        "segment": "2",
        "name": "SAAEG GUARATINGUET A",
        "time": "15H"
    },
    {
        "code": "71",
        "segment": "2",
        "name": "SAAE INDAIATUBA",
        "time": "15H"
    },
    {
        "code": "72",
        "segment": "2",
        "name": "SAAE ITAPIRA",
        "time": "15H"
    },
    {
        "code": "74",
        "segment": "2",
        "name": "SUPERINTENDENCIA DE  AGUA E ESGOTO DE ITUIUTABA",
        "time": "15H"
    },
    {
        "code": "75",
        "segment": "2",
        "name": "SAAEJ SERVICO AUTONOMO DE  AGUA E ESGOTO DE JABOTICABAL",
        "time": "15H"
    },
    {
        "code": "76",
        "segment": "2",
        "name": "SAAE JACAREI",
        "time": "15H"
    },
    {
        "code": "77",
        "segment": "2",
        "name": "SERVICO AUTONOMO DE  AGUA E ESGOTO DE LENCOIS PAULISTA",
        "time": "15H"
    },
    {
        "code": "78",
        "segment": "2",
        "name": "SAAE LIMEIRA",
        "time": "15H"
    },
    {
        "code": "79",
        "segment": "2",
        "name": "SERVICO AUTONIOMO DE  AGUA E ESGOTO DE LINHARES",
        "time": "15H"
    },
    {
        "code": "81",
        "segment": "2",
        "name": "SAAE DE MOGI MIRIM",
        "time": "15H"
    },
    {
        "code": "82",
        "segment": "2",
        "name": "SAAE NOVA MUTUM",
        "time": "15H"
    },
    {
        "code": "83",
        "segment": "2",
        "name": "SAAE PALMITAL",
        "time": "15H"
    },
    {
        "code": "85",
        "segment": "2",
        "name": "SAAE DE PASSOS",
        "time": "15H"
    },
    {
        "code": "86",
        "segment": "2",
        "name": "Servico Autonomo de Saneamento de Pelotas",
        "time": "15H"
    },
    {
        "code": "87",
        "segment": "2",
        "name": "SAAE DE PROMISS AO",
        "time": "15H"
    },
    {
        "code": "89",
        "segment": "2",
        "name": "SAAE SAO CARLOS",
        "time": "15H"
    },
    {
        "code": "91",
        "segment": "2",
        "name": "SAAE SOROCABA",
        "time": "15H"
    },
    {
        "code": "92",
        "segment": "2",
        "name": "TAQUARITINGA",
        "time": "15H"
    },
    {
        "code": "93",
        "segment": "2",
        "name": "SERV MUNICIPAL DE SANEAMENTO B ASICO DE UNAI",
        "time": "15H"
    },
    {
        "code": "95",
        "segment": "2",
        "name": "SAAE VOLTA REDONDA",
        "time": "15H"
    },
    {
        "code": "98",
        "segment": "2",
        "name": "SAECIL DE LEME",
        "time": "15H"
    },
    {
        "code": "99",
        "segment": "2",
        "name": "SAEMA ARARAS",
        "time": "15H"
    },
    {
        "code": "101",
        "segment": "2",
        "name": "SAMAE JARAGU A DO SUL",
        "time": "15H"
    },
    {
        "code": "102",
        "segment": "2",
        "name": "SAMAE",
        "time": "15H"
    },
    {
        "code": "103",
        "segment": "2",
        "name": "SAAE TIETE SP",
        "time": "15H"
    },
    {
        "code": "105",
        "segment": "2",
        "name": "SANASA",
        "time": "15H"
    },
    {
        "code": "106",
        "segment": "2",
        "name": "SANEAGO",
        "time": "15H"
    },
    {
        "code": "107",
        "segment": "2",
        "name": "SANEATINS",
        "time": "15H"
    },
    {
        "code": "108",
        "segment": "2",
        "name": "SANEMAT",
        "time": "15H"
    },
    {
        "code": "109",
        "segment": "2",
        "name": "SANEPAR",
        "time": "15H"
    },
    {
        "code": "110",
        "segment": "2",
        "name": "SANESUL",
        "time": "15H"
    },
    {
        "code": "111",
        "segment": "2",
        "name": "SEMAE SERVICO MUNICIPAL DE  AGUAS E ESGOTOS DE MOGI DAS",
        "time": "15H"
    },
    {
        "code": "112",
        "segment": "2",
        "name": "S S LEOPOLDO",
        "time": "15H"
    },
    {
        "code": "113",
        "segment": "2",
        "name": "SEMASA",
        "time": "15H"
    },
    {
        "code": "114",
        "segment": "2",
        "name": "SIMAE JOACABA",
        "time": "15H"
    },
    {
        "code": "115",
        "segment": "2",
        "name": "SAE OURINHOS",
        "time": "15H"
    },
    {
        "code": "116",
        "segment": "2",
        "name": "SAEV",
        "time": "15H"
    },
    {
        "code": "118",
        "segment": "2",
        "name": "SAMAE BLUMENAU",
        "time": "15H"
    },
    {
        "code": "119",
        "segment": "2",
        "name": "SAMAE BRUSQUE",
        "time": "15H"
    },
    {
        "code": "120",
        "segment": "2",
        "name": "SAMAE S AO BENTO DO SUL",
        "time": "15H"
    },
    {
        "code": "121",
        "segment": "2",
        "name": "SEMAE PIRACICABA",
        "time": "15H"
    },
    {
        "code": "122",
        "segment": "2",
        "name": "SANED DIADEMA",
        "time": "15H"
    },
    {
        "code": "124",
        "segment": "2",
        "name": "AGUAS DE LIMEIRA S A",
        "time": "15H"
    },
    {
        "code": "126",
        "segment": "2",
        "name": "SAEP PIRASSUNUNGA",
        "time": "15H"
    },
    {
        "code": "127",
        "segment": "2",
        "name": "SAMA MAUA",
        "time": "15H"
    },
    {
        "code": "129",
        "segment": "2",
        "name": "SAAE ALAGOINHAS",
        "time": "15H"
    },
    {
        "code": "134",
        "segment": "2",
        "name": "SAAE DE ITAPETININGA",
        "time": "15H"
    },
    {
        "code": "135",
        "segment": "2",
        "name": "SERVICO AUTONOMO DE  AGUA E ESGOTO DE JUAZEIRO",
        "time": "15H"
    },
    {
        "code": "140",
        "segment": "2",
        "name": "SAAE ORLEANS",
        "time": "15H"
    },
    {
        "code": "141",
        "segment": "2",
        "name": "SAMAE URUSSANGA",
        "time": "15H"
    },
    {
        "code": "142",
        "segment": "2",
        "name": "SAMAE COCAL DO SUL",
        "time": "15H"
    },
    {
        "code": "143",
        "segment": "2",
        "name": "SAMAE DE GR AO PAR A",
        "time": "15H"
    },
    {
        "code": "144",
        "segment": "2",
        "name": "SAMAE S AO LUDGERO",
        "time": "15H"
    },
    {
        "code": "146",
        "segment": "2",
        "name": "SAMAE JACINTO MACHADO",
        "time": "15H"
    },
    {
        "code": "147",
        "segment": "2",
        "name": "SAMAE SANTA ROSA DO SUL",
        "time": "15H"
    },
    {
        "code": "148",
        "segment": "2",
        "name": "SAMAE JAGUARUNA",
        "time": "15H"
    },
    {
        "code": "149",
        "segment": "2",
        "name": "SAMAE CAMPOS NOVOS",
        "time": "15H"
    },
    {
        "code": "151",
        "segment": "2",
        "name": "SAMAE NOVA TRENTO",
        "time": "15H"
    },
    {
        "code": "152",
        "segment": "2",
        "name": "SAMAE S AO FRANCISCO DO SUL",
        "time": "15H"
    },
    {
        "code": "153",
        "segment": "2",
        "name": "SERVICO AUTONOMO MUNICIPAL DE  AGUA E ESGOTO DE RIO",
        "time": "15H"
    },
    {
        "code": "154",
        "segment": "2",
        "name": "SIMAE",
        "time": "15H"
    },
    {
        "code": "156",
        "segment": "2",
        "name": "SAAE BARRA MANSA",
        "time": "15H"
    },
    {
        "code": "157",
        "segment": "2",
        "name": "SANEBAVI SANEAMENTO B ASICO DE VINHEDO ANTIGA SAEMA DE",
        "time": "15H"
    },
    {
        "code": "158",
        "segment": "2",
        "name": "SAAE GASPAR",
        "time": "15H"
    },
    {
        "code": "159",
        "segment": "2",
        "name": "SAMAE POMERODE",
        "time": "15H"
    },
    {
        "code": "160",
        "segment": "2",
        "name": "SAAE PORTO FELIZ",
        "time": "15H"
    },
    {
        "code": "161",
        "segment": "2",
        "name": "SERVICO AUTONOMO DE SANEAMENTO DE CABECEIRA GRANDE",
        "time": "15H"
    },
    {
        "code": "164",
        "segment": "2",
        "name": "SAAE AXIXA",
        "time": "15H"
    },
    {
        "code": "178",
        "segment": "2",
        "name": "SAAE LUCAS DO RIO VERDE",
        "time": "15H"
    },
    {
        "code": "180",
        "segment": "2",
        "name": "SAAE PLANALTO DA SERRA",
        "time": "15H"
    },
    {
        "code": "184",
        "segment": "2",
        "name": "SAEE BAIA DA TRAIC AO",
        "time": "15H"
    },
    {
        "code": "197",
        "segment": "2",
        "name": "SAAE CASA NOVA",
        "time": "15H"
    },
    {
        "code": "199",
        "segment": "2",
        "name": "SERVICO MUNICIPAL DE  AGUA E ESGOTO DE CATU",
        "time": "15H"
    },
    {
        "code": "205",
        "segment": "2",
        "name": "SAAE FEIRA DA MATA",
        "time": "15H"
    },
    {
        "code": "209",
        "segment": "2",
        "name": "SAAE ITAJUIPE",
        "time": "15H"
    },
    {
        "code": "222",
        "segment": "2",
        "name": "SAAE SITIO DO MATO",
        "time": "15H"
    },
    {
        "code": "225",
        "segment": "2",
        "name": "SAAE XIQUE XIQUE",
        "time": "15H"
    },
    {
        "code": "228",
        "segment": "2",
        "name": "SAAE BALSAS",
        "time": "15H"
    },
    {
        "code": "230",
        "segment": "2",
        "name": "SAAE CAXIAS",
        "time": "15H"
    },
    {
        "code": "233",
        "segment": "2",
        "name": "SERV AUTONOMO DE  AGUA E ESGOTO DE ESTREITO",
        "time": "15H"
    },
    {
        "code": "236",
        "segment": "2",
        "name": "SAAE NOVA OLINDA DO MARANH AO",
        "time": "15H"
    },
    {
        "code": "238",
        "segment": "2",
        "name": "SAAE PASTOS BONS",
        "time": "15H"
    },
    {
        "code": "252",
        "segment": "2",
        "name": "SAAE ICAPUI CE",
        "time": "15H"
    },
    {
        "code": "253",
        "segment": "2",
        "name": "SERV AUT A/E IGUATU CE",
        "time": "15H"
    },
    {
        "code": "274",
        "segment": "2",
        "name": "SAAE CAMPESTRE DO MARANH AO",
        "time": "15H"
    },
    {
        "code": "277",
        "segment": "2",
        "name": "SAAE S AO JOAO DO SOTER",
        "time": "15H"
    },
    {
        "code": "279",
        "segment": "2",
        "name": "SAAE ALVORADA D OESTE",
        "time": "15H"
    },
    {
        "code": "282",
        "segment": "2",
        "name": "SAAE VOTORANTIM",
        "time": "15H"
    },
    {
        "code": "285",
        "segment": "2",
        "name": "SAAEC CERQUILHO",
        "time": "15H"
    },
    {
        "code": "286",
        "segment": "2",
        "name": " AGUAS DE PARANAGU A S A",
        "time": "15H"
    },
    {
        "code": "292",
        "segment": "2",
        "name": "SAAEB BEBEDOURO",
        "time": "15H"
    },
    {
        "code": "297",
        "segment": "2",
        "name": "SAAE VILHENA",
        "time": "15H"
    },
    {
        "code": "304",
        "segment": "2",
        "name": "SEMAE DE S AO JOSE DO RIO PRETO",
        "time": "15H"
    },
    {
        "code": "305",
        "segment": "2",
        "name": "SAAE DE S AO MATEUS",
        "time": "15H"
    },
    {
        "code": "307",
        "segment": "2",
        "name": "SAE DE SALTO",
        "time": "15H"
    },
    {
        "code": "311",
        "segment": "2",
        "name": "DEMAE CALDAS NOVAS",
        "time": "15H"
    },
    {
        "code": "312",
        "segment": "2",
        "name": "SAAE ALEGRE",
        "time": "15H"
    },
    {
        "code": "313",
        "segment": "2",
        "name": "DAE AMERICO BRASILIENSE",
        "time": "15H"
    },
    {
        "code": "314",
        "segment": "2",
        "name": "SAAE S AO LOURENCO",
        "time": "15H"
    },
    {
        "code": "315",
        "segment": "2",
        "name": "SAAE IBITINGA",
        "time": "15H"
    },
    {
        "code": "316",
        "segment": "2",
        "name": "SAE PORTO FERREIRA",
        "time": "15H"
    },
    {
        "code": "318",
        "segment": "2",
        "name": "SAAE GOVERNADOR VALADARES",
        "time": "15H"
    },
    {
        "code": "319",
        "segment": "2",
        "name": "CODEN NOVA ODESSA",
        "time": "15H"
    },
    {
        "code": "320",
        "segment": "2",
        "name": " AGUAS DO IMPERADOR",
        "time": "15H"
    },
    {
        "code": "322",
        "segment": "2",
        "name": " AGUAS DE JUTURNAIBA",
        "time": "15H"
    },
    {
        "code": "325",
        "segment": "2",
        "name": "SAAE DE ABADIANIA",
        "time": "15H"
    },
    {
        "code": "326",
        "segment": "2",
        "name": "SAAE CORUMBA",
        "time": "15H"
    },
    {
        "code": "327",
        "segment": "2",
        "name": "SAAE FAINA",
        "time": "15H"
    },
    {
        "code": "330",
        "segment": "2",
        "name": "DAE CARANGOLA",
        "time": "15H"
    },
    {
        "code": "334",
        "segment": "2",
        "name": "SAAE RIO PEDRAS",
        "time": "15H"
    },
    {
        "code": "336",
        "segment": "2",
        "name": "SAAE DE MANHUACU",
        "time": "15H"
    },
    {
        "code": "337",
        "segment": "2",
        "name": "SAMAE CAXIAS DO SUL",
        "time": "15H"
    },
    {
        "code": "341",
        "segment": "2",
        "name": "DAE RONDONOPOLISSANEAR RONDONOPOLIS ANTIGO DAE",
        "time": "15H"
    },
    {
        "code": "343",
        "segment": "2",
        "name": "PM CASTANHEIRAS",
        "time": "15H"
    },
    {
        "code": "348",
        "segment": "2",
        "name": "SAAE PIUMHI",
        "time": "15H"
    },
    {
        "code": "349",
        "segment": "2",
        "name": "DAE PATROCINIO",
        "time": "15H"
    },
    {
        "code": "352",
        "segment": "2",
        "name": "SAAE DE BOA ESPERANCA",
        "time": "15H"
    },
    {
        "code": "353",
        "segment": "2",
        "name": "SAAE MACHADO",
        "time": "15H"
    },
    {
        "code": "354",
        "segment": "2",
        "name": "SAAE TRES PONTAS",
        "time": "15H"
    },
    {
        "code": "357",
        "segment": "2",
        "name": "SAAE DE TIJUCAS",
        "time": "15H"
    },
    {
        "code": "358",
        "segment": "2",
        "name": "SERV.MUN.DE AGUA E ESGO",
        "time": "15H"
    },
    {
        "code": "361",
        "segment": "2",
        "name": "SAAE ITABIRITO",
        "time": "15H"
    },
    {
        "code": "362",
        "segment": "2",
        "name": "SAAE GUANHAES",
        "time": "15H"
    },
    {
        "code": "365",
        "segment": "2",
        "name": "SAAEB BELEM",
        "time": "15H"
    },
    {
        "code": "366",
        "segment": "2",
        "name": "SAE OLIVEIRA",
        "time": "15H"
    },
    {
        "code": "368",
        "segment": "2",
        "name": "DAE JACIARA",
        "time": "15H"
    },
    {
        "code": "370",
        "segment": "2",
        "name": "PROLAGOS S A CONS SERV PUBL  AGUA E ESGOTO CABO FRIO",
        "time": "15H"
    },
    {
        "code": "372",
        "segment": "2",
        "name": "SAAE BOCAIUVA",
        "time": "15H"
    },
    {
        "code": "374",
        "segment": "2",
        "name": "SERVICO AUTONOMO AGUA E ESGOTO DE BANDEIRANTES",
        "time": "15H"
    },
    {
        "code": "376",
        "segment": "2",
        "name": "SAAE DE CORGUINHO",
        "time": "15H"
    },
    {
        "code": "377",
        "segment": "2",
        "name": "SAEE JARAGUARI",
        "time": "15H"
    },
    {
        "code": "378",
        "segment": "2",
        "name": "DIRET MUN DE  AGUA E SANEAMENTO ROCHEDO",
        "time": "15H"
    },
    {
        "code": "379",
        "segment": "2",
        "name": "SAAE S AO GABRIEL DO OESTE",
        "time": "15H"
    },
    {
        "code": "380",
        "segment": "2",
        "name": "DMAES PONTE NOVA",
        "time": "15H"
    },
    {
        "code": "381",
        "segment": "2",
        "name": "DAE PARATY",
        "time": "15H"
    },
    {
        "code": "382",
        "segment": "2",
        "name": "DAE VARZEA GRANDE",
        "time": "15H"
    },
    {
        "code": "384",
        "segment": "2",
        "name": "SAAE DE QUATIS",
        "time": "15H"
    },
    {
        "code": "385",
        "segment": "2",
        "name": "SAAE DE ORATORIOS",
        "time": "15H"
    },
    {
        "code": "388",
        "segment": "2",
        "name": "DAE ILHA SOLTEIRA",
        "time": "15H"
    },
    {
        "code": "389",
        "segment": "2",
        "name": "SAAE CAETE",
        "time": "15H"
    },
    {
        "code": "390",
        "segment": "2",
        "name": "SAERB",
        "time": "15H"
    },
    {
        "code": "391",
        "segment": "2",
        "name": " AGUAS DO PARAIBA",
        "time": "15H"
    },
    {
        "code": "394",
        "segment": "2",
        "name": "DAMAE  S AO JO AO DEL REI",
        "time": "15H"
    },
    {
        "code": "399",
        "segment": "2",
        "name": "SERV AUT A/E CAMBUI MG",
        "time": "15H"
    },
    {
        "code": "400",
        "segment": "2",
        "name": "SAAE DE BURITIZEIRO MG",
        "time": "15H"
    },
    {
        "code": "402",
        "segment": "2",
        "name": "DAE TUPACIGUARA",
        "time": "15H"
    },
    {
        "code": "406",
        "segment": "2",
        "name": "SAAE PRIMAVERA DE RONDONIA",
        "time": "15H"
    },
    {
        "code": "408",
        "segment": "2",
        "name": "DAE PARAISO",
        "time": "15H"
    },
    {
        "code": "411",
        "segment": "2",
        "name": "SERV AUTONOMO DE  AGUA E ESGOTO DE BREJINHO",
        "time": "15H"
    },
    {
        "code": "412",
        "segment": "2",
        "name": "SAAE MAXARANGUAPE",
        "time": "15H"
    },
    {
        "code": "415",
        "segment": "2",
        "name": "SAAE DE SANTA CRUZ",
        "time": "15H"
    },
    {
        "code": "416",
        "segment": "2",
        "name": "SAAE S AO GONCALO DO AMARANTE",
        "time": "15H"
    },
    {
        "code": "419",
        "segment": "2",
        "name": "SAAE RIO BANANAL",
        "time": "15H"
    },
    {
        "code": "420",
        "segment": "2",
        "name": "SAAE ABRE CAMPO",
        "time": "15H"
    },
    {
        "code": "421",
        "segment": "2",
        "name": "ESAMUR",
        "time": "15H"
    },
    {
        "code": "422",
        "segment": "2",
        "name": "CONSORCIO  AGUAS DE MIRASSOL",
        "time": "15H"
    },
    {
        "code": "424",
        "segment": "2",
        "name": "DAE GUARARAPES",
        "time": "15H"
    },
    {
        "code": "425",
        "segment": "2",
        "name": "PREFEITURA MUNICIPAL DE LOUVEIRA SERVICO DE  AGUA",
        "time": "15H"
    },
    {
        "code": "427",
        "segment": "2",
        "name": "SAAE PIRAPORA",
        "time": "15H"
    },
    {
        "code": "428",
        "segment": "2",
        "name": "DAE SERTAOZINHO",
        "time": "15H"
    },
    {
        "code": "429",
        "segment": "2",
        "name": "SAEC CATANDUVA",
        "time": "15H"
    },
    {
        "code": "436",
        "segment": "2",
        "name": "SEMAE MORRO GRANDE",
        "time": "15H"
    },
    {
        "code": "438",
        "segment": "2",
        "name": "SAAE DE JAMPRUCA",
        "time": "15H"
    },
    {
        "code": "440",
        "segment": "2",
        "name": "SAAE DE MARECHAL CANDIDO",
        "time": "15H"
    },
    {
        "code": "443",
        "segment": "2",
        "name": "SAE VARGEM GRANDE DO SUL",
        "time": "15H"
    },
    {
        "code": "446",
        "segment": "2",
        "name": "CENF CONCESSIONARIA DE AGUA E ESGOTO DE NOVA FRIBURGO",
        "time": "15H"
    },
    {
        "code": "448",
        "segment": "2",
        "name": "SAAE PIMENTA",
        "time": "15H"
    },
    {
        "code": "449",
        "segment": "2",
        "name": "SAMAE TANGAR A DA SERRA",
        "time": "15H"
    },
    {
        "code": "451",
        "segment": "2",
        "name": "PM DE NOVA OLIMPIA",
        "time": "15H"
    },
    {
        "code": "463",
        "segment": "2",
        "name": "DAE BOM JESUS DOS PERDOES",
        "time": "15H"
    },
    {
        "code": "467",
        "segment": "2",
        "name": "SANEAR COLATINA",
        "time": "15H"
    },
    {
        "code": "469",
        "segment": "2",
        "name": "SAAE GUAPE",
        "time": "15H"
    },
    {
        "code": "470",
        "segment": "2",
        "name": "SAAE S AO MIGUEL DOS CAMPOS",
        "time": "15H"
    },
    {
        "code": "473",
        "segment": "2",
        "name": "SAAE LAMBARI",
        "time": "15H"
    },
    {
        "code": "476",
        "segment": "2",
        "name": "SAAE DE ITAMBACURI",
        "time": "15H"
    },
    {
        "code": "477",
        "segment": "2",
        "name": "AGUAS DO AMAZANOAS",
        "time": "15H"
    },
    {
        "code": "478",
        "segment": "2",
        "name": "SAAE ITABIRA",
        "time": "15H"
    },
    {
        "code": "479",
        "segment": "2",
        "name": "AGUAS DE NITEROI",
        "time": "15H"
    },
    {
        "code": "480",
        "segment": "2",
        "name": "SAAE DE LASSANCE",
        "time": "15H"
    },
    {
        "code": "483",
        "segment": "2",
        "name": "SAS DE BARBACENA",
        "time": "15H"
    },
    {
        "code": "488",
        "segment": "2",
        "name": "SAEEC CRATO",
        "time": "15H"
    },
    {
        "code": "493",
        "segment": "2",
        "name": "SAAE ITACOATIARA",
        "time": "15H"
    },
    {
        "code": "494",
        "segment": "2",
        "name": "SAAE MAUES",
        "time": "15H"
    },
    {
        "code": "495",
        "segment": "2",
        "name": "SAAE DE URUCARA",
        "time": "15H"
    },
    {
        "code": "498",
        "segment": "2",
        "name": "SERV AUTONOMO DE  AGUA E ESGOTO DE PARINTINS",
        "time": "15H"
    },
    {
        "code": "499",
        "segment": "2",
        "name": "SAAE PRESIDENTE FIGUEREDO",
        "time": "15H"
    },
    {
        "code": "500",
        "segment": "2",
        "name": "PM DE GAVIAO PEIXOTO",
        "time": "15H"
    },
    {
        "code": "505",
        "segment": "2",
        "name": "DAEV",
        "time": "15H"
    },
    {
        "code": "506",
        "segment": "2",
        "name": "SAEP POTIRENDABA",
        "time": "15H"
    },
    {
        "code": "508",
        "segment": "2",
        "name": "EMDAEP EMPRESA MUN DE DESENVOL DE AGUA ESGOTO E",
        "time": "15H"
    },
    {
        "code": "513",
        "segment": "2",
        "name": "DEPARTAMENTO MUNICIPAL AUTONOMO DE  AGUA E ESGOTO DE",
        "time": "15H"
    },
    {
        "code": "516",
        "segment": "2",
        "name": "SAAE DE ANGRA DOS REIS",
        "time": "15H"
    },
    {
        "code": "518",
        "segment": "2",
        "name": "PM TXS BOM PRINCIPIO",
        "time": "15H"
    },
    {
        "code": "520",
        "segment": "2",
        "name": "PREFEITURA MUNICIPAL DE DENISE",
        "time": "15H"
    },
    {
        "code": "522",
        "segment": "2",
        "name": "DMAEG GUIRATINGA",
        "time": "15H"
    },
    {
        "code": "524",
        "segment": "2",
        "name": "SAAE PEDREIRA",
        "time": "15H"
    },
    {
        "code": "525",
        "segment": "2",
        "name": "SAE BATATAIS",
        "time": "15H"
    },
    {
        "code": "527",
        "segment": "2",
        "name": " AGUAS DE SORRISO",
        "time": "15H"
    },
    {
        "code": "532",
        "segment": "2",
        "name": "PREFEITURA MUNICIPAL DE S AO JOSE DO RIO PARDO",
        "time": "15H"
    },
    {
        "code": "533",
        "segment": "2",
        "name": "SAMAE ARARANGUA",
        "time": "15H"
    },
    {
        "code": "534",
        "segment": "2",
        "name": "AGUAS GUARIROBA",
        "time": "15H"
    },
    {
        "code": "543",
        "segment": "2",
        "name": "AGUAS DE ARENOPOLIS",
        "time": "15H"
    },
    {
        "code": "544",
        "segment": "2",
        "name": "SAAE COCOS",
        "time": "15H"
    },
    {
        "code": "548",
        "segment": "2",
        "name": "SAAE DE BARRO PRETO",
        "time": "15H"
    },
    {
        "code": "554",
        "segment": "2",
        "name": " AGUAS DE PEIXOTO AZEVEDO GRUPO KULLINAN",
        "time": "15H"
    },
    {
        "code": "557",
        "segment": "2",
        "name": "SERV AUT DE  AGUA E ESGOTO DE BARCELOS",
        "time": "15H"
    },
    {
        "code": "558",
        "segment": "2",
        "name": "SAEE BOA VISTA DO RAMOS",
        "time": "15H"
    },
    {
        "code": "559",
        "segment": "2",
        "name": "SAAE  S AO SEBASTI AO DO UATUM A",
        "time": "15H"
    },
    {
        "code": "578",
        "segment": "2",
        "name": "SAAE SANTA ISABEL DO PARA",
        "time": "15H"
    },
    {
        "code": "586",
        "segment": "2",
        "name": "DAE TOME ACU",
        "time": "15H"
    },
    {
        "code": "590",
        "segment": "2",
        "name": "SAAE BOCA DA MATA",
        "time": "15H"
    },
    {
        "code": "595",
        "segment": "2",
        "name": "SAAE MARECHAL DEODORO",
        "time": "15H"
    },
    {
        "code": "598",
        "segment": "2",
        "name": "SAAE PORTO REAL DO COLEGIO",
        "time": "15H"
    },
    {
        "code": "606",
        "segment": "2",
        "name": "SAAE COSMORAMA",
        "time": "15H"
    },
    {
        "code": "607",
        "segment": "2",
        "name": "SAAE IBIRACU",
        "time": "15H"
    },
    {
        "code": "609",
        "segment": "2",
        "name": "SERVICO AUTONOMO DE AGUA E ESGOTO DE MARILANDIA",
        "time": "15H"
    },
    {
        "code": "612",
        "segment": "2",
        "name": "EMDHOSP",
        "time": "15H"
    },
    {
        "code": "614",
        "segment": "2",
        "name": " AGUAS DE P0NTES E LACERDA",
        "time": "15H"
    },
    {
        "code": "615",
        "segment": "2",
        "name": "SAG GUARACAI",
        "time": "15H"
    },
    {
        "code": "618",
        "segment": "2",
        "name": "SAAE GONZAGA",
        "time": "15H"
    },
    {
        "code": "619",
        "segment": "2",
        "name": "PM SANTA BRANCA AGUA",
        "time": "15H"
    },
    {
        "code": "620",
        "segment": "2",
        "name": "DAE GUAPIACU",
        "time": "15H"
    },
    {
        "code": "621",
        "segment": "2",
        "name": "DAE B BUGRES",
        "time": "15H"
    },
    {
        "code": "622",
        "segment": "2",
        "name": "SANESSOL",
        "time": "15H"
    },
    {
        "code": "626",
        "segment": "2",
        "name": "DAE COSMOPOLIS",
        "time": "15H"
    },
    {
        "code": "627",
        "segment": "2",
        "name": "PM DE DOM AQUINO",
        "time": "15H"
    },
    {
        "code": "629",
        "segment": "2",
        "name": "PM DE POXOREU",
        "time": "15H"
    },
    {
        "code": "630",
        "segment": "2",
        "name": "PM STO Antonio DO LEVERGER",
        "time": "15H"
    },
    {
        "code": "631",
        "segment": "2",
        "name": "DAE NOSSA SENHORA DO LIVRAMENTO",
        "time": "15H"
    },
    {
        "code": "632",
        "segment": "2",
        "name": "DAE CAMPO NOVO DO PARECIS",
        "time": "15H"
    },
    {
        "code": "639",
        "segment": "2",
        "name": "PM PONTAL DO ARAGUAIA",
        "time": "15H"
    },
    {
        "code": "641",
        "segment": "2",
        "name": "DAE S AO PEDRO DO TURVO",
        "time": "15H"
    },
    {
        "code": "642",
        "segment": "2",
        "name": "SAE MORRO AGUDO",
        "time": "15H"
    },
    {
        "code": "643",
        "segment": "2",
        "name": "PM DE ITAPURA",
        "time": "15H"
    },
    {
        "code": "644",
        "segment": "2",
        "name": "JARI CELULOSE S A  SERVICOS DE  AGUA E ESGOTO",
        "time": "15H"
    },
    {
        "code": "647",
        "segment": "2",
        "name": "DAE CERQUEIRA CESAR",
        "time": "15H"
    },
    {
        "code": "652",
        "segment": "2",
        "name": "CIA AUTONOMA DE  AGUA  ESGOTO E SANEAMENTO DE ITINGA",
        "time": "15H"
    },
    {
        "code": "653",
        "segment": "2",
        "name": "PM CASTILHO",
        "time": "15H"
    },
    {
        "code": "655",
        "segment": "2",
        "name": "DAEP",
        "time": "15H"
    },
    {
        "code": "660",
        "segment": "2",
        "name": "DAE PINDORAMA",
        "time": "15H"
    },
    {
        "code": "661",
        "segment": "2",
        "name": "SAE BROTAS",
        "time": "15H"
    },
    {
        "code": "662",
        "segment": "2",
        "name": "PM DE TERRA NOVA DO NORTE",
        "time": "15H"
    },
    {
        "code": "664",
        "segment": "2",
        "name": "AGUAS DE GUARANTA",
        "time": "15H"
    },
    {
        "code": "667",
        "segment": "2",
        "name": "DAE ALTO TAQUARI",
        "time": "15H"
    },
    {
        "code": "668",
        "segment": "2",
        "name": "AGUAS DE BARCARENA",
        "time": "15H"
    },
    {
        "code": "670",
        "segment": "2",
        "name": "SAE FONTES DA SERRA GUAPIMIRIM",
        "time": "15H"
    },
    {
        "code": "671",
        "segment": "2",
        "name": "DAE S AO JOSE DOS QUATRO MARCOS",
        "time": "15H"
    },
    {
        "code": "673",
        "segment": "2",
        "name": "SAE CHAPADA DOS GUIMAR AES",
        "time": "15H"
    },
    {
        "code": "676",
        "segment": "2",
        "name": "SERV AUTONOMO DE  AGUA E ESGOTO DE MANACAPURU",
        "time": "15H"
    },
    {
        "code": "677",
        "segment": "2",
        "name": "DAE COMODORO",
        "time": "15H"
    },
    {
        "code": "678",
        "segment": "2",
        "name": "SEMUSA",
        "time": "15H"
    },
    {
        "code": "682",
        "segment": "2",
        "name": "SAAE S AO SIMAO",
        "time": "15H"
    },
    {
        "code": "684",
        "segment": "2",
        "name": "DAE ALTO PARAGUAI",
        "time": "15H"
    },
    {
        "code": "685",
        "segment": "2",
        "name": "DAE PARANAITA",
        "time": "15H"
    },
    {
        "code": "690",
        "segment": "2",
        "name": "PREF MUN DE PANORAMA SP",
        "time": "15H"
    },
    {
        "code": "691",
        "segment": "2",
        "name": "PM PITANGUEIRAS",
        "time": "15H"
    },
    {
        "code": "693",
        "segment": "2",
        "name": "SERV AUT DE  AGUA E ESGOTO DE LAJINHA",
        "time": "15H"
    },
    {
        "code": "694",
        "segment": "2",
        "name": "SAAE DE NOVA BRASILANDIA",
        "time": "15H"
    },
    {
        "code": "695",
        "segment": "2",
        "name": "SAAE PIRAJUI",
        "time": "15H"
    },
    {
        "code": "698",
        "segment": "2",
        "name": "PM ITIRAPINA",
        "time": "15H"
    },
    {
        "code": "699",
        "segment": "2",
        "name": "DAE GUAIRA",
        "time": "15H"
    },
    {
        "code": "701",
        "segment": "2",
        "name": "DAES JUINA",
        "time": "15H"
    },
    {
        "code": "703",
        "segment": "2",
        "name": "PM DE ALTO DO ARAGUAIA",
        "time": "15H"
    },
    {
        "code": "704",
        "segment": "2",
        "name": "DAAE PENAPOLIS",
        "time": "15H"
    },
    {
        "code": "707",
        "segment": "2",
        "name": "SAE DE AGU AS DE MATUP A",
        "time": "15H"
    },
    {
        "code": "708",
        "segment": "2",
        "name": "SAE URUPES",
        "time": "15H"
    },
    {
        "code": "709",
        "segment": "2",
        "name": "PM DE RANCHARIA",
        "time": "15H"
    },
    {
        "code": "710",
        "segment": "2",
        "name": "SAE CATALAO",
        "time": "15H"
    },
    {
        "code": "712",
        "segment": "2",
        "name": "SAAEI  IPU A",
        "time": "15H"
    },
    {
        "code": "714",
        "segment": "2",
        "name": "SAAE DE GOVERNADOR LINDENBERG",
        "time": "15H"
    },
    {
        "code": "715",
        "segment": "2",
        "name": " AGUAS DE SANTA CARMEM  GRUPO KULLINAN",
        "time": "15H"
    },
    {
        "code": "716",
        "segment": "2",
        "name": "SAE STO AFONSO",
        "time": "15H"
    },
    {
        "code": "718",
        "segment": "2",
        "name": "PREFEITURA MUNICIPAL DE AGUA BOA",
        "time": "15H"
    },
    {
        "code": "720",
        "segment": "2",
        "name": "SAE TAIACU",
        "time": "15H"
    },
    {
        "code": "721",
        "segment": "2",
        "name": "PM DE IPAUSSU",
        "time": "15H"
    },
    {
        "code": "723",
        "segment": "2",
        "name": "PM JAGUARIUNA",
        "time": "15H"
    },
    {
        "code": "725",
        "segment": "2",
        "name": "SAMOTRACIA EMPREENDIMENTOS LTDA SERVICOS DE",
        "time": "15H"
    },
    {
        "code": "730",
        "segment": "2",
        "name": "SAAE SANTA ISABEL",
        "time": "15H"
    },
    {
        "code": "731",
        "segment": "2",
        "name": "SAAE NOVA UBIRATA",
        "time": "15H"
    },
    {
        "code": "732",
        "segment": "2",
        "name": " AGUAS DE CAMPO VERDE GRUPO KULLINAN",
        "time": "15H"
    },
    {
        "code": "738",
        "segment": "2",
        "name": "PM S AO JOSE DO RIO CLARO",
        "time": "15H"
    },
    {
        "code": "739",
        "segment": "2",
        "name": "SAEMAS",
        "time": "15H"
    },
    {
        "code": "746",
        "segment": "2",
        "name": "SAAE DE PEREIRA BARRETO",
        "time": "15H"
    },
    {
        "code": "762",
        "segment": "2",
        "name": " AGUAS DE PRIMAVERA GRUPO KULLINAN",
        "time": "15H"
    },
    {
        "code": "765",
        "segment": "2",
        "name": "PM DE RINC AO",
        "time": "15H"
    },
    {
        "code": "766",
        "segment": "2",
        "name": "SANELIDER",
        "time": "15H"
    },
    {
        "code": "767",
        "segment": "2",
        "name": "PM DE ARIPUAN A",
        "time": "15H"
    },
    {
        "code": "768",
        "segment": "2",
        "name": "SANECAP",
        "time": "15H"
    },
    {
        "code": "769",
        "segment": "2",
        "name": "PM ITANHANDU",
        "time": "15H"
    },
    {
        "code": "771",
        "segment": "2",
        "name": "SAAE APARECIDA",
        "time": "15H"
    },
    {
        "code": "772",
        "segment": "2",
        "name": "DMAE VICENTI",
        "time": "15H"
    },
    {
        "code": "775",
        "segment": "2",
        "name": "PM de Piracema",
        "time": "15H"
    },
    {
        "code": "780",
        "segment": "2",
        "name": "PREFEITURA MUNICIPAL DE CORUMBATAI CONTA DE  AGUA",
        "time": "15H"
    },
    {
        "code": "782",
        "segment": "2",
        "name": "OURILANDIA N",
        "time": "15H"
    },
    {
        "code": "785",
        "segment": "2",
        "name": " AGUAS DE NORTEL ANDIA",
        "time": "15H"
    },
    {
        "code": "786",
        "segment": "2",
        "name": "AGUA PM CAICARA",
        "time": "15H"
    },
    {
        "code": "787",
        "segment": "2",
        "name": "SAAE TEFE",
        "time": "15H"
    },
    {
        "code": "789",
        "segment": "2",
        "name": "DAE JURUENA",
        "time": "15H"
    },
    {
        "code": "790",
        "segment": "2",
        "name": "SERV AUTONOMO DE  AGUA E ESGOTO DE ENGENHEIRO COELHO",
        "time": "15H"
    },
    {
        "code": "791",
        "segment": "2",
        "name": "SAMAE DE SANG AO",
        "time": "15H"
    },
    {
        "code": "792",
        "segment": "2",
        "name": "PM DE NEVES PAULISTA",
        "time": "15H"
    },
    {
        "code": "793",
        "segment": "2",
        "name": "SERV AUTONOMO DE  AGUA E ESGOTO DE PARAISOPOLIS",
        "time": "15H"
    },
    {
        "code": "796",
        "segment": "2",
        "name": "PREFEITURA MUNICIPAL DE NOVA SANTA HELENA",
        "time": "15H"
    },
    {
        "code": "798",
        "segment": "2",
        "name": "CORSAN",
        "time": "15H"
    },
    {
        "code": "801",
        "segment": "2",
        "name": " AGUAS DE UNI AO DO SUL  GRUPO KULLINAN",
        "time": "15H"
    },
    {
        "code": "802",
        "segment": "2",
        "name": " AGUAS DE ALTA FLORESTA",
        "time": "15H"
    },
    {
        "code": "807",
        "segment": "2",
        "name": "SAAE POMPEIA",
        "time": "15H"
    },
    {
        "code": "812",
        "segment": "2",
        "name": "DAE CEDRAL",
        "time": "15H"
    },
    {
        "code": "815",
        "segment": "2",
        "name": "DAE PARISI",
        "time": "15H"
    },
    {
        "code": "816",
        "segment": "2",
        "name": "SAMAE TIMBO",
        "time": "15H"
    },
    {
        "code": "819",
        "segment": "2",
        "name": "PM DE OURO VERDE",
        "time": "15H"
    },
    {
        "code": "822",
        "segment": "2",
        "name": "PREFEITURA MUNICIPAL DE VILA BELA DA SANTISSIMA TRINDADE",
        "time": "15H"
    },
    {
        "code": "824",
        "segment": "2",
        "name": "PM EST H M ALEGRE SUL",
        "time": "15H"
    },
    {
        "code": "834",
        "segment": "2",
        "name": "PREFEITURA MUNCIPAL DE SANTA ADELIA",
        "time": "15H"
    },
    {
        "code": "835",
        "segment": "2",
        "name": " AGUAS DE MONTE AZUL PAULISTA",
        "time": "15H"
    },
    {
        "code": "836",
        "segment": "2",
        "name": "PM PATROCINIO PAULISTA AGUA",
        "time": "15H"
    },
    {
        "code": "843",
        "segment": "2",
        "name": "SEMASA LAGES",
        "time": "15H"
    },
    {
        "code": "845",
        "segment": "2",
        "name": "SEMASA  SERVICO MUNIC DE  AGUA SANEAMENTO E INFRA",
        "time": "15H"
    },
    {
        "code": "846",
        "segment": "2",
        "name": "DEPARTAMENTO DE  AGUA E ESGOTO DE PORTO REAL",
        "time": "15H"
    },
    {
        "code": "849",
        "segment": "2",
        "name": "PM DESCALVADO",
        "time": "15H"
    },
    {
        "code": "853",
        "segment": "2",
        "name": "SAAE RIO PRETO DA EVA",
        "time": "15H"
    },
    {
        "code": "859",
        "segment": "2",
        "name": "DAE DE RINOPOLIS",
        "time": "15H"
    },
    {
        "code": "866",
        "segment": "2",
        "name": "SAMAE TREVISO",
        "time": "15H"
    },
    {
        "code": "868",
        "segment": "2",
        "name": "SAAE DE ANAJATUBA",
        "time": "15H"
    },
    {
        "code": "870",
        "segment": "2",
        "name": " AGUAS DE MARCEL ANDIA  GRUPO KULLINAN",
        "time": "15H"
    },
    {
        "code": "877",
        "segment": "2",
        "name": "SAAE DUMONT",
        "time": "15H"
    },
    {
        "code": "878",
        "segment": "2",
        "name": "DEDIAC DO CAREIRO",
        "time": "15H"
    },
    {
        "code": "883",
        "segment": "2",
        "name": "SAAE DE CRUZEIRO",
        "time": "15H"
    },
    {
        "code": "885",
        "segment": "2",
        "name": "SAE MURUTINGA DO SUL",
        "time": "15H"
    },
    {
        "code": "887",
        "segment": "2",
        "name": "SANEAMENTO B ASICO DE PEDRA PRETA GRUPO KULLINAN",
        "time": "15H"
    },
    {
        "code": "888",
        "segment": "2",
        "name": "PM PANAMA",
        "time": "15H"
    },
    {
        "code": "907",
        "segment": "2",
        "name": "DEMAE DEP MUNICIPAL DE AGUA E ESGOTO DA PM DE RIO",
        "time": "15H"
    },
    {
        "code": "908",
        "segment": "2",
        "name": " AGUAS DE VERA  GRUPO KULLINAN",
        "time": "15H"
    },
    {
        "code": "909",
        "segment": "2",
        "name": "PM NOVA ARIPUANA",
        "time": "15H"
    },
    {
        "code": "910",
        "segment": "2",
        "name": "AGUAS ITAPEMA",
        "time": "15H"
    },
    {
        "code": "911",
        "segment": "2",
        "name": "SANEFRAI",
        "time": "15H"
    },
    {
        "code": "915",
        "segment": "2",
        "name": "COHASB",
        "time": "15H"
    },
    {
        "code": "918",
        "segment": "2",
        "name": "SAAE SAO PEDRO",
        "time": "15H"
    },
    {
        "code": "919",
        "segment": "2",
        "name": "SAAE CRAVINHOS",
        "time": "15H"
    },
    {
        "code": "926",
        "segment": "2",
        "name": "E J W  CONCES SERV ABAST  AGUA  MUN BALNE ARIO DO  ARROIO",
        "time": "15H"
    },
    {
        "code": "927",
        "segment": "2",
        "name": "JOINVILE A E",
        "time": "15H"
    },
    {
        "code": "928",
        "segment": "2",
        "name": "SOUZA INDIVIDUALIZADORA E ADMINISTRADORA DE  AGUA DE",
        "time": "15H"
    },
    {
        "code": "929",
        "segment": "2",
        "name": "SAE  JANGADA",
        "time": "15H"
    },
    {
        "code": "930",
        "segment": "2",
        "name": "NATURAGUA",
        "time": "15H"
    },
    {
        "code": "931",
        "segment": "2",
        "name": " AGUAS DE SANTO ANTONIO",
        "time": "15H"
    },
    {
        "code": "934",
        "segment": "2",
        "name": "SAAE DE ARAREND A",
        "time": "15H"
    },
    {
        "code": "936",
        "segment": "2",
        "name": "SAAE FORMOSA DA SERRA NEGRA",
        "time": "15H"
    },
    {
        "code": "937",
        "segment": "2",
        "name": "PM LAVINIA",
        "time": "15H"
    },
    {
        "code": "944",
        "segment": "2",
        "name": "SAAE DE PACO LUNIAR",
        "time": "15H"
    },
    {
        "code": "945",
        "segment": "2",
        "name": "SAAE MINEIROS GO",
        "time": "15H"
    },
    {
        "code": "950",
        "segment": "2",
        "name": "PM DE CONCHAL",
        "time": "15H"
    },
    {
        "code": "958",
        "segment": "2",
        "name": "SAAE S AO CRISTOV AO",
        "time": "15H"
    },
    {
        "code": "961",
        "segment": "2",
        "name": "JOINVILE A E",
        "time": "15H"
    },
    {
        "code": "966",
        "segment": "2",
        "name": "SAAE CAIUA",
        "time": "15H"
    },
    {
        "code": "968",
        "segment": "2",
        "name": "DAE IPEUNA",
        "time": "15H"
    },
    {
        "code": "969",
        "segment": "2",
        "name": "F M S FUND M SAN",
        "time": "15H"
    },
    {
        "code": "977",
        "segment": "2",
        "name": "SERVICO DE SANEAMENTO BASICO SESB CAMBORIU",
        "time": "15H"
    },
    {
        "code": "984",
        "segment": "2",
        "name": "PM DORES DE GUANHAES",
        "time": "15H"
    },
    {
        "code": "990",
        "segment": "2",
        "name": "CAE ACORIZAL",
        "time": "15H"
    },
    {
        "code": "995",
        "segment": "2",
        "name": "DMAAT TEUTONIA",
        "time": "15H"
    },
    {
        "code": "997",
        "segment": "2",
        "name": "PM DE BARAO DE MELGACO",
        "time": "15H"
    },
    {
        "code": "999",
        "segment": "2",
        "name": "SASB BRAUNA",
        "time": "15H"
    },
    {
        "code": "1001",
        "segment": "2",
        "name": "DAESC CORURIPE",
        "time": "15H"
    },
    {
        "code": "1002",
        "segment": "2",
        "name": "DAE DA PREFEITURA MUNICIPAL DE MARIALVA",
        "time": "15H"
    },
    {
        "code": "1003",
        "segment": "2",
        "name": "SAMAE PAPANDUVA",
        "time": "15H"
    },
    {
        "code": "1005",
        "segment": "2",
        "name": "SAE ARAPORA",
        "time": "15H"
    },
    {
        "code": "1006",
        "segment": "2",
        "name": "ASSOC PRO LANGUIRU",
        "time": "15H"
    },
    {
        "code": "1007",
        "segment": "2",
        "name": "AMAE CACHOEIRA DE MACACU",
        "time": "15H"
    },
    {
        "code": "1008",
        "segment": "2",
        "name": "PM JULIO MESQUITA",
        "time": "15H"
    },
    {
        "code": "1011",
        "segment": "2",
        "name": "PORTO INDIVIDUALIZADORA",
        "time": "15H"
    },
    {
        "code": "1012",
        "segment": "2",
        "name": "SAEMI MIRASSOL D OESTE",
        "time": "15H"
    },
    {
        "code": "1014",
        "segment": "2",
        "name": "PM DE GLORIA D OESTE",
        "time": "15H"
    },
    {
        "code": "1017",
        "segment": "2",
        "name": "PREFEITURA MUNICPAL DE MENDONCA  SERVICO DE  AGUA",
        "time": "15H"
    },
    {
        "code": "1025",
        "segment": "2",
        "name": "SAE TABATINGA",
        "time": "15H"
    },
    {
        "code": "1027",
        "segment": "2",
        "name": "EMASA BALNEARIO CAMBORIU",
        "time": "15H"
    },
    {
        "code": "1033",
        "segment": "2",
        "name": "PM ARAPUTANGA",
        "time": "15H"
    },
    {
        "code": "1037",
        "segment": "2",
        "name": "PM TUBARAO",
        "time": "15H"
    },
    {
        "code": "1040",
        "segment": "2",
        "name": "PM ITAUBA DAE",
        "time": "15H"
    },
    {
        "code": "1044",
        "segment": "2",
        "name": "SAAEI   SERV AUT A E DE IBIRAREMA",
        "time": "15H"
    },
    {
        "code": "1056",
        "segment": "2",
        "name": "PREFEITURA MUNICIPAL DE TOCOS DE MOJI",
        "time": "15H"
    },
    {
        "code": "1058",
        "segment": "2",
        "name": "AGUAS SCHROEDER",
        "time": "15H"
    },
    {
        "code": "1059",
        "segment": "2",
        "name": "EMBRASA",
        "time": "15H"
    },
    {
        "code": "1064",
        "segment": "2",
        "name": "SAE JARDINOPOLIS",
        "time": "15H"
    },
    {
        "code": "1072",
        "segment": "2",
        "name": "SAEMBA BARIRI",
        "time": "15H"
    },
    {
        "code": "1073",
        "segment": "2",
        "name": "PREFEITURA MUNICIPAL DE FONTE BOA",
        "time": "15H"
    },
    {
        "code": "1075",
        "segment": "2",
        "name": "SAAE CARMO DO CAJURU",
        "time": "15H"
    },
    {
        "code": "1076",
        "segment": "2",
        "name": "SAAE DE SANTA TEREZINHA",
        "time": "15H"
    },
    {
        "code": "1079",
        "segment": "2",
        "name": "PM DE CACHOEIRA DOURADA",
        "time": "15H"
    },
    {
        "code": "1080",
        "segment": "2",
        "name": "SAMAE SOMBRIO",
        "time": "15H"
    },
    {
        "code": "1085",
        "segment": "2",
        "name": "PREFEITURA MUNICIPAL DE GUARAMIRIM   AGUA E ESGOTO",
        "time": "15H"
    },
    {
        "code": "1086",
        "segment": "2",
        "name": "SAAE IRANDUBA",
        "time": "15H"
    },
    {
        "code": "1094",
        "segment": "2",
        "name": "SEMAE CAJOBI",
        "time": "15H"
    },
    {
        "code": "1097",
        "segment": "2",
        "name": "DAE CASSILANDIA",
        "time": "15H"
    },
    {
        "code": "1098",
        "segment": "2",
        "name": "PM PALHOCA",
        "time": "15H"
    },
    {
        "code": "1099",
        "segment": "2",
        "name": "PM DE LUISBURGO",
        "time": "15H"
    },
    {
        "code": "1100",
        "segment": "2",
        "name": "CORSAN",
        "time": "15H"
    },
    {
        "code": "1102",
        "segment": "2",
        "name": "SAAE RIBEIRAO DO LARGO",
        "time": "15H"
    },
    {
        "code": "1103",
        "segment": "2",
        "name": " AGUAS COMODORO",
        "time": "15H"
    },
    {
        "code": "1105",
        "segment": "2",
        "name": " AGUAS ITU",
        "time": "15H"
    },
    {
        "code": "1106",
        "segment": "2",
        "name": " AGUAS DE NOVO PROGRESSO TRATAMENTO E DISTRIBUIDORA",
        "time": "15H"
    },
    {
        "code": "1108",
        "segment": "2",
        "name": "SANDRINI E BOTEGAL",
        "time": "15H"
    },
    {
        "code": "1109",
        "segment": "2",
        "name": "AGUA DE MINEIROS DO TIETE",
        "time": "15H"
    },
    {
        "code": "1111",
        "segment": "2",
        "name": "SAMAE JUSSARA",
        "time": "15H"
    },
    {
        "code": "1113",
        "segment": "2",
        "name": " AGUAS DAS AGULHAS NEGRAS",
        "time": "15H"
    },
    {
        "code": "1115",
        "segment": "2",
        "name": "SANEAMENTO AMBIENTAL DE VIRADOURO   SAV",
        "time": "15H"
    },
    {
        "code": "1116",
        "segment": "2",
        "name": "COPANOR",
        "time": "15H"
    },
    {
        "code": "1119",
        "segment": "2",
        "name": "ESAP PALESTINA",
        "time": "15H"
    },
    {
        "code": "1128",
        "segment": "2",
        "name": "COMUSA",
        "time": "15H"
    },
    {
        "code": "1132",
        "segment": "2",
        "name": "SAE JOSE BONIF ACIO",
        "time": "15H"
    },
    {
        "code": "1137",
        "segment": "2",
        "name": "PM DE BELTERRA PA",
        "time": "15H"
    },
    {
        "code": "1138",
        "segment": "2",
        "name": "AGUAS DE POCONE MT",
        "time": "15H"
    },
    {
        "code": "1139",
        "segment": "2",
        "name": "SAAE DOIS CORREGOS",
        "time": "15H"
    },
    {
        "code": "1143",
        "segment": "2",
        "name": "PM ITAJU",
        "time": "15H"
    },
    {
        "code": "1146",
        "segment": "2",
        "name": "PM MONTE ALEGRE DE MINAS",
        "time": "15H"
    },
    {
        "code": "1152",
        "segment": "2",
        "name": "PM DOM BOSCO",
        "time": "15H"
    },
    {
        "code": "1153",
        "segment": "2",
        "name": "PREFEITURA MUNICIPAL DE CAPITAO ANDRADE SMAE",
        "time": "15H"
    },
    {
        "code": "1160",
        "segment": "2",
        "name": "CAESC DE COARI",
        "time": "15H"
    },
    {
        "code": "1167",
        "segment": "2",
        "name": "PM DE SANTA GERTRUDES",
        "time": "15H"
    },
    {
        "code": "1172",
        "segment": "2",
        "name": "AGUA TRES PALMEIRAS",
        "time": "15H"
    },
    {
        "code": "1175",
        "segment": "2",
        "name": "SANEPAR DE PARAGOMINAS",
        "time": "15H"
    },
    {
        "code": "1183",
        "segment": "2",
        "name": "SERV  AUTONOMO DE  AGUA E ESGOTO DE PITANGUEIRAS",
        "time": "15H"
    },
    {
        "code": "1184",
        "segment": "2",
        "name": "SEMAIS CANELINHA",
        "time": "15H"
    },
    {
        "code": "1185",
        "segment": "2",
        "name": "DEMAE  NOVA MARIL ANDIA",
        "time": "15H"
    },
    {
        "code": "1186",
        "segment": "2",
        "name": "PM DE CACONDE",
        "time": "15H"
    },
    {
        "code": "1187",
        "segment": "2",
        "name": "CAMPO ALEGRE",
        "time": "15H"
    },
    {
        "code": "1194",
        "segment": "2",
        "name": "SISAR SOBRAL",
        "time": "15H"
    },
    {
        "code": "1195",
        "segment": "2",
        "name": "SAAE ACAILANDIA",
        "time": "15H"
    },
    {
        "code": "1198",
        "segment": "2",
        "name": "SISTEMA AUTONOMO DE  AGUA E ESGOTO DE MANICORE",
        "time": "15H"
    },
    {
        "code": "1199",
        "segment": "2",
        "name": "SAAQ DE QUATIPURU",
        "time": "15H"
    },
    {
        "code": "1200",
        "segment": "2",
        "name": "PM DE GENERAL CARNEIRO",
        "time": "15H"
    },
    {
        "code": "1202",
        "segment": "2",
        "name": "PM DESTERRO ENTRE RIOS",
        "time": "15H"
    },
    {
        "code": "1207",
        "segment": "2",
        "name": "EMBASA BA",
        "time": "15H"
    },
    {
        "code": "1217",
        "segment": "2",
        "name": " AGUAS DE ARACOIABA",
        "time": "15H"
    },
    {
        "code": "1223",
        "segment": "2",
        "name": "SAE PEDRA BRANCA",
        "time": "15H"
    },
    {
        "code": "1225",
        "segment": "2",
        "name": "PREFEITURA DE API ACAS  CONTA DE  AGUA E ESGOTO",
        "time": "15H"
    },
    {
        "code": "1231",
        "segment": "2",
        "name": "SERVICO MUNICIPAL DA  AGUA E ESGOTO DE OURO PRETO",
        "time": "15H"
    },
    {
        "code": "1236",
        "segment": "2",
        "name": "SAATE PRESIDENTE GETULIO",
        "time": "15H"
    },
    {
        "code": "1246",
        "segment": "2",
        "name": "SISAR BACIA HIDROGRAFICA DO PARNAIBA",
        "time": "15H"
    },
    {
        "code": "1247",
        "segment": "2",
        "name": "SISAR QUIXADA",
        "time": "15H"
    },
    {
        "code": "1248",
        "segment": "2",
        "name": "SISAR BACIA HIDROGRAFICA DO SALGADO",
        "time": "15H"
    },
    {
        "code": "1249",
        "segment": "2",
        "name": "SISAR BACIA DO JAGUARIBE ACOPIARA",
        "time": "15H"
    },
    {
        "code": "1250",
        "segment": "2",
        "name": "SISAR DE ITAPIPOCA",
        "time": "15H"
    },
    {
        "code": "1252",
        "segment": "2",
        "name": "SISAR JAGUARIBE",
        "time": "15H"
    },
    {
        "code": "1254",
        "segment": "2",
        "name": "SAAE SAO JORGE DO IVAI",
        "time": "15H"
    },
    {
        "code": "1261",
        "segment": "2",
        "name": "SAAE DE JEQUIA DA PRAIA",
        "time": "15H"
    },
    {
        "code": "1262",
        "segment": "2",
        "name": "BAL GAIVOTA",
        "time": "15H"
    },
    {
        "code": "1263",
        "segment": "2",
        "name": "FOZ DE SANTA GERTRUDES S A",
        "time": "15H"
    },
    {
        "code": "1264",
        "segment": "2",
        "name": "SAE MAIRINQUE S.A SP",
        "time": "15H"
    },
    {
        "code": "1267",
        "segment": "2",
        "name": " AGUA DE MASSARANDUBA",
        "time": "15H"
    },
    {
        "code": "1269",
        "segment": "2",
        "name": "DAE DE SALTO GRANDE",
        "time": "15H"
    },
    {
        "code": "1270",
        "segment": "2",
        "name": " AGUAS DE ANDRADINA",
        "time": "15H"
    },
    {
        "code": "1272",
        "segment": "2",
        "name": " AGUAS DE GUAR A",
        "time": "15H"
    },
    {
        "code": "1278",
        "segment": "2",
        "name": "SAMASA",
        "time": "15H"
    },
    {
        "code": "1280",
        "segment": "2",
        "name": "AGUAS DE CASTILHO",
        "time": "15H"
    },
    {
        "code": "1281",
        "segment": "2",
        "name": " AGUAS DE CAPIVARI",
        "time": "15H"
    },
    {
        "code": "1292",
        "segment": "2",
        "name": "CEDAE FIDC",
        "time": "15H"
    },
    {
        "code": "1293",
        "segment": "2",
        "name": "CEDAE TESOURO",
        "time": "15H"
    },
    {
        "code": "1295",
        "segment": "2",
        "name": " AGUAS DE PALHOCA",
        "time": "15H"
    },
    {
        "code": "1298",
        "segment": "2",
        "name": "SAAEP  SERV AUTONOMO DE  AGUA E ESGOTO",
        "time": "15H"
    },
    {
        "code": "1300",
        "segment": "2",
        "name": "SERVICO AUTONOMO DE  AGUA E ESGOTO DE LUZ",
        "time": "15H"
    },
    {
        "code": "1302",
        "segment": "2",
        "name": "DATEMA AMBIENTAL SANEAMENTO B ASICO LTDA",
        "time": "15H"
    },
    {
        "code": "1304",
        "segment": "2",
        "name": "FOZ BLUMENAU",
        "time": "15H"
    },
    {
        "code": "1310",
        "segment": "2",
        "name": "URUGUAIANA",
        "time": "15H"
    },
    {
        "code": "1314",
        "segment": "2",
        "name": "SAAE IBITURUNA",
        "time": "15H"
    },
    {
        "code": "1316",
        "segment": "2",
        "name": "SAAE DE PEDREIRA",
        "time": "15H"
    },
    {
        "code": "1318",
        "segment": "2",
        "name": "FOZ DE PORTO FERREIRA",
        "time": "15H"
    },
    {
        "code": "1319",
        "segment": "2",
        "name": "HIDROMAR",
        "time": "15H"
    },
    {
        "code": "1320",
        "segment": "2",
        "name": "SAAEP   SERV  AUTONOMO DE  AGUA E ESGOTO DE PARAUEPEBAS",
        "time": "15H"
    },
    {
        "code": "1321",
        "segment": "2",
        "name": "SEMAS AGUA FCO PAULA",
        "time": "15H"
    },
    {
        "code": "1324",
        "segment": "2",
        "name": "PM MACATUBA",
        "time": "15H"
    },
    {
        "code": "1326",
        "segment": "2",
        "name": " AGUAS DE ITAPOCOROY",
        "time": "15H"
    },
    {
        "code": "1329",
        "segment": "2",
        "name": "CAB CUIABA",
        "time": "15H"
    },
    {
        "code": "1330",
        "segment": "2",
        "name": "TUBAR AO SANEAMENTO",
        "time": "15H"
    },
    {
        "code": "1333",
        "segment": "2",
        "name": "FAB ZONA OESTE S A  FAB CEDAE",
        "time": "15H"
    },
    {
        "code": "1334",
        "segment": "2",
        "name": "PM GUARUVA",
        "time": "15H"
    },
    {
        "code": "1335",
        "segment": "2",
        "name": "AGUAS DE VOTORANTIM",
        "time": "15H"
    },
    {
        "code": "1337",
        "segment": "2",
        "name": "S AO GABRIEL SANEAMENTO",
        "time": "15H"
    },
    {
        "code": "1338",
        "segment": "2",
        "name": "SISAR PICOS PIAUI",
        "time": "15H"
    },
    {
        "code": "1340",
        "segment": "2",
        "name": "VIDA AMBIENTAL DO BRASIL",
        "time": "15H"
    },
    {
        "code": "1341",
        "segment": "2",
        "name": "ATS AGENCIA TOCANTINENSE DE SANEAMENTO",
        "time": "15H"
    },
    {
        "code": "1345",
        "segment": "2",
        "name": "SAMAR ARACATUBA",
        "time": "15H"
    },
    {
        "code": "1346",
        "segment": "2",
        "name": "FOZ DE REDENC AO",
        "time": "15H"
    },
    {
        "code": "1347",
        "segment": "2",
        "name": "ITAPOA SANEAMENTO",
        "time": "15H"
    },
    {
        "code": "1349",
        "segment": "2",
        "name": "FOZ DE MACAE RJ",
        "time": "15H"
    },
    {
        "code": "1351",
        "segment": "2",
        "name": "CASAL  COMPANHIA DE SANEAMENTO DE ALAGOAS",
        "time": "15H"
    },
    {
        "code": "1356",
        "segment": "2",
        "name": "SAAE ROSARIO",
        "time": "15H"
    },
    {
        "code": "1362",
        "segment": "2",
        "name": "PM SIGEFREDO PACHECO",
        "time": "15H"
    },
    {
        "code": "1365",
        "segment": "2",
        "name": "SAEMA MARIALVA",
        "time": "15H"
    },
    {
        "code": "1367",
        "segment": "2",
        "name": "AGUA SAO VENDELINO",
        "time": "15H"
    },
    {
        "code": "1372",
        "segment": "2",
        "name": "SEMAE EMBAUBA",
        "time": "15H"
    },
    {
        "code": "1378",
        "segment": "2",
        "name": "DALZISA DA ROCHA TEIXEIRA ME",
        "time": "15H"
    },
    {
        "code": "1379",
        "segment": "2",
        "name": "FOZ DE GOIAS SANEAMENTO S A",
        "time": "15H"
    },
    {
        "code": "1380",
        "segment": "2",
        "name": "AGUA PM IVOTI",
        "time": "15H"
    },
    {
        "code": "1381",
        "segment": "2",
        "name": "PREFEITURA MUNICIPAL DE ALTO GARCAS",
        "time": "15H"
    },
    {
        "code": "1382",
        "segment": "2",
        "name": "AERG DE REDENC AO DO GURGUEIA",
        "time": "15H"
    },
    {
        "code": "1385",
        "segment": "2",
        "name": "SAAE DE CORDEIROPOLIS",
        "time": "15H"
    },
    {
        "code": "1387",
        "segment": "2",
        "name": " AGUAS DE MAT AO",
        "time": "15H"
    },
    {
        "code": "1389",
        "segment": "2",
        "name": "SAAE SOLEDADE DE MINAS",
        "time": "15H"
    },
    {
        "code": "1391",
        "segment": "2",
        "name": "SAMAE DE  AGUA DOS CANYONS",
        "time": "15H"
    },
    {
        "code": "1393",
        "segment": "2",
        "name": "AGUAS DE S AO FRANCISCO",
        "time": "15H"
    },
    {
        "code": "1398",
        "segment": "2",
        "name": "P.M. IMBITUBA",
        "time": "15H"
    },
    {
        "code": "1400",
        "segment": "2",
        "name": "PREFEITURA MUNICIPAL DE TRABIJU",
        "time": "15H"
    },
    {
        "code": "1402",
        "segment": "2",
        "name": "AGUAS DE PARATY",
        "time": "15H"
    },
    {
        "code": "1404",
        "segment": "2",
        "name": "SAAE DE ALTO ALEGRE DO APRECIS",
        "time": "15H"
    },
    {
        "code": "1406",
        "segment": "2",
        "name": "ASSOCIAC AO DOS MORADORES DO PARQUE PETROPOLIS  ",
        "time": "15H"
    },
    {
        "code": "1407",
        "segment": "2",
        "name": "AGUAS DE DIAMANTINO",
        "time": "15H"
    },
    {
        "code": "1409",
        "segment": "2",
        "name": "AGUA PM LAJEADO",
        "time": "15H"
    },
    {
        "code": "1413",
        "segment": "2",
        "name": "AGUAS DE BARRA DO GARCAS LTDA",
        "time": "15H"
    },
    {
        "code": "1417",
        "segment": "2",
        "name": "CISAB S AO JOSE DE RIBAMAR",
        "time": "15H"
    },
    {
        "code": "1420",
        "segment": "2",
        "name": "SAAE CHUPINGUAIA",
        "time": "15H"
    },
    {
        "code": "1422",
        "segment": "2",
        "name": "AGUAS DE SINOP",
        "time": "15H"
    },
    {
        "code": "1423",
        "segment": "2",
        "name": " AGUAS DE JAHU",
        "time": "15H"
    },
    {
        "code": "1424",
        "segment": "2",
        "name": "PM PAU D ARCO",
        "time": "15H"
    },
    {
        "code": "1426",
        "segment": "2",
        "name": " AGUAS DE S AO FRANCISCO DO SUL LTDA",
        "time": "15H"
    },
    {
        "code": "1429",
        "segment": "2",
        "name": "ODEBRECHT AMBIENTAL MARANH AO S A",
        "time": "15H"
    },
    {
        "code": "1431",
        "segment": "2",
        "name": "PREFEITURA MUNICIPAL DE ITAJOBI",
        "time": "15H"
    },
    {
        "code": "1432",
        "segment": "2",
        "name": "AGUAS DE PARANATINGA LTDA",
        "time": "15H"
    },
    {
        "code": "1436",
        "segment": "2",
        "name": "ODEBRECHT AMBIENTAL SUMARE",
        "time": "15H"
    },
    {
        "code": "1437",
        "segment": "2",
        "name": "SAERP S AO JOSE DO RIO PARDO",
        "time": "15H"
    },
    {
        "code": "1438",
        "segment": "2",
        "name": "AGUA ASSOC LOT FELDM",
        "time": "15H"
    },
    {
        "code": "1441",
        "segment": "2",
        "name": "PM JO AO RAMALHO",
        "time": "15H"
    },
    {
        "code": "1442",
        "segment": "2",
        "name": "AGUAS DE PARA DE MINAS",
        "time": "15H"
    },
    {
        "code": "1443",
        "segment": "2",
        "name": " AGUAS DE TIMON SANEAMENTO",
        "time": "15H"
    },
    {
        "code": "1445",
        "segment": "2",
        "name": "AGUA PM BOA VISTA CADEADO",
        "time": "15H"
    },
    {
        "code": "1446",
        "segment": "2",
        "name": "AGUAS DE BURITI S A",
        "time": "15H"
    },
    {
        "code": "1447",
        "segment": "2",
        "name": "SANESALTO SANEAMENTO SA",
        "time": "15H"
    },
    {
        "code": "1452",
        "segment": "2",
        "name": "PM DE MARTINOPOLIS",
        "time": "15H"
    },
    {
        "code": "1456",
        "segment": "2",
        "name": "CAEPA PARAIBUNA",
        "time": "15H"
    },
    {
        "code": "1462",
        "segment": "2",
        "name": "AGUAS DE HOLAMBRA",
        "time": "15H"
    },
    {
        "code": "1466",
        "segment": "2",
        "name": "AGUAS DE PENHA",
        "time": "15H"
    },
    {
        "code": "1473",
        "segment": "2",
        "name": " AGUAS DE CAMBORIU",
        "time": "15H"
    },
    {
        "code": "1474",
        "segment": "2",
        "name": "AGUAS DE PIMENTA BUENO",
        "time": "15H"
    },
    {
        "code": "1475",
        "segment": "2",
        "name": "CASAL  COMPANHIA DE SANEAMENTO DE ALAGOAS   SANEMA",
        "time": "15H"
    },
    {
        "code": "1476",
        "segment": "2",
        "name": "SAEC CACERES",
        "time": "15H"
    },
    {
        "code": "1482",
        "segment": "2",
        "name": "JAGUARUNA SANEAMENTO SPE S A",
        "time": "15H"
    },
    {
        "code": "1484",
        "segment": "2",
        "name": "COMASA  Companhia Aguas de Santa Rita  Santa Rita do Passa",
        "time": "15H"
    },
    {
        "code": "1486",
        "segment": "2",
        "name": "ASSOC AGUA NOVO PARAISO",
        "time": "15H"
    },
    {
        "code": "1488",
        "segment": "2",
        "name": "CASAL  COMPANHIA DE SANEAMENTO DE ALAGOAS   SANAMA",
        "time": "15H"
    },
    {
        "code": "1491",
        "segment": "2",
        "name": " AGUAS DE ROLIM DE MOURA",
        "time": "15H"
    },
    {
        "code": "1492",
        "segment": "2",
        "name": "AGUAS DE SANTIAGO MT",
        "time": "15H"
    },
    {
        "code": "1493",
        "segment": "2",
        "name": "AGUAS DE ARIQUEMES SANEAMENTO SPE LTDA  RO",
        "time": "15H"
    },
    {
        "code": "1494",
        "segment": "2",
        "name": "EPPO SANEAMENTO AMBIENTAL E OBRAS LTDA",
        "time": "15H"
    },
    {
        "code": "1495",
        "segment": "2",
        "name": "SETAE DE NOVA XAVANTINA",
        "time": "15H"
    },
    {
        "code": "1496",
        "segment": "2",
        "name": "SETAE  NOVO S AO JOAQUIM",
        "time": "15H"
    },
    {
        "code": "1498",
        "segment": "2",
        "name": "PM ENTRE RIOS DO OESTE",
        "time": "15H"
    },
    {
        "code": "1499",
        "segment": "2",
        "name": "AGUAS DE BOMBINHAS SANEAMENTO SPE",
        "time": "15H"
    },
    {
        "code": "1504",
        "segment": "2",
        "name": "ASSOC AGUA ROTA DO SOL",
        "time": "15H"
    },
    {
        "code": "1506",
        "segment": "2",
        "name": "AGUAS DE S AO SEBASTI AO DA GRAMA SPE S A",
        "time": "15H"
    },
    {
        "code": "1515",
        "segment": "2",
        "name": "SAAE CAMESIA",
        "time": "15H"
    },
    {
        "code": "1520",
        "segment": "2",
        "name": "CIS COMPANHIA ITUANA DE SANEAMENTO",
        "time": "15H"
    },
    {
        "code": "1528",
        "segment": "2",
        "name": " AGUAS DE NOVO REPARTIMENTO SANEAMENTO SPE LTDA",
        "time": "15H"
    },
    {
        "code": "1534",
        "segment": "2",
        "name": "SAAE DE CAFELANDIA SP",
        "time": "15H"
    },
    {
        "code": "1535",
        "segment": "2",
        "name": " AGUAS DE TERESINA",
        "time": "15H"
    },
    {
        "code": "1538",
        "segment": "2",
        "name": "SAAE SEVERINIA",
        "time": "15H"
    },
    {
        "code": "1543",
        "segment": "2",
        "name": "UNICATU AGUA E SOLO",
        "time": "15H"
    },
    {
        "code": "1560",
        "segment": "2",
        "name": "AGUA GRAMADO XAVIER",
        "time": "15H"
    },
    {
        "code": "1577",
        "segment": "2",
        "name": "PM DE AMERICO DE CAMPOS",
        "time": "15H"
    },
    {
        "code": "1582",
        "segment": "2",
        "name": "AGUAS CASA BRANCA SPE L",
        "time": "15H"
    },
    {
        "code": "1600",
        "segment": "2",
        "name": "GAIVOTA SANEAMENTO SPE SA",
        "time": "15H"
    },
    {
        "code": "2386",
        "segment": "2",
        "name": "PM LAJEADO AGUA",
        "time": "15H"
    },
    {
        "code": "2499",
        "segment": "2",
        "name": "SERVICO AUTONOMO DE  AGUA  ESGOTO E SANEAMENTO URBANO",
        "time": "15H"
    },
    {
        "code": "3742",
        "segment": "2",
        "name": "SANESC",
        "time": "15H"
    },
    {
        "code": "3847",
        "segment": "2",
        "name": "ODEBRECHT AMBIENTAL MAU A SP",
        "time": "15H"
    },
    {
        "code": "4526",
        "segment": "2",
        "name": "DAET   DEPARTAMENTO  DE  AGUA E ESGOTO DE TESOURO",
        "time": "15H"
    },
    {
        "code": "4642",
        "segment": "2",
        "name": "PREFEITURA MUNICIPAL DE UCHOA   AGUA E ESGOTO",
        "time": "15H"
    },
    {
        "code": "4728",
        "segment": "2",
        "name": "SEMAE VERA CRUZ",
        "time": "15H"
    },
    {
        "code": "5432",
        "segment": "2",
        "name": "AGUA PM CARAA",
        "time": "15H"
    },
    {
        "code": "5468",
        "segment": "2",
        "name": "AGUA PM JARI",
        "time": "15H"
    },
    {
        "code": "5500",
        "segment": "2",
        "name": "AGUA PARECI NOVO",
        "time": "15H"
    },
    {
        "code": "5521",
        "segment": "2",
        "name": "AGUA SAO MARTINHO SERRA",
        "time": "15H"
    },
    {
        "code": "5670",
        "segment": "2",
        "name": "AGUA PM BOA V CADEAD",
        "time": "15H"
    },
    {
        "code": "1",
        "segment": "3",
        "name": "CAIUA S A",
        "time": "15H"
    },
    {
        "code": "2",
        "segment": "3",
        "name": "CEA",
        "time": "15H"
    },
    {
        "code": "3",
        "segment": "3",
        "name": "CEAL",
        "time": "15H"
    },
    {
        "code": "4",
        "segment": "3",
        "name": "CEAM",
        "time": "15H"
    },
    {
        "code": "6",
        "segment": "3",
        "name": "CEEE",
        "time": "15H"
    },
    {
        "code": "7",
        "segment": "3",
        "name": "CELB",
        "time": "15H"
    },
    {
        "code": "9",
        "segment": "3",
        "name": "CELG CENTRAIS ELETRICAS DE GO",
        "time": "15H"
    },
    {
        "code": "10",
        "segment": "3",
        "name": "CELPA",
        "time": "15H"
    },
    {
        "code": "11",
        "segment": "3",
        "name": "CELPE CIA ELETRICIDADE DE PERNANBUCO",
        "time": "15H"
    },
    {
        "code": "12",
        "segment": "3",
        "name": "CELTINS",
        "time": "15H"
    },
    {
        "code": "13",
        "segment": "3",
        "name": "CEMAR",
        "time": "15H"
    },
    {
        "code": "14",
        "segment": "3",
        "name": "CEMAT",
        "time": "15H"
    },
    {
        "code": "16",
        "segment": "3",
        "name": "CENF",
        "time": "15H"
    },
    {
        "code": "17",
        "segment": "3",
        "name": "CEPISA",
        "time": "15H"
    },
    {
        "code": "18",
        "segment": "3",
        "name": "CERIPA",
        "time": "15H"
    },
    {
        "code": "19",
        "segment": "3",
        "name": "AMPLA CERJ RJ",
        "time": "15H"
    },
    {
        "code": "20",
        "segment": "3",
        "name": "CERON",
        "time": "15H"
    },
    {
        "code": "23",
        "segment": "3",
        "name": "CHESP CERES",
        "time": "15H"
    },
    {
        "code": "24",
        "segment": "3",
        "name": "CFLCL",
        "time": "15H"
    },
    {
        "code": "25",
        "segment": "3",
        "name": "CFLO",
        "time": "15H"
    },
    {
        "code": "26",
        "segment": "3",
        "name": "CLFM",
        "time": "15H"
    },
    {
        "code": "27",
        "segment": "3",
        "name": "CLFSC",
        "time": "15H"
    },
    {
        "code": "28",
        "segment": "3",
        "name": "CNEE CIA NACIONAL DE ENERGIA ELETRICA GRUPO REDE",
        "time": "15H"
    },
    {
        "code": "29",
        "segment": "3",
        "name": "COCEL",
        "time": "15H"
    },
    {
        "code": "30",
        "segment": "3",
        "name": "COELBA CIA ELETRICIDADE DO EST DA BA",
        "time": "15H"
    },
    {
        "code": "31",
        "segment": "3",
        "name": "COELCE",
        "time": "15H"
    },
    {
        "code": "36",
        "segment": "3",
        "name": "CERTAJA ENERGIA LTDA",
        "time": "15H"
    },
    {
        "code": "37",
        "segment": "3",
        "name": "COPEL",
        "time": "15H"
    },
    {
        "code": "38",
        "segment": "3",
        "name": "COSERN",
        "time": "15H"
    },
    {
        "code": "39",
        "segment": "3",
        "name": "CPEE",
        "time": "15H"
    },
    {
        "code": "41",
        "segment": "3",
        "name": "DME DISTRIBUIC AO S A",
        "time": "15H"
    },
    {
        "code": "42",
        "segment": "3",
        "name": "EEB EMPRESA ELETRICA BRAGANTINA GRUPO REDE",
        "time": "15H"
    },
    {
        "code": "43",
        "segment": "3",
        "name": "EEVP EMPRESA ELETRICA VALE DO PARANAPANEMA GRUPO REDE",
        "time": "15H"
    },
    {
        "code": "44",
        "segment": "3",
        "name": "EMPRESA LUZ E FORCA SANTA MARIA S A",
        "time": "15H"
    },
    {
        "code": "45",
        "segment": "3",
        "name": "ELETROACRE",
        "time": "15H"
    },
    {
        "code": "46",
        "segment": "3",
        "name": "ELETROCAR",
        "time": "15H"
    },
    {
        "code": "47",
        "segment": "3",
        "name": "AMAZONAS ENERGIA ANTIGA ELETRONORTE",
        "time": "15H"
    },
    {
        "code": "49",
        "segment": "3",
        "name": "ENERGISA SERGIPE",
        "time": "15H"
    },
    {
        "code": "50",
        "segment": "3",
        "name": "ENERSUL",
        "time": "15H"
    },
    {
        "code": "51",
        "segment": "3",
        "name": "ESCELSA GRUPO ENERGIAS DO BRASIL",
        "time": "15H"
    },
    {
        "code": "52",
        "segment": "3",
        "name": "COMPANHIA JAGUARI DE ENERGIA GRUPO CMS ENERGY",
        "time": "15H"
    },
    {
        "code": "54",
        "segment": "3",
        "name": "ENERGISA PARAIBA ANTIGA SAELPA  GRUPO ENERGISA",
        "time": "15H"
    },
    {
        "code": "55",
        "segment": "3",
        "name": "COMPANHIA SUL PAULISTA DE ENERGIA GRUPO CMS ENERGY",
        "time": "15H"
    },
    {
        "code": "57",
        "segment": "3",
        "name": "COMGAS CIA DE GAS DE SP",
        "time": "15H"
    },
    {
        "code": "60",
        "segment": "3",
        "name": "CERT DE TUP A",
        "time": "15H"
    },
    {
        "code": "61",
        "segment": "3",
        "name": "COOP DE ELETR RURAL DE MOGI MIRIM CERMM",
        "time": "15H"
    },
    {
        "code": "65",
        "segment": "3",
        "name": "CERMISSOES",
        "time": "15H"
    },
    {
        "code": "66",
        "segment": "3",
        "name": "HIDROPAN HIDROELETRICA DE PANAMBI",
        "time": "15H"
    },
    {
        "code": "67",
        "segment": "3",
        "name": "DEMEI DEPARTAMENTO MUNICIPAL DE ENERGIA DE IJUI",
        "time": "15H"
    },
    {
        "code": "68",
        "segment": "3",
        "name": "IGUACU ENERGIA",
        "time": "15H"
    },
    {
        "code": "71",
        "segment": "3",
        "name": "CERTEL",
        "time": "15H"
    },
    {
        "code": "72",
        "segment": "3",
        "name": "CERMC",
        "time": "15H"
    },
    {
        "code": "73",
        "segment": "3",
        "name": "EMPRESA BANDEIRANTE DE ENERGIA",
        "time": "15H"
    },
    {
        "code": "74",
        "segment": "3",
        "name": "COPERALIANCA",
        "time": "15H"
    },
    {
        "code": "75",
        "segment": "3",
        "name": "BOA VISTA ENERGIA S A",
        "time": "15H"
    },
    {
        "code": "76",
        "segment": "3",
        "name": "COOPERZEM",
        "time": "15H"
    },
    {
        "code": "77",
        "segment": "3",
        "name": "COMPAGAS CIA PARANAENSE",
        "time": "15H"
    },
    {
        "code": "78",
        "segment": "3",
        "name": "COOPERATIVA DE ELETRIFICACAO ANITA GARIBALDI",
        "time": "15H"
    },
    {
        "code": "79",
        "segment": "3",
        "name": "CERPALO",
        "time": "15H"
    },
    {
        "code": "80",
        "segment": "3",
        "name": "CERMESO COOP ELETRIF DA MEDIA SOROCABANA",
        "time": "15H"
    },
    {
        "code": "81",
        "segment": "3",
        "name": "CERMOFUL MORRO DA FUMACA",
        "time": "15H"
    },
    {
        "code": "82",
        "segment": "3",
        "name": "COOP  PRESTACAO  SERV PUBL  DISTRIB  ENERGIA ELE  SENADOR",
        "time": "15H"
    },
    {
        "code": "84",
        "segment": "3",
        "name": "COOPERATIVA DE ELETRIFICAC AO DE LAURO MULLER",
        "time": "15H"
    },
    {
        "code": "85",
        "segment": "3",
        "name": "COORSEL",
        "time": "15H"
    },
    {
        "code": "86",
        "segment": "3",
        "name": "AESPOA",
        "time": "15H"
    },
    {
        "code": "87",
        "segment": "3",
        "name": "MUXFELDT MARIN E CIA",
        "time": "15H"
    },
    {
        "code": "89",
        "segment": "3",
        "name": "RGE RIO GRANDE ENERGIA S A",
        "time": "15H"
    },
    {
        "code": "90",
        "segment": "3",
        "name": "CIA SUL SERGIPANA DE ELETRICIDADE SULGIPE",
        "time": "15H"
    },
    {
        "code": "91",
        "segment": "3",
        "name": "CERGRAL",
        "time": "15H"
    },
    {
        "code": "92",
        "segment": "3",
        "name": "CERILUZ COOP REGIONAL ENERGIA E DESENV DE IJUI",
        "time": "15H"
    },
    {
        "code": "93",
        "segment": "3",
        "name": "CELTINS BID GRUPO REDE",
        "time": "15H"
    },
    {
        "code": "94",
        "segment": "3",
        "name": "COOP DISTRIB ENERGIA LT",
        "time": "15H"
    },
    {
        "code": "95",
        "segment": "3",
        "name": "FORQUILHINHA",
        "time": "15H"
    },
    {
        "code": "97",
        "segment": "3",
        "name": "COOP REGIONAL DE ENERGIA E SESENV DO LITORAL NORTE LTDA",
        "time": "15H"
    },
    {
        "code": "98",
        "segment": "3",
        "name": "JARI CELULOSE S A",
        "time": "15H"
    },
    {
        "code": "99",
        "segment": "3",
        "name": "USIN HIDR NOVA PALMA",
        "time": "15H"
    },
    {
        "code": "100",
        "segment": "3",
        "name": "CEG RIO S A",
        "time": "15H"
    },
    {
        "code": "101",
        "segment": "3",
        "name": "COPREL ENERGIA",
        "time": "15H"
    },
    {
        "code": "102",
        "segment": "3",
        "name": "CERSUL",
        "time": "15H"
    },
    {
        "code": "103",
        "segment": "3",
        "name": "COOP LUDGERO",
        "time": "15H"
    },
    {
        "code": "104",
        "segment": "3",
        "name": "CERBEMS",
        "time": "15H"
    },
    {
        "code": "106",
        "segment": "3",
        "name": "EFLUL",
        "time": "15H"
    },
    {
        "code": "109",
        "segment": "3",
        "name": "COOP DE ELETR RURAL DA REGI AO DE ITAPECERICA DA SERRA",
        "time": "15H"
    },
    {
        "code": "111",
        "segment": "3",
        "name": "COPEL DISTRIBUICAO SA",
        "time": "15H"
    },
    {
        "code": "116",
        "segment": "3",
        "name": "GAS NATURAL SPS SA",
        "time": "15H"
    },
    {
        "code": "119",
        "segment": "3",
        "name": "CERVAM  COOPERATIVA DE ENERGIZAC AO E DESENVOL RURAL DO",
        "time": "15H"
    },
    {
        "code": "123",
        "segment": "3",
        "name": "GBD S A",
        "time": "15H"
    },
    {
        "code": "125",
        "segment": "3",
        "name": "CERRP",
        "time": "15H"
    },
    {
        "code": "127",
        "segment": "3",
        "name": "BAHIAG AS  CIA DE G AS DA BAHIA",
        "time": "15H"
    },
    {
        "code": "132",
        "segment": "3",
        "name": "CERBRANORTE",
        "time": "15H"
    },
    {
        "code": "133",
        "segment": "3",
        "name": "Cooperativa Regional de Eletrificacao Rural do Alto Uruguai",
        "time": "15H"
    },
    {
        "code": "134",
        "segment": "3",
        "name": "COOPERATIVA DE ENERGIA TREVISO",
        "time": "15H"
    },
    {
        "code": "135",
        "segment": "3",
        "name": "COOPERSUL",
        "time": "15H"
    },
    {
        "code": "137",
        "segment": "3",
        "name": "ULTRAGAZ",
        "time": "15H"
    },
    {
        "code": "138",
        "segment": "3",
        "name": "CEMIG DISTRIBUICAO SA",
        "time": "15H"
    },
    {
        "code": "139",
        "segment": "3",
        "name": "CEMIG",
        "time": "15H"
    },
    {
        "code": "145",
        "segment": "3",
        "name": "ENERGISA",
        "time": "15H"
    },
    {
        "code": "146",
        "segment": "3",
        "name": "ENERGISA NOVA FRIBURGO",
        "time": "15H"
    },
    {
        "code": "147",
        "segment": "3",
        "name": "ENERGISA BORBOR",
        "time": "15H"
    },
    {
        "code": "148",
        "segment": "3",
        "name": "ENERGISA SERGIPE",
        "time": "15H"
    },
    {
        "code": "149",
        "segment": "3",
        "name": "ENERGISA PARAIBA",
        "time": "15H"
    },
    {
        "code": "154",
        "segment": "3",
        "name": "CEMAT",
        "time": "15H"
    },
    {
        "code": "155",
        "segment": "3",
        "name": "CAIU A DISTRIBUIDORA DE ENERGIA S A GRUPO REDE",
        "time": "15H"
    },
    {
        "code": "156",
        "segment": "3",
        "name": "COOPERATIVA ENERGETICA COCOAL",
        "time": "15H"
    },
    {
        "code": "157",
        "segment": "3",
        "name": "CERGAPA COOPERATIVA DE ELETRICIDADE DE GR AO PAR A",
        "time": "15H"
    },
    {
        "code": "159",
        "segment": "3",
        "name": "CEMAT  MT GRUPO REDE",
        "time": "15H"
    },
    {
        "code": "160",
        "segment": "3",
        "name": "CELPA GRUPO REDE",
        "time": "15H"
    },
    {
        "code": "162",
        "segment": "3",
        "name": "CELESC DISTRIBUICAO SA",
        "time": "15H"
    },
    {
        "code": "165",
        "segment": "3",
        "name": "Companhia Estadual de Distribuicao de Energia Eletrica-Geracao",
        "time": "15H"
    },
    {
        "code": "166",
        "segment": "3",
        "name": "Companhia Estadual de Distribuicao de Energia Eletrica-",
        "time": "15H"
    },
    {
        "code": "167",
        "segment": "3",
        "name": "FORCA E LUZ JO AO CESA",
        "time": "15H"
    },
    {
        "code": "170",
        "segment": "3",
        "name": "ALG AS  G AS DE ALAGOAS",
        "time": "15H"
    },
    {
        "code": "172",
        "segment": "3",
        "name": "Cooperativa de Geracao e Distribuicao de Energia Fontoura Xavier",
        "time": "15H"
    },
    {
        "code": "173",
        "segment": "3",
        "name": "CELTINS",
        "time": "15H"
    },
    {
        "code": "177",
        "segment": "3",
        "name": "Cooperativa de Eletrificacao Rural Vale Jaguari",
        "time": "15H"
    },
    {
        "code": "178",
        "segment": "3",
        "name": "LIQUIG AS DISTRIBUIDORA S A",
        "time": "15H"
    },
    {
        "code": "179",
        "segment": "3",
        "name": "COOPERATIVA DE DISTRIBUICAO DE ENERGIA TEUTONIA",
        "time": "15H"
    },
    {
        "code": "181",
        "segment": "3",
        "name": "COOP DE DISTRIBUIC AO DE ENERGIA ELETRICA SANTA MARIA",
        "time": "15H"
    },
    {
        "code": "182",
        "segment": "3",
        "name": "BAHIANA GAS BRASILG AS",
        "time": "15H"
    },
    {
        "code": "183",
        "segment": "3",
        "name": "CERSAD DE SALTO DONER",
        "time": "15H"
    },
    {
        "code": "185",
        "segment": "3",
        "name": "COOP DE ELETRIFICAC AO DE IBIUNA E REGI AO",
        "time": "15H"
    },
    {
        "code": "186",
        "segment": "3",
        "name": "Cooperativa de distribuicao de energia entre rios LTDA",
        "time": "15H"
    },
    {
        "code": "192",
        "segment": "3",
        "name": "SUPERGASBRAS ENERGIA LTDA",
        "time": "15H"
    },
    {
        "code": "197",
        "segment": "3",
        "name": "MINASGASBRAS INDUSTRIA E COMERCIO",
        "time": "15H"
    },
    {
        "code": "199",
        "segment": "3",
        "name": "ENERSUL",
        "time": "15H"
    },
    {
        "code": "211",
        "segment": "3",
        "name": "CEDRAP PARAIBUNA",
        "time": "15H"
    },
    {
        "code": "212",
        "segment": "3",
        "name": "CIA DE GAS DE MINAS GER",
        "time": "15H"
    },
    {
        "code": "215",
        "segment": "3",
        "name": "COOPERATIVA DE ENERGIZAC AO E DESENV RURAL DE NOVO",
        "time": "15H"
    },
    {
        "code": "4",
        "segment": "4",
        "name": "ALTERADO DE CTBC PARA ALGAR TELECOM FIXA/MG",
        "time": "15H"
    },
    {
        "code": "7",
        "segment": "4",
        "name": "SERCOMTEL SERV COMUNIC TELEFONICAS DE LONDRINA",
        "time": "15H"
    },
    {
        "code": "19",
        "segment": "4",
        "name": "BRASIL TELECOM FILIAL MS",
        "time": "15H"
    },
    {
        "code": "34",
        "segment": "4",
        "name": "TIM CELULAR CE",
        "time": "15H"
    },
    {
        "code": "35",
        "segment": "4",
        "name": "TIM CELULAR MG BA SE",
        "time": "15H"
    },
    {
        "code": "37",
        "segment": "4",
        "name": "TIM CELULAR PI",
        "time": "15H"
    },
    {
        "code": "40",
        "segment": "4",
        "name": "TIM CELULAR RN",
        "time": "15H"
    },
    {
        "code": "42",
        "segment": "4",
        "name": "VIVO",
        "time": "15H"
    },
    {
        "code": "43",
        "segment": "4",
        "name": "TIM CELULAR PB",
        "time": "15H"
    },
    {
        "code": "44",
        "segment": "4",
        "name": "VIVO",
        "time": "15H"
    },
    {
        "code": "46",
        "segment": "4",
        "name": "TIM CELULAR PE",
        "time": "15H"
    },
    {
        "code": "49",
        "segment": "4",
        "name": "VIVO",
        "time": "15H"
    },
    {
        "code": "50",
        "segment": "4",
        "name": "TELAIMA CEL",
        "time": "15H"
    },
    {
        "code": "51",
        "segment": "4",
        "name": "TELAMAZON CELULAR GRUPO AMAZONIA CELULAR",
        "time": "15H"
    },
    {
        "code": "52",
        "segment": "4",
        "name": "TIM CELULAR AL",
        "time": "15H"
    },
    {
        "code": "53",
        "segment": "4",
        "name": "VIVO",
        "time": "15H"
    },
    {
        "code": "54",
        "segment": "4",
        "name": "TELEAMAPA C",
        "time": "15H"
    },
    {
        "code": "55",
        "segment": "4",
        "name": "VIVO",
        "time": "15H"
    },
    {
        "code": "56",
        "segment": "4",
        "name": "TIM SUL - PR",
        "time": "15H"
    },
    {
        "code": "57",
        "segment": "4",
        "name": "TELEPARA CELULA",
        "time": "15H"
    },
    {
        "code": "58",
        "segment": "4",
        "name": "VIVO",
        "time": "15H"
    },
    {
        "code": "59",
        "segment": "4",
        "name": "TIM SUL - SC",
        "time": "15H"
    },
    {
        "code": "60",
        "segment": "4",
        "name": "VIVO",
        "time": "15H"
    },
    {
        "code": "61",
        "segment": "4",
        "name": "TELMA CELULAR GRUPO AMAZONIA CELULAR",
        "time": "15H"
    },
    {
        "code": "62",
        "segment": "4",
        "name": "TIM SUL - PELOTAS",
        "time": "15H"
    },
    {
        "code": "66",
        "segment": "4",
        "name": "CTBC CELULAR ALTERADO PARA ALGAR CELULAR PRE MG",
        "time": "15H"
    },
    {
        "code": "71",
        "segment": "4",
        "name": "CLARO FIXO RJ",
        "time": "15H"
    },
    {
        "code": "72",
        "segment": "4",
        "name": "VIVO",
        "time": "15H"
    },
    {
        "code": "73",
        "segment": "4",
        "name": "VIVO",
        "time": "15H"
    },
    {
        "code": "74",
        "segment": "4",
        "name": "VIVO",
        "time": "15H"
    },
    {
        "code": "75",
        "segment": "4",
        "name": "VIVO",
        "time": "15H"
    },
    {
        "code": "76",
        "segment": "4",
        "name": "VIVO",
        "time": "15H"
    },
    {
        "code": "77",
        "segment": "4",
        "name": "INTELIG",
        "time": "15H"
    },
    {
        "code": "78",
        "segment": "4",
        "name": "CLARO FIXO SP",
        "time": "15H"
    },
    {
        "code": "81",
        "segment": "4",
        "name": "VIVO",
        "time": "15H"
    },
    {
        "code": "83",
        "segment": "4",
        "name": "ENGEVOX TEL.",
        "time": "15H"
    },
    {
        "code": "84",
        "segment": "4",
        "name": "TELEFONICA EMPR",
        "time": "15H"
    },
    {
        "code": "87",
        "segment": "4",
        "name": "TELECOM UBER",
        "time": "15H"
    },
    {
        "code": "88",
        "segment": "4",
        "name": "TELECOM MG",
        "time": "15H"
    },
    {
        "code": "89",
        "segment": "4",
        "name": "NEXTEL TELECOMUNICACOES LTDA",
        "time": "15H"
    },
    {
        "code": "106",
        "segment": "4",
        "name": "COPEL TELECOMUNICACOES S A",
        "time": "15H"
    },
    {
        "code": "107",
        "segment": "4",
        "name": "TCO IP",
        "time": "15H"
    },
    {
        "code": "108",
        "segment": "4",
        "name": "TMAIS S A",
        "time": "15H"
    },
    {
        "code": "109",
        "segment": "4",
        "name": "TIM CEL SP",
        "time": "15H"
    },
    {
        "code": "110",
        "segment": "4",
        "name": "TIM CELULAR  CENTRO SUL",
        "time": "15H"
    },
    {
        "code": "111",
        "segment": "4",
        "name": "TIM CELULAR  RIO ES E NORTE",
        "time": "15H"
    },
    {
        "code": "112",
        "segment": "4",
        "name": "NORTELPA",
        "time": "15H"
    },
    {
        "code": "114",
        "segment": "4",
        "name": "IDT BRASIL",
        "time": "15H"
    },
    {
        "code": "120",
        "segment": "4",
        "name": "TRANSIT TELECOM",
        "time": "15H"
    },
    {
        "code": "125",
        "segment": "4",
        "name": "VESPER S A",
        "time": "15H"
    },
    {
        "code": "126",
        "segment": "4",
        "name": "EMBRATEL L CORP",
        "time": "15H"
    },
    {
        "code": "149",
        "segment": "4",
        "name": "BRASIL TELECOM CEL AC",
        "time": "15H"
    },
    {
        "code": "150",
        "segment": "4",
        "name": "BRASIL TELECOM CEL DF",
        "time": "15H"
    },
    {
        "code": "151",
        "segment": "4",
        "name": "BRASIL TELECOM CEL GO",
        "time": "15H"
    },
    {
        "code": "152",
        "segment": "4",
        "name": "BRASIL TELECOM CEL MT",
        "time": "15H"
    },
    {
        "code": "153",
        "segment": "4",
        "name": "BRASIL TELECOM CEL MS",
        "time": "15H"
    },
    {
        "code": "154",
        "segment": "4",
        "name": "BRASIL TELECOM CEL PR",
        "time": "15H"
    },
    {
        "code": "155",
        "segment": "4",
        "name": "BRASIL TELECOM CEL RS",
        "time": "15H"
    },
    {
        "code": "156",
        "segment": "4",
        "name": "BRASIL TELECOM CEL RO",
        "time": "15H"
    },
    {
        "code": "157",
        "segment": "4",
        "name": "BRASIL TELECOM CEL SC",
        "time": "15H"
    },
    {
        "code": "164",
        "segment": "4",
        "name": "TELECOM",
        "time": "15H"
    },
    {
        "code": "166",
        "segment": "4",
        "name": "PEGASUS S A",
        "time": "15H"
    },
    {
        "code": "194",
        "segment": "4",
        "name": "TNL PCS S A",
        "time": "15H"
    },
    {
        "code": "200",
        "segment": "4",
        "name": "TNL PCS S A",
        "time": "15H"
    },
    {
        "code": "202",
        "segment": "4",
        "name": "TNL PCS S A",
        "time": "15H"
    },
    {
        "code": "204",
        "segment": "4",
        "name": "TNL PCS S A",
        "time": "15H"
    },
    {
        "code": "205",
        "segment": "4",
        "name": "TNL PCS S A",
        "time": "15H"
    },
    {
        "code": "206",
        "segment": "4",
        "name": "TNL PCS S A",
        "time": "15H"
    },
    {
        "code": "211",
        "segment": "4",
        "name": "TNL PCS S A",
        "time": "15H"
    },
    {
        "code": "212",
        "segment": "4",
        "name": "TELEMAR  31 GLOBAL",
        "time": "15H"
    },
    {
        "code": "214",
        "segment": "4",
        "name": "TNL PCS S A",
        "time": "15H"
    },
    {
        "code": "216",
        "segment": "4",
        "name": "TNL PCS S A",
        "time": "15H"
    },
    {
        "code": "217",
        "segment": "4",
        "name": "TNL PCS S A",
        "time": "15H"
    },
    {
        "code": "219",
        "segment": "4",
        "name": "TNL PCS S A",
        "time": "15H"
    },
    {
        "code": "220",
        "segment": "4",
        "name": "TNL PCS S A",
        "time": "15H"
    },
    {
        "code": "259",
        "segment": "4",
        "name": "NET GOIANIA",
        "time": "15H"
    },
    {
        "code": "261",
        "segment": "4",
        "name": "NET RECIFE",
        "time": "15H"
    },
    {
        "code": "270",
        "segment": "4",
        "name": "BTC PELOTAS",
        "time": "15H"
    },
    {
        "code": "274",
        "segment": "4",
        "name": "EPSILON",
        "time": "15H"
    },
    {
        "code": "275",
        "segment": "4",
        "name": "SIDYS LTDA",
        "time": "15H"
    },
    {
        "code": "278",
        "segment": "4",
        "name": "NET LEOPOLDO",
        "time": "15H"
    },
    {
        "code": "279",
        "segment": "4",
        "name": "NET CURITIBA",
        "time": "15H"
    },
    {
        "code": "280",
        "segment": "4",
        "name": "COPREL GERACAO",
        "time": "15H"
    },
    {
        "code": "281",
        "segment": "4",
        "name": "FONAR",
        "time": "15H"
    },
    {
        "code": "284",
        "segment": "4",
        "name": "CTBC MULTIMIDIA ALTERADO PARA ALGAR MULTIMIDA MG",
        "time": "15H"
    },
    {
        "code": "285",
        "segment": "4",
        "name": "S TECNOLOGIA",
        "time": "15H"
    },
    {
        "code": "286",
        "segment": "4",
        "name": "TELECOMDADOS",
        "time": "15H"
    },
    {
        "code": "290",
        "segment": "4",
        "name": "VIVO",
        "time": "15H"
    },
    {
        "code": "291",
        "segment": "4",
        "name": "VIVO",
        "time": "15H"
    },
    {
        "code": "292",
        "segment": "4",
        "name": "VIVO",
        "time": "15H"
    },
    {
        "code": "293",
        "segment": "4",
        "name": "VIVO",
        "time": "15H"
    },
    {
        "code": "294",
        "segment": "4",
        "name": "VIVO",
        "time": "15H"
    },
    {
        "code": "295",
        "segment": "4",
        "name": "VIVO",
        "time": "15H"
    },
    {
        "code": "297",
        "segment": "4",
        "name": "CLARO FILIAS NORTE",
        "time": "15H"
    },
    {
        "code": "313",
        "segment": "4",
        "name": "OI CEL BR",
        "time": "15H"
    },
    {
        "code": "369",
        "segment": "4",
        "name": "OI TV TNL PCS",
        "time": "15H"
    },
    {
        "code": "370",
        "segment": "4",
        "name": "NET VITORIA",
        "time": "15H"
    },
    {
        "code": "379",
        "segment": "4",
        "name": "SKY BRASIL SERVICOS LTDA",
        "time": "15H"
    },
    {
        "code": "392",
        "segment": "4",
        "name": "TIM CELULAR",
        "time": "15H"
    },
    {
        "code": "396",
        "segment": "4",
        "name": "SIMTERNET TECNOLOGIA DA INFORMAC AO",
        "time": "15H"
    },
    {
        "code": "397",
        "segment": "4",
        "name": "ALIANCA TELECOM",
        "time": "15H"
    },
    {
        "code": "402",
        "segment": "4",
        "name": "PORTO SEGURO TELECOMUNICACOES",
        "time": "15H"
    },
    {
        "code": "405",
        "segment": "4",
        "name": "COPREL",
        "time": "15H"
    },
    {
        "code": "416",
        "segment": "4",
        "name": "TUBARON TECNOLOGIAS",
        "time": "15H"
    },
    {
        "code": "423",
        "segment": "4",
        "name": "QNET TELECOM LTDA ME PR",
        "time": "15H"
    },
    {
        "code": "427",
        "segment": "4",
        "name": "ON TELECOMUNICACOES LTDA",
        "time": "15H"
    },
    {
        "code": "430",
        "segment": "4",
        "name": "HUGUES TELECOMUNICACOES DO BRASIL LTDA",
        "time": "15H"
    },
    {
        "code": "437",
        "segment": "4",
        "name": "ULTRAWAVE TELECOM EIRELI EPP",
        "time": "15H"
    },
    {
        "code": "446",
        "segment": "4",
        "name": "LGTEL61 INTERNET LTDA M",
        "time": "15H"
    },
    {
        "code": "464",
        "segment": "4",
        "name": "ALGAR SOLUCOES EM TIC S A",
        "time": "15H"
    },
    {
        "code": "466",
        "segment": "4",
        "name": "YAH TELECOMUNICAÇÕES RJ",
        "time": "15H"
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
