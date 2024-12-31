import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_explore_data(file_path='BitcoinHeistData.csv'):
    """Load and explore the Bitcoin Heist dataset"""
    try:
        df = pd.read_csv(file_path)
        print("Dataset shape:", df.shape)
        print("\nFirst 5 rows:")
        print(df.head())
        print("\nMissing values:")
        print(df.isnull().sum())
        
        # Plotting the income distribution
        sns.histplot(df['income'])
        plt.title('Income Distribution')
        plt.xlabel('Income (Satoshis)')
        plt.ylabel('Frequency')
        plt.savefig('histogram.png')
        plt.close()
        
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def perform_basic_analysis(df):
    """Perform basic statistical analysis"""
    try:
        # Numerical columns analysis
        numerical_cols = ['year', 'day', 'length', 'weight', 'count', 
                         'looped', 'neighbors', 'income']
        print("\nNumerical Statistics:")
        print(df[numerical_cols].describe())
        
        # Ransomware family distribution
        print("\nRansomware Family Distribution:")
        print(df['label'].value_counts())
        
        # Average income by ransomware family
        print("\nAverage Income by Ransomware Family:")
        print(df.groupby('label')['income'].mean().sort_values(ascending=False))
        
        return True
    except Exception as e:
        print(f"Error in analysis: {e}")
        return False

def create_visualizations(df):
    """Create visualizations for Bitcoin heist data"""
    try:
        plt.figure(figsize=(15, 10))
        
        # 1. Line chart: Time series of transactions by year
        plt.subplot(2, 2, 1)
        yearly_counts = df.groupby('year').size()
        plt.plot(yearly_counts.index, yearly_counts.values, marker='o')
        plt.title('Transactions by Year')
        plt.xlabel('Year')
        plt.ylabel('Number of Transactions')
        
        # 2. Bar chart: Average income by label
        plt.subplot(2, 2, 2)
        avg_income = df.groupby('label')['income'].mean().sort_values(ascending=True)
        avg_income.plot(kind='barh')
        plt.title('Average Income by Ransomware Family')
        plt.xlabel('Average Income (Satoshis)')
        
        # 3. Histogram: Distribution of transaction weights
        plt.subplot(2, 2, 3)
        sns.histplot(data=df, x='weight', bins=50, log_scale=True)
        plt.title('Distribution of Transaction Weights')
        plt.xlabel('Weight (log scale)')
        
        # 4. Scatter plot: Neighbors vs income
        plt.subplot(2, 2, 4)
        plt.scatter(df['neighbors'], df['income'], alpha=0.5)
        plt.title('Neighbors vs Income')
        plt.xlabel('Number of Neighbors')
        plt.ylabel('Income (Satoshis)')
        plt.yscale('log')
        
        plt.tight_layout()
        plt.savefig('visualizations1.png')
        plt.close()
        
        # Additional visualization: Network characteristics
        plt.figure(figsize=(12, 5))
        
        plt.subplot(1, 2, 1)
        sns.boxplot(x='label', y='length', data=df)
        plt.xticks(rotation=45)
        plt.title('Transaction Chain Length by Label')
        
        plt.subplot(1, 2, 2)
        sns.boxplot(x='label', y='neighbors', data=df)
        plt.xticks(rotation=45)
        plt.title('Number of Neighbors by Label')
        
        plt.tight_layout()
        plt.savefig('visualizations2.png')
        plt.close()
        
        return True
    except Exception as e:
        print(f"Error in visualization: {e}")
        return False

def main():
    """Main function to run the analysis"""
    df = load_and_explore_data()
    if df is not None:
        perform_basic_analysis(df)
        create_visualizations(df)

if __name__ == "__main__":
    main()