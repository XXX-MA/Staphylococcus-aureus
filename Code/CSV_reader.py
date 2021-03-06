import csv


class ReadIt:
    """
    A ReadIt object can be read from a csv file containing results from a laboratory study and then some constants
    normally needed in calculating bacterial growth can be identified.

     Parameters
    ----------
    filepath: String
        The file name specifies a unique location in the system

    Attributes
    ----------
    filepath
        Stores the file name specifies a unique location in the system
    """
    # the constructor
    def __init__(self, filepath: str):
        self.filepath = filepath

        self.lijst = self.readd(self.filepath)

    def readd(self, filepath: str) -> list:
        """
        Will look up the file path and read the values from it and convert the type of the values to float.

        Parameters
        ----------
        filepath: String
            The file name specifies a unique location in the system

        cellen_index: list
            The list where the time read values would be temporary stored

        tijd_index: list
             The list where the growth read values would be temporary stored

        Raises
        ----------
        FileNotFoundError
            When the file could not be found with the given path


        Returns
        -------
            List
                A list containing two lists, which are the time and the cells growth lists.

        """

        try:
            cellen_index, tijd_index = [], []
            with open(str(filepath)) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                next(csv_reader)  # This skips the first row of the CSV file.
                for row in csv_reader:
                    tijd_index.append(row[0])
                    cellen_index.append(row[1])
                tijd_lijst = [float(i) for i in tijd_index]
                cellen_lijst = [float(i) for i in cellen_index]
            return [tijd_lijst, cellen_lijst]

        except FileNotFoundError as e:
            print("Unexpected error ", e)

        except UnicodeDecodeError as e:
            print("Unexpected error ", e)

    def bereken_growth_rate(self) -> float:
        """
        Here the growth rate is calculated using the following equation:
                    μ = (ln N - Ln N0)/(t-t0)

        which is derived from this equation:
                    Ln N - Ln N0 = μ (t-t0)

        where:
            μ stands for the growth rate per h^-1
            N stands for the number of CFU / ml at time t
            N0 stands for the initial number of CFU / ml at time t0
            t stands for time

        Returns
        -------
            Float
                The grawth rate would be a float number

        """
        growth_rate = 0
        if self.lijst is not None:
            lijst_cellen, lijst_tijd =  self.lijst[1],  self.lijst[0]
            lnN, lnN0 = lijst_cellen[-1], lijst_cellen[0]
            t, t0 = lijst_tijd[-1], lijst_tijd[0]
            growth_rate = (lnN - lnN0)/(t - t0)

        return growth_rate

    def bereken_maxcellen(self) -> list:
        """
        Here is the max number of cells made, and the duration of the experiment in time are also calculated.
        Therefore, the start and end values N at t and N0 at t are used for this.

        Returns
        -------
        List
             A list containing two lists, which are the duration of the experiment over time
            and the max number of cells made in CFU / ml.

        """
        if self.lijst is not None:
            delta_tijd = max(self.lijst[0]) - min(self.lijst[0])
            delta_cellen = max(self.lijst[1]) - min(self.lijst[1])
            return [delta_tijd, delta_cellen]
