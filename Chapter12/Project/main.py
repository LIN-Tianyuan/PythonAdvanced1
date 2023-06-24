# import libraires
from pyecharts.charts import Map,Geo
from pyecharts import options as opts
from pyecharts.globals import ThemeType
import pandas as pd

# https://github.com/owid/covid-19-data/tree/master/public/data
# Python master
# Object Oriented programming(OOP)
# -> 1.data analyse 2.web 3.jeu

dataset = pd.read_csv("owid-covid-data.csv")
# changer la date du type de données objet
# en type de données datetime
dataset["date"] = pd.to_datetime(dataset["date"])
# trier les données par date
df = dataset.sort_values(by=["date"],ascending=False)
map_df = df[df['date'] == '2022-08-01']
map_df.reset_index(drop=True, inplace=True)

country = list(map_df['location'])
total_cases = list(map_df['total_cases'])

list1 = [[country[i], total_cases[i]] for i in range(len(country))]
# Créer la carte et définir la taille de la carte
map_1 = Map(init_opts=opts.InitOpts(width="1000px", height="460px"))
map_1.add("Total Confirmed Cases", list1, maptype="world", is_map_symbol_show=False)
map_1.set_global_opts(
    # max_: Spécifier la valeur maximale du composant VisualMapOpts
    # is_piecewise: Segmenter ou non
    visualmap_opts=opts.VisualMapOpts(max_=1100000, is_piecewise=True,
                                      pieces=[
                                          {"min": 500000},
                                          {"min": 200000, "max": 499999},
                                          {"min": 100000, "max": 199999},
                                          {"min": 50000, "max": 99999},
                                          {"min": 10000, "max": 49999},
                                          {"max": 9999}, ]),
    title_opts=opts.TitleOpts(
    title='Covid-19 Worldwide Total Cases',
    subtitle="Till August 1st,2022",
    pos_left="center",
    padding=0,
    item_gap=2,# gap between title and subtitle
    title_textstyle_opts= opts.TextStyleOpts(color="darkblue",
    font_weight="bold",
    font_family="Courier New",
    font_size=30),
    subtitle_textstyle_opts= opts.TextStyleOpts(color="grey",
    font_weight="bold",
    font_family="Courier New",
    font_size=13)),
    # Montrer la légende ou non
    legend_opts=opts.LegendOpts(is_show=False)
)
map_1.set_series_opts(
    label_opts=opts.LabelOpts(is_show=False)
)
map_1.render() # montrer la carte
