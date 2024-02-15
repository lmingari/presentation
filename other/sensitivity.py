import numpy as np
from matplotlib import pyplot as plt

fig, ax = plt.subplots()

rows = ["Meteo","Eruption\nSource\nParameters","Diffusivity"]
columns = ['Short-term\nforecasting', 'Long-term\nforecasting']
conf_data = [["Medium", "High"],["Medium","Medium"],["Low","Low"]]
conf_data = np.array(conf_data)

colors = np.full_like(conf_data,'', dtype=object)
colors[conf_data=='High']   = '#E74C3C'
colors[conf_data=='Low']    = '#82E0AA'
colors[conf_data=='Medium'] = '#85C1E9'
print(colors)

ax.set_axis_off()

table = ax.table(cellText=conf_data,
                 rowLabels=rows,
                 colLabels=columns,
                 cellColours=colors,
                 cellLoc="center",
                 loc='center',
                 colWidths=[0.1 for x in columns])
table.auto_set_font_size(False)
table.set_fontsize(24)
table.scale(10, 8) # make table a little bit larger
plt.savefig("sensitivity.pdf",bbox_inches='tight')
