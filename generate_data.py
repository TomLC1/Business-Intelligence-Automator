import pandas as pd
import numpy as np
import os

def generate_big_data(num_rows=1000):
    if not os.path.exists('input'):
        os.makedirs('input')
    
    products = {
        'Laptop Pro': 1200, 'Wireless Mouse': 25, 'Monitor 4K': 350,
        'Mechanical Keyboard': 80, 'USB-C Hub': 45, 'Webcam HD': 60
    }
    
    locations = ['Lisbon', 'Porto', 'Braga']
    
    for loc in locations:
        data = {
            'Date': pd.date_range(start='2024-01-01', periods=num_rows, freq='h'),
            'Product': np.random.choice(list(products.keys()), num_rows),
            'Quantity': np.random.randint(1, 10, num_rows),
            'Customer_ID': [f"CUST-{i}" for i in np.random.randint(1000, 2000, num_rows)]
        }
        
        df = pd.DataFrame(data)
        
        # Map prices and add some "noise"
        df['Price_Unit'] = df['Product'].map(products)
        
        # Adding some NaN values to 5% of the Price column
        df.loc[df.sample(frac=0.05).index, 'Price_Unit'] = np.nan
        
        # Calculate Total
        df['Total_Value'] = df['Quantity'] * df['Price_Unit']
        
        filename = f"input/invoice_{loc.lower()}.xlsx"
        df.to_excel(filename, index=False)
        print(f"✅ Generated {filename} with {num_rows} rows.")

if __name__ == "__main__":
    generate_big_data(2000) # (Generates 6000 rows total)