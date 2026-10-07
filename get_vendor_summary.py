import sqlite3
import pandas as pd
import numpy as np
import logging

from ingestion_db import ingest_db

# Configure Logging
logging.basicConfig(
    filename="logs/get_vendor_summary.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)


def create_vendor_summary(conn):
    """
    Merge multiple tables and create vendor sales summary.
    """

    vendor_sales_summary = pd.read_sql_query("""
    WITH FreightSummary AS (
        SELECT
            VendorNumber,
            SUM(Freight) AS FreightCost
        FROM vendor_invoice
        GROUP BY VendorNumber
    ),

    PurchaseSummary AS (
        SELECT
            p.VendorNumber,
            p.VendorName,
            p.Brand,
            p.Description,
            p.PurchasePrice,
            pp.Price AS ActualPrice,
            pp.Volume,
            SUM(p.Quantity) AS TotalPurchaseQuantity,
            SUM(p.Dollars) AS TotalPurchaseDollars
        FROM purchases p
        JOIN purchase_prices pp
            ON p.Brand = pp.Brand
        WHERE p.PurchasePrice > 0
        GROUP BY
            p.VendorNumber,
            p.VendorName,
            p.Brand,
            p.Description,
            p.PurchasePrice,
            pp.Price,
            pp.Volume
    ),

    SalesSummary AS (
        SELECT
            VendorNo,
            Brand,
            SUM(SalesQuantity) AS TotalSalesQuantity,
            SUM(SalesDollars) AS TotalSalesDollars,
            SUM(SalesPrice) AS TotalSalesPrice,
            SUM(ExciseTax) AS TotalExciseTax
        FROM sales
        GROUP BY VendorNo, Brand
    )

    SELECT
        ps.VendorNumber,
        ps.VendorName,
        ps.Brand,
        ps.Description,
        ps.PurchasePrice,
        ps.ActualPrice,
        ps.Volume,
        ps.TotalPurchaseQuantity,
        ps.TotalPurchaseDollars,
        ss.TotalSalesQuantity,
        ss.TotalSalesDollars,
        ss.TotalSalesPrice,
        ss.TotalExciseTax,
        fs.FreightCost
    FROM PurchaseSummary ps
    LEFT JOIN SalesSummary ss
        ON ps.VendorNumber = ss.VendorNo
        AND ps.Brand = ss.Brand
    LEFT JOIN FreightSummary fs
        ON ps.VendorNumber = fs.VendorNumber
    ORDER BY ps.TotalPurchaseDollars DESC
    """, conn)

    return vendor_sales_summary


def clean_data(df):
    """
    Clean data and create KPI columns.
    """

    # Convert Volume to float
    df["Volume"] = df["Volume"].astype(float)

    # Fill missing values
    df.fillna(0, inplace=True)

    # Remove extra spaces
    df["VendorName"] = df["VendorName"].astype(str).str.strip()
    df["Description"] = df["Description"].astype(str).str.strip()

    # Gross Profit
    df["GrossProfit"] = (
        df["TotalSalesDollars"] -
        df["TotalPurchaseDollars"]
    )

    # Profit Margin
    df["ProfitMargin"] = np.where(
        df["TotalSalesDollars"] == 0,
        0,
        (df["GrossProfit"] / df["TotalSalesDollars"]) * 100
    )

    # Stock Turnover
    df["StockTurnover"] = np.where(
        df["TotalPurchaseQuantity"] == 0,
        0,
        df["TotalSalesQuantity"] /
        df["TotalPurchaseQuantity"]
    )

    # Sales to Purchase Ratio
    df["SalesToPurchaseRatio"] = np.where(
        df["TotalPurchaseDollars"] == 0,
        0,
        df["TotalSalesDollars"] /
        df["TotalPurchaseDollars"]
    )

    return df


if __name__ == "__main__":

    # Create database connection
    conn = sqlite3.connect("inventory.db")

    logging.info("Creating Vendor Summary Table...")

    summary_df = create_vendor_summary(conn)

    logging.info(
        f"Summary Data Shape: {summary_df.shape}"
    )

    logging.info("Cleaning Data...")

    clean_df = clean_data(summary_df)

    logging.info(
        f"Clean Data Shape: {clean_df.shape}"
    )

    logging.info("Ingesting Data...")

    ingest_db(
        clean_df,
        "vendor_sales_summary",
        conn
    )

    logging.info("Process Completed Successfully")

    print("Vendor Summary Table Created Successfully!")

    conn.close()

















































# import sqlite3
# import pandas as pd
# import logging
# from ingestion_db 
# import ingest_db

# logging.basicConfig(
#     filename="logs/get_vendor_summary.log",
#     level = logging.DEBUG,
#     formats = "%(asctime)s - %(levelname)s - %(message)s",
#     filemode="a"
# )

# def create_vendor_summary(conn):
#     ''' this function will merge the different tables to get the overall vendor summary and adding new columns in the resultant data '''
#     vendor_sales_summary = pd.read_sql_query(""" WITH FreightSummary AS (
#     SELECT 
#         VendorNumber,
#         SUM(Freight) AS FreightCost
#     FROM vendor_invoice
#     GROUP BY VendorNumber
#     ),
#     PurchaseSummary AS (
#     SELECT 
#         p.VendorNumber,
#         p.VendorName,
#         p.Brand,
#         p.Description,
#         p.PurchasePrice,
#         pp.Price AS ActualPrice,
#         pp.volume,
#         SUM(p.Quantity) AS TotalPurchaseQuantity,
#         SUM(p.Dollars) AS TotalPurchaseDollars
#     FROM purchases p
#     JOIN purchase_prices pp
#          ON p.Brand = pp.Brand
#     WHERE p.PurchasePrice > 0 
#     GROUP BY p.VendorNumber , p.VendorName, p.Brand ,p.Description , p.PurchasePrice , pp.Price , pp.Volume
#     ),

#     SalesSummary AS (
#          SELECT 
#               VendorNo,
#               Brand,
#               SUM(SalesQuantity) AS TotalSalesQuantity,
#               SUM(SalesDollars) AS TotalSalesDollars,
#               SUM(SalesPrice) AS TotalSalesPrice,
#               SUM(ExciseTax) AS TotalExciseTax
#         FROM sales
#         GROUP BY VendorNo , Brand
#         )

#         SELECT 
#            ps.VendorNumber,
#            ps.vendorName,
#            ps.Brand,
#            ps.Description,
#            ps.PurchasePrice,
#            ps.ActualPrice,
#            ps.Volume,
#            ps.TotalPurchaseQuantity,
#            ps.TotalPurchaseDollars,
#            ss.TotalSalesQuantity,
#            ss.TotalSalesDollars,
#            ss.TotalSalesPrice,
#            ss.TotalExciseTax,
#            fs.FreightCost
#            FROM PurchaseSummary ps
#            LEFT JOIN SalesSummary ss
#            ON ps.VendorNumber = ss.VendorNo
#            AND ps.Brand = ss.Brand
#            LEFT  JOIN FreightSummary fs
#            ON ps.VendorNumber = fs.VendorNumber
#            ORDER BY ps.TotalPurchaseDollars DESC""",conn)
#     return vendor_sales_summary

#     def clean_data(df):
#         ''' This function will clean the data'''
#         # changing datatype to float 
#         df['Volume'] = df['Volume'].astype['float']
#         # filling missing value with # 
#         df.fillna(0,inplace = true)

#         # removing space from categorical columns 
#         df['VendorName'] = df['VendorName'].str.strip()
#         df['Desciption'] = df['Description'].str.strip()

#         # creating new columns for better analysis
#         vendor_sales_summary['GrossProfit'] = vendor_sales_summary['TotalSalesDollars'] - vendor_sales_summary['TotalPurchaseDollars']
#         vendor_sales_summary['ProfitMargin'] = vendor_sales_summary['GrossProfit'] / vendor_sales_summary['TotalSalesDollars'])*100
#         vendor_sales_summary['StockTurnover'] = vendor_sales_summary['TotalSalesQuantity'] /vendor_sales_summary['TotalPurchaseQuantity']
#         vendor_sales_summary['SalesToPurchaseRation'] = vendor_sales_summary['TotalSalesDollars'] / vendor_sales_summary['TotalPurchaseDollars']

#         return df

# if __name__ == '__main__':
#     # creating datadase connection 
#     conn = sqlite3.connect('inventory.db')

#     logging.info('Creating Vendor Summary Table.....')
#     summary_df = create_vendor_summary(conn)
#     logging.info(summary_df.head())

#     logging.info('Cleaning Data.....')
#     clean_df = clean_data(summary_df)
#     logging.info(clean_df.head())

#     logging.info('Ingesting data.....')
#     ingest_db(clean_df,'vendor_sales_summary',conn)
#     logging.info('Completed')
           
    