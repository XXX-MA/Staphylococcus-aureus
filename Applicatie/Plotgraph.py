import json
import tkinter as tk
from tkinter import messagebox

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from Code.EndResults import EndResults
from Code.JsonChecker import JsonChecker


class PlotGraph(tk.Frame):
    """
    In dit klass worden de inputs die nodig voor het bereken van de intervals en het tekenen van het
    grafiek van het gebruiker gevraagd. Verolgens wordt het gerafiek aan de op een nieuwe scher aangetoond.

    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        frameBovenPlotGraph = tk.Frame(self, bg="#81B29A")

        titel = tk.Label(frameBovenPlotGraph, text="Grafiek tekenen", fg="#3D405B", bg="#81B29A", font='Arial 35 bold')
        tk.Frame.configure(self, bg="#FFEEDD")

        # buttons aanmaken
        buttonTerugNaarHome = tk.Button(frameBovenPlotGraph, text="Terug naar de homepagina", height=5, width=23,
                              font='Arial 12',  fg="#3D405B", command=lambda: controller.showFrame("MainPage"))

        # Deze button rest de input van de gebruiker in de entry
        restInputButton = tk.Button(frameBovenPlotGraph, text="Clear input", height=5, width=23, font='Arial 12',
                                    fg="#3D405B", command=lambda: reset())
        # Labels aanmaken
        bactLab = tk.Label(frameBovenPlotGraph, text="Wat is de naam bacterie?", font='Arial 18', bg="#81B29A", fg="#3D405B")
        tempLab = tk.Label(frameBovenPlotGraph, text="Wat is de tempratuur?", font='Arial 18', bg="#81B29A", fg="#3D405B")
        pHLab = tk.Label(frameBovenPlotGraph, text="Wat is de pH waarde?", font='Arial 18', bg="#81B29A", fg="#3D405B")
        awLab = tk.Label(frameBovenPlotGraph, text="Wat is de water activiteit?", font='Arial 18', bg="#81B29A", fg="#3D405B")
        tim2Lab = tk.Label(frameBovenPlotGraph, text="Wat is de eind groeitijd in uren?", font='Arial 18', bg="#81B29A", fg="#3D405B")
        grafiekLab = tk.Label(frameBovenPlotGraph, text="Kies de soort berekening \n", font='Arial 18 bold', fg="#FFEEDD",
                              bg="#81B29A")
        legeLabel= tk.Label(frameBovenPlotGraph,  bg="#81B29A")

        # om de waarde van de radiobuttons te getten
        typeGrafiek = tk.IntVar()

        # wordt altijd eerst op 1 geset
        typeGrafiek.set(1)

        RadioButton1 = tk.Radiobutton(frameBovenPlotGraph, text=" Logistic met de maximum aantal \ncellen als beperkende factor",
                                      variable=typeGrafiek, value=1,  bg="#81B29A",  font='Arial 18', fg="#3D405B")
        RadioButton2 = tk.Radiobutton(frameBovenPlotGraph , text=" Logistic curve met sterffase", variable=typeGrafiek,
                                      value=2,  bg="#81B29A", font='Arial 18', fg="#3D405B")
        RadioButton3 = tk.Radiobutton(frameBovenPlotGraph, text=" Log groei met 4 faces, lag, log, \nstationaire en sterffases",
                                      variable=typeGrafiek, value=3,  bg="#81B29A", font='Arial 18', fg="#3D405B")
        RadioButton4 = tk.Radiobutton(frameBovenPlotGraph, text=" De verandering van de groeifactor\n ten opzichte van de tempartuur",
                                      variable=typeGrafiek, value=4,  bg="#81B29A",  font='Arial 18', fg="#3D405B")

        # De entries aamnaken
        bactEN = tk.Entry(frameBovenPlotGraph, font='Arial 14')
        tempEN = tk.Entry(frameBovenPlotGraph, font='Arial 14')
        phEN = tk.Entry(frameBovenPlotGraph, font='Arial 14')
        tim2EN = tk.Entry(frameBovenPlotGraph, font='Arial 14')
        awEN = tk.Entry(frameBovenPlotGraph, font='Arial 14')

        # De entries waardes naar de functie PlotGrafiek doorsturen

        laatGrafiekZien=tk.Button(frameBovenPlotGraph, text="Laat de grafiek zien!", height=5, width=23,
                            font='Arial 12', fg="#3D405B", command=lambda: PlotGraph.PlotGrafiek(self, (bactEN.get()),
                                  tempEN.get(), phEN.get(), awEN.get(), tim2EN.get(), typeGrafiek.get()))

        # Functie die de entries kan reseten
        def reset():
            bactEN.delete(0, tk.END)
            tempEN.delete(0, tk.END)
            phEN.delete(0, tk.END)
            tim2EN.delete(0, tk.END)
            awEN.delete(0, tk.END)

        # Hier wordt alles in de schrem aangetood
        frameBovenPlotGraph.pack(side=tk.LEFT, fill=tk.BOTH)
        titel.grid(row=0, column=1, pady= 10, padx= 10)
        bactLab.grid(row=6, column=0, sticky="w")
        tempLab.grid(row=8, column=0, sticky="w")
        pHLab.grid(row=10, column=0, sticky="w")
        tim2Lab.grid(row=14, column=0, sticky="w")
        awLab.grid(row=15, column=0, sticky="w")
        grafiekLab.grid(row=6, column=4, sticky="w")
        laatGrafiekZien.grid(row=33, column=0)
        buttonTerugNaarHome.grid(row=33, column=3, sticky="s")

        restInputButton.grid(row=33, column=1, sticky="s")

        bactEN.grid(row=6, column=1, pady=10, padx=10, ipady=10, ipadx=100)
        tempEN.grid(row=8, column=1, pady=10, padx=10, ipady=10, ipadx=100)
        phEN.grid(row=10, column=1, pady=10, padx=10, ipady=10, ipadx=100)
        tim2EN.grid(row=14, column=1, pady=10, padx=10, ipady=10, ipadx=100)
        awEN.grid(row=15, column=1, pady=10, padx=10, ipady=10, ipadx=100)
        legeLabel.grid(row=30, column=1, pady=10, padx=10, ipady=25, ipadx=100)

        RadioButton1.grid(row=8, column=4, sticky="w")
        RadioButton2.grid(row=10, column=4, sticky="w")
        RadioButton3.grid(row=14, column=4, sticky="w")
        RadioButton4.grid(row=15, column=4, sticky="w")

    def PlotGrafiek(self, bact_naam: str, temperature: float, pH: float, aw: float, endTime: int, typeG: int):
        """  Hier wordt de entries naar het algoritme doorgetuurd en het grafiek wordt hier getekent. """

        check = PlotGraph.waring(self,bact_naam, temperature, pH, aw)
        if check == "":
            # hier wordt er een nieuwe window aangemaakt voor het showen van de grfaiek
            newwindow = tk.Toplevel()
            newwindow.title('Growth Curve app')
            screenWidth = newwindow.winfo_screenwidth()
            screenHeight = newwindow.winfo_screenheight()
            newwindow.geometry("{}x{}+-7+0".format(screenWidth, screenHeight - 27))
            newwindow.iconphoto(False, tk.PhotoImage(file="../Extra bestanden/graphicon.png"))

            bact_naam = str(bact_naam)
            temperature = float(temperature)
            pH = float(pH)
            aw = float(aw)

            y = EndResults(bact_naam, temperature, pH, aw, endTime, typeG)
            # wordt op basis van de lengte van y gemaakt
            x = np.linspace(0, len(y), (len(y)))
            # hier wordt er figure gemaakt en aangepast
            f = Figure(figsize=(5, 5), dpi=100)
            f.suptitle('Growth Curve', fontsize=14, fontweight='bold')
            f.patch.set_facecolor("#F4F1DE")
            a = f.add_subplot(111)
            a.set_ylabel('Groei in CFU/ml (Ln)')

            if typeG == 4: # hier is de groeifactor wat op de y-as staat
                x = np.linspace(int(temperature), 46,len(y))
                a.set_ylabel("μ (h−1)")
                a.set_xlabel("Temperature in celsius")
            else: # hier moet de x-as tijd zijn
                a.set_xlabel('Tijd in uur')

            a.plot(x, np.array(y), "#3D405B")
            a.plot(x, np.array(y), "o", color="#E07A5F")

            # Hier wordt het grafiek in getekend
            canvas = FigureCanvasTkAgg(f, newwindow)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
            # Hier wordt de toolbar aangetoond
            toolbar = NavigationToolbar2Tk(canvas, newwindow)
            toolbar.config(background="#F4F1DE")
            toolbar.message_label.config(background="#F4F1DE")
            toolbar.update()
            canvas.tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        else:

            messagebox.showwarning("warning",
                                   f"Je hebt {check} niet/verkeerd ingevoerd.\n ----probeer het opnieuw----")

    def waring(self,bact_naam: str, temperature: float, pH: float, aw: float):
        """
        In deze functie wordt de input(entries) waardes gecheckt, met behulp van de json bestand en class JsonChecker

        """
        waring_ = ""
        try:
            bact_naam = str(bact_naam)
            temperature = float(temperature)
            pH= float(pH)
            aw = float(aw)
        except ValueError:
           waring_ += ""

        try:
            with open("../Extra bestanden/" + bact_naam + ".json", "r") as f:
                info = json.load(f)
        except FileNotFoundError:
            waring_ += " bacterie naam , "

        temp_check = JsonChecker(bact_naam, temperature, pH, "temp", temperature)
        temp_check_terug = temp_check.values_check()

        ph_check = JsonChecker(bact_naam, temperature, pH, "ph", pH)
        ph_check_terug = ph_check.values_check()

        aw_check = JsonChecker(bact_naam, temperature, pH, "aw", aw)
        aw_check_terug = aw_check.values_check()

        if temp_check_terug is None: waring_ += "tempratuur ,"
        if ph_check_terug is None: waring_ += "pH , "
        if aw_check_terug is None: waring_ += "water activiteit, "
        return waring_