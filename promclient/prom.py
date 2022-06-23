from dataclasses import dataclass
from typing import Any

import matplotlib.pyplot as plt
import requests

Numeric = int | float


@dataclass
class Metric:
    name: str
    timestamps: list[Numeric]
    values: list[Numeric]


class ResponseException(Exception):
    pass


def concat_dict_values(dictionary: dict[str, str]) -> str:
    return "-".join(dictionary.values())


def query(
    metric_name: str, start_time: str, end_time: str, step_size: int
) -> list[Metric]:
    """Query time range data from the prometheus database."""

    url = f"http://localhost:9090/api/v1/query_range?query={metric_name}&start={start_time}&end={end_time}&step={step_size}s"
    response = requests.get(url)

    raw_dict: dict[str, Any] = response.json()

    if response.status_code != 200:
        raise ResponseException(
            f"Error in response ({response.status_code}): {raw_dict['errorType']} - {raw_dict['error']}"
        )

    data: dict[str, Any] = raw_dict["data"]
    result_type: str = data["resultType"]
    result: list[dict[str, Any]] = data["result"]

    metrics: list[Metric] = []
    for metric in result:
        metric_info: dict[str, Any] = metric["metric"]
        metric_data: list[list[Numeric]] = metric["values"]

        metric_name = concat_dict_values(metric_info)

        metric_timestamps = list(map(lambda d: float(d[0]), metric_data))
        metric_values = list(map(lambda d: float(d[1]) / 100000, metric_data))
        metrics.append(Metric(metric_name, metric_timestamps, metric_values))

    if not metrics:
        raise ResponseException("No metrics returned in query.")

    return metrics


def plot(metrics: list[Metric]) -> None:
    """Plot a list of time range metrics in separate figures."""

    for index, metric in enumerate(metrics):
        plt.figure(index + 1)
        plt.plot(metric.timestamps, metric.values)
        plt.title(metric.name)
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.grid(True)
    plt.show()
