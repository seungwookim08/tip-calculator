province_list = {'AB':0,'BC':7,'MB':8,'NB':10,'NL':10,'NS':10,'NT':0,'NU':0,'ON':13,'PE':10,'QC':10,'SK':6,'YT':10}
federal_tax = 5
def getTax(price,province):
    return (price*(1+(province_list[province] + federal_tax)/100))

def getTip(price, tipRate):
    tipRate = 15 # for now hard-coded
    return (price*(1+tipRate/100))
