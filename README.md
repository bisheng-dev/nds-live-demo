# nds-live-demo
NDS.Live data channel demo
# NDS.Live Data Pipeline Project

## Feature Overview
- Convert TomTom Maps data to NDS.Live format
- Automated processing with AWS S3 and Lambda
- simulating data request and response between vehicle and cloud


##flowchart LR
    A[TomTom sample data] -->|tomtom_to_nds| B[NDS.Live tranformation]
    B -->|Zserio binary| C[S3 Bucket]
    C -->|Lambda trigger| D[vehicle simulator]
