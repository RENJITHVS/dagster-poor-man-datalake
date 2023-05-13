from dagster import Definitions, load_assets_from_modules

from . import assets

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
)

# from dagster import Definitions, load_assets_from_modules
# from . import assets
# from datalake.duckpond import DuckPondIOManager

# all_assets = load_assets_from_modules([assets])

# duckdb_localstack = DuckDB("""
# set s3_access_key_id='test';
# set s3_secret_access_key='test';
# set s3_endpoint='localhost:4566';
# set s3_use_ssl='false';
# set s3_url_style='path';
# """
# )

# defs = Definitions(
#     assets=all_assets,
#     resources={
#         "io_manager": DuckPondIOManager(bucket_name="datalake", duckdb_options=DUCKDB_LOCAL_CONFIG)
#     }
# )

