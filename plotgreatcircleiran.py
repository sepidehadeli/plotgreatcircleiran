from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

# ایجاد نمودار جدید
fig = plt.figure(figsize=(14, 10))  # تغییر سایز نقشه
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# اطلاعات شهرها
city = ["Tehran", "Mashhad", "Esfahan", "Shiraz", "Ahwaz", "Tabriz", "Karaj", "Qom", "Kerman", "Sari"]
lat = [35.6892, 36.2605, 32.6525, 29.5918, 31.3204, 38.0962, 35.8372, 34.6399, 30.2832, 35.5642]
lon = [51.3890, 59.6162, 51.6680, 52.5836, 48.6937, 46.2735, 50.9914, 50.8759, 57.0787, 53.0630]
population = [9000, 3000, 2000, 1800, 1500, 1600, 1600, 1200, 600, 200]

m = Basemap(llcrnrlon=40, llcrnrlat=20, urcrnrlon=70, urcrnrlat=45,
            rsphere=(6378137.00, 6356752.3142),
            resolution='l', projection='merc',
            lat_0=35, lon_0=55, lat_ts=20)

m.drawcoastlines()
m.fillcontinents(color='lightgray', lake_color='aqua')
m.drawcountries(linewidth=0.5)

# تبدیل مختصات جغرافیایی به مختصات نقشه
x, y = m(lon, lat)

# نمایش شهرها با دستور scatter
m.scatter(x, y, s=np.array(population) / 20, marker='o', color='b', alpha=0.7)

# تعریف تابعی که کمک کند تا شهرهایی که به هم نزدیک هستند همپوشانی کمتری داشته باشند
def adjust_text_position(city_name, xpt, ypt):
    if city_name == "Tehran":
        return xpt - 200000, ypt + 100000
    elif city_name == "Karaj":
        return xpt - 200000, ypt - 100000
    elif city_name == "Qom":
        return xpt + 150000, ypt + 50000
    elif city_name == "Sari":
        return xpt + 100000, ypt + 80000  
    else:
        return xpt + 100000, ypt + 100000

for i in range(len(city)):
    xpt, ypt = adjust_text_position(city[i], x[i], y[i])
    plt.text(xpt, ypt, city[i], fontsize=10, ha='left', va='bottom', color='black',
             bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))
    plt.text(xpt, ypt - 20000, f'{population[i]}K', fontsize=9, ha='left', va='top', color='blue')
    plt.plot([x[i], xpt], [y[i], ypt], linestyle='--', color='gray', linewidth=0.5)  # افزودن خطوط راهنما

# افزودن عنوان و نمایش نمودار
ax.set_title('Comparison of the 10 Largest Cities in Iran', fontsize=15)
plt.show()
