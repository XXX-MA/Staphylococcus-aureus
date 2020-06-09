import json
#This is for Staphylococcus aureus bactrie
#gr is de growth rate
#br is de beperkingsfactor

aureus = {
  "name": "s-aureus",
  "info": "Staphylococcus aureus is een stafylokok die toxinen afscheidt en grampositief kleurt.[1] De toxinen hebben een negatieve werking op het menselijk lichaam."
          " Staphylococcus aureus zit in 20 tot 30 procent van de gevallen op de huid van mens en dier en op de slijmvliezen, zoals de neusholte. Als de bacterie door de huid heen het lichaam binnendringt kan deze huidinfecties en wondinfectie veroorzaken (ook na operaties), maar ook urineweginfecties, longontsteking en bij koeien uierontsteking.De identificatie van Staphylococcus aureus gebeurt via een coagulasetest, "
          "waarbij de typische Staphylococcus aureus een positief resultaat zal geven, in tegenstelling tot andere soorten stafylokokken. Atypische varianten kunnen echter ook een negatief resultaat geven bij de coagulasetest.",
  "env-info": {
                "temp": { "temp": 37, "min": 7 , "max": 48},
                "aw":{"aw": "bestaat ffetje niet"},
                "ph": {"ph": [6,7], "min": 4.0, "max":10.0},
                "gr":{"gr":2},
                "br":{"br":10000000000000000000000000000},


  }
}
with open("s-aureus.json", "w") as f:
     json.dump(aureus, f)
     f.close()

