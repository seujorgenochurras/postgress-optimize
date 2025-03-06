from prisma.models import Card, User, Task

Card.create_partial("CardWithoutRelation", exclude_relational_fields=True)

User.create_partial("UserSafe", relations={"cards": "CardWithoutRelation"})

Task.create_partial(
    "SimpleTask", exclude_relational_fields=True, exclude=["cardId", "id"]
)
