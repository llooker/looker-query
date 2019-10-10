# This file is the actual code for the custom Python dataset looker-query_run-query

from dataiku.connector import Connector

import logging
import pprint

import json

from looker_sdk import client, models, error

class MyConnector(Connector):

    def __init__(self, config, plugin_config):
        logging.basicConfig(level=logging.INFO, format='dss-plugin-looker-query %(levelname)s - %(message)s')
        self.logger = logging.getLogger()

        Connector.__init__(self, config, plugin_config)  # pass the parameters to the base class

        self.base_url = self.plugin_config["Looker API"]["baseurl"]
        self.client_id = self.plugin_config["Looker API"]["clientid"]
        self.client_secret = self.plugin_config["Looker API"]["clientsecret"]
        self.look_id = int(self.config["lookid"])
        #self.limit = int(self.config["limit"])
        
        print(self.plugin_config)

        if not (self.base_url and self.client_id and self.client_secret):
            self.logger.error('Connection params: {}'.format(
                {'Client ID:' : self.client_id,
                'Client secret:' : '#' * len(self.client_secret),
                'Base URL:' : self.base_url})
            )
            raise ValueError("Client ID, Client secret and Base URL must be filled")

        if not self.look_id:
            raise ValueError("Look ID was not set")

        #if self.limit is None or self.limit = 0:
        #    self.limit = 500

        file = open("looker.ini", "w")
        line_list = ["[Looker]", "api_version=3.1", "base_url=" + self.base_url, "client_id=" + self.client_id, "client_secret=" + self.client_secret, "verify_ssl=True"]
        file.write('\n'.join(line_list) + '\n')
        file.close()

        self.looker_client = client.setup("looker.ini")
        print(self.looker_client)

    def get_read_schema(self):
        return None

    def generate_rows(self, dataset_schema=None, dataset_partitioning=None,
                            partition_id=None, records_limit = -1):

        response = self.looker_client.run_look(self.look_id, "json")
        data = json.loads(response)
        
        for row in data:
            yield row

    def get_writer(self, dataset_schema=None, dataset_partitioning=None,
                         partition_id=None):
        raise NotImplementedError("Writer")


    def get_partitioning(self):
        raise NotImplementedError("Partition list")


    def list_partitions(self, partitioning):
        return []


    def partition_exists(self, partitioning, partition_id):
        raise NotImplementedError("Partition check")


    def get_records_count(self, partitioning=None, partition_id=None):
        raise NotImplementedError("Count records")
