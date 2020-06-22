import tkinter as tk
from tkinter import messagebox

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from Code.EndResults import EndResults
from Code.JsonChecker import JsonChecker


class PlotGraph(tk.Frame):
    """In dit klass worden de inputs die nodig voor het bereken van de intervals en het tekenen van het
       grafiek van het gebruiker gevraagd verolgens wordt het gerafiek aan de rechtere kant van de scherm
       geschowed, hier ook maak ik gebruik van de try, except voor het geval dat de gebruiker een verkerede
        type input in toetst """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        frameBovenPlotGraph = tk.Frame(self, bg="#81B29A")

        titel = tk.Label(frameBovenPlotGraph, text="Grafiek tekenen",fg = "#3D405B", bg= "#81B29A", font='Arial 35 bold')
        tk.Frame.configure(self, bg="#FFEEDD")#ROSY BROWN
        buttonTerugNaarHome =tk.Button(frameBovenPlotGraph, text="Terug naar de homepagina",height=5, width=23,
                             bg='#F4F1DE', font='Arial 12',  fg =  "#3D405B" ,command=lambda: controller.showFrame("MainPage"))

        restInputButton = tk.Button(frameBovenPlotGraph, text="Clear input", height=5, width=23,
                                     bg="#F4F1DE", font='Arial 12', fg ="#3D405B",command=lambda: rest())

        bactLab= tk.Label(frameBovenPlotGraph,text="Wat is de naam bacterie?", font='Arial 18', bg="#81B29A", fg = "#3D405B")
        tempLab = tk.Label(frameBovenPlotGraph, text="Wat is de tempratuur?",font='Arial 18', bg="#81B29A", fg = "#3D405B")
        pHLab= tk.Label(frameBovenPlotGraph,text="Wat is de pH waarde?",font='Arial 18', bg="#81B29A", fg = "#3D405B")
        awLab= tk.Label(frameBovenPlotGraph,text="Wat is de water activiteit?", font='Arial 18', bg="#81B29A", fg = "#3D405B")

        tim2Lab= tk.Label(frameBovenPlotGraph, text="Wat is de eindtijd in uren?",font='Arial 18', bg="#81B29A", fg = "#3D405B")
        grafiekLab = tk.Label(frameBovenPlotGraph, text="Kies de soort berekening \n",font='Arial 18 bold', fg = "#FFEEDD",
                              bg="#81B29A")

        typeGrafiek = tk.IntVar()
        typeGrafiek.set(1)

        RadioButton1= tk.Radiobutton( frameBovenPlotGraph, text = "1. logistic met de maximum aantaal cellen \nals beperkende factor",
                                      variable = typeGrafiek, value = 1,  bg="#81B29A",  font='Arial 18', fg = "#3D405B")
        RadioButton2= tk.Radiobutton( frameBovenPlotGraph, text = "2. logistic curve met sterffase", variable=typeGrafiek,
                                      value = 2,  bg="#81B29A", font='Arial 18', fg = "#3D405B")
        RadioButton3= tk.Radiobutton( frameBovenPlotGraph, text = "3. log groei met 4 faces, lag, log, \nstationaire en sterffases",
                                      variable = typeGrafiek, value = 3,  bg="#81B29A", font='Arial 18', fg = "#3D405B")
        RadioButton4= tk.Radiobutton( frameBovenPlotGraph, text = "4. logistic met de maximum tempratuur \nals beperkende factor",
                                      variable = typeGrafiek, value = 4,  bg="#81B29A",  font='Arial 18', fg = "#3D405B")

        legeLabel= tk.Label(frameBovenPlotGraph,  bg="#81B29A")#PEACH PUFF
        bactEN = tk.Entry(frameBovenPlotGraph, font='Arial 14', )# bg='#F4F1DE')
        tempEN = tk.Entry(frameBovenPlotGraph, font='Arial 14', )# bg='#F4F1DE')
        phEN = tk.Entry(frameBovenPlotGraph, font='Arial 14', )# bg='#F4F1DE')
        tim2EN = tk.Entry(frameBovenPlotGraph, font='Arial 14',) #bg='#F4F1DE')
        awEN = tk.Entry(frameBovenPlotGraph, font='Arial 14', )# bg='#F4F1DE')

        try:
            laatGrafiekZien=tk.Button(frameBovenPlotGraph, text="Laat de grafiek zien!", height=5, width=23,
                                bg="#F4F1DE", font='Arial 12', fg =  "#3D405B",command=lambda: PlotGraph.PlotGrafiek(self, str(bactEN.get()),
                                float(tempEN.get()), float(phEN.get()), float(awEN.get()),int(tim2EN.get()),
                                                                                    int(typeGrafiek.get())))
        except ValueError:
            messagebox.showwarning("warning", "Je hebt 1 of meerdere inputs verkeerd ingevoerd,\n probeer het opnieuw")

        frameBovenPlotGraph.pack(side=tk.LEFT, fill=tk.BOTH)

        def rest():
            bactEN.delete(0, tk.END)
            tempEN.delete(0, tk.END)
            phEN.delete(0, tk.END)
            tim2EN.delete(0, tk.END)
            awEN.delete(0, tk.END)

        #Hier wordt alles in de schrem aangetood
        titel.grid(row=0, column=1, pady= 10, padx= 10)
        bactLab.grid(row=6, column=0, sticky="w")
        tempLab.grid(row=8, column=0, sticky="w")
        pHLab.grid(row=10, column=0, sticky="w")
        tim2Lab.grid(row=14, column=0, sticky="w")
        awLab.grid(row=15, column=0, sticky="w")
        grafiekLab.grid(row=6, column=4, sticky="w")
        laatGrafiekZien.grid(row=33, column=1)
        buttonTerugNaarHome.grid(row=33, column=0, sticky="s")

        restInputButton.grid(row= 33, column=3, sticky="s")

        bactEN.grid(row=6, column=1, pady= 10, padx= 10, ipady=10, ipadx=100)
        tempEN.grid(row=8, column=1, pady= 10, padx= 10, ipady=10, ipadx=100)
        phEN.grid(row=10, column=1, pady= 10, padx= 10, ipady=10, ipadx=100)
        tim2EN.grid(row=14, column=1, pady= 10, padx= 10, ipady=10, ipadx=100)
        awEN.grid(row=15, column=1, pady= 10, padx= 10, ipady=10, ipadx=100)
        legeLabel.grid(row=30, column=1, pady= 10, padx= 10, ipady=25, ipadx=100)

        RadioButton1.grid(row=8, column=4, sticky="w")
        RadioButton2.grid(row=10, column=4, sticky="w")
        RadioButton3.grid(row=14, column=4, sticky="w")
        RadioButton4.grid(row=15, column=4, sticky="w")

    def PlotGrafiek(self, bact_naam, temperature, pH, aw, endTime, typeG):
        """Hier wordt de y voor het grafiek van het aloritme opgehaald en getekent."""

        temp_check = JsonChecker(bact_naam, temperature, pH, "temp", temperature)
        temp_check_terug = temp_check.values_check()

        ph_check = JsonChecker(bact_naam, temperature, pH, "ph", pH)
        ph_check_terug = ph_check.values_check()

        aw_check = JsonChecker(bact_naam, temperature, pH, "aw", aw)
        aw_check_terug = aw_check.values_check()

        if (temp_check_terug and ph_check_terug and aw_check_terug) is not None:
            try:
                newwindow = tk.Toplevel()
                newwindow.title('Growth Curve app')
                screenWidth = newwindow.winfo_screenwidth()
                screenHeight = newwindow.winfo_screenheight()
                newwindow.geometry("{}x{}+-7+0".format(screenWidth, screenHeight - 27))

                y = EndResults(bact_naam, temperature, pH, aw, endTime, typeG)
                x = np.linspace(0, len(y), (len(y)))  # wordt op basis van de lengte van y gemaakt
                f = Figure(figsize=(5, 5), dpi=100)
                f.suptitle('Growth Curve', fontsize=14, fontweight='bold')
                a = f.add_subplot(111)
                a.set_ylabel('Groei in CFU/ml')
                if typeG == 1 or typeG == 3 or typeG == 2: # hier moet de x-as tijd zijn
                    a.set_xlabel('Tijd in uur')
                if typeG == 4:
                    x = np.linspace(int(temperature), 46 ,len(y))
                    a.set_ylabel("μ (h−1)")
                    a.set_xlabel("Temperature in celsius")

                a.plot(x, np.array(y))

                # Hier wordt het grafiek in getekend
                canvas = FigureCanvasTkAgg(f, newwindow)
                canvas.draw()
                canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
                # Hier wordt de toolbar aangetoond
                toolbar = NavigationToolbar2Tk(canvas, newwindow)
                toolbar.update()
                canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
            except ValueError:
                messagebox.showwarning("warning", "Je hebt 1 of meerdere inputs verkeerd ingevoerd,\n "
                                                  "probeer het opnieuw")
        else:
            messagebox.showwarning("warning",
                                   "Je hebt 1 of meerdere inputs verkeerd ingevoerd,\n probeer het opnieuw")

