from transaction.models import Transaction
from home.models import *
from transaction import models


def initialize_transaction(owner, price, transaction_type):
    obj = Transaction.objects.create(
        owner=owner,
        total_price=price,
        transaction_type=transaction_type,
    )

    return obj.id


def initalize_transaction_click(owner, price, tour_id):
    tours = Tours.objects.get(id=tour_id)
    obj = Transaction.objects.create(
        owner=owner,
        total_price=price,
        transaction_type=models.TRANSACTIONTYPECHOICES.CLICK,
        tour=tours
    )
    return obj.id


def initalize_transaction_payme(owner, price, tour_id):
    tours = Tours.objects.get(id=tour_id)
    obj = Transaction.objects.create(
        owner=owner,
        total_price=price,
        transaction_type=models.TRANSACTIONTYPECHOICES.PAYME,
        tour=tours
    )
    return obj.id


def pay_transaction(transaction_id):
    try:
        instance = Transaction.objects.get(id=transaction_id)
        instance.make_payment()
    except Transaction.DoesNotExist:
        return


def cancel_transaction(transaction_id):
    try:
        instance = Transaction.objects.get(id=transaction_id)
        instance.cancel()
    except Transaction.DoesNotExist:
        return
