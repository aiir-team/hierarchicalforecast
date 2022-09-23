# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/utils.ipynb.

# %% auto 0
__all__ = ['aggregate', 'HierarchicalPlot']

# %% ../nbs/utils.ipynb 2
from itertools import chain
from typing import Callable, Dict, List, Optional

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from matplotlib import rcParams
from mycolorpy import colorlist as mcp

plt.rcParams['font.family'] = 'serif'

# %% ../nbs/utils.ipynb 4
def _to_summing_matrix(S_df: pd.DataFrame):
    """Transforms the DataFrame `df` of hierarchies to a summing matrix S."""
    categories = [S_df[col].unique() for col in S_df.columns]
    cat_sizes = [len(cats) for cats in categories]
    idx_bottom = np.argmax(cat_sizes)
    cats_bottom = categories[idx_bottom]
    encoder = OneHotEncoder(categories=categories, sparse=False, dtype=np.float32)
    S = encoder.fit_transform(S_df).T
    S = pd.DataFrame(S, index=chain(*categories), columns=cats_bottom)
    tags = dict(zip(S_df.columns, categories))
    return S, tags

# %% ../nbs/utils.ipynb 5
def aggregate(
        df: pd.DataFrame, # DataFrame with columns `['ds', 'y']` and columns to aggregate
        spec: List[List[str]], # List of levels. Each element of the list contains a list of columns of `df` to aggregate.
        agg_fn: Callable = np.sum# Function used to aggregate `'y'`.
    ):
    """Aggregates `df` according to `spec` using `agg_fn`."""
    max_len_idx = np.argmax([len(hier) for hier in spec])
    bottom_comb = spec[max_len_idx]
    orig_cols = df.drop(labels=['ds', 'y'], axis=1).columns.to_list()
    df_hiers = []
    for hier in spec:
        df_hier = df.groupby(hier + ['ds'])['y'].apply(agg_fn).reset_index()
        df_hier['unique_id'] = df_hier[hier].agg('/'.join, axis=1)
        if hier == bottom_comb:
            bottom_hier = df_hier['unique_id'].unique()
        df_hiers.append(df_hier)
    df_hiers = pd.concat(df_hiers)
    S_df = df_hiers[['unique_id'] + bottom_comb].drop_duplicates().reset_index(drop=True)
    S_df = S_df.set_index('unique_id')
    S_df = S_df.fillna('agg')
    hiers_cols = []
    for hier in spec:
        hier_col = '/'.join(hier) 
        S_df[hier_col] = S_df[hier].agg('/'.join, axis=1)
        hiers_cols.append(hier_col)
    y_df = df_hiers[['unique_id', 'ds', 'y']].set_index('unique_id')
    #S definition
    S, tags = _to_summing_matrix(S_df.loc[bottom_hier, hiers_cols])
    return y_df, S, tags

# %% ../nbs/utils.ipynb 9
class HierarchicalPlot:
    
    def __init__(
        self,
        S: pd.DataFrame,    #  Summing matrix of size `(base, bottom)`.
        tags: Dict[str, np.ndarray], # Each key is a level and its value contains tags associated to that level.
    ):
        self.S = S
        self.tags = tags
        
    def plot_summing_matrix(self):
        plt.figure(num=1, figsize=(4, 6), dpi=80, facecolor='w')
        plt.spy(self.S)
        plt.show()
        plt.close()
        
    def plot_series(
            self, 
            series: str, # Time series to plot
            Y_df: Optional[pd.DataFrame] = None, # Dataframe with columns `ds` and models to plot indexed by `unique_id`.
            models: Optional[List[str]] = None, # Models to plot. 
            level: Optional[List[int]] = None # Levels for probabilistic intervals
        ):
        if series not in self.S.index:
            raise Exception(f'time series {series} not found')
        fig, ax = plt.subplots(1, 1, figsize = (20, 7))
        df_plot = Y_df.loc[series].set_index('ds')
        cols = models if models is not None else df_plot.columns
        cols_wo_levels = [col for col in cols if ('lo' not in col and 'hi' not in col)]
        cmap = mcp.gen_color('tab10', 10)[:len(cols_wo_levels)]
        cmap_dict = dict(zip(cols_wo_levels, cmap))
        df_plot[cols_wo_levels].plot(ax=ax, linewidth=2, color=cmap)
        if level is not None:
            for lv in level:
                for col in cols_wo_levels:
                    if col == 'y':
                        # we dont need intervals
                        # for the actual value
                        continue
                    if f'{col}-lo-{lv}' not in df_plot.columns:
                        # if model
                        # doesnt have levels
                        continue
                    ax.fill_between(
                        df_plot.index, 
                        df_plot[f'{col}-lo-{lv}'], 
                        df_plot[f'{col}-hi-{lv}'],
                        alpha=-lv/50 + 2,
                        color=cmap_dict[col],
                        label=f'{col}_level_{lv}'
                    )
        ax.set_title(f'{series} Forecast', fontsize=22)
        ax.set_xlabel('Timestamp [t]', fontsize=20)
        ax.legend(prop={'size': 15})
        ax.grid()
        for label in (ax.get_xticklabels() + ax.get_yticklabels()):
            label.set_fontsize(20)
                    
    def plot_hierarchically_linked_series(
        self,
        bottom_series: str, # Bottom time series to plot
        Y_df: Optional[pd.DataFrame] = None, # Dataframe with columns `ds` and models to plot indexed by `unique_id`.
        models: Optional[List[str]] = None, # Models to plot. 
        level: Optional[List[int]] = None # Levels for probabilistic intervals
    ):
        if bottom_series not in self.S.columns:
            raise Exception(f'bottom time series {bottom_series} not found')
        linked_series = self.S[bottom_series].loc[lambda x: x == 1.].index
        fig, axs = plt.subplots(len(linked_series), 1, figsize=(20, 2 * len(linked_series)))
        cols = models if models is not None else Y_df.drop(['ds'], axis=1)
        cols_wo_levels = [col for col in cols if ('lo' not in col and 'hi' not in col)]
        cmap = mcp.gen_color('tab10', 10)[:len(cols_wo_levels)]
        cmap_dict = dict(zip(cols_wo_levels, cmap))
        for idx, series in enumerate(linked_series):
            df_plot = Y_df.loc[series].set_index('ds')
            df_plot[cols_wo_levels].plot(ax=axs[idx], linewidth=2, color=cmap)
            if level is not None:
                for lv in level:
                    for col in cols_wo_levels:
                        if col == 'y':
                            # we dont need intervals
                            # for the actual value
                            continue
                        if f'{col}-lo-{lv}' not in df_plot.columns:
                            # if model
                            # doesnt have levels
                            continue
                        axs[idx].fill_between(
                            df_plot.index, 
                            df_plot[f'{col}-lo-{lv}'], 
                            df_plot[f'{col}-hi-{lv}'],
                            alpha=-lv/50 + 2,
                            color=cmap_dict[col],
                            label=f'{col}_level_{lv}'
                        )
            axs[idx].set_title(f'{series}', fontsize=10)
            axs[idx].grid()
            axs[idx].get_xaxis().label.set_visible(False)
            axs[idx].legend().set_visible(False)
            for label in (axs[idx].get_xticklabels() + axs[idx].get_yticklabels()):
                label.set_fontsize(10)
        plt.subplots_adjust(hspace=0.4)
        handles, labels = axs[0].get_legend_handles_labels()
        fig.legend(handles, labels, loc='lower center', 
                   prop={'size': 10}, ncols=np.ceil(len(labels) / 2), 
                   bbox_to_anchor=(0, 0.05, 1, 1))
