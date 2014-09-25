from core_model import CoreModel


class TransactionCollectionModel(CoreModel):

    status = unicode()
    transaction = list()
    saldo = float()