from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# Obtenir un objet graphique linéaire
line = Line()
# Ajouter les données de l'axes des x
line.add_xaxis(["France", "America", "China"])
# Ajouter les données de l'axes des y
line.add_yaxis("GDP", [30, 20, 10])

# Définir les éléments de configuration globale
line.set_global_opts(
    # Contrôle des titres:
    # titre: Nom du titre
    # pos_left: A quelle distance se trouve l'extrême gauche
    # pos_bottom: Contrôle vers le haut et vers le bas.
    # Distance par rapport au 1% intérieur
    title_opts=TitleOpts(title="GDP Show", pos_left="center", pos_bottom="1%"),
    # Légende de la carte de contrôle:
    # is_show: Montrer ou ne pas montrer
    legend_opts=LegendOpts(is_show=True),
    # Affichage de la boîte à outils
    # is_show: Montrer ou ne pas montrer
    toolbox_opts=ToolboxOpts(is_show=True),
    # Cartographie visuelle
    # is_show: Montrer ou ne pas montrer
    visualmap_opts=VisualMapOpts(is_show=True)
)

# Générer des graphiques
line.render()