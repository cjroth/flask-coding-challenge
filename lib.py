from datetime import timedelta, datetime


def daterange(start_date_string, end_date_string, existing_only=True):
    """A utility function to generate a list of YYYY-MM-DD date strings between a start and end date."""
    start_date = datetime.strptime(start_date_string, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_string, '%Y-%m-%d')
    return [(start_date + timedelta(days=x)).strftime('%Y-%m-%d') for x in range(0, (end_date - start_date).days)]


def get_data_from_cache(cache, start_date, end_date):
    today = datetime.today()

    if datetime.strptime(start_date, '%Y-%m-%d') > today:
        return []

    if datetime.strptime(end_date, '%Y-%m-%d') > today:
        tomorrow = today + timedelta(days=1)
        end_date = tomorrow.strftime('%Y-%m-%d')

    return cache.get_or_compute_values(start_date, end_date)


class InMemoryDateStatCache:
    """Could be replaced with a persistant backend such as memcached, redis, or Postgres for scaling"""

    cache = {}

    def has(self, date):
        return date in self.cache

    def get(self, date):
        return self.cache.get(date, None)

    def set(self, date, stat):
        self.cache[date] = stat

    def compute_values(self, start_date, end_date):
        import quandl

        # TODO put me into secrets!
        quandl.ApiConfig.api_key = "zMfYAxi_LMaoGSkyGN2u"

        df = quandl.get(['BCHAIN/MKPRU', 'BCHAIN/TOUTV', 'BCHAIN/NADDU'], start_date=start_date, end_date=end_date)
        for index, row in df.iterrows():
            date = index.strftime('%Y-%m-%d')
            stat = {
                'date': date,
                'btc_price': row['BCHAIN/MKPRU - Value'],
                'output_volume': row['BCHAIN/TOUTV - Value'],
                'unique_addresses': row['BCHAIN/NADDU - Value'],
            }
            print('setting {}'.format(date), stat)
            self.set(date, stat)

    def get_or_compute_values(self, start_date, end_date, existing_only=True):
        """This could be further optimized to get only missing date ranges"""
        dates = daterange(start_date, end_date)

        if any([not self.has(date) for date in dates]):
            self.compute_values(start_date, end_date)

        return [self.get(date) for date in dates]
