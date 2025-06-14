import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_cancellation_trends(df, output_path):
    """Plot cancellation trends by hotel type."""
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='hotel', hue='is_canceled')
    plt.title('Cancellation Trends by Hotel Type')
    plt.xlabel('Hotel Type')
    plt.ylabel('Count')
    plt.legend(title='Canceled', labels=['No', 'Yes'])
    os.makedirs(output_path, exist_ok=True)
    plt.savefig(os.path.join(output_path, 'cancellation_by_hotel.png'))
    plt.close()

def plot_lead_time_analysis(df, output_path):
    """Plot lead time vs cancellation."""
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='is_canceled', y='lead_time')
    plt.title('Lead Time vs Cancellation')
    plt.xlabel('Canceled')
    plt.ylabel('Lead Time')
    os.makedirs(output_path, exist_ok=True)
    plt.savefig(os.path.join(output_path, 'lead_time_vs_cancellation.png'))
    plt.close()

def plot_correlation_matrix(df, output_path):
    """Plot correlation matrix."""
    plt.figure(figsize=(12, 8))
    corr = df.corr()
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm')
    plt.title('Correlation Matrix')
    os.makedirs(output_path, exist_ok=True)
    plt.savefig(os.path.join(output_path, 'correlation_matrix.png'))
    plt.close()