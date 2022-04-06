from rw_sheet import write_final_result
from tradingview_ta import TA_Handler, Interval, Exchange
from time import sleep

SPREADSHEET_ID = '1ozni20iCfhX-GjpMfUk4vSNxVDnAEo93C1QqQirfJyU'


def Cedear(accion,tipo):
    tesla = TA_Handler(
    symbol=accion,
    screener="america",
    exchange=tipo,
    interval=Interval.INTERVAL_1_WEEK
    )
    valorDelRsi =  tesla.get_analysis().indicators["RSI"]
    estadoDelRsi = tesla.get_analysis().oscillators["COMPUTE"]["RSI"]
    valorDelDmiPo =  tesla.get_analysis().indicators["ADX+DI"]
    valorDelDmiNe =  tesla.get_analysis().indicators["ADX-DI"]
    estadoDelDmi =  tesla.get_analysis().oscillators["COMPUTE"]["ADX"]
    valorDelMacd = tesla.get_analysis().indicators["MACD.macd"]
    valorDelMacdSignal = tesla.get_analysis().indicators["MACD.signal"]
    estadoDelMacd = tesla.get_analysis().oscillators["COMPUTE"]["MACD"]
    valorDeMm30 = tesla.get_analysis().indicators["SMA30"]
    estadoDeMm30 = tesla.get_analysis().moving_averages["COMPUTE"]["SMA30"]
    volume = tesla.get_analysis().indicators["volume"]
    mapa = {accion:{"RSI": valorDelRsi,"Volumen": volume, "RSI-Estado": estadoDelRsi, "DI-":valorDelDmiNe,"DI+":valorDelDmiPo, "DMI-Estado": estadoDelDmi,"MACD":valorDelMacd,"MACD-Signal":valorDelMacdSignal, "MACD-Estado": estadoDelMacd, "MM30": valorDeMm30, "MM30-Estado":estadoDeMm30}}
    return mapa 


listaNasdaq = [
"AAPL",
"ADBE",
"ADI",
"ADP",
"AMAT",
"AMD",
"AMGN",
"AMZN",
"AVGO",
"AZN",
"BIDU",
"BIIB",
"BIOX",
"CAR",
"COST",
"CSCO",
"DOCU",
"EBAY",
"ERIC",
"ETSY",
"FB",
"FSLR",
"GILD",
"GOOGL",
"GRMN",
"HON",
"INTC",
"JD",
"MELI",
"MSFT",
"NFLX",
"NTES",
"NVDA",
"PAAS",
"PCAR",
"PEP",
"PYPL",
"QCOM",
"ROST",
"SBUX",
"TRIP",
"TSLA",
"TXN",
"VOD",
"VRSN",
"WBA",
"WB",
"YY",
"ZM",
]

mapaCompletoNasdaq = []

for i in listaNasdaq:
    mapaCompletoNasdaq.append(Cedear(i,"NASDAQ"))
    index= listaNasdaq.index(i)
    numero = 4 + index
    string = "CEDEARS!E" + str(numero)
    where_to_write = string
    data_to_write = [[mapaCompletoNasdaq[index][i]["Volumen"]]]
    data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)



listaNyse = [
"ABBV",
"ABEV",
"ABT",
"ACH",
"AEG",
"AEM",
"AIG",
"AMX",
"ARCO",
"ASR",
"AUY",
"AVY",
"AXP",
"BA",
"BABA",
"BB",
"BBD",
"BCS",
"BHP",
"BK",
"BMY",
"BP",
"BRFS",
"BRK.B",
"BSBR",
"C",
"CAAP",
"CAH",
"CAJ",
"CAT",
"CDE",
"CL",
"CRM",
"CS",
"CVX",
"CX",
"DD",
"DE",
"DEO",
"DESP",
"E",
"EFX",
"ERJ",
"FCX",
"FDX",
"FMX",
"GE",
"GFI",
"GGB",
"GLW",
"GOLD",
"GPRK",
"GS",
"GSK",
"HAL",
"HD",
"HDB",
"HL",
"HMC",
"HMY",
"HNP",
"HOG",
"HPQ",
"HSBC",
"HSY",
"HWM",
"IBM",
"IBN",
"IFF",
"ING",
"IP",
"ITUB",
"JCI",
"JNJ",
"JPM",
"KB",
"KEP",
"KGC",
"KMB",
"KO",
"LFC",
"LLY",
"LMT",
"LVS",
"LYG",
"MA",
"MBT",
"MCD",
"MDT",
"MFG",
"MMC",
"MMM",
"MO",
"MRK",
"MSI",
"MUFG",
"NEM",
"NGG",
"NKE",
"NMR",
"NTCO",
"NUE",
"NVS",
"ORAN",
"ORCL",
"PAC",
"PBI",
"PBR",
"PFE",
"PG",
"PHG",
"PSO",
"PSX",
"PTR",
"RDS.B",
"RIO",
"RTX",
"SAN",
"SAP",
"SBS",
"SCCO",
"SHOP",
"SID",
"SLB",
"SNA",
"SNAP",
"SNOW",
"SNP",
"SONY",
"SPOT",
"SQ",
"SUZ",
"SYY",
"T",
"TGT",
"TM",
"TMO",
"TSM",
"TTE",
"TTM",
"TV",
"TWTR",
"UGP",
"UL",
"UNH",
"UNP",
"USB",
"V",
"VALE",
"VIST",
"VIV",
"VZ",
"WBK",
"WFC",
"WMT",
"X",
"XOM",
"YELP",
]




sleep(5)

mapaCompletoNyse = []


for i in listaNyse:
    mapaCompletoNyse.append(Cedear(i,"NYSE"))
    index= listaNyse.index(i)
    numero = 188 + index
    string = "CEDEARS!E" + str(numero)
    where_to_write = string
    data_to_write = [[mapaCompletoNyse[index][i]["Volumen"]]]
    data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)







