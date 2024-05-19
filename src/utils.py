from babel.numbers import format_currency
from streamlit_javascript import st_javascript

def format_pesos_colombianos(value):
    """
    Formatea un valor numérico a una cadena representando pesos colombianos sin decimales.
    
    Args:
    value (float): El valor numérico a formatear.
    
    Returns:
    str: La cadena formateada.
    """
    return format_currency(int(round(value, 0)), 'COP', locale='es_CO', format='#,##0')

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

def get_user_agent():
    try:
        user_agent = st_javascript('navigator.userAgent')
        if user_agent: return user_agent
        else: return None
    except: return None

def get_screen_resolution():
    script = '({width: window.screen.width, height: window.screen.height})'
    try:
        screen_res = st_javascript(script)
        if screen_res:
            width = screen_res.get('width')
            height = screen_res.get('height')
            return f"{width}x{height}"
        else: return None
    except: return None