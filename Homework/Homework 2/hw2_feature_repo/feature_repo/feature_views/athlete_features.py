
from feast import Entity, FeatureView, Field
from feast.types import Float32, Int64, String
# from feast.file_source import FileSource
from feast.infra.offline_stores.file_source import FileSource
# 
athlete = Entity(
    name="athlete_id",
    join_keys=["athlete_id"],
    # value_type=Int64,
    description="Unique athlete identifier"
)

athlete_source = FileSource(
    path="data/athlete_features.parquet",
    event_timestamp_column="event_timestamp",
)

athlete_features = FeatureView(
    name="athlete_features",
    entities=[athlete],
    ttl=None,
    schema=[
        Field(name="gender", dtype=String),
        Field(name="age", dtype=Float32),
        Field(name="height", dtype=Float32),
        Field(name="weight", dtype=Float32),
        Field(name="candj", dtype=Float32),
        Field(name="snatch", dtype=Float32),
        Field(name="deadlift", dtype=Float32),
        Field(name="backsq", dtype=Float32),
        Field(name="eat", dtype=String),
        Field(name="train", dtype=String),
        Field(name="background", dtype=String),
        Field(name="experience", dtype=String),
        Field(name="schedule", dtype=String),
        Field(name="howlong", dtype=String),
        Field(name="total_lift", dtype=Float32),
    ],
    source=athlete_source,
    online=True,
)