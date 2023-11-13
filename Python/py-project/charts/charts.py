import matplotlib.pyplot as plt

def generar_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]

    # aca se genera la grafica
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    # aca guardamos la grafica en un archivo
    plt.savefig('pie.png')

    plt.close()

    