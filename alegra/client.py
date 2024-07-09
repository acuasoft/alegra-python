import requests

from alegra.config import ApiConfig
from alegra.models.company import Company
from alegra.models.dian import DianResource
from alegra.models.payroll import Payroll
from alegra.models.test_set import TestSet
from alegra.resources.factory import ResourceFactory


class ApiClient:
    def __init__(self, config: ApiConfig):
        self.config = config
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {self.config.api_key}"})
        self.base_url = self.config.get_base_url()
        self._initialize_resources()

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.request(method, url, **kwargs)
        # response.raise_for_status()
        return response.json()

    def _initialize_resources(self):
        self.company = ResourceFactory(
            self,
            "company",
            self._request,
            {
                "get": {"model": Company, "response_key": "company"},
                "update": {"model": Company, "response_key": "company"},
            },
        )
        self.companies = ResourceFactory(
            self,
            "companies",
            self._request,
            {
                "create": {"model": Company, "response_key": "company"},
                "get": {"model": Company, "response_key": "company"},
                "update": {"model": Company, "response_key": "company"},
                "list": {"model": Company, "response_key": "companies"},
            },
        )
        self.payrolls = ResourceFactory(
            self,
            "payrolls",
            self._request,
            {
                "create": {"model": Payroll, "response_key": "payroll"},
                "get": {"model": Payroll, "response_key": "payroll"},
                "update": {"model": Payroll, "response_key": "payroll"},
                "list": {"model": Payroll, "response_key": "payrolls"},
                "perform__replace": {"model": Payroll, "response_key": "payroll"},
                "perform__cancel": {"model": Payroll, "response_key": "payroll"},
            },
        )
        self.dian = ResourceFactory(
            self,
            "dian",
            self._request,
            {"list": {"model": DianResource, "response_key": "dian"}},
        )
        self.test_sets = ResourceFactory(
            self,
            "test-sets",
            self._request,
            {
                "create": {"model": TestSet, "response_key": "test_set"},
                "get": {"model": TestSet, "response_key": "test_set"},
            },
        )
