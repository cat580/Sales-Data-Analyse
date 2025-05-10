"""
Module for analyzing product sales data.
No external dependencies required.
"""
from collections import defaultdict

def analyze_products(data):
    """
    Analyze product sales data.
    
    Args:
        data (list): List of dictionaries containing sales data
        
    Returns:
        tuple: (sorted_products, sorted_categories, total_revenue)
            - sorted_products: List of tuples (product_name, revenue) sorted by revenue
            - sorted_categories: List of tuples (category_name, revenue) sorted by revenue
            - total_revenue: Total revenue across all products
    """
    # Initialize product and category sales dictionaries
    product_sales = defaultdict(float)
    category_sales = defaultdict(float)
    
    # Process each row
    for row in data:
        try:
            # Convert amount to float, handling empty values
            amount = float(row['amount']) if row['amount'] else 0
            
            # Update product and category totals
            product_sales[row['product_name']] += amount
            category_sales[row['category']] += amount
            
        except ValueError:
            print(f"Warning: Skipping invalid amount in row: {row}")
            continue
        except KeyError as e:
            print(f"Warning: Missing required field {e} in row: {row}")
            continue

    # Calculate total revenue
    total_revenue = sum(product_sales.values())
    
    # Sort products by sales amount
    sorted_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)
    
    # Sort categories by sales amount
    sorted_categories = sorted(category_sales.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_products, sorted_categories, total_revenue

def generate_insights(sorted_products, total_revenue):
    """
    Generate business insights from product data.
    
    Args:
        sorted_products (list): List of tuples (product_name, revenue) sorted by revenue
        total_revenue (float): Total revenue across all products
        
    Returns:
        dict: Dictionary containing business insights
    """
    insights = {}
    
    # Calculate how many products make up 80% of revenue (Pareto principle)
    cumulative_percentage = 0
    products_for_80_percent = 0
    
    for product, amount in sorted_products:
        percentage = (amount / total_revenue) * 100
        cumulative_percentage += percentage
        products_for_80_percent += 1
        
        if cumulative_percentage >= 80:
            break
    
    insights['pareto_count'] = products_for_80_percent
    insights['pareto_percentage'] = cumulative_percentage
    
    # Top 3 products insights
    top_3 = sorted_products[:3] if len(sorted_products) >= 3 else sorted_products
    top_3_revenue = sum(amount for _, amount in top_3)
    top_3_percentage = (top_3_revenue / total_revenue) * 100
    
    insights['top_3'] = top_3
    insights['top_3_revenue'] = top_3_revenue
    insights['top_3_percentage'] = top_3_percentage
    
    return insights