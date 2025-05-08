import sys
import os
from data_reader import read_data
from analysis import analyze_sales_data
from report_writer import write_report

def main():
    try:
        # Check command line arguments
        if len(sys.argv) != 3:
            print("Usage: python main.py <input_file> <output_file>")
            sys.exit(1)

        input_file = sys.argv[1]
        output_file = sys.argv[2]

        # Verify input file exists
        if not os.path.exists(input_file):
            print(f"Error: Input file '{input_file}' not found.")
            sys.exit(1)

        # Read and process data
        print(f"Reading data from {input_file}...")
        data = read_data(input_file)
        
        if not data:
            print("No data found in input file.")
            sys.exit(1)

        # Print first row and data summary for debugging
        print(f"\nTotal rows read: {len(data)}")
        print("First row of data:", data[0])

        # Analyze data
        print("\nAnalyzing data...")
        analysis = analyze_sales_data(data)

        # Write report
        print(f"\nWriting report to {output_file}...")
        write_report(output_file, analysis)

        print(f"Report successfully generated: {output_file}")

    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()