# This file is the actual code for the custom Python dataset looker-query_run-query

from dataiku.connector import Connector
from lookerapi import LookerApi

import pprint

class MyConnector(Connector):

    def __init__(self, config, plugin_config):
        Connector.__init__(self, config, plugin_config)  # pass the parameters to the base class

        self.baseurl = self.config["baseurl"]
        self.clientid = self.config["clientid"]
        self.clientsecret = self.config["clientsecret"]
        self.lookid = int(self.config["lookid"])
        #self.limit = int(self.config["limit"])

        if self.baseurl is None or self.clientid is None or self.clientsecret is None:
            raise ValueError("Missing parameters (Base URL, or Client ID, or Client Secret")
        
        #if self.limit is None or self.limit = 0:
        #    self.limit = 500
        
    def get_read_schema(self):
        return None

    def generate_rows(self, dataset_schema=None, dataset_partitioning=None,
                            partition_id=None, records_limit = -1):

        looker = LookerApi(host=self.baseurl, token=self.clientid, secret = self.clientsecret)

        data = looker.get_look(self.lookid, "json", limit=100000)

        for row in data:
            yield row
        
        #print(data)

        ### ------- Done -------

        #print("Done")
        
        """
        looping = True
        offset = None
        params = {
            "pageSize": 100
        }

        # if sort_by is not None:
        #     params.update({
        #         "sort[0][field]": sort_by,
        #         "sort[0][direction]": sort_order}
        #     )

        while looping:
            if offset != None:
                params.update({'offset':offset})
            results = airtable_api(self.base, self.table, self.key, parameters=params)
            for record in results.get("records"):
                if self.retrieve_id == 'yes':
                    record["fields"]["id"] = record["id"]
                yield record["fields"]
            offset = results.get("offset")
            looping = False if offset is None else True

        """
        
    def get_writer(self, dataset_schema=None, dataset_partitioning=None,
                         partition_id=None):
        raise Exception("Unimplemented")


    def get_partitioning(self):
        raise Exception("Unimplemented")


    def list_partitions(self, partitioning):
        return []


    def partition_exists(self, partitioning, partition_id):
        raise Exception("Unimplemented")


    def get_records_count(self, partitioning=None, partition_id=None):
        raise Exception("Unimplemented")


