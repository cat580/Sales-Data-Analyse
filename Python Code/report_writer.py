def write_report(output_file, analysis):
    """Write sales report to file"""
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            # Write summary
            file.write("Sales Analysis Report\n")
            file.write("===================\n\n")
            file.write(f"Total Sales: ${analysis['total_sales']:.2f}\n")
            file.write(f"Average Sale: ${analysis['average_sale']:.2f}\n")
            file.write(f"Number of Transactions: {analysis['num_transactions']}\n\n")

            # Write region breakdown
            file.write("Sales by Region\n")
            file.write("--------------\n")
            for region, amount in sorted(analysis['region_totals'].items()):
                file.write(f"{region}: ${amount:.2f}\n")
            file.write("\n")

            # Write category breakdown
            file.write("Sales by Category\n")
            file.write("----------------\n")
            for category, amount in sorted(analysis['category_totals'].items()):
                file.write(f"{category}: ${amount:.2f}\n")
            file.write("\n")

            # Write payment method breakdown
            file.write("Sales by Payment Method\n")
            file.write("----------------------\n")
            for method, amount in sorted(analysis['payment_totals'].items()):
                file.write(f"{method}: ${amount:.2f}\n")

    except Exception as e:
        raise Exception(f"Error writing report: {str(e)}")