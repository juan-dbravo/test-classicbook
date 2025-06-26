# main/run_pipeline.py
import argparse
import logging
from extract.extract_data import extract_main
from transform.transform_data import transform_main
from load.load_data import load_main

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline(step):
    if step == "extract":
        extract_main()
    elif step == "transform":
        transform_main()
    elif step == "load":
        load_main()
    elif step == "all":
        extract_main()
        transform_main()
        load_main()
    else:
        logging.error("Invalid step. Use extract, transform, load, or all.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the ETL pipeline.")
    parser.add_argument("--step", required=True, choices=["extract", "transform", "load", "all"])
    args = parser.parse_args()
    run_pipeline(args.step)
