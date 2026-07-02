#Austin Lineberry
#Code appended for use in Bellevue Course CSD325
#All changes documented (Requirement G)
#7/1/2026

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'

def readData(columnIndex):
    #Reads the dates and desired temperature column (high or low) from the CSV provided.
    dates, temps = [], []
    with open(filename) as f:
        reader = csv.reader(f)
        #Skip header row
        next(reader)
        for row in reader:
            try:
                currentDate = datetime.strptime(row[2], '%Y-%m-%d')
                temp = int(row[columnIndex])
            except ValueError:
                #Skips rows with invalid data
                print(f"Error reading data from {row[2]}")
                continue
            dates.append(currentDate)
            temps.append(temp)
        return(dates, temps)

def plotTemps(dates, temps, color, label):
    #Plot the requested temps over the provided dates
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)

    # Format Plot
    plt.title(f"Daily {label} temps - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

def showHighs():
    #Show High temps recorded over provided dates
    dates, highs = readData(column_index=5)
    plotTemps(dates, highs, color='red', label='high')

def showLows():
    # Show Low temps recorded over provided dates (Requirement C)
    dates, lows = readData(column_index=6)
    plotTemps(dates, lows, color='blue', label='low')


def printInstructions():
    #Print initial usage instructions (Requirement A)
    print("\nWelcome to the Sitka 2018 Weather Viewer!")
    print("Choose an option from the menu below:")
    print("  highs - View a graph of daily high temperatures")
    print("  lows  - View a graph of daily low temperatures")
    print("  exit  - Quit the program")


def main():
    printInstructions()
    while True:
        #Takes input to decide highs, lows, or exit (Requirement B)
        #Loops until exit is requested (Requirement D)
        choice = input("\nEnter your choice (highs/lows/exit): ").strip().lower()
        if choice == 'highs':
            showHighs()
        elif choice == 'lows':
            showLows()
        elif choice == 'exit':
            #Prints exit message when exit is selected (Requirement E)
            print("Thanks for checking out the Sitka weather data. Goodbye!")
            #Uses 'sys' as recommended to aid in quitting (Requirement F)
            sys.exit()
        else:
            print("Sorry, I didn't recognize that option. Please try again.")


if __name__ == '__main__':
    main()
