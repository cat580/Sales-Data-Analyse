"""
Module for generating reports from product sales analysis.
No external dependencies required.
"""

def write_report(sorted_products, sorted_categories, total_revenue, insights, output_file):
    """
    Write product analysis report to file.
    
    Args:
        sorted_products (list): List of tuples (product_name, revenue) sorted by revenue
        sorted_categories (list): List of tuples (category_name, revenue) sorted by revenue
        total_revenue (float): Total revenue across all products
        insights (dict): Dictionary containing business insights
        output_file (str): Path to the output report file
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            # Write header
            file.write("Product Sales Analysis Report\n")
            file.write("===========================\n\n")
            
            # Write summary
            file.write(f"Total Revenue: ${total_revenue:.2f}\n")
            file.write(f"Number of Products: {len(sorted_products)}\n")
            file.write(f"Number of Categories: {len(sorted_categories)}\n\n")
            
            # Write product breakdown
            file.write("Products Ranked by Revenue\n")
            file.write("-----------------------\n")
            
            # Write each product with its revenue and percentage of total
            for i, (product, amount) in enumerate(sorted_products, 1):
                percentage = (amount / total_revenue) * 100
                file.write(f"{i}. {product}: ${amount:.2f} ({percentage:.1f}% of total revenue)\n")
            
            file.write("\n")
            
            # Write category breakdown
            file.write("Categories Ranked by Revenue\n")
            file.write("-------------------------\n")
            
            # Write each category with its revenue and percentage of total
            for i, (category, amount) in enumerate(sorted_categories, 1):
                percentage = (amount / total_revenue) * 100
                file.write(f"{i}. {category}: ${amount:.2f} ({percentage:.1f}% of total revenue)\n")
            
            file.write("\n")
            
            # Write business insights
            file.write("Business Insights\n")
            file.write("----------------\n")
            
            # Pareto principle insights
            file.write(f"Top {insights['pareto_count']} products generate {insights['pareto_percentage']:.1f}% of total revenue\n")
            
            # Top 3 products insights
            file.write(f"Top 3 products account for {insights['top_3_percentage']:.1f}% of total revenue\n\n")
            
            # Write recommendations
            file.write("Recommendations\n")
            file.write("--------------\n")
            file.write("1. Focus marketing efforts on top-performing products\n")
            file.write("2. Ensure adequate inventory for high-revenue products\n")
            file.write("3. Consider bundling lower-performing products with top sellers\n")
            file.write("4. Analyze why top products are successful and apply insights to other products\n")

    except Exception as e:
        print(f"Error writing report: {str(e)}")

def print_summary(sorted_products, total_revenue, count=5):
    """
    Print a summary of top products to the console.
    
    Args:
        sorted_products (list): List of tuples (product_name, revenue) sorted by revenue
        total_revenue (float): Total revenue across all products
        count (int): Number of top products to display
    """
    print(f"\nTop {count} Products by Revenue:")
    for i, (product, amount) in enumerate(sorted_products[:count], 1):
        percentage = (amount / total_revenue) * 100
        print(f"{i}. {product}: ${amount:.2f} ({percentage:.1f}%)")