# test-classicbook

This is a dummy pipeline to practice orchestration concepts like testing with pytest, running with argparse and integration with GitHub actions.

It is structured as an ETL pipeline, like my Classicbook ETL Pipeline.

I´m planning to Dockerize it in a close future.

## Folder Structure

``` 
test-classicbook/
├── main/                # CLI entrypoint
│   └── run_pipeline.py
├── extract/
│   └── extract_data.py
├── transform/
│   └── transform_data.py
├── load/
│   └── load_data.py
├── tests/
│   ├── test_extract.py
│   └── ...
├── pytest.ini           
├── requirements.txt     
├── .github/
│   └── workflows/
│       └── test.yml     
└── README.md            
```
