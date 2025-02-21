from babel.numbers import format_currency
from streamlit_javascript import st_javascript
from dotenv import load_dotenv
import os
import requests

load_dotenv()

def format_pesos_colombianos(value):
    """
    Formatea un valor numérico a una cadena representando pesos colombianos sin decimales.
    Args:
        value (float): El valor numérico a formatear.
    Returns:
        str: La cadena formateada.
    """
    # Redondeamos al centenar de miles más cercano (-5 significa centenos de miles)
    rounded_value = round(value, -5)
    return format_currency(int(rounded_value), 'COP', locale='es_CO', format='#,##0')

def client_ip():
    url = 'https://api.ipify.org?format=json'
    script = (f'await fetch("{url}").then('
                'function(response) {'
                    'return response.json();'
                '})')
    try:
        result = st_javascript(script)
        if isinstance(result, dict) and 'ip' in result:
            return result['ip']
        else: return None
    except: return None

def get_info_from_ip():
    token = os.environ['IP_INFO_TOKEN']
    ip = client_ip()
    if ip is None:
        new_ip = '45.5.167.153'
        ipapi_url = f"https://ipinfo.io/{new_ip}?token={token}"
    else: 
        ipapi_url = f"https://ipinfo.io/{ip}?token={token}"
    response_json = requests.get(ipapi_url).json()
    return response_json