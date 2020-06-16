import json
#This is for Staphylococcus aureus bactrie
#gr is de growth rate
#br is de beperkingsfactor

aureus = {
  "name": "xx",
  "info": "Geen informatie beschikbaar momenteel",
  "env-info": {
                "temp": { "temp": 37.0, "min": 6.0 , "max": 45.0},
                "aw":{"aw": "bestaat ffetje niet"},
                "ph": {"ph": 5.0, "min":4., "max":10.0},
                "gr":{"gr":0.3486},
                "br":{"br":17.863441536524924},
                "bw":{"bw":14.53335035111459},



  }
}
with open("../Code/xx.json", "w") as f:
     json.dump(aureus, f)
     f.close()


