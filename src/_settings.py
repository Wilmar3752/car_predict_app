from dotenv import load_dotenv
load_dotenv()
import os
#CAR_PREDICT_URL = "http://0.0.0.0:8080/predict"
CAR_PREDICT_URL = "https://wilmars-car-predict.hf.space/predict"
all_makes = {'Volkswagen': ['Jetta',
  'Tiguan',
  'Voyage',
  'Parati',
  'Beetle',
  'Escarabajo',
  'Amarok',
  'Saveiro',
  'Polo',
  'Gol',
  'T-cross',
  'Bora',
  'Taos',
  'Fox',
  'Virtus',
  'Passat',
  'Cross',
  'New',
  'Crossfox',
  'Golf',
  'Transporter',
  'Nivus',
  'Nuevo',
  'Spacefox'],
 'Mazda': ['Cx-5',
  'Cx-30',
  '2',
  '3',
  'Bt-50',
  'B2200',
  'Mpv',
  'Cx-50',
  'Cx-3',
  'Cx-9',
  'B2600',
  '6',
  '626',
  'Mx-30',
  '5',
  'Allegro',
  'Cx-7',
  'Mx-5',
  'Cx-90',
  '323'],
 'Bmw': ['X3',
  'X1',
  'Serie',
  'X5',
  'M340i',
  'I3',
  '335',
  'X4',
  '120i',
  'Cabrio',
  '420i',
  '128ti',
  '225xe',
  'M240i',
  '340i',
  'Ix3',
  '2181i',
  'X2',
  '325i',
  'Bmw',
  '116',
  'M3',
  'M',
  'M2',
  'X6',
  'Z4',
  'M5',
  '218i',
  '330i',
  '320'],
 'Chevrolet': ['Aveo',
  'Bolt',
  'Spark',
  'Optra',
  'Vitara',
  'Sail',
  'Silverado',
  'D-max',
  'N300',
  'Tracker',
  'Super',
  'Onix',
  'Sonic',
  'Samurai',
  'Equinox',
  'Captiva',
  'Luv',
  'Rodeo',
  'Chevrolet',
  'Cruze',
  'Grand',
  'Traverse',
  'Joy',
  'Epica',
  'Beat',
  'Vivant',
  'Colorado',
  'Van',
  'Blazer',
  'Nhr',
  'Swift',
  'Trooper',
  'Tahoe',
  'Zafira',
  'Hhr',
  'Trailblazer',
  'Wagon',
  'Camaro',
  'Cheyenne',
  'Corsa',
  'Orlando',
  'N400',
  'Cobalt',
  'Chevy',
  'Sprint',
  'Esteem'],
 'Hyundai': ['Accent',
  'Santa',
  'Tucson',
  'Creta',
  'Elantra',
  'Starex',
  'Graviti',
  'New',
  'Getz',
  'H100',
  'Grand',
  'Veracruz',
  'I35',
  'Atos',
  'Hb20x',
  'Santamo',
  'Kona',
  'I20',
  'Hb20s',
  'Sonata',
  'Ioniq',
  'I30',
  'Porter',
  'I10',
  'Hb20',
  'H1'],
 'Hafei': ['Minyi'],
 'Honda': ['Cr-v',
  'Pilot',
  'Hr-v',
  'Accord',
  'Fit',
  'Odyssey',
  'Wr-v',
  'Civic',
  'Crx'],
 'Mini': ['Cooper', 'John', 'Countryman', 'Morris', 'Countryman\xa0hibrid'],
 'Ram': ['V700', '700', 'Ram', '1000'],
 'Citroën': ['C4', 'C3', 'C-elysée', 'Berlingo', 'C5', 'Ds3'],
 'Audi': ['Q5',
  'A4',
  'A3',
  'Q3',
  'Q7',
  'A5',
  'A6',
  'Q8',
  'Q2',
  'Tt',
  'E-tron',
  'A1',
  'S4'],
 'Toyota': ['4runner',
  'Fj',
  'Prado',
  'Corolla',
  'Yaris',
  'Fortuner',
  'Land',
  'Rav4',
  'Tundra',
  'Hilux',
  'Tacoma',
  'Estacas',
  'Sequoia',
  'Burbuja',
  'Rush'],
 'Nissan': ['Frontier',
  'Murano',
  'Sentra',
  'March',
  'X-trail',
  'Np300',
  'Note',
  'D22',
  'Kicks',
  'Xtrail',
  'Versa',
  'Qashqai',
  'Altima',
  'Tiida',
  'Pathfinder',
  'Patrol',
  'Navara',
  'D22/np300',
  'D21',
  'Urvan',
  'Ad',
  'Almera'],
 'Ford': ['Explorer',
  'Ranger',
  'Escape',
  'F-150',
  'Bronco',
  'Fusion',
  'Fiesta',
  'Edge',
  'Ecosport',
  'Sport',
  'Focus',
  'Mustang',
  'Raptor',
  'Nueva'],
 'Mercedes-benz': ['Ml',
  'Clase',
  'Cla',
  'Vito',
  'Glc',
  'E',
  'C',
  'Mb',
  'Amg',
  '350',
  '250',
  'B',
  '190',
  'Gle',
  'Glc250',
  'Gla',
  '4.6',
  '2004',
  '230',
  '180',
  'A',
  'C250',
  'Glk300',
  'Clk'],
 'Renault': ['Twizy',
  'Kangoo',
  'Duster',
  'Sandero',
  'Logan',
  'Symbol',
  'Stepway',
  'Fluence',
  'Twingo',
  'Kwid',
  'Captur',
  'Megane',
  'Koleos',
  'Scenic',
  'Trafic',
  'Clio',
  'Oroch',
  'New',
  'R4',
  'Alaskan',
  'Scala',
  'Zoe',
  'Scénic',
  'Master'],
 'Kia': ['Cerato',
  'Rio',
  'New',
  'Sportage',
  'Soul',
  'Picanto',
  'Sorento',
  'Niro',
  'Carens',
  'Stonic',
  'Carnival',
  'Seltos',
  'K',
  'Optima',
  'Tonic',
  'Cadenza',
  'Grand',
  'Soluto',
  'Mohave',
  'Opirus'],
 'Mitsubishi': ['2.6',
  'Lancer',
  'Montero',
  'Nativa',
  'Outlander',
  'L200',
  'Asx',
  'Eclipse'],
 'Subaru': ['Forester',
  'Legacy',
  'Outback',
  'Xv',
  'Impreza',
  'Evoltis',
  'Tribeca',
  'Cross'],
 'Land': ['Rover'],
 'Suzuki': ['S-cross',
  'Grand',
  'Vitara',
  'Swift',
  'Celerio',
  'Alto',
  'Jimny',
  'Baleno',
  'Ertiga',
  'Xl7',
  'Sj',
  'Ciaz',
  'Apv'],
 'Volvo': ['Xc90', 'Xc60', 'S40', 'S60', 'V40', 'Xc40', 'C30'],
 'Jeep': ['Willys',
  'Renegade',
  'Grand',
  'Wrangler',
  'Compass',
  'Cherokee',
  'Gladiator'],
 'Chery': ['Qq', 'Yoya', 'Tiggo', 'Qq3'],
 'Byd': ['Song', 'Idolphin', 'Yuan', 'Qin', 'Dolphin'],
 'Dahiatsu': ['Delta'],
 'Dodge': ['Journey', 'Ram', 'Coronet', 'Durango'],
 'Jac': ['E10x', 'S2', 'B-cross'],
 'Ds': ['Ds3', 'Ds4', 'Ds7'],
 'Fiat': ['Strada',
  'Uno',
  'Fiorino',
  '500',
  'Mobi',
  'Pulse',
  'Cronos',
  'Palio',
  '500c'],
 'Peugeot': ['3008',
  '207',
  '206',
  '407',
  '2008',
  '308',
  'Partner',
  '5008',
  '306',
  '208',
  '301',
  '406'],
 'Mg': ['Zs', '3', 'Gt', 'Marvel'],
 'Daihatsu': ['Grand', 'Terios', 'Sirion'],
 'Dfm/dfsk': ['Eq6410lf', 'Eq6390pf22qx', 'Van', 'Glory'],
 'Changan': ['Cs', 'Cargo'],
 'Seat': ['Arona', 'Altea', 'Leon', 'Ibiza', 'Ateca'],
 'Porsche': ['Macan', '911', 'Cayenne'],
 'Ssangyong': ['Actyon', 'Korando', 'Rexton', 'Kyron', 'Tivoli', 'Rodius'],
 'Great': ['Wall'],
 'Baic': ['Kenbo'],
 'Cupra': ['Formentor'],
 'Opel': ['Crossland'],
 'Alfa': ['Romeo'],
 'Jetour': ['X70'],
 'Lexus': ['Gx', 'Lx'],
 'Skoda': ['Yeti', 'Rapid', 'Fabia', 'Octavia', 'Superb'],
 'Jmc': ['Landwind'],
 'Zhidou': ['D2s'],
 'Daewoo': ['Cielo', 'Nubira', 'Damas'],
 'Jaguar': ['F-pace', 'E-pace'],
 'Hummer': ['H3'],
 'Dfsk': ['Van', 'K05', 'Glory'],
 'Brilliance': ['V5'],
 'Foton': ['Cargo'],
 'Mahindra': ['Kuv100'],
 'Huanghai': ['Tucson'],
 'Chrysler': ['Neon'],
 'Isuzu': ['Amigo']}


locations = {'Bogotá D.C.': ['Usaquén',
  'Fontibón',
  'Chapinero',
  'Barrios Unidos',
  'Engativa',
  'Teusaquillo',
  'Suba',
  'Puente Aranda',
  'Kennedy',
  'Martires',
  'Rafael Uribe Uribe',
  'Bosa',
  'Ciudad Bolívar',
  'Tunjuelito',
  'Antonio Nariño',
  'Usme',
  'San Cristobal Sur',
  'Santa Fe'],
 'Antioquia': ['Envigado',
  'La Estrella',
  'Medellín',
  'Sabaneta',
  'Bello',
  'Girardota',
  'Retiro',
  'Itaguí',
  'El Carmen de Viboral',
  'Copacabana',
  'Caldas',
  'Abejorral',
  'Rionegro'],
 'Cundinamarca': ['Chía',
  'Cota',
  'La Calera',
  'Facatativá',
  'Soacha',
  'Mosquera',
  'Cajicá',
  'Tabio',
  'Cáqueza',
  'Funza',
  'Fusagasugá',
  'Tenjo',
  'Madrid',
  'Zipaquirá',
  'La Vega',
  'Tocancipá',
  'Bogota',
  'Sopó',
  'Sibaté'],
 'Santander': ['Floridablanca', 'Bucaramanga', 'Barichara', 'Barbosa'],
 'Boyaca': ['Tunja', 'Duitama', 'Chiquinquirá'],
 'Valle Del Cauca': ['Cali', 'Roldanillo'],
 'Meta': ['Villavicencio'],
 'Huila': ["Neiva", 'Pitalito'],
 'Norte De Santander': ['Cúcuta'],
 'Quindio': ['Armenia'],
 "Caldas": ["Manizales"],
 "Atlantico": ["Barranquilla"],
 "Magdalena": ["Santa Marta"],
 "Cauca": ["Popayán"],
 "Nariño": ["Pasto"]
 }

all_models = [1954, 1966, 1971, 1977, 1980, 1981, 1982, 1984, 1985, 1986, 1987,
       1988, 1989, 1990, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000,
       2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011,
       2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022,
       2023, 2024]
DATABASE_CONFIG = {
    "dbname": os.environ['DB_NAME'],
    "user":  os.environ['USER_NAME'],
    "password":  os.environ['PASSWORD'],
    "host":  os.environ['HOST']
}