
import json
import tkinter as tk

bg_background = "#81B29A"
bg_button = "#F4F1DE"
fg = "#3D405B"


class InfoBact(tk.Frame):
    """In dit klass kunnen er informatie over een bepaalde bactrie geshowed worden, door gebruik van de json bestand
        te maken"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # 2 frames aangemaakt om  de layout beter te kunnen organisieren
        frameBovenInfoBact = tk.Frame(self, bg=bg_background)
        frameOnderInfoBact = tk.Frame(self, bg=bg_background)

        titel=tk.Label(frameOnderInfoBact, text="Informatie over de bacterie", fg='black', font='Arial 35 bold', bg =bg_background)
        tk.Frame.configure(self, bg=bg_background)

        buttonMainPage = tk.Button(frameBovenInfoBact, text="Terug naar de homepagina",height=5, width=23, fg=fg,
                             bg="white", font='Arial 10',command=lambda: controller.showFrame("MainPage"))

        buttonPlotGraph = tk.Button(frameBovenInfoBact, text="Teken de grafiek",height=5, width=23, fg=fg,
                             bg="white", font='Arial 10', command=lambda: controller.showFrame("PlotGraph"))

        LabelVraag = tk.Label(frameOnderInfoBact, text="Over welke bacterie wil je informatie krijgen?\n "
                                             "Type de naam van de  bacterie hieronder:", font='Arial 18', bg=bg_background)

        entryBactName = tk.Entry(frameOnderInfoBact, font="Arial 18")

        buttonInfoJson = tk.Button(frameOnderInfoBact, text="Zoek het op!",height=2, width=12, fg=fg,
                             bg="white", font='Arial 10', command=lambda: findJson(entryBactName.get()))


        def findJson(input):
            """De entry van de gebruiker wordt naar deze functie doorgestuurd om vervolgens de bijhornde info in de json
                bestand te zoeken. Voor het gevaal dat de gebruiker een naam invoert die niet tussen de json bestanden staat,
                 gebruik ik een try except"""
            try:
                with open("../json bestanden/"+str(input) + ".json", "r") as f:
                    info = json.load(f)
                    informatieVanJson= info["info"]
                    infoUitprinten= tk.Label(frameOnderInfoBact,text="", font='Arial 16 ', bg=bg_background)
                    infoUitprinten.config(text= informatieVanJson)
                    infoUitprinten.pack(side=tk.TOP, fill=tk.X, padx=5)

            except FileNotFoundError:
                infoUitprinten = tk.Label(frameOnderInfoBact, text="We hebben helaas geen informatie kunnen vinden over deze bacterie",
                                          font='Arial 16 ', bg=bg_background)
                infoUitprinten.pack(side=tk.TOP, fill=tk.X, padx=5)

        # hier wordt alles op het scherm aangetoond
        frameOnderInfoBact.pack(pady=0, expand=tk.TRUE)
        frameBovenInfoBact.pack(expand=tk.TRUE)
        titel.pack(side=tk.TOP, fill=tk.X)
        LabelVraag.pack(side=tk.TOP, fill=tk.X, padx=5)
        entryBactName.pack(side=tk.TOP, padx=40, pady=40, ipady=10, ipadx=130)
        buttonInfoJson.pack(side=tk.TOP, ipady=10, ipadx=110)
        buttonPlotGraph.pack(side=tk.LEFT, fill=tk.X, padx=10)
        buttonMainPage.pack(side=tk.LEFT, fill=tk.X, padx=10)
