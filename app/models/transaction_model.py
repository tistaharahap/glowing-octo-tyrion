from core_model import CoreModel
from datetime import date


class TransactionModel(CoreModel):

    balance = float()
    created_at = date()
    branch = unicode()
    mutation = float()
    mutation_type = unicode()
    description = unicode()