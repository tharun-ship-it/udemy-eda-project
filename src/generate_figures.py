"""
Generate sample visualizations for README screenshots.

Run this script to create the visualization figures shown in the README.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set random seed for reproducibility
np.random.seed(42)

# Create figures directory if it doesn't exist
os.makedirs('../figures', exist_ok=True)

# Configure plotting style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette('husl')
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 11
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12

COLORS = {
    'primary': '#5A4FCF',
    'secondary': '#FF6B6B',
    'accent': '#4ECDC4',
    'neutral': '#95A5A6'
}

print("Generating sample visualizations...")

# Generate synthetic data that resembles Udemy courses
n_samples = 3500

subjects = ['Web Development', 'Business Finance', 'Musical Instruments', 'Graphic Design']
levels = ['All Levels', 'Beginner Level', 'Intermediate Level', 'Expert Level']

# Create synthetic dataset
data = {
    'price': np.concatenate([
        np.zeros(300),  # Free courses
        np.random.choice([19.99, 24.99, 29.99, 49.99, 99.99, 149.99, 199.99], n_samples - 300)
    ]),
    'num_subscribers': np.random.lognormal(mean=7, sigma=2, size=n_samples).astype(int),
    'num_reviews': np.random.lognormal(mean=4, sigma=1.5, size=n_samples).astype(int),
    'num_lectures': np.random.lognormal(mean=3.5, sigma=0.8, size=n_samples).astype(int),
    'content_duration': np.random.lognormal(mean=2, sigma=0.7, size=n_samples),
    'subject': np.random.choice(subjects, n_samples, p=[0.4, 0.3, 0.15, 0.15]),
    'level': np.random.choice(levels, n_samples, p=[0.35, 0.30, 0.25, 0.10]),
    'year': np.random.choice(range(2012, 2021), n_samples, p=[0.02, 0.03, 0.05, 0.08, 0.12, 0.15, 0.18, 0.20, 0.17])
}

df = pd.DataFrame(data)

# 1. Correlation Matrix
print("  Creating correlation matrix...")
fig, ax = plt.subplots(figsize=(10, 8))
numeric_cols = ['price', 'num_subscribers', 'num_reviews', 'num_lectures', 'content_duration']
corr_matrix = df[numeric_cols].corr()
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

sns.heatmap(
    corr_matrix,
    mask=mask,
    annot=True,
    fmt='.2f',
    cmap='RdBu_r',
    center=0,
    square=True,
    linewidths=0.5,
    ax=ax,
    cbar_kws={'shrink': 0.8}
)
ax.set_title('Feature Correlation Matrix')
plt.tight_layout()
plt.savefig('../figures/correlation_matrix.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

# 2. Subject Distribution (Pie Chart)
print("  Creating subject distribution...")
fig, ax = plt.subplots(figsize=(10, 8))
subject_counts = df['subject'].value_counts()
colors = sns.color_palette('Set2', len(subject_counts))

wedges, texts, autotexts = ax.pie(
    subject_counts.values,
    labels=subject_counts.index,
    autopct='%1.1f%%',
    colors=colors,
    explode=[0.02] * len(subject_counts),
    shadow=True,
    textprops={'fontsize': 11}
)
ax.set_title('Course Distribution by Subject Category', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('../figures/subject_distribution.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

# 3. Subscribers Distribution (Log Scale)
print("  Creating subscribers distribution...")
fig, ax = plt.subplots(figsize=(12, 6))
subscribers_nonzero = df[df['num_subscribers'] > 0]['num_subscribers']

sns.histplot(np.log10(subscribers_nonzero), bins=50, kde=True, 
             color=COLORS['accent'], alpha=0.7, ax=ax)
ax.set_title('Distribution of Subscribers (log₁₀ scale)', fontsize=14, fontweight='bold')
ax.set_xlabel('log₁₀(Number of Subscribers)')
ax.set_ylabel('Frequency')

for val, label in [(2, '100'), (3, '1K'), (4, '10K'), (5, '100K')]:
    ax.axvline(val, color=COLORS['neutral'], linestyle=':', alpha=0.5)
    ax.text(val, ax.get_ylim()[1]*0.95, label, ha='center', fontsize=9)

plt.tight_layout()
plt.savefig('../figures/subscribers_distribution.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

# 4. Price vs Subscribers
print("  Creating price vs subscribers plot...")
fig, ax = plt.subplots(figsize=(12, 6))
paid_df = df[(df['price'] > 0) & (df['num_subscribers'] > 0)]

scatter = ax.scatter(
    paid_df['price'],
    paid_df['num_subscribers'],
    alpha=0.4,
    c=COLORS['primary'],
    s=20
)

ax.set_xlabel('Price ($)')
ax.set_ylabel('Number of Subscribers')
ax.set_title('Price vs Subscribers for Paid Courses', fontsize=14, fontweight='bold')
ax.set_yscale('log')

plt.tight_layout()
plt.savefig('../figures/price_vs_subscribers.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

# 5. Yearly Trend
print("  Creating yearly trend...")
fig, ax = plt.subplots(figsize=(14, 6))
yearly_counts = df.groupby('year').size()

bars = ax.bar(yearly_counts.index, yearly_counts.values, color=COLORS['primary'], alpha=0.8)
ax.plot(yearly_counts.index, yearly_counts.values, 'o-', color=COLORS['secondary'], linewidth=2, markersize=8)

ax.set_xlabel('Year')
ax.set_ylabel('Number of Courses Published')
ax.set_title('Course Publications Over Time', fontsize=14, fontweight='bold')

# Add growth annotations
for i in range(1, len(yearly_counts)):
    growth = (yearly_counts.iloc[i] - yearly_counts.iloc[i-1]) / yearly_counts.iloc[i-1] * 100
    if abs(growth) > 10:
        ax.annotate(f'{growth:+.0f}%', 
                   xy=(yearly_counts.index[i], yearly_counts.iloc[i]),
                   xytext=(0, 10), textcoords='offset points',
                   ha='center', fontsize=9, color=COLORS['secondary'], fontweight='bold')

plt.tight_layout()
plt.savefig('../figures/yearly_trend.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

# 6. Free vs Paid Distribution
print("  Creating free vs paid distribution...")
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

df['is_paid'] = df['price'].apply(lambda x: 'Paid' if x > 0 else 'Free')

sns.boxplot(data=df, x='is_paid', y='num_subscribers', ax=axes[0], palette='Set2')
axes[0].set_yscale('log')
axes[0].set_title('Subscriber Distribution: Free vs Paid', fontsize=12, fontweight='bold')
axes[0].set_xlabel('')
axes[0].set_ylabel('Subscribers (log scale)')

pricing_counts = df['is_paid'].value_counts()
axes[1].pie(pricing_counts.values, labels=pricing_counts.index, autopct='%1.1f%%',
            colors=[COLORS['accent'], COLORS['secondary']], explode=[0.02, 0.02], shadow=True)
axes[1].set_title('Course Distribution: Free vs Paid', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('../figures/free_vs_paid.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

# 7. Subject Trends Over Time
print("  Creating subject trends...")
fig, ax = plt.subplots(figsize=(14, 6))
subject_yearly = df.groupby(['year', 'subject']).size().unstack(fill_value=0)

subject_yearly.plot(kind='area', stacked=True, alpha=0.8, ax=ax)
ax.set_xlabel('Year')
ax.set_ylabel('Number of Courses')
ax.set_title('Subject Category Trends Over Time', fontsize=14, fontweight='bold')
ax.legend(title='Subject', bbox_to_anchor=(1.02, 1), loc='upper left')

plt.tight_layout()
plt.savefig('../figures/subject_trends.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

# 8. Level Distribution
print("  Creating level distribution...")
fig, ax = plt.subplots(figsize=(10, 6))
level_counts = df['level'].value_counts()
colors = sns.color_palette('husl', len(level_counts))

bars = ax.barh(level_counts.index, level_counts.values, color=colors)
ax.set_xlabel('Number of Courses')
ax.set_title('Course Distribution by Difficulty Level', fontsize=14, fontweight='bold')

for bar, val in zip(bars, level_counts.values):
    ax.text(val + 20, bar.get_y() + bar.get_height()/2, 
            f'{val:,}', va='center', fontsize=10)

ax.set_xlim(0, level_counts.max() * 1.15)
plt.tight_layout()
plt.savefig('../figures/level_distribution.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

# 9. Price Distribution
print("  Creating price distribution...")
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

paid_prices = df[df['price'] > 0]['price']
sns.histplot(paid_prices, bins=30, kde=True, ax=axes[0], color=COLORS['primary'], alpha=0.7)
axes[0].set_title('Distribution of Course Prices')
axes[0].set_xlabel('Price ($)')
axes[0].axvline(paid_prices.mean(), color=COLORS['secondary'], linestyle='--', 
                label=f'Mean: ${paid_prices.mean():.2f}')
axes[0].axvline(paid_prices.median(), color=COLORS['accent'], linestyle='-', 
                label=f'Median: ${paid_prices.median():.2f}')
axes[0].legend()

sns.boxplot(x=paid_prices, ax=axes[1], color=COLORS['primary'])
axes[1].set_title('Box Plot of Course Prices')
axes[1].set_xlabel('Price ($)')

plt.tight_layout()
plt.savefig('../figures/price_distribution.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

# 10. Create a banner image
print("  Creating banner...")
fig, ax = plt.subplots(figsize=(16, 4))

# Background gradient effect
x = np.linspace(0, 10, 100)
y = np.linspace(0, 4, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(X * 0.5) * np.cos(Y * 0.5) * 0.5

ax.contourf(X, Y, Z, levels=20, cmap='Blues', alpha=0.3)

# Add decorative circles
for cx, cy, r, c in [(1.5, 2, 0.6, COLORS['primary']), (8.5, 2, 0.6, COLORS['accent']),
                      (2.5, 3.2, 0.3, COLORS['secondary']), (7.5, 0.8, 0.3, COLORS['secondary'])]:
    circle = plt.Circle((cx, cy), r, color=c, alpha=0.3)
    ax.add_patch(circle)

# Add title text
ax.text(5, 2.2, 'Udemy Courses', fontsize=42, ha='center', va='center', 
        fontweight='bold', color='#2C3E50')
ax.text(5, 1.2, 'Exploratory Data Analysis', fontsize=24, ha='center', va='center',
        color='#5A4FCF', fontstyle='italic')

ax.set_xlim(0, 10)
ax.set_ylim(0, 4)
ax.axis('off')

plt.tight_layout()
plt.savefig('../figures/banner.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

print("\n✓ All visualizations generated successfully!")
print(f"  Figures saved to: ../figures/")
