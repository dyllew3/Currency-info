import currency,test
from test import num_threads
from currency import CurrencyThread
from math import log
from BellmanFord import BellmanFord

def set_edges(rates,currencies = currency.CURRENCIES):
    edges = dict()
    for  i in currencies:
        edges[i] = dict()
    for j in rates:

        u,v = j["id"][0:3],j["id"][3:]
        print(u + " " +  v + " " +  j["Rate"])
        weight = log(round(float(j["Rate"]) ** -1,4))
        edges[u][v] = weight
    return edges

if __name__ == "__main__":
    threads_len = num_threads()
    threads = currency.make_threads(threads_len)
    CurrencyThread.run_all_threads(threads)
    currency_rates = []
    vertices = currency.CURRENCIES
    for  i in  threads:
        for j in i.data:
            currency_rates.append(j)

    edges =set_edges(currency_rates)
    for u in  edges:
        print(edges[u])

    a =BellmanFord(vertices,set_edges(currency_rates),currency.CURRENCIES[0])
