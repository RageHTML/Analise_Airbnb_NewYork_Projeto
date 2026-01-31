import pandas as pd 

df = pd.read_csv("listings.csv")


# Configurando para ler melhor, nao altera nada
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

renomear = { 
    'name':'nome',
    'host_id':'id_anfitriao',
    'host_profile_id':'qtde_anuncios_anfitriao',
    'host_name':'nome_anfitriao',
    'neighbourhood_group':'regiao',
    'neighbourhood':'bairro',
    'room_type':'tipo_acomodacao',
    'minimum_nights':'minimo_noites',
    'number_of_reviews':'total_avaliacoes',
    'last_review':'ultima_avaliacao',
    'reviews_per_month':'avaliacoes_por_mes',
    'calculated_host_listing_count':'qtde_anuncios_anfitriao',
    'availability_365':'dias_disponiveis_ano',
    'number_of_reviews_ltm':'avaliacoes_ultimos_12_meses',
    'license':'licensa'
}

df.rename(columns=renomear, inplace=True)
print(df.dtypes)