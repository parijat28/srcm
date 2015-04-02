from django.shortcuts import render
import urllib, json

def index(request):
    return render(request, 'index.html')

def login(request):
    url = "http://52.74.39.93/api/abhyasis/"
    response = urllib.urlopen(url)
    a = json.loads(response.read())
#    a = {u'count': 539, u'previous': None, u'results': [{u'first_name': None, u'last_name': None, u'ref': u'BHKIAA001', u'id': 1687, u'name': u'KANNAN  IYER'}, {u'first_name': None, u'last_name': None, u'ref': u'BHSIAA001', u'id': 1710, u'name': u'SRIRAM IYER'}, {u'first_name': None, u'last_name': None, u'ref': u'SGDPAA002', u'id': 8139, u'name': u'DEEBHA PONNURAJ'}, {u'first_name': None, u'last_name': None, u'ref': u'INKRAE399', u'id': 13604, u'name': u'K. RAMESH BABU'}, {u'first_name': None, u'last_name': None, u'ref': u'INNRAE228', u'id': 13622, u'name': u'N. RAJAN'}, {u'first_name': None, u'last_name': None, u'ref': u'INKJAE100', u'id': 15267, u'name': u'KRISHNA JOSHI'}, {u'first_name': None, u'last_name': None, u'ref': u'INAMAE432', u'id': 17126, u'name': u'ABHISHEK MEHRA'}, {u'first_name': None, u'last_name': None, u'ref': u'INBSAE560', u'id': 19859, u'name': u'BHARAT SONI'}, {u'first_name': None, u'last_name': None, u'ref': u'INSPAF154', u'id': 21066, u'name': u'SHIV PRASAD'}, {u'first_name': None, u'last_name': None, u'ref': u'INMTAE215', u'id': 21970, u'name': u'M. TEJASWINI'}, {u'first_name': None, u'last_name': None, u'ref': u'INDSAE469', u'id': 22062, u'name': u'D. SHANMUGASUNDARAM'}, {u'first_name': None, u'last_name': None, u'ref': u'INSKAF453', u'id': 22063, u'name': u'S. KALAVATHI'}, {u'first_name': None, u'last_name': None, u'ref': u'INKVAE226', u'id': 23375, u'name': u'KIRAN VYAS'}, {u'first_name': None, u'last_name': None, u'ref': u'INCLAE029', u'id': 24213, u'name': u'CHANDAN LAL GUPTA'}, {u'first_name': None, u'last_name': None, u'ref': u'INVIAE078', u'id': 24215, u'name': u'VASUNDHARA I. MUKKANNAVAR'}, {u'first_name': None, u'last_name': None, u'ref': u'INTNAE040', u'id': 25626, u'name': u'TALLAPALEM NARAYANA'}, {u'first_name': None, u'last_name': None, u'ref': u'INRCAE302', u'id': 26159, u'name': u'RAMESH CHANDRA KHANNA'}, {u'first_name': None, u'last_name': None, u'ref': u'INSSAG345', u'id': 26252, u'name': u'SUNIL SOLANKI'}, {u'first_name': None, u'last_name': None, u'ref': u'INPSAE872', u'id': 26253, u'name': u'PREETI SOLANKI'}, {u'first_name': None, u'last_name': None, u'ref': u'INMVAE259', u'id': 27425, u'name': u'M. VEERA RAGHAVAMMA'}], u'next': u'http://52.74.39.93/api/abhyasis/?page=2'}
    results = a['results']
    left = results[0:-1:2]
    right = results[1:-1:2]
    return render(request, 'login.html', {'y':results,'left':left, 'right':right})
# Create your views here.
