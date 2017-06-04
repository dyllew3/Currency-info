import time,sys
from currencyvalues import CURRENCIES, make_threads, CurrencyThread

MAX_REQ_ALLOWED = 7
NUM_TESTS = 1
MIN = 1
MAX = 34


def num_threads(num_tests = NUM_TESTS,min_t = MIN,max_t = MAX):
    min_time = float("inf")
    amount = MIN
    for i in range(min_t,max_t + 1):

        div = int(len(CURRENCIES)/i)
        mod = len(CURRENCIES)% i


        total_time = 0

        if( (len(CURRENCIES) - (div * (i - 1))) > MAX_REQ_ALLOWED  ):
            continue
        if(num_tests <= 0):
            num_tests = NUM_TESTS
        for j in range(num_tests):
            start = time.time()
            threads = make_threads(i,CURRENCIES)
            CurrencyThread.run_all_threads(threads)
            time_taken = time.time() - start
            total_time += time_taken
        avg = total_time/num_tests
        if(avg < min_time):
            min_time = avg
            amount = i
        test_str = str(num_tests)  + ( " tests" if NUM_TESTS > 1 else " test" ) + " for "
        print("Average of " + test_str  + str(i) + " threads is " + str(avg))
    return amount




if __name__ == "__main__":

    num_tests = NUM_TESTS
    if(len(sys.argv) > 1):
        num_tests = argv[1]
    threads = []
    for  i in range(MIN,(MAX + 1)):

        div = int(len(CURRENCIES)/i)
        mod = len(CURRENCIES)% i


        total_time = 0

        if( (len(CURRENCIES) - (div * (i - 1))) > MAX_REQ_ALLOWED  ):
            continue
        if(num_tests <= 0):
            break
        for j in range(num_tests):
            start = time.time()
            threads = make_threads(i,CURRENCIES)
            CurrencyThread.run_all_threads(threads)
            time_taken = time.time() - start
            total_time += time_taken
        avg = total_time/num_tests
        test_str = str(num_tests)  + ( " tests" if NUM_TESTS > 1 else " test" ) + " for "
        print("Average of " + test_str  + str(i) + " threads is " + str(avg))
    count = 0
    for k in threads:
        for l  in k.data:
            count += 1
            #print(l)

    print(count)
