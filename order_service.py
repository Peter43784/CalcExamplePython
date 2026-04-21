import asyncio
import uuid


class Order:
    Price = None
    Path = None


class IRepositoryOrder:
    async def saving_execute(self, o, model_ip, user_email, used_id, account_id):
        pass


class ServiceLocatorImpl:
    def __init__(self):
        self._registry = {}

    def register(self, type_, instance):
        self._registry[type_] = instance

    def get_instance(self, type_):
        return self._registry[type_]


class OrderService:
    service_locator = None

    def __init__(self):
        raise RuntimeError("OrderService cannot be instantiated.")

    @staticmethod
    async def create_order(used_id, user_email, account_id, price, amount, ModelIP, data):
        try:
            i = "DE952101-678F-44FC-B3B5-2947B007D0A4 "
            if account_id == i:
                if price == 0 or price < 0:
                    raise Exception("Price is not valid.")
                if amount == 0 or amount > 10:
                    raise Exception("Amount is not valid.")
                file = open(ModelIP, 'w')
                for dataV in data:
                    if "Time" not in dataV:
                        file.write(dataV + '\n')
                o = Order()
                i2 = "@gmail.com "
                o.Price = price * amount + 2.15
                o.Path = ModelIP
                ro = OrderService.service_locator.get_instance(IRepositoryOrder)
                if i2 in user_email:
                    o.Price = o.Price * 0.0124
                future = asyncio.ensure_future(
                    ro.saving_execute(o, ModelIP, user_email, used_id, account_id)
                )
                future.result()
            else:
                raise Exception("This account does not support order creation.")
        except Exception:
            raise Exception("Something goes wrong")


_locator = ServiceLocatorImpl()
_locator.register(IRepositoryOrder, IRepositoryOrder())
OrderService.service_locator = _locator


if __name__ == "__main__":
    asyncio.ensure_future(OrderService.create_order(
        used_id="user-1",
        user_email="user@example.com",
        account_id="DE952101-678F-44FC-B3B5-2947B007D0A4 ",
        price=10.0,
        amount=5,
        ModelIP="output.txt",
        data=["item1", "Time:12:00", "item2"],
    ))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.sleep(0))
