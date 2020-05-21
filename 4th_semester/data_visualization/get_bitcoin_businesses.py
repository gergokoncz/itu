import requests, json
import pandas as pd
from datetime import datetime

if __name__ == "__main__":
    url = 'https://coinmap.org/api/v1/venues/'
    ids, lats, lons, cats, names, created_ons = [], [], [], [], [], []
    for idx, venue in enumerate(json.loads(requests.get(url).text)['venues']):
        ids.append(venue['id'])
        lats.append(venue['lat'])
        lons.append(venue['lon'])
        cats.append(venue['category'])
        names.append(venue['name'])
        created_ons.append(venue['created_on'])
    
    this_df = pd.DataFrame({'id': ids, 'latitude': lats, 'longitude': lons,
    'category': cats, 'name': names, 'created_on': created_ons})
    this_df['created_on'] = this_df['created_on'].apply(lambda x: int(x))
    this_df['created'] = this_df['created_on'].apply(lambda x: datetime.fromtimestamp(x))
    this_df['created_date'] = this_df['created'].apply(lambda x: x.date())
    print(this_df.head())
    this_df.to_csv('bitcoin_accepting_business.csv', index = False)