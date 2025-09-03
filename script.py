import pandas as pd
import matplotlib.pyplot as plt
import schedule
from datetime import datetime
import time as tm
import boto3

S3 = boto3.client("s3")
BUCKET_NAME = "script.automacao.do.schmitz"

def Nacionalidades_de_Jogadores():
    data = pd.read_csv("fifa.csv")
    const = data["Nationality"].value_counts().head(10)

    plt.figure(figsize=(10,6))
    plt.bar(const.index, const.values)
    plt.title("Nacionalidades de Jogadores")
    plt.xticks(rotation=45)
    plt.yticks(rotation=45)
    plt.xlabel("Nationality")
    plt.ylabel("ID")
    plt.tight_layout()

    nome_grafico = f"nacionalidades_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    plt.savefig(nome_grafico)
    plt.close()

    S3.upload_file(nome_grafico, BUCKET_NAME, nome_grafico)
    print("Gráfico enviado a", nome_grafico)

schedule.every(5).seconds.do(Nacionalidades_de_Jogadores)

while True:
    schedule.run_pending()
    tm.sleep(1)
