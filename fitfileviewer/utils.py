
import pandas as pd




## extract file_id data
def get_file_id_data(fitfile):
    df = pd.DataFrame(
        (
            (
                file_id.get_value("time_created").strftime("%Y-%m-%d %H:%M:%S"),
                file_id.get_value("type"),
                file_id.get_value("manufacturer"),
                file_id.get_value("product"),
                file_id.get_value("serial_number"),
            )
            for file_id in fitfile.get_messages("file_id")
        ),
        columns=["time_created", "type", "manufacturer", "product", "serial_number"],
    )

    return df.to_json(orient="records")