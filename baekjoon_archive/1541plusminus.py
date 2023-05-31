import re
minus_search = re.compile("[-]")
plus_minus_search = re.compile("[+]|[-]")
form = input()

span = re.search(minus_search,form)
#span.span()[0] #2
#span.span()[1] #3
if span:
    fir_num_array = re.split(plus_minus_search,form[:span.span()[0]])
    sec_num_array = re.split(plus_minus_search,form[span.span()[1]:])

    result = sum(map(int,fir_num_array)) - sum(map(int,sec_num_array))
    print(result)
else:
    num_array = re.split(plus_minus_search,form)
    print(sum(map(int,num_array)))