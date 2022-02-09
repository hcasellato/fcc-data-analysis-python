import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
def d_par(x): return dt.datetime.strptime(x, '%Y-%m-%d')
df = pd.read_csv('data/fcc-forum-pageviews.csv', sep=',', index_col=['date'],
                 parse_dates=['date'], date_parser=d_par)

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) &
            (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(16, 6))
    ax = sns.lineplot(data=df, x='date', y='value', color='red')
    ax.set(title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019',
           xlabel='Date', ylabel='Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby([df.index.year, df.index.month])['value'].mean()
    df_bar = df_bar.unstack()

    # Draw bar plot
    fig = df_bar.plot.bar(legend=True, figsize=(14,7), ylabel='Average Page Views', xlabel='Years').figure
    plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    df_box['nm'] = df_box['date'].dt.month
    df_box = df_box.sort_values('nm')

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))
    ax[0] = sns.boxplot(data=df_box, x='year', y='value', ax=ax[0])
    ax[0].set_ylabel('Page Views')
    ax[0].set_xlabel('Year')
    ax[0].set_title('Year-wise Box Plot (Trend)')
    
    ax[1] = sns.boxplot(data=df_box, x='month', y='value', ax=ax[1])
    ax[1].set_ylabel('Page Views')
    ax[1].set_xlabel('Month')
    ax[1].set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

# Ran 11 tests in 11.832s