# sofomo
available methods:
locations/ - get: gets list of all locations from db
           - post: requires either "ip" or "link", adds location to db based on input
locations/pk/ - get: gets information about specific location
              - delete: removes entry from db
and django simplejwt endpoints
