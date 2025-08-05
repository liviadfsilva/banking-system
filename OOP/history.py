from datetime import datetime

class History:
    def __init__(self):
        self._transactions = []
        
    @property
    def transactions(self):
        return self._transactions
    
    def add_activity(self, transaction):
        self._transactions.append(
            {
                "type": transaction.__class__.__name__,
                "amount": transaction.amount,
                "date": datetime.now().strftime("%d-%m-%Y %H:%M:%s")
            }
        )