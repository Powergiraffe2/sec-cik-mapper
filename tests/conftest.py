from pathlib import Path
from typing import Dict

import pytest

from sec_cik_mapper import (
    MutualFundMapper,
    MutualFundRetriever,
    StockMapper,
    StockRetriever,
)


@pytest.fixture(scope="session")
def stock_mapper() -> StockMapper:
    return StockMapper()


@pytest.fixture(scope="session")
def mutual_fund_mapper() -> MutualFundMapper:
    return MutualFundMapper()


@pytest.fixture(scope="session")
def generated_mappings_path_stocks() -> Path:
    return Path("auto_generated_mappings/stocks")


@pytest.fixture(scope="session")
def generated_mappings_path_mutual_funds() -> Path:
    return Path("auto_generated_mappings/mutual_funds")


@pytest.fixture(scope="session")
def stock_retriever() -> StockRetriever:
    return StockRetriever()


@pytest.fixture(scope="session")
def mutual_fund_retriever() -> MutualFundRetriever:
    return MutualFundRetriever()


@pytest.fixture(scope="session")
def apple_stock() -> Dict[str, str]:
    return {
        "ticker": "AAPL",
        "cik": "0000320193",
        "name": "Apple Inc.",
        "exchange": "Nasdaq",
    }
