# Looker Query plugin

This plugin allows one to get records from a [Looker](https://looker.com/) saved query (Look) via API.

Looker query result sets are read-only. This plugin does not offer the option to write-back to the database.

If you know the underlying database and schema, you can use a separate dataset as a write-back target.

You will need a URL pointing to the API of your Looker instance (e.g. https://yourinstance.looker.com:19999/api/3.1/).

You will need a Client ID & Secret Key for a user that has access to your instance.

You will need a valid saved query / Look ID to retrieve result sets.

## Changelog

**Version 0.0.2 (2019-10-01)**

* Adds code env to rely on looker-sdk module

**Version 0.0.1 (2019-08-27)**

* Initial release

## Need help?

Read [Looker API documentation](https://docs.looker.com/reference/api-and-integration/api-reference/v3.1) for more information on the Looker API.

Ask your question on [answers.dataiku.com](https://answers.dataiku.com). Or, [open an issue](https://github.com/dataiku/dataiku-contrib/issues).
