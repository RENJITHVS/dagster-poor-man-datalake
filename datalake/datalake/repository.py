from dagster import load_assets_from_package_module, repository, resources, io_manager, with_resources
from datalake.duckpond import DuckDB, DuckPondIOManager
from datalake import assets


@resources(config_schema={"vars":str})
def duckdb(init_context):
    return DuckDB(init_context.resources_config["vars"])    

duckdb_localstack = duckdb.configured({
    "vars" : """
set s3_access_key_id='test';
set s3_secret_access_key='test';
set s3_endpoint='localhost:4566';
set s3_use_ssl='false';
set s3_url_style='path';
"""
})

@io_manager(required_resource_keys={"duckdb"})
def duckpond_io_manager(init_context):
    return DuckPondIOManager("datalake", init_context.resources.duckdb)

@repository
def datalake():
    return [
        with_resources(
            load_assets_from_package_module(assets),
            { "io_manager": duckpond_io_manager,"duckdb":duckdb_localstack},
        )
        ]