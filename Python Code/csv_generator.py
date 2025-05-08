import csv
import random
import datetime
import os
from tkinter import Tk, Label, Entry, Button, StringVar, OptionMenu, Frame, Scrollbar, Text, END, messagebox

class SalesDataGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Sales Data Generator")
        self.root.geometry("700x650")
        self.root.resizable(True, True)
        
        # Set up the form
        self.setup_form()
        
    def setup_form(self):
        # File name
        frame_file = Frame(self.root)
        frame_file.pack(fill="x", padx=10, pady=5)
        
        Label(frame_file, text="Output CSV File:").pack(side="left")
        self.filename = Entry(frame_file, width=30)
        self.filename.pack(side="left", padx=5)
        self.filename.insert(0, "custom_sales_data.csv")
        
        # Number of records
        frame_records = Frame(self.root)
        frame_records.pack(fill="x", padx=10, pady=5)
        
        Label(frame_records, text="Number of Records:").pack(side="left")
        self.num_records = Entry(frame_records, width=10)
        self.num_records.pack(side="left", padx=5)
        self.num_records.insert(0, "10")
        
        # Date range
        frame_dates = Frame(self.root)
        frame_dates.pack(fill="x", padx=10, pady=5)
        
        Label(frame_dates, text="Date Range (YYYY-MM-DD):").pack(side="left")
        self.start_date = Entry(frame_dates, width=12)
        self.start_date.pack(side="left", padx=5)
        self.start_date.insert(0, "2023-01-01")
        
        Label(frame_dates, text="to").pack(side="left")
        self.end_date = Entry(frame_dates, width=12)
        self.end_date.pack(side="left", padx=5)
        self.end_date.insert(0, "2023-12-31")
        
        # Products
        frame_products = Frame(self.root)
        frame_products.pack(fill="x", padx=10, pady=5)
        
        Label(frame_products, text="Products (one per line):").pack(anchor="w")
        
        # Create a frame for the text and scrollbar
        text_frame = Frame(frame_products)
        text_frame.pack(fill="both", expand=True, pady=5)
        
        # Add a scrollbar
        scrollbar = Scrollbar(text_frame)
        scrollbar.pack(side="right", fill="y")
        
        # Add the text widget
        self.products_text = Text(text_frame, height=5, width=50, yscrollcommand=scrollbar.set)
        self.products_text.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.products_text.yview)
        
        # Default products
        default_products = "Wireless Headphones,Electronics,125.99\nT-Shirt,Clothing,22.75\nFitness Tracker,Electronics,89.99\nCoffee Mug,Home Goods,12.99\nSmart Speaker,Electronics,199.99"
        self.products_text.insert(END, default_products)
        
        # Regions
        frame_regions = Frame(self.root)
        frame_regions.pack(fill="x", padx=10, pady=5)
        
        Label(frame_regions, text="Regions (comma separated):").pack(anchor="w")
        self.regions = Entry(frame_regions, width=50)
        self.regions.pack(fill="x", padx=5, pady=5)
        self.regions.insert(0, "North,South,East,West")
        
        # Payment methods
        frame_payments = Frame(self.root)
        frame_payments.pack(fill="x", padx=10, pady=5)
        
        Label(frame_payments, text="Payment Methods (comma separated):").pack(anchor="w")
        self.payment_methods = Entry(frame_payments, width=50)
        self.payment_methods.pack(fill="x", padx=5, pady=5)
        self.payment_methods.insert(0, "Credit Card,PayPal,Cash,Bank Transfer")
        
        # Generate button
        generate_btn = Button(self.root, text="Generate CSV", command=self.generate_csv, bg="#4CAF50", fg="white", padx=10, pady=5)
        generate_btn.pack(pady=20)
        
        # Status message
        self.status_var = StringVar()
        status_label = Label(self.root, textvariable=self.status_var, fg="blue")
        status_label.pack(pady=5)
        
    def generate_csv(self):
        try:
            # Get values from form
            filename = self.filename.get()
            if not filename.endswith('.csv'):
                filename += '.csv'
                
            num_records = int(self.num_records.get())
            start_date = datetime.datetime.strptime(self.start_date.get(), "%Y-%m-%d")
            end_date = datetime.datetime.strptime(self.end_date.get(), "%Y-%m-%d")
            
            # Parse products (format: name,category,price)
            products_text = self.products_text.get("1.0", END).strip()
            products = []
            for line in products_text.split('\n'):
                if line.strip():
                    parts = line.split(',')
                    if len(parts) >= 3:
                        products.append({
                            'name': parts[0].strip(),
                            'category': parts[1].strip(),
                            'price': float(parts[2].strip())
                        })
            
            if not products:
                messagebox.showerror("Error", "Please enter at least one product")
                return
                
            regions = [r.strip() for r in self.regions.get().split(',') if r.strip()]
            payment_methods = [p.strip() for p in self.payment_methods.get().split(',') if p.strip()]
            
            if not regions:
                messagebox.showerror("Error", "Please enter at least one region")
                return
                
            if not payment_methods:
                messagebox.showerror("Error", "Please enter at least one payment method")
                return
            
            # Generate the CSV file
            self.create_csv_file(filename, num_records, start_date, end_date, products, regions, payment_methods)
            
            self.status_var.set(f"CSV file '{filename}' generated successfully with {num_records} records!")
            
            # Ask if user wants to open the file
            if messagebox.askyesno("Success", f"CSV file '{filename}' generated successfully!\n\nWould you like to run the analysis on this file now?"):
                self.run_analysis(filename)
                
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.status_var.set(f"Error: {str(e)}")
    
    def create_csv_file(self, filename, num_records, start_date, end_date, products, regions, payment_methods):
        # Calculate date range in days
        date_range = (end_date - start_date).days
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['transaction_id', 'date', 'amount', 'quantity', 'unit_price', 
                         'customer', 'email', 'product', 'category', 'payment_method', 'region']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            
            for i in range(num_records):
                # Generate random data
                product = random.choice(products)
                quantity = random.randint(1, 5)
                unit_price = product['price']
                amount = quantity * unit_price
                
                # Random date within range
                random_days = random.randint(0, max(0, date_range))
                transaction_date = start_date + datetime.timedelta(days=random_days)
                date_str = transaction_date.strftime("%Y-%m-%d")
                
                # Generate a customer name
                first_names = ["John", "Jane", "Michael", "Emily", "David", "Sarah", "Robert", "Lisa", "James", "Jennifer"]
                last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Wilson", "Taylor", "Anderson"]
                customer_name = f"{random.choice(first_names)} {random.choice(last_names)}"
                
                # Generate email
                email = f"{customer_name.lower().replace(' ', '.')}@example.com"
                
                writer.writerow({
                    'transaction_id': f"TX{i+1:03d}",
                    'date': date_str,
                    'amount': f"{amount:.2f}",
                    'quantity': quantity,
                    'unit_price': f"{unit_price:.2f}",
                    'customer': customer_name,
                    'email': email,
                    'product': product['name'],
                    'category': product['category'],
                    'payment_method': random.choice(payment_methods),
                    'region': random.choice(regions)
                })
    
    def run_analysis(self, input_file):
        try:
            output_file = os.path.splitext(input_file)[0] + "_report.txt"
            
            # Run the analysis script
            import sys
            from main import main
            
            # Temporarily redirect sys.argv
            original_argv = sys.argv
            sys.argv = ["main.py", input_file, output_file]
            
            try:
                main()
                messagebox.showinfo("Analysis Complete", f"Analysis complete!\nReport saved to {output_file}")
            finally:
                # Restore original argv
                sys.argv = original_argv
                
        except Exception as e:
            messagebox.showerror("Error", f"Error running analysis: {str(e)}")

def main():
    root = Tk()
    app = SalesDataGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()