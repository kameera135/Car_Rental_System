from customer.customer import Customer

class RegularCustomer(Customer):
    def __init__(self, name, customer_id):
        super().__init__(name, customer_id)
        self.reward_points = 0

    def earn_points(self, amount_spent):
        # Earn 1 point for every $10 spent
        earned = int(amount_spent // 10)
        self.reward_points += earned
        print(f"You earned {earned} reward points. Total: {self.reward_points}")

    def get_discount(self):
        # 10 points = $1 discount
        return self.reward_points * 0.1

    def redeem_points(self):
        discount = self.get_discount()
        print(f"You redeemed {self.reward_points} points for ${discount:.2f} discount.")
        self.reward_points = 0
        return discount
