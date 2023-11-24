import pandas as pd
import requests

# Función para cargar datos demográficos desde una URL
def cargar_datos_demograficos(url):
    data = pd.read_csv(url, sep=';')
    return data

# Función para procesar datos demográficos
def procesar_datos_demograficos(data):
    # Limpieza de datos demográficos
    data = data.drop(['Race', 'Count', 'Number of Veterans'], axis=1)
    data = data.drop_duplicates()
    return data

# Función para obtener datos de calidad del aire desde una API
# Función para obtener datos de calidad del aire desde una API
def obtener_calidad_aire(ciudades):
    api_url = 'https://api.api-ninjas.com/v1/airquality'

    calidad_aire_df = pd.DataFrame(columns=[

    
'city', 'CO', 'NO2', 'O3', 'SO2', 'PM2.5', 'PM10', 'overall_aqi'])

    for ciudad in ciudades:
        response = requests.get(api_url, params={
        
'city': ciudad}, headers={'X-Api-Key': 'PFqW9gMGiXufx6OYCFwbOA==RNu24oPiJKv6mRrf'})
        if response.status_code == 200:
            air_quality_data = response.json()
            calidad_aire_df = pd.concat([calidad_aire_df, pd.DataFrame({
                'city': [ciudad],
                'CO': [air_quality_data['data']['concentration']['co']],
                'NO2': [air_quality_data['data']['concentration']['no2']],
                'O3': [air_quality_data['data']['concentration']['o3']],
                'SO2': [air_quality_data['data']['concentration']['so2']],
                'PM2.5': [air_quality_data['data']['concentration']['pm25']],
                'PM10': [air_quality_data['data']['concentration']['pm10']],
                'overall_aqi': [air_quality_data['data']['aqi']['overall']]
            })], ignore_index=True)
    
    return calidad_aire_df

# Función principal
def main():
    # URL de los datos demográficos
    url_demograficos = "https://public.opendatasoft.com/explore/dataset/us-cities-demographics/download/?format=csv&timezone=Europe/Berlin&lang=en&use_labels_for_header=true&csv_separator=%3B"

    # Ciudades para obtener datos de calidad del aire
    ciudades = ['city1', 'city2', 'city3']  # Reemplaza con las ciudades reales que necesitas

    # Cargar y procesar datos demográficos
    datos_demograficos = cargar_datos_demograficos(url_demograficos)
    datos_demograficos_procesados = procesar_datos_demograficos(datos_demograficos)

    # Obtener datos de calidad del aire
    datos_calidad_aire = obtener_calidad_aire(ciudades)

    # Exportar resultados a CSV
    datos_demograficos_procesados.to_csv("datos_demograficos.csv", index=False)
    datos_calidad_aire.to_csv("datos_calidad_aire.csv", index=False)

if __name__ == "__main__":
    main()
