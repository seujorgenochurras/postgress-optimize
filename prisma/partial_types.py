from prisma.models import Card, User

Card.create_partial("CardWithoutRelation", exclude_relational_fields=True)

User.create_partial("UserSafe", relations={"cards" : "CardWithoutRelation"})