from feast import Entity, FeatureView, Field
from feast.types import Float32, Int64, String
# from feast.file_source import FileSource
from feast.infra.offline_stores.file_source import FileSource

athlete = Entity(
    name="athlete_id",
    join_keys=["athlete_id"],
    # value_type=Int64,
    description="Unique athlete identifier"
)

athlete_source_v2 = FileSource(
    path="data/athlete_features_v2.parquet",
    event_timestamp_column="event_timestamp",
)

athlete_features_v2 = FeatureView(
    name="athlete_features_v2",
    entities=[athlete],
    ttl=None,
    schema=[
        Field(name="gender", dtype=String),
        Field(name="height", dtype=Float32),
        Field(name="weight", dtype=Float32),
        Field(name="total_lift", dtype=Float32),
    ],
    source=athlete_source_v2,
    online=True,
)