# GET https://simpledebit.gocardless.io/merchants HTTP/1.1
import requests
import csv

url = "https://simpledebit.gocardless.io/merchants"
#print(url)
resp1 = requests.get(url)
#print(resp1.json())
resp_data = resp1.json()
discount = {}
s = 0
with open('payments1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["iban", "amount_in_pence"])

    for i in resp_data:
        s = s+1
        total_amt = 0
        total_fee = 0
        trans = 0

        url1 = url + "/" + str(i)
        #print(url1)
        resp2 = requests.get(url1)
        resp2_data = resp2.json()
        #print(resp2_data)
        id = resp2_data['id']
        iban = resp2_data['iban']
        print(iban)
        discount['min'] = resp2_data['discount']['minimum_transaction_count']
        discount['fees'] = resp2_data['discount']['fees_discount']
        for amt in resp2_data['transactions']:
            trans += 1

            total_amt = total_amt + amt['amount']
            total_fee = total_fee + amt['fee']
        # print(trans)
        # print(discount['min'])
        if trans >= discount['min']:
            total_fee = total_fee - ((discount['fees']) * total_fee) / 100
        total_amt = int(total_amt - total_fee)
        writer.writerow([iban, total_amt])

        #print(total_amt)

# print(iban)
# print(total_amt)

