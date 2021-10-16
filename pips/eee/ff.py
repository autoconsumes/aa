import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def readAllSheets(filename):

    xls = pd.ExcelFile(filename)
    sheets = xls.sheet_names
    libro = {}
    for sheet in sheets:
        libro[sheet] = xls.parse(sheet)
        libro[sheet] = libro[sheet].fillna("")
    xls.close()
    return libro


def mapa_ubicacion(lat, lon):
    # png=mapa_ubicacion(37.3,-2)
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="1kwm2")

    import geopandas as gpd
    #
    try:
        location = geolocator.reverse(str(lat)+","+str(lon))
        direccion = location.address
    except:
        direccion = 'Ubicacion'
    fig, ax = plt.subplots(figsize=(3, 3))
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    spain = (world.loc[world['name'] == 'Spain'])
    spain.boundary.plot(ax=ax, color='grey', alpha=.5)
    ax.axis('off')
    ax.plot([lon], [lat], 'ro')
    t = 'lat, lon = ' + str(round(lat, 2))+', ' + str(round(lon, 2))
    ax.text(lon, lat+.5, direccion, family='serif', color='blue',
            style='italic', wrap=True)
    ax.set_title(t)
    # ax.xaxis.set_ticks_position('top')  # the rest is the same
    ax.spines['bottom'].set_color('w')
    ax.spines['top'].set_color('w')
    ax.spines['right'].set_color('w')
    ax.spines['left'].set_color('w')
    plt.close()

    fig = mpl_to_html(fig)
    return fig


def _mpl_to_png_bytestring(fig):
    """This function uses Matplotlib's FigureCanvasAgg backend to convert a MPL
    figure into a PNG bytestring. The bytestring is not encoded in this step.
    """
    import io

    from matplotlib.backends.backend_agg import FigureCanvasAgg

    if isinstance(fig, plt.Axes):
        fig = fig.figure
    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)

    return output.getvalue()


def mpl_to_html(fig, **kwargs):
    """Take a figure and render it directly to HTML. A PNG is created, and
    then encoded into base64 and decoded back to UTF-8 so that it can be stored
    inside a <img> HTML tag.
    ``kwargs`` supports arbitrary HTML attributes. An example usage of kwargs:
    >>> render_mpl(fig, style='width:480px; height:auto;')
    """
    from flask import Markup
    import base64

    bstring = _mpl_to_png_bytestring(fig)
    png = base64.b64encode(bstring).decode("utf8")
    options = " ".join([f'{key}="{val}"' for key, val in kwargs.items()])

    # return png
    pngb64 = f"data:image/png;base64,{png}"
    return pngb64
    return Markup(f'<center><img src="data:image/png;base64,{png}" {options}></center>')


def paneles_planta(lat, lon, inclinacion, orientacion, mx, my, muro_sur):
    '''
    devuelve un grafico con la planta de placas
    '''

    from matplotlib.patches import Rectangle

    fig, ax = plt.subplots(figsize=(3, 4))
    superficie_m = (2, 4)
    oo = np.array([0, 0])

    k = 1/np.tan((61 - lat)*np.pi/180)
    hn = my*np.sin(inclinacion*np.pi/180)
    dn = hn*k+my*np.cos(inclinacion*np.pi/180)
    # dn=200
    hs = muro_sur
    ds = hs*k
    if orientacion < 0:
        mx = -mx

    modulo = Rectangle(oo,  mx,  my*np.cos(inclinacion *
                       np.pi/180)+5,  angle=orientacion)
    ax.add_patch(modulo)

    modulo = Rectangle(oo+[0, dn],  mx,  my *
                       np.cos(inclinacion*np.pi/180)+5,  angle=orientacion)
    ax.add_patch(modulo)

    modulo = Rectangle(oo+[0, -ds],  mx*2,  5,  angle=orientacion, color='g')
    ax.add_patch(modulo)

    def eje(xy, xytext, ttx):
        ax.annotate(ttx, xy=xy, xycoords='data',
                    xytext=xytext, textcoords='data',
                    arrowprops=dict(arrowstyle="<->", ls='dashed', alpha=.5), va='center', ha='center', color='grey', alpha=.5)

    # fig,ax = plt.subplots(figsize=tuple([4*x for x in superficie_m]))
    ax.axhline(y=0, color='r', linestyle=':', alpha=.1)
    ax.axhline(y=dn, color='r', linestyle=':', alpha=.1)
    ax.axhline(y=-ds, color='g', linestyle=':', alpha=.1)
    ax.axhline(y=my*np.cos(inclinacion*np.pi/180),
               color='r', linestyle=':', alpha=.1)

    xy = (0, 400)
    xytext = (0, -300)
    eje(xy, xytext, 'S')

    xytext = (-200, 0)
    xy = (200, 0)
    eje(xy, xytext, 'O')

    ax.set_xlim([-superficie_m[0]*100, superficie_m[0]*100])
    ax.set_ylim([-superficie_m[1]*100*3/4, superficie_m[1]*100*4/4])
    ax.axis('off')
    ax.set_title('$\\alpha$= '+str(orientacion)+'\n')

    plt.close()

    fig = mpl_to_html(fig)
    return fig


def paneles_lateral(lat, lon, inclinacion, orientacion, mx, my, muro_sur):
    '''
    devuelve un grafico con ellateral de las placas

    lat=38
    lon=-3
    my=100
    mx=150
    inclinacion=40
    orientacion=-30
    muro_sur=50
    display(HTML(Markup(f'<center><img src={paneles_lateral(lat,lon,inclinacion,orientacion,mx,my,muro_sur)}></center>')))
    '''

    from matplotlib.patches import Rectangle

    fig, ax = plt.subplots(figsize=(3, 4))
    superficie_m = (2, 4)
    oo = np.array([0, 0])

    # fig,ax = plt.subplots(figsize=tuple([4*x for x in superficie_m]))

    # medidas del modulo

    # diatancia entre modulos

    k = 1/np.tan((61 - lat)*np.pi/180)
    hn = my*np.sin(inclinacion*np.pi/180)
    dn = hn*k+my*np.cos(inclinacion*np.pi/180)
    # dn=200
    hs = muro_sur
    ds = hs*k

    def eje(xy, xytext, ttx):
        ax.annotate(ttx, xy=xy, xycoords='data',
                    xytext=xytext, textcoords='data',
                    arrowprops=dict(arrowstyle="<->", ls='dashed', alpha=.5), va='center', ha='center', color='grey', alpha=.5)

    # fig,ax = plt.subplots(figsize=tuple([4*x for x in superficie_m]))
    ax.axhline(y=0, color='r', linestyle=':', alpha=.1)
    ax.axhline(y=dn, color='r', linestyle=':', alpha=.1)
    ax.axhline(y=-ds, color='g', linestyle=':', alpha=.1)
    ax.axhline(y=my*np.cos(inclinacion*np.pi/180),
               color='r', linestyle=':', alpha=.1)
    ax.axvline(x=muro_sur, color='g', linestyle=':', alpha=.1)

    # COTAS

    ax.text(100, 0, str(0), color='red')
    ax.text(-100, my*np.cos(inclinacion*np.pi/180),
            str(round(my*np.cos(inclinacion*np.pi/180)/100, 2)), color='red')
    ax.text(100, dn, str(round(dn/100, 2)), color='red')
    ax.text(-100, -ds, str(round(-ds/100, 2)), color='g')
    ax.text(muro_sur+10, -ds-70, str(muro_sur/100),
            color='g', rotation=-90)

    modulo = Rectangle((0, 0), 100, -10,  angle=-(inclinacion+270))
    ax.add_patch(modulo)

    modulo = Rectangle((0, dn), 100, -10,  angle=-(inclinacion+270))
    ax.add_patch(modulo)

    oo = np.array([0, -ds])
    muro_sur = Rectangle(oo, muro_sur, -10,  angle=-
                         (90+270), color='g')
    ax.add_patch(muro_sur)

    def eje(xy, xytext, txx):
        ax.annotate(txx, xy=xy, xycoords='data',
                    xytext=xytext, textcoords='data',
                    arrowprops=dict(arrowstyle="<->", ls='dashed', alpha=.5), va='center', ha='center', alpha=.5)

    xy = np.array([0, 400])
    xytext = (0, -300)
    eje(xy, xytext, 'S')

    # cotas

    ax.set_xlim([-superficie_m[0]*100, superficie_m[0]*100])
    ax.set_ylim([-superficie_m[1]*100*3/4, superficie_m[1]*100*4/4])

    ax.set_title('$\\beta$= '+str(inclinacion)+'$^o$; ' +
                 '$(a,h)_{mod.}$=('+str(my)+','+str(mx)+')')

    ax.axis('off')

    plt.close()

    fig = mpl_to_html(fig)
    return fig


def sombras(lat, lon, sombra):
    '''
    lat=40
    lon=-3
    sombra=[ (-150, 0), (-100, 20), (-140, 20), (-99, 0),(140, 20), (99, 0), ]
    fig, horizonte=sombras(lat,lon,sombra)

    # para pasarle del df de leer el excel
    matrix = [
    ...     [1, 2, 3, 4],
    ...     [5, 6, 7, 8],
    ... ]
    list(zip(*matrix))

    '''

    import requests as requests
    import json

    lat_s, lon_s = lat, lon

    url = "https://re.jrc.ec.europa.eu/api/"
    url = url + "printhorizon?"
    url = url + "lat="+f'{lat_s}'
    url = url + "&lon="+f'{lon_s}'
    url = url + "&outputformat=json"
    # with open('pvgis_horizon
    #     # ==========================
    rrqq = requests.get(url)
    #     # ==========================
    fsi = pd.read_json(json.dumps(
        rrqq.json()["outputs"]['winter_solstice'], indent=2), orient="records")
    fsv = pd.read_json(json.dumps(
        rrqq.json()["outputs"]['summer_solstice'], indent=2), orient="records")
    fhh = pd.read_json(json.dumps(
        rrqq.json()["outputs"]['horizon_profile'], indent=2), orient="records")

    fhh.set_index('A', inplace=True)
    fsi.set_index('A_sun(w)', inplace=True)
    fsv.set_index('A_sun(s)', inplace=True)

    try:
        azimut_sombra = []
        elevac_sombra = []
        for i in range(0, len(sombra)):
            azimut_sombra.append(sombra[i][0])
            elevac_sombra.append(sombra[i][1])

        df = pd.DataFrame(index=azimut_sombra)
        df['el'] = elevac_sombra
        df = df.sort_index()
        horizonte = df.reindex(df.index.union(
            np.linspace(-180, 179, 360))).interpolate('values')
    except:
        horizonte = fhh

    horizonte = horizonte.replace(np.nan, 0)

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.set_facecolor('xkcd:blue')

    titulo = 'Tayectorias del sol y Sombras'
    fsv.plot(kind='area', stacked=False, color='orange', ax=ax, alpha=.991)
    fsi.plot(kind='area', stacked=False, color='blue', alpha=1, ax=ax)
    horizonte.plot(kind='area', stacked=False, color='grey', ax=ax, alpha=.921)
    fhh.plot(kind='area', stacked=False, color='green', ax=ax, alpha=1)
    horizonte.plot(kind='line', color='k', ax=ax, alpha=1)
    fsi.plot(kind='line',  color='grey', alpha=1, ax=ax)

    ax.legend([])
    ax.set_xlabel('Azimut($^o$)')
    ax.set_ylabel('Elevacion($^o$)')
    ax.set_title('Sombras')
    # ax.xaxis.set_ticks_position('top')  # the rest is the same
    ax.spines['bottom'].set_color('w')
    ax.spines['top'].set_color('w')
    ax.spines['right'].set_color('w')
    ax.spines['left'].set_color('w')
    plt.close()

    fig = mpl_to_html(fig)
    return fig, horizonte


def sombras_perdidas2(lat_s, lon_s, horizonte):
    '''
    lat=40
    lon=-3
    sombra=[ (-150, 0), (-100, 20), (-140, 20),(-10,0),(-9,60),(10,60),(11,0),  (-99, 0),(140, 20), (99, 0), ]
    fig, horizonte=sombras(lat,lon,sombra)
    '''

    import requests
    import json

    #
    hor = [0]*8
    #
    url = "https://re.jrc.ec.europa.eu/api/tmy"
    url = url + '?lat='+str(lat_s)
    url = url + '&lon='+str(lon_s)
    url = url + '&angle='+str(lat_s+10)
    url = url + '&aspect=0'
    url = url + '&global=1'
    url = url + "&userhorizon="+str(hor).strip('[]')
    url = url + '&outputformat=json'
    # print(url)
    respuesta = requests.get(url)  # api
    df = pd.read_json(json.dumps(
        respuesta.json()["outputs"]["tmy_hourly"], indent=2), orient="records")

    tmy = df.copy()
    tmy['dti'] = pd.date_range("2021-01-01", periods=365 * 24, freq="H")
    tmy = tmy.set_index('dti')
    tmy['D'] = tmy.index.date
    tmy['H'] = tmy.index.hour

    df = tmy.pivot(index=['D'], columns='H', values='G(h)')
    df.index = pd.to_datetime(df.index)
    df_despejado = df.copy()

    hor = horizonte['el'].values.tolist()
    hor = str(hor).strip('[]').replace(' ', '')
    #
    url = "https://re.jrc.ec.europa.eu/api/tmy"
    url = url + '?lat='+str(lat_s)
    url = url + '&lon='+str(lon_s)
    url = url + '&angle='+str(lat_s+10)
    url = url + '&aspect=0'
    url = url + '&global=1'
    url = url + "&userhorizon="+str(hor).strip('[]')
    url = url + '&outputformat=json'
    # print(url)
    respuesta = requests.get(url)  # api
    df = pd.read_json(json.dumps(
        respuesta.json()["outputs"]["tmy_hourly"], indent=2), orient="records")

    tmy = df.copy()
    tmy['dti'] = pd.date_range("2021-01-01", periods=365 * 24, freq="H")
    tmy = tmy.set_index('dti')
    tmy['D'] = tmy.index.date
    tmy['H'] = tmy.index.hour

    df = tmy.pivot(index=['D'], columns='H', values='G(h)')
    df.index = pd.to_datetime(df.index)
    df_sombra = df.copy()

    FS = round(1-(df_despejado-df_sombra).sum().sum() /
               df_despejado.sum().sum(), 2)

    fig, ax = plt.subplots(figsize=(3, 4))

    ax.imshow((df_sombra).values.tolist(), cmap='binary', aspect=.03)

    ax.set_title('Perdidas por sombra. FS = '+str(FS))
    ax.set_xlabel('hora')
    ax.set_ylabel('dia del anio')
    # ax.xaxis.set_ticks_position('top')  # the rest is the same
    ax.spines['bottom'].set_color('w')
    ax.spines['top'].set_color('w')
    ax.spines['right'].set_color('w')
    ax.spines['left'].set_color('w')
    plt.close()

    fig = mpl_to_html(fig)
    return fig, horizonte, tmy


def sombras_perdidas(lat, lon, horizonte):

    # lat=40
    # lon=-3
    # sombra=[ (-150, 0), (-100, 20), (-140, 20),(-10,0),(-9,60),(10,60),(11,0),  (-99, 0),(140, 20), (99, 0), ]
    # fig,FS,tmy=sombras_perdidas(lat,lon,horizonte)

    import requests
    import json

    from matplotlib import cm

    #
    hor = [0]*8
    #
    url = "https://re.jrc.ec.europa.eu/api/tmy"
    url = url + '?lat='+str(lat)
    url = url + '&lon='+str(lon)
    url = url + '&angle='+str(lat+10)
    url = url + '&aspect=0'
    url = url + '&global=1'
    url = url + "&userhorizon="+str(hor).strip('[]')
    url = url + '&outputformat=json'
    # print(url)
    respuesta = requests.get(url)  # api
    df = pd.read_json(json.dumps(
        respuesta.json()["outputs"]["tmy_hourly"], indent=2), orient="records")

    tmy = df.copy()
    tmy['dti'] = pd.date_range("2021-01-01", periods=365 * 24, freq="H")
    tmy = tmy.set_index('dti')
    tmy['D'] = tmy.index.date
    tmy['H'] = tmy.index.hour

    df = tmy.pivot(index=['D'], columns='H', values='G(h)')
    df.index = pd.to_datetime(df.index)
    df_despejado = df.copy()

    hor = horizonte['el'].values.tolist()
    hor = str(hor).strip('[]').replace(' ', '')
    #
    url = "https://re.jrc.ec.europa.eu/api/tmy"
    url = url + '?lat='+str(lat)
    url = url + '&lon='+str(lon)
    url = url + '&angle='+str(lat+10)
    url = url + '&aspect=0'
    url = url + '&global=1'
    url = url + "&userhorizon="+str(hor).strip('[]')
    url = url + '&outputformat=json'
    # print(url)
    respuesta = requests.get(url)  # api
    df = pd.read_json(json.dumps(
        respuesta.json()["outputs"]["tmy_hourly"], indent=2), orient="records")

    tmy = df.copy()
    tmy['dti'] = pd.date_range("2021-01-01", periods=365 * 24, freq="H")
    tmy = tmy.set_index('dti')
    tmy['D'] = tmy.index.date
    tmy['H'] = tmy.index.hour

    df = tmy.pivot(index=['D'], columns='H', values='G(h)')
    df.index = pd.to_datetime(df.index)
    df_sombra = df.copy()
    FS = round(1-(df_despejado-df_sombra).sum().sum() /
               df_despejado.sum().sum(), 2)
    # ax.imshow((df_sombra).values.tolist(), cmap='binary', aspect=.03)
    # Load1=tmy['G(h)']

    #     fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize=(6,5))

    #     Y=df_sombra.index.dayofyear.to_numpy()
    #     X=df_sombra.columns.to_numpy()
    #     Z=df_sombra.values
    #     X, Y = np.meshgrid(X, Y)
    #     ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
    #                                linewidth=2.7, antialiased=True)
    fig, ax = plt.subplots(figsize=(5, 3))
    im1 = plt.imshow(df_sombra.T, cmap=plt.cm.coolwarm,
                     interpolation='bilinear', aspect=10,alpha=.5)
    ax.set_ylabel('horas')
    ax.set_xlabel('dia del ano')
    plt.text(365-28*2,-1,'Diciembre')
    plt.text(30*5,-1,'Junio')
    plt.axvline(x=365-28, color='b', linestyle='-',linewidth=31, alpha=.2)
    plt.axvline(x=30*6, color='r', linestyle='-',linewidth=30, alpha=.2)
    # #     ax.set_zlabel('$kWh/m^2$')
    # ax.view_init(elev=60., azim=110)
    # ax.set_title('Sombras')
    # # ax.xaxis.set_ticks_position('top')  # the rest is the same
    # ax.spines['bottom'].set_color('w')
    # ax.spines['top'].set_color('w')
    # ax.spines['right'].set_color('w')
    # ax.spines['left'].set_color('w')
    # ax.axis('off')
    plt.close()
    fig = mpl_to_html(fig)
    return fig, FS, tmy


def foto_satelite(lat, lon):
    '''
    lat,lon=36.664187, -4.458605    
    foto_satelite(lat,lon)    
    '''
    token = 'pk.eyJ1Ijoia2duZXRlIiwiYSI6ImNrOHZrYnNuYTAyYzAzcGp3YXQ1bnZ4MTQifQ._73-EOK63N0679gZle29fw'
    #
    url = "https://api.mapbox.com/styles/v1/mapbox/light-v10"
    url = "https://api.mapbox.com/styles/v1/mapbox/satellite-v9"
    url = "https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v11"
    url = url+"/static"
    url = url+"/pin-s-f+f00("
    url = url+str(lon)
    url = url+","
    url = url+str(lat)
    url = url+")/"
    # url=url+"["
    url = url+str(lon)
    url = url+","
    url = url+str(lat)
    url = url+",18"
    url = url+"/300x300?access_token="
    url = url+token
    return url


def boxplots_meses(tmy):

    # tmy = df.copy()
    tmy['dti'] = pd.date_range("2021-01-01", periods=365 * 24, freq="H")
    tmy = tmy.set_index('dti')
    tmy['D'] = tmy.index.date
    tmy['H'] = tmy.index.hour

    df = tmy.pivot(index=['D'], columns='H', values='G(h)')
    df.index = pd.to_datetime(df.index)
    fig, [ax7, ax12] = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))
    color = {
    "boxes": "r",
    "whiskers": "orange",
    "medians": "yellow",
    "caps": "orange",
    }
    #     ax3 = plt.imshow(dh.T.astype(float), cmap=plt.cm.coolwarm,
    #                      interpolation='bilinear', aspect=11.04)
    df[(df.index.month == 7)].boxplot(ax=ax7,vert=False,color=color)
    df[(df.index.month == 12)].boxplot(ax=ax12,vert=False)

    ax12.set_xlim(0, 1000)
    ax7.set_xlim(0, 1000)
    ax12.set_title('Diciembre')
    ax7.set_title('Junio')
    #     plt.close()
    fig = mpl_to_html(fig)
    return fig


def tarifa_hora(tarifa, fecha_ini):
    from matplotlib import colors

    # fig,dh,hh=tarifa_hora(tarifa='20TD',fecha_ini='2021-01-01')
    # display(HTML(Markup(f"<center><img src={fig}></center>")))

    #
    # Cuadro 3. Discriminaciones horarias aplicables a los consumidores conectados en baja
    # tensión con potencia contratada igual o inferior a 15 kW según la estructura de peajes
    # vigentes (RD 1164/2001) y según la estructura de la Circular 3/2021
    hora = np.arange(0, 24)
    mes = np.arange(0, 12)
    # T_20TD
    if tarifa == '20TD':
        laborable = [[3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 1,
                      1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2]]*12
        festivo = [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]*12
    else:
        laborable = [[3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 1,
                      1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2]]*12
        festivo = [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]*12
    #
    T_20TD_L = pd.DataFrame(data=laborable, index=mes, columns=hora)
    T_20TD_F = pd.DataFrame(data=festivo, index=mes, columns=hora)
    # _F

    dti = pd.date_range(start=fecha_ini, periods=365, freq="D")
    df = pd.DataFrame(index=dti, columns=hora)
    # separa laborables y fines de semana
    df['LF'] = dti.strftime("%w")
    df['LF'] = np.where((df['LF'] == "6") | (df['LF'] == "0"), 'F', 'L')
    # separa festivos
    fecha_festivos = ['2021-01-01', '2021-01-06', '2021-12-25', ]
    df['LF'] = np.where(df.index.isin(fecha_festivos) == True, 'F', df['LF'])
    # df
    #  por meses
    for ii in range(0, 12):
        #     print(T_20TD_L.T[ii].tolist())
        df.loc[(df['LF'] == 'L') & (df.index.month == ii+1),
               hora] = T_20TD_L.T[ii].tolist()
        df.loc[(df['LF'] == 'F') & (df.index.month == ii+1),
               hora] = T_20TD_F.T[ii].tolist()

    df = df.drop(columns=['LF'])
    dh = df.copy()
    # para pasarlo tod a serie horaria lo mismo que las series de medidas y poner el indice
    (pd.melt(df))['value'].tolist()
    dti = pd.date_range(start=fecha_ini, periods=365*24, freq="H")
    hh = pd.DataFrame(index=dti)
    hh['periodo'] = ((pd.melt(df))['value'].tolist())

    # grafico
    fig, ax = plt.subplots(figsize=(4, 3))
    cmap = colors.ListedColormap(['r', 'orange', '#88e124'])

    ax.imshow(dh.astype(float), cmap=cmap, aspect=.04)
    plt.close()
    fig = mpl_to_html(fig)

    # dfs['periodo']=dfs['periodo'].astype(int)
    return fig, dh, hh


def irradiacionXmesYtarifa(hh, tmy):
    # fig,dh,hh=tarifa_hora(tarifa='20TD',fecha_ini='2021-01-01')
    # fig,FS,tmy=sombras_perdidas(lat,lon,horizonte)
    # fig,gxt_m=irradiacionXmesYtarifa(hh,tmy)
    tmy['G(h)']=tmy['G(h)']/1000
    tmy['tarifa'] = hh['periodo'].tolist()
    b = tmy[['G(h)', 'tarifa']].copy()
    gxt_h = b.pivot(columns='tarifa', values='G(h)')
    gxt_m = gxt_h.groupby(gxt_h.index.month).sum()
    fig, ax = plt.subplots(figsize=(4, 3))
    gxt_m.plot(kind='bar', stacked=True, ax=ax)

    plt.close()
    fig = mpl_to_html(fig)
    return fig, gxt_m


def Inclinacion_optima(periodo,latitud):
    FF=latitud
    columns = ['$\\beta_{opt}$', 'K', ]
    index = ['Diciembre', 'Julio', 'Anual', ]
    df = pd.DataFrame(columns=columns, index=index)
    #
    df['$\\beta_{opt}$'] = [FF+10, FF-20, FF-10]
    df['K'] = [1.7, 1, 1.15]
    BBo = int(df.loc[df.index.isin([periodo])]
              ['$\\beta_{opt}$'].to_list()[0])
    kk = df.loc[df.index.isin([periodo])]['K'].to_list()[0]

    return BBo,kk



def tablaIII():
    parametros=[
    '$Localidad$',
    '$Latitud(\phi)$',
    '$E_D$', 
    '$Periodo_{Dis}$',
    '$(\\alpha_{opt},\\beta_{opt})$',
    '$(\\alpha,\\beta)$',
    '$G_{dm}(0)$',
    '$FI$', 
    '$FS$', 
    '$PR$',
    '$G_{dm}(\\alpha,\\beta)$',
    '$P_{mp,min}$'
     ]

    comentarios=[
    'Efic. energ. global',
    'Ver mapa',
    'Fuente: PVGIS',
    '$FI=1-[1.2 x 10^{-4}(\\beta-\\beta_{opt})^2]$\n$+3.5x10^{-5}\\alpha^2$',
    '$G_{dm}(\\alpha,\\beta)=G_{dm}(0)\\cdot K\\cdot FI\\cdot FS$',
    'Sist. inversor y batería',
    '$PR=\\frac{E_D \\cdot G_{CEM}}{G_{dm}(\\alpha, \\beta) \\cdot P_{mp}}$',
    '$ P_{mp}=\\frac{E_D \\cdot G_{CEM}}{G_{dm}(\\alpha, \\beta) \\cdot PR}$',
    'IDAE-Tabla.III; K=',
    '',
    'Fuente: PVGIS',
        '',
    ]
    uds=[
    '$\\frac{kWh}{dia}$',
    '$\\frac{kWh}{(m^2 \cdot dia)}$',
    '$\\frac{kWh}{(m^2 \cdot dia)}$',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',    
    ]

    valores=[
    333,
    333,
    333,
    333,
    333,
    333,
    333,
    333,
    333,
    333,
    333,
    333,
    ]
    columns = ['Parametro', 'Ud', 'Valor', 'Comentario']
    df = pd.DataFrame(columns=columns)
    df['Parametro'] = ['']*12
    df['Ud'] = uds
    df['Valor'] = valores
    df['Comentario'] = comentarios
    df['Parametro'] = parametros
    df = df.set_index('Parametro')
    
    fig, ax = plt.subplots(figsize=(10, 10))

    tt = ax.table(
        cellText=df.values.tolist(),
        colWidths=[0.1210451, .210451, .681420],
        colLabels=df.columns.to_list(),
        rowLabels=df.index.to_list(),
        edges="closed",
        loc="center",
    )

    tt.scale(1, 3)
    tt.set_fontsize(14)
    ax.axis('off')
    ax.set_title('Cálculo de la potencia mínima del generador.')
#     plt.close()
    fig = mpl_to_html(fig)
    return fig

# fig=tablaIII()
# display(HTML(Markup(f'<center><img src={fig}></center>')))