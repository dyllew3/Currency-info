
import urllib.request, json,threading,time


CURRENCIES =["USD",  "EUR", "JPY", "BGN", "CZK", "DKK", "GBP", "HUF", "LTL", "LVL", "PLN", "RON", "SEK", "CHF", "NOK", "HRK", "RUB" ,"TRY", "AUD" ,"BRL",
            "CAD", "CNY", "HKD","ILS","INR", "KRW", "MXN", "MYR", "NZD", "PHP", "SGD", "THB","ZAR"]

def thread_id():
    id = 0
    while True:
        yield id
        id += 1

ids = thread_id()

class CurrencyThread(threading.Thread):


    def __init__(self,start,end,currency_list):
        threading.Thread.__init__(self)

        self.subset = []
        if(start < end and start >= 0):
            if(end >= len(currency_list)):
                end = len(currency_list)
            self.subset = currency_list[start:end]
        self.full_list = currency_list
        self.full_list_len = len(self.full_list)
        self.subset_len = len(self.subset)
        self.data = []
        self.base_url_end = ")&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback="

    def run(self):

        self.data = self.get_currency_rates()

    def get_currency_rates(self):
        base_url_begin = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20("

        for i in self.subset:
            final_cur = len(self.full_list) -1
            if(i == self.full_list[self.full_list_len - 1]):
                final_cur = len(self.full_list) - 2
            for j in self.full_list:
                if(i != j):
                    base_url_begin += "%22" +  i + j + "%22"
                    if(i != self.subset[self.subset_len - 1] or j != self.full_list[final_cur] ):
                        base_url_begin += "%2C"
        try:
            with urllib.request.urlopen(base_url_begin + self.base_url_end) as url:
                data = json.loads(url.read().decode())
                return data["query"]["results"]["rate"]

        except Exception as e:

            print(base_url_begin + self.base_url_end)
            return None

    def __repr__(self):
        return ("Subset is " + str(self.subset) )


    @staticmethod
    def run_all_threads(thread_list):
        for i in thread_list:
            i.start()
        for j in thread_list:
            j.join()
pass



def make_threads(amount,cur_list = CURRENCIES):
    threads = []
    if amount > 0:
        inc = int(len(cur_list)/amount)
        prev = 0
        for i in range(0,amount):
            if(i != amount - 1):
                threads.append( CurrencyThread( (inc * i),(inc * (i + 1)), cur_list))
                prev =inc *(i + 1)
            else:
                threads.append( CurrencyThread(prev, len(cur_list),cur_list))
    return threads

def main():
    start_time = time.time()
    inc  = 5
    start = 0
    end = inc
    threads = []
    while start < len(CURRENCIES):
        if(end >= len(CURRENCIES)):
            end = len(CURRENCIES)
        threads.append(CurrencyThread(start,end,CURRENCIES) )
        start = end
        end += inc
    for i in threads:
        print(i)
        i.start()

    count = 0
    for i in threads:
        i.join()
        for item in i.data:
            print(item["id"])
            count += 1
    time_taken = time.time() - start_time
    print("Time take is " +  str(time_taken)  + " seconds" )
    print("Number of currency matches is " + str(count))
    pass
if __name__ == "__main__":
    main()
