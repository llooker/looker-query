PLUGIN_VERSION=0.0.3
PLUGIN_ID=looker-query

plugin:
	cat plugin.json|json_pp > /dev/null
	rm -rf dist
	mkdir dist
	zip -r dist/dss-plugin-${PLUGIN_ID}-${PLUGIN_VERSION}.zip code-env parameter-sets plugin.json python-connectors
