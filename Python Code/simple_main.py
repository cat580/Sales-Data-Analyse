"""
Main module for simple product sales analysis application.
No external dependencies required.
"""
import sys
import os
from simple_data_reader import read_data
from simple_analyzer import analyze_products, generate_insights
from simple_report_writer import write_report, print_summary

def main():
    """Main function to run the product sales analysis."""
    # Check command line arguments
    if len(sys.argv) != 3:
        print("Usage: python simple_main.py <input_file> <output_file>")
        print("Example: python simple_main.py sales_data.csv sales_report.txt")
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

    print(f"\nTotal rows read: {len(data)}")
    
    # Analyze products
    print("\nAnalyzing product performance...")
    sorted_products, sorted_categories, total_revenue = analyze_products(data)
    
    # Generate business insights
    insights = generate_insights(sorted_products, total_revenue)
    
    # Write report
    print(f"\nWriting report to {output_file}...")
    write_report(sorted_products, sorted_categories, total_revenue, insights, output_file)
    
    # Print summary to console
    print_summary(sorted_products, total_revenue)
    
    print("\nAnalysis complete!")
    print(f"Report generated: {output_file}")

if __name__ == "__main__":
    main()