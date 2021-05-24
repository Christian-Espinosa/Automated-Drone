import numpy as np
import matplotlib.pyplot as plt

bins = ["sc","sl","sr"]
plt.ion()
fig,ax = plt.subplots()
barchart = ax.bar(bins,[0,0,0])
for i in range(50):
    for bar, val in zip(barchart, [np.random.randint(0,1),np.random.randint(0,1),np.random.randint(0,1)]):
        bar.set_height(val)
    fig.canvas.draw()
    fig.canvas.flush_events()