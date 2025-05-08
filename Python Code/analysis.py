from collections import defaultdict

def analyze_sales_data(data):
    """Analyze sales data and return summary statistics"""
    try:
        # Initialize counters
        total_sales = 0
        regions = defaultdict(float)
        categories = defaultdict(float)
        payment_methods = defaultdict(float)
        
        # Process each row
        for row in data:
            try:
                # Convert amount to float, handling empty values
                amount = float(row['amount']) if row['amount'] else 0
                
                # Update totals
                total_sales += amount
                regions[row['region']] += amount
                categories[row['category']] += amount
                payment_methods[row['payment_method']] += amount
                
            except ValueError as e:
                print(f"Warning: Skipping invalid amount in row: {row}")
                continue

        # Calculate average sale
        avg_sale = total_sales / len(data) if data else 0

        return {
            'total_sales': total_sales,
            'average_sale': avg_sale,
            'region_totals': dict(regions),
            'category_totals': dict(categories),
            'payment_totals': dict(payment_methods),
            'num_transactions': len(data)
        }
        
    except Exception as e:
        raise Exception(f"Error analyzing data: {str(e)}")