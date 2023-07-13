import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import geopandas as gpd

def heatmap(arg):
    geo_df = gpd.read_file("BR_UF_2021.shp")[["NM_UF", "SIGLA", "geometry"]]
    brazil_df = pd.read_csv(f'{arg}.csv')
    brazil_df = brazil_df.drop('Description', axis=1)

    # Localiza todas as ocorrências de "Brazil" e remove do dataframe
    brazil_df_no_remote = brazil_df.drop(brazil_df.loc[brazil_df["Location"] == "Brazil"].index)
    # Divide-se o valor com base nas vírgulas [ split() ] e acessamos o penúltimo item (-2) da lista
    brazil_df_no_remote['Location'] = brazil_df_no_remote['Location'].str.split(',').str[-2].str.strip()
    # Devido a operação anterior, todos os casos que não seguirem a regra resultarão em NaN e serão removidos
    brazil_no_null = brazil_df_no_remote.dropna()
    brazil_new_df = brazil_no_null.groupby("Location").agg({"Title": "count"}).reset_index()

    merged_df = pd.merge(left=geo_df, right=brazil_new_df, how="left", left_on="NM_UF", right_on="Location")

    # Indicadores
    merged_df["Title"].fillna(0, inplace=True)
    merged_df["Razão"] = round(merged_df["Title"] / merged_df["Title"].sum(), 2)

    # Análise de Dados
    title = f'Oportunidades de Vagas de {arg.replace("_"," ")} no Brasil'
    col = "Razão"
    source = "Fonte: LinkedIn\nTaxa de Oportunidades = Anúncios por Estado / Total"
    vmin = merged_df[col].min()
    vmax = merged_df[col].max()
    cmap = 'plasma'

    # Criando a figura
    fig, ax = plt.subplots(1, figsize=(14, 12))

    # Removendo os eixos
    ax.axis('off')
    merged_df.plot(column=col, ax=ax, edgecolor='1', linewidth=0.5, cmap=cmap)

    ax.set_title(title, fontdict={'fontsize': '20', 'fontweight': '3'})
    ax.annotate(source, xy=(0.1, .08), xycoords='figure fraction', horizontalalignment='left', verticalalignment='bottom', fontsize=10)
    sm = plt.cm.ScalarMappable(norm=plt.Normalize(vmin=vmin, vmax=vmax), cmap=cmap)

    # Array vazio para o range de dados
    sm._A = []

    # Adicionando a barra de cor ao mapa
    cbaxes = fig.add_axes([0.15, 0.25, 0.01, 0.3])
    cbar = fig.colorbar(sm, cax=cbaxes)

    fig.savefig(f'{arg}.png', dpi=300)
