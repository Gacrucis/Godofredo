data = df_integrants.groupby(["Qué semeste wn?"]).mean()

lockdown_start = data.iloc[3][
    "Cuántas materias han tenido acompañamiento por aulas virtuales?"
]

# for manim
plt.style.use("dark_background")

fig, ax = plt.subplots()
fig.set_size_inches(*FIG_SIZE_INCHES)
ax.plot(data, marker=".", color=palette["purple"], linewidth=2, markersize=20)

# lockdown started at about 4th semester
ls = ax.scatter(4, lockdown_start, s=250, color="r")

ax.set_xlabel("Semestre", fontsize=18)
ax.set_ylabel("Cantidad de materias con acompañamiento", fontsize=18)

plt.tight_layout()
plt.legend((ls,), ("Inicio de la pandemia",), fontsize=12)

# it's important to save fig before showing it up
plt.savefig("time-series.png")

plt.show()

# files.download("time-series.png")
