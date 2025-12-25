"""
Utility functions for Udemy EDA project.

This module contains helper functions for data processing, 
visualization, and statistical analysis.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Union, List, Dict, Optional, Tuple


def load_data(filepath: str) -> pd.DataFrame:
    """
    Load and perform initial preprocessing on the dataset.
    
    Parameters
    ----------
    filepath : str
        Path to the CSV file.
        
    Returns
    -------
    pd.DataFrame
        Loaded and preprocessed dataframe.
    """
    df = pd.read_csv(filepath)
    
    # Convert timestamp
    if 'published_timestamp' in df.columns:
        df['published_timestamp'] = pd.to_datetime(df['published_timestamp'])
    
    return df


def analyze_missing_values(df: pd.DataFrame) -> Union[pd.DataFrame, str]:
    """
    Generate a comprehensive missing value report.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe.
        
    Returns
    -------
    Union[pd.DataFrame, str]
        DataFrame with missing value statistics or message if no missing values.
    """
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100
    
    report = pd.DataFrame({
        'Missing Count': missing,
        'Missing %': missing_pct,
        'Data Type': df.dtypes
    })
    
    report = report[report['Missing Count'] > 0].sort_values(
        'Missing %', ascending=False
    )
    
    return report if len(report) > 0 else "No missing values detected."


def detect_outliers_iqr(
    series: pd.Series, 
    multiplier: float = 1.5
) -> Dict[str, Union[int, float]]:
    """
    Detect outliers using the Interquartile Range (IQR) method.
    
    Parameters
    ----------
    series : pd.Series
        Numerical series to analyze.
    multiplier : float, optional
        IQR multiplier for bounds calculation. Default is 1.5.
        
    Returns
    -------
    dict
        Dictionary containing outlier count, percentage, and bounds.
    """
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - multiplier * IQR
    upper_bound = Q3 + multiplier * IQR
    
    outliers = (series < lower_bound) | (series > upper_bound)
    
    return {
        'count': outliers.sum(),
        'percentage': (outliers.sum() / len(series)) * 100,
        'lower_bound': lower_bound,
        'upper_bound': upper_bound
    }


def create_distribution_plot(
    df: pd.DataFrame,
    column: str,
    figsize: Tuple[int, int] = (10, 6),
    color: str = 'steelblue',
    title: Optional[str] = None,
    save_path: Optional[str] = None
) -> plt.Figure:
    """
    Create a distribution plot with mean and median markers.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe.
    column : str
        Column name to plot.
    figsize : tuple, optional
        Figure size. Default is (10, 6).
    color : str, optional
        Plot color. Default is 'steelblue'.
    title : str, optional
        Plot title. If None, uses column name.
    save_path : str, optional
        Path to save the figure.
        
    Returns
    -------
    plt.Figure
        Matplotlib figure object.
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    sns.histplot(data=df, x=column, kde=True, ax=ax, color=color, alpha=0.7)
    
    mean_val = df[column].mean()
    median_val = df[column].median()
    
    ax.axvline(mean_val, color='red', linestyle='--', linewidth=2, 
               label=f'Mean: {mean_val:,.2f}')
    ax.axvline(median_val, color='green', linestyle='-.', linewidth=2, 
               label=f'Median: {median_val:,.2f}')
    
    ax.set_title(title or f'Distribution of {column}', fontweight='bold')
    ax.legend()
    
    plt.tight_layout()
    
    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches='tight')
    
    return fig


def calculate_summary_stats(df: pd.DataFrame, numerical_cols: List[str]) -> pd.DataFrame:
    """
    Calculate comprehensive summary statistics for numerical columns.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe.
    numerical_cols : list
        List of numerical column names.
        
    Returns
    -------
    pd.DataFrame
        Summary statistics dataframe.
    """
    stats = df[numerical_cols].describe().T
    
    # Add additional statistics
    stats['skew'] = df[numerical_cols].skew()
    stats['kurtosis'] = df[numerical_cols].kurtosis()
    stats['missing'] = df[numerical_cols].isnull().sum()
    stats['missing_pct'] = (stats['missing'] / len(df)) * 100
    
    return stats


def create_correlation_heatmap(
    df: pd.DataFrame,
    columns: List[str],
    figsize: Tuple[int, int] = (10, 8),
    save_path: Optional[str] = None
) -> plt.Figure:
    """
    Create a correlation heatmap for specified columns.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe.
    columns : list
        List of column names for correlation analysis.
    figsize : tuple, optional
        Figure size. Default is (10, 8).
    save_path : str, optional
        Path to save the figure.
        
    Returns
    -------
    plt.Figure
        Matplotlib figure object.
    """
    correlation_matrix = df[columns].corr()
    mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
    
    fig, ax = plt.subplots(figsize=figsize)
    
    sns.heatmap(
        correlation_matrix,
        mask=mask,
        annot=True,
        fmt='.3f',
        cmap='RdBu_r',
        center=0,
        square=True,
        linewidths=2,
        cbar_kws={'shrink': 0.8, 'label': 'Correlation Coefficient'},
        ax=ax
    )
    
    ax.set_title('Correlation Matrix', fontweight='bold', pad=20)
    plt.tight_layout()
    
    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches='tight')
    
    return fig


def extract_temporal_features(df: pd.DataFrame, timestamp_col: str) -> pd.DataFrame:
    """
    Extract temporal features from a timestamp column.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe.
    timestamp_col : str
        Name of the timestamp column.
        
    Returns
    -------
    pd.DataFrame
        Dataframe with added temporal features.
    """
    df = df.copy()
    
    df[timestamp_col] = pd.to_datetime(df[timestamp_col])
    df['year'] = df[timestamp_col].dt.year
    df['month'] = df[timestamp_col].dt.month
    df['day_of_week'] = df[timestamp_col].dt.dayofweek
    df['quarter'] = df[timestamp_col].dt.quarter
    df['day_of_year'] = df[timestamp_col].dt.dayofyear
    df['week_of_year'] = df[timestamp_col].dt.isocalendar().week
    
    return df


def format_large_number(num: Union[int, float]) -> str:
    """
    Format large numbers for display (e.g., 1000000 -> '1.0M').
    
    Parameters
    ----------
    num : int or float
        Number to format.
        
    Returns
    -------
    str
        Formatted string representation.
    """
    if abs(num) >= 1e9:
        return f'{num/1e9:.1f}B'
    elif abs(num) >= 1e6:
        return f'{num/1e6:.1f}M'
    elif abs(num) >= 1e3:
        return f'{num/1e3:.1f}K'
    else:
        return str(num)


if __name__ == '__main__':
    # Run basic tests
    print("Utils module loaded successfully.")
    print(f"Available functions: {[name for name in dir() if not name.startswith('_')]}")
