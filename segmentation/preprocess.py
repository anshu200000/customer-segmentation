import pandas as pd

def create_rfm(df):
    # Parse InvoiceDate robustly, supporting day-first and mixed formats
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], dayfirst=True, errors='coerce', infer_datetime_format=True)
    # Ensure Amount column exists
    if 'Amount' not in df.columns:
        df['Amount'] = df['Quantity'] * df['UnitPrice']
    
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    ref_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)
    
    rfm = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (ref_date - x.max()).days,
        'CustomerID': 'count',
        'Amount': 'sum'
    }).rename(columns={
        'InvoiceDate': 'Recency',
        'CustomerID': 'Frequency',
        'Amount': 'Monetary'
    })
    return rfm