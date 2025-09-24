print("soham sonawane")
import abc

class PaymentStrategy(abc.ABC):

    @abc.abstractmethod
    def pay(self, amount):

        pass
class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Processing credit card payment for ${amount:.2f}")


class PaytmPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Processing Paytm payment for ${amount:.2f}")


class BitcoinPayment(PaymentStrategy):


    def pay(self, amount):
        print(f"Processing Bitcoin payment for ${amount:.2f}")

class PaymentProcessor:


    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy
        print(f"Payment processor initialized with {self._strategy.__class__.__name__} strategy.")

    def process_payment(self, amount):
        """Processes the payment using the current strategy."""
        print("Starting payment process...")
        self._strategy.pay(amount)
        print("Payment process completed.")


    def set_strategy(self, new_strategy: PaymentStrategy):

        self._strategy = new_strategy
        print(f"Payment strategy changed to {self._strategy.__class__.__name__}.")



if __name__ == "__main__":
    credit_card_strategy = CreditCardPayment()
    paytm_strategy = PaytmPayment()
    bitcoin_strategy = BitcoinPayment()
    processor = PaymentProcessor(credit_card_strategy)
    print("\n--- Processing first payment ---")
    processor.process_payment(50.00)

    print("\n--- Changing strategy to Paytm ---")
    processor.set_strategy(paytm_strategy)

    print("\n--- Processing second payment ---")
    processor.process_payment(125.75)

    print("\n--- Changing strategy to Bitcoin ---")
    processor.set_strategy(bitcoin_strategy)

    print("\n--- Processing third payment ---")
    processor.process_payment(34.50)
