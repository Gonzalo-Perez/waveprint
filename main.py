# coding=utf-8
""" WavePrint
_______________________________________________________________________________
Copyright (c) 2020 WavePrint-Dev - WavePrint SPA
This software cannot be distributed.
For more information, visit waveprint.com
Current version developer: Waveprint Team
_______________________________________________________________________________
"""

import argparse
import matplotlib.pyplot as plt
import numpy as np
import csv

def reader_csv(input_file):
    """Gets a CSV reader for given directory and file.
    @param input_file: string file name to read
    """
    in_file = open(input_file, 'r')
    # TODO: Check options below are correct
    return csv.DictReader(
        in_file, delimiter=',', quotechar='"', skipinitialspace=True)


# def writer_csv(output_file, fieldnames):
#     """Gets a CSV writer for file.
#     @param output_file: string file name to write
#     @param fieldnames: list with string column names to write
#     """
#     out_file = open(output_file, 'wb')
#     return csv.DictWriter(
#         out_file, delimiter=',', fieldnames=fieldnames)

class WavePrint(object):

    def __init__(self, waves_per_day):
        """Constructor of DemandMonthlyPPA.
                @param waves: number of waves to plot per data point
                """
        self.waves_per_day = waves_per_day

    def __waveprint(self):

        # READ WAVE DATA AND DEFINE RANGES
        wave_data = list(reader_csv('data.csv'))

        waves = 0
        max_period = 0

        for wave in wave_data:
            waves += 1
            if int(wave['period']) > max_period:
                max_period = int(wave['period'])
        
        print('waves: ' + str(waves))
        print('max_period: ' + str(max_period))

        # SET X AND Y RANGES AND INITIALIZE MATRIX
        range_x = self.waves_per_day * max_period
        range_y = waves

        wave_matrix = np.zeros((range_y, range_x))
       
        # ITERATE THROUGH DATA
        i = 0
        for wave in wave_data:

            period = int(wave['period'])
            height = float(wave['height'])

            for j in range(0, self.waves_per_day, 1):
                wave_matrix[i , j * period] = height
            
            i += 1

        # PLOT
        plt.matshow(wave_matrix)
        plt.show()

    def run(self):
        """Main execution point."""
        self.__waveprint()

def main():
    """Main program."""
    parser = argparse.ArgumentParser(description='WavePrint')
    parser.add_argument(
        'waves_per_day', type=int, help='Waves per day')
    args = parser.parse_args()
    WavePrint(args.waves_per_day).run()

if __name__ == '__main__':
    main()