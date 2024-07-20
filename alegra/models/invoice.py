from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from alegra.models.customer import Customer


class Resolution(BaseModel):
    resolutionNumber: str
    prefix: str
    minNumber: int
    maxNumber: int
    startDate: str
    endDate: str
    technicalKey: str


class Item(BaseModel):
    code: str
    description: str
    price: float
    quantity: int
    unitCode: str
    note: Optional[str] = ""
    subtotal: float
    taxAmount: float
    total: float


class Payment(BaseModel):
    paymentForm: str
    paymentMethod: str
    paymentDueDate: str


class DiscountOrCharge(BaseModel):
    # Define los campos necesarios para los descuentos y cargos aquí
    pass


class TotalAmounts(BaseModel):
    grossTotal: float
    taxableTotal: float
    taxTotal: float
    discountTotal: float
    chargeTotal: float
    advanceTotal: float
    payableTotal: float
    currencyCode: str


class CompanyID(BaseModel):
    id: str


class Invoice(BaseModel):
    documentType: str
    resolution: Resolution
    company: CompanyID
    customer: Customer
    number: int
    note: Optional[str]
    items: List[Item]
    payments: List[Payment]
    discountsAndCharges: List[DiscountOrCharge] = []
    totalAmounts: TotalAmounts


class GovernmentResponse(BaseModel):
    code: str
    message: str
    errorMessages: List[str]


class InvoiceResponse(BaseModel):
    id: str
    companyIdentification: str
    customerIdentification: str
    type: str
    cufe: str
    date: datetime
    prefix: str
    number: int
    fullNumber: str
    status: str
    legalStatus: str
    governmentResponse: GovernmentResponse
    xmlFileName: str
    zipFileName: str
    qrCodeContent: str
